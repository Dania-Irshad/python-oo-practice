"""Word Finder: finds random words from a dictionary."""


from random import randrange


class WordFinder:
    """Machine to read file and return random words from file
    >>> wf = WordFinder("wordfindertest.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """

    def __init__(self, path):
        """Read file and makes an attribute of list of words"""
        f = open(path, "r")
        self.lst = self.get_words(f)
        f.close()
        print(f"{len(self.lst)} words read")

    def get_words(self, f):
        """Read each line without newline from file"""
        return [line.strip() for line in f]

    def random(self):
        """Return random word from list"""
        return self.lst[randrange(0, len(self.lst))]


class SpecialWordFinder(WordFinder):
    """
    >>> wf = SpecialWordFinder("specialwordfindertest.txt")
    4 words read

    >>> wf.random() in ["kale", "parsnips", "apple", "mango"]
    True
    """

    def get_words(self, f):
        """Read each line with exception of blank lines and comments from file"""
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]
