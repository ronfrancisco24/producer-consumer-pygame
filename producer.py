import random

class Producer:
    def __init__(self):
        self.store = None
        self.produce()

    def produce(self):
        self.store = random.randint(1, 99)

    def reset(self):
        self.store = None
