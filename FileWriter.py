import os
import re
from Substitute import Substitute


class FileWriter:

    def __init__(self):
        self.substitute = Substitute()

    # Deprecated!
    # Replace flag with fetched substitute.
    # Places in tmp, then replaces the original with the tmp.
    def replace_all(self, file):
        try:
            tmp = file + ".tmp"
            with open(tmp, "wt") as fout:
                with open(file, "rt") as fin:
                    for line in fin:
                        fout.write(line.replace('A', self.substitute.fetch_substitue(1)))
                fin.close()
                fout.close()
            os.remove(file)
            os.rename(tmp, file)
        except PermissionError:
            print(file, 'File was in use!')
        except UnicodeDecodeError:
            print(file, 'Encoding not supported!')

    # Places in tmp, then replaces the original with tmp, using a regex.
    def reg_replace_all(self, file):
        try:
            tmp = file + ".tmp"
            with open(tmp, "wt") as fout:
                with open(file, "rt") as fin:
                    for line in fin:
                        result = re.search(r'(?<=\[)(.*?)(?=\>)', line)
                        if result is not None:
                            id = result.group(1)
                            print(id, 'Substituted!')
                            fout.write(re.sub(r'(\[)(.*?)(\>)', '!!!!', line))
                        else:
                            fout.write(line)
                fin.close()
            fout.close()
            os.remove(file)
            os.rename(tmp, file)
        except PermissionError:
            print(file, 'File was in use!')
        except UnicodeDecodeError:
            print(file, 'Encoding not supported!')

    # Creating file with given id and name.
    def create_file(self, id, name=None):
        print('Creating file', id, name)

# Main testing method.
if __name__ == '__main__':
    test = FileWriter()
    # test.replace_all('test/test.txt')
    test.reg_replace_all('test/test.txt')
