"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial
    <SerialGenerator start=100 next=101>

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100

    """

    def __init__(self, start):
        """initialize with a start number."""
        self.start = start
        self.num = start

    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.num}>"

    def generate(self):
        """return next sequential number."""
        self.num += 1
        return self.num - 1

    def reset(self):
        """reset number back to start."""
        self.num = self.start
