import os
import threading

from FileMonitor import FileMonitor


class Command:

    def __init__(self):
        self.exit = False
        self.fileMonitor = FileMonitor()
        self.poll_thread = None

    def start_threads(self):
        try:
            command_handler = threading.Thread(target=self.launch)
            command_handler.start()
            self.poll_thread = \
                threading.Thread(target=self.fileMonitor.poll_changes)
            print('now it works.')
        except:
            print('nty mate.')

    # Starts listening for commands.
    def launch(self):
        os.system('color 5f')
        print("Ladle started.")
        print("Type help for help, exit to halt.")
        while not self.exit:
            prompt_input = input('>_')
            if prompt_input == 'exit':
                self.exit_ladle()
                break
            elif prompt_input == 'help':
                print('Commands:')
                print('* substitute to substitute all flags in directory.')
                print('* run to keep polling the directory for flags.')
                print('* printdir to print the directory.')
                print('* exit to stop.')
            elif prompt_input == 'substitute':
                self.fileMonitor.substitute_flags()
            elif prompt_input == 'run':
                self.poll_thread.start()
                print('Now polling files for changes.')
                print('Type stop to halt polling.')
            elif prompt_input == 'stop':
                print('This is not supported yet.')
            elif prompt_input == 'printdir':
                self.fileMonitor.print_directory()
            else:
                print('Command not found, try again...')

    def exit_ladle(self):
        print('Exiting...')

if __name__ == '__main__':
    command = Command()
    # command.launch()
    command.start_threads()
