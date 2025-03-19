class Consumer:

    def __init__(self):
        self.store = None

    def feed(self, value):
        self.store = value

    def digest(self):
        self.store = None