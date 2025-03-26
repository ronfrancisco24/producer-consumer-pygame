from producer import Producer
from consumer import Consumer


class Buffer:

    def __init__(self, size):
        # Maximum Buffer Size
        self.size = size
        self.last_produced = None
        self.last_consumed = None

        # Semaphores
        self.mutex = False  # lock
        self.full = 0  # filled slots
        self.empty = size  # empty slots

        # Stores Values in Buffer
        self.slots = []

        # List of Producers
        self.producers = []

        # List of Consumers
        self.consumers = []

    def add_producer(self):
        producer = Producer()
        self.producers.append(producer)

    def add_consumer(self):
        consumer = Consumer()
        self.consumers.append(consumer)

    def delete_producer(self):
        self.producers.pop()

    def delete_consumer(self):
        self.consumers.pop()

    # producer logic
    def produce_item(self):
        if not self.mutex and self.empty > 0:
            self.mutex = True
            self.add_producer()
            value = self.producers[-1].store
            self.slots.append(value)  # append latest value from latest producer
            self.last_produced = value
            self.full += 1
            self.empty -= 1
            self.mutex = False

    #consumer logic
    def consume_item(self):
        if not self.mutex and self.full > 0:
            self.mutex = True
            self.add_consumer()
            value = self.slots.pop()  # remove the first value inputted.
            self.consumers[-1].feed(value)
            self.consumers[-1].digest()
            self.empty += 1
            self.full -= 1
            self.last_consumed = value
            self.mutex = False

    def is_full(self):
        return self.full == self.size

    def is_empty(self):
        return self.full == 0

    def is_locked(self):
        return self.mutex
