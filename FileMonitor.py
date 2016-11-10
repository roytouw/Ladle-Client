import os
import time

from FileWriter import FileWriter


class FileMonitor:
    # For mapping the files in the starting directory(place called from)
    # For monitoring changes in the mapped files.

    def __init__(self):
        print('Mapping directory.')
        self.directory = self.map_directory()
        self.fileWriter = FileWriter()
        self.stop_polling = False

    # Recursive method to map all files with last modified time
    def map_directory(self, path=os.getcwd()):
        result = {}
        for file in os.listdir(path):
            if os.path.isdir(os.path.join(path, file)):
                result[os.path.join(path, file)] = (self.map_directory(os.path.join(path, file)),
                                                    os.path.getmtime(os.path.join(path, file)))
            else:
                result[os.path.join(path, file)] = os.path.getmtime(os.path.join(path, file))
        return result

    # Map newly added files to directory
    def map_new(self, dir=None, path=os.getcwd()):
        if dir is None:
            dir = self.directory
        for file in os.listdir(path):
            if os.path.join(path, file) not in dir:     # New file detected.
                time.sleep(1)
                print('New file detected.', os.path.join(path, file))
                if os.path.isdir(os.path.join(path, file)):     # Newly detected file is a subdirectory.
                    dir[os.path.join(path, file)] = \
                        ({}, os.path.getmtime(os.path.join(path, file)))
                    self.map_new(dir[os.path.join(path, file)], os.path.join(path, file))
                else:
                    try:
                        dir[os.path.join(path, file)] = os.path.getmtime(os.path.join(path, file))
                    except FileNotFoundError:   # Temporary file detected, should be ignored.
                        continue

    # Keep polling files for changes.
    def poll_changes(self):
        self.stop_polling = False
        while not self.stop_polling:
            self.scan_directory(self.directory)  # Start with scanning the root directory.
            time.sleep(1)
            self.map_new()      # Check if new files where added during the polling.

    # Substitute all given flags in root and sub directories on changes.
    def substitute_flags(self, dir=None):
        if dir is None:
            dir = self.directory
        for key, value in dir.items():
            if isinstance(value, tuple):
                self.substitute_flags(value[0])  # If it's registered as a subdirectory.
            else:
                self.fileWriter.reg_replace_all(key)

    # Scan a directory for changes, recursive call on sub directories.
    def scan_directory(self, dir):
        temp = []
        for key, value in dir.items():
            if isinstance(value, tuple):  # If it's registered as a subdirectory.
                self.scan_directory(value[0])
            else:
                try:
                    if value != os.path.getmtime(key):
                        self.fileWriter.reg_replace_all(key)
                        dir[key] = os.path.getmtime(key)
                except FileNotFoundError:   # Temporary file detected, place on list for removal.
                    temp.append(key)
        for key in temp:    # Remove all detected temporary files.
            dir.pop(key)

    # Print the directory recursive.
    def print_directory(self, dir=None):
        if dir is None:
            print('Path, last_edit')
            dir = self.directory
        for key, value in dir.items():
            if isinstance(value, tuple):
                self.print_directory(value[0])
            else:
                print(key, value)


# Main testing method.
if __name__ == "__main__":
    print('Testing method is empty.')
    # fileMonitor = FileMonitor()
    # fileMonitor.print_directory()
    # fileMonitor.map_new()
    # fileMonitor.print_directory()
