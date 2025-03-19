from producer import Producer
from consumer import Consumer

class Buffer:

    def __init__(self, size=8):
        # Maximum Buffer Size
        self.size = size

        # Semaphores
        self.mutex = False
        self.full = 0
        self.empty = size

        # Stores Values in Buffer
        self.slots = []

        # List of Producers
        self.producers = []

        # List of Consumers
        self.consumers = []

    def add_producer(self):
        producer = Producer()
        self.slots.append(producer)

    def add_consumer(self):
        consumer = Consumer()
        self.slots.append(consumer)

    def delete_producer(self):
        self.producers.pop()

    def delete_consumer(self):
        self.consumers.pop()

    

    
