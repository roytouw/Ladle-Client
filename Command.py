import os

from FileMonitor import FileMonitor


class Command:

    def __init__(self):
        self.exit = False
        self.fileMonitor = FileMonitor()

    # Starts listening for commands.
    def launch(self):
        os.system('color bd')
        print("Ladle started.")
        print("Type help for help, exit to halt.")
        while not self.exit:
            prompt_input = input('>_')
            if prompt_input == 'exit':
                break
            elif prompt_input == 'help':
                print('No help available yet...')
            elif prompt_input == 'substitute':
                self.fileMonitor.substitute_flags()
            elif prompt_input == 'run':
                print('Now polling files for changes.')
                self.fileMonitor.poll_changes()
            elif prompt_input == 'printdir':
                self.fileMonitor.print_directory()
            else:
                print('Command not found, try again...')

        print('Exiting...')

if __name__ == '__main__':
    command = Command()
    command.launch()
