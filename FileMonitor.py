import os
import time

from FileWriter import FileWriter


class FileMonitor:
    # check directory structure
    # binary set all files
    # keep polling all root folders and files to compare binary value
    # if binary of one changes
    # locate change file
    # call FileWriter on it
    # register new binary value
    # get back to polling all root folders and files to compare binary values

    def __init__(self):
        print('Mapping directory.')
        self.directory = self.map_directory()
        self.fileWriter = FileWriter()
        self.substitute_flags()

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

    # Keep polling files for changes.
    def poll_changes(self):
        # self.substitute_flags()     # Check all files initially.
        while True:
            self.scan_directory(self.directory)  # Start with scanning the root directory.
            time.sleep(1)

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
        for key, value in dir.items():
            if isinstance(value, tuple):  # If it's registered as a subdirectory.
                self.scan_directory(value[0])
            else:
                if value != os.path.getmtime(key):
                    self.fileWriter.reg_replace_all(key)
                    dir[key] = os.path.getmtime(key)

    # Print the directory recursive.
    def print_directory(self, dir=None):
        if dir is None:
            print('Path, last_edit')
            dir = self.directory
        for key, value in dir.items():
            if isinstance(value, tuple):
                self.print_directory(value[0])
            else:
                print(key, value, '\n')


# Main testing method.
if __name__ == "__main__":
    fileMonitor = FileMonitor()
    fileMonitor.print_directory()
