# 1, decide what file needs substitute
# 2, for each substitute fetch it
# 3, place the substitute
from Authenticator import Authenticator


class Ladle:

    def __init__(self):
        self.substituteFetcher = SubstituteFetcher()
        self.authenticator = Authenticator()


# Main method
if __name__ == '__main__':
    ladle = Ladle()
