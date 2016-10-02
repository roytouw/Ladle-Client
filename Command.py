import os
import threading

from FileMonitor import FileMonitor
from FileWriter import FileWriter


class Command:

    def __init__(self):
        self.exit = False
        self.fileMonitor = FileMonitor()
        self.poll_thread = None
        self.fileWriter = FileWriter()

    def start_threads(self):
        try:
            command_handler = threading.Thread(target=self.launch)
            command_handler.start()
            self.poll_thread = \
                threading.Thread(target=self.fileMonitor.poll_changes)
        except:
            print('An error occurred starting the threads.')

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
                print('* stop to halt polling the directory for flags.')
                print('* printdir to print the directory.')
                print('* pull id (name) to pull file with given id.')
                print('     e.g. pull 7 test.py')
                print('* exit to exit.')
            elif prompt_input == 'substitute':
                self.fileMonitor.substitute_flags()
            elif prompt_input == 'run':
                self.poll_thread.start()
                print('Now polling files for changes.')
                print('Type stop to halt polling.')
            elif prompt_input == 'stop':
                self.fileMonitor.stop_polling = True
                print('Polling stopped.')
                self.poll_thread = \
                    threading.Thread(target=self.fileMonitor.poll_changes)
            elif prompt_input == 'printdir':
                self.fileMonitor.print_directory()
            elif prompt_input.split(' ')[0] == 'pull':
                try:
                    if len(prompt_input.split(' ')) == 3:   # If both id and name are given.
                        self.fileWriter.create_file(prompt_input.split(' ')[1],
                                                    prompt_input.split(' ')[2])
                    else:                                   # If only the required is is given.
                        self.fileWriter.create_file(prompt_input.split(' ')[1])
                except IndexError:
                    print('Pull file error.')
                    print('No file id given!')
            else:
                print('Command not found, try again...')

    def exit_ladle(self):
        print('Exiting...')

if __name__ == '__main__':
    command = Command()
    # command.launch()
    command.start_threads()
