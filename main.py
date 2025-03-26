from consumer import Consumer
from producer import Producer
from buffer import Buffer
import random
import time

start_loop = True
buffer = Buffer(size=8)
producer = Producer()
consumer = Consumer()

# this code is only to show the producer-consumer problem in the terminal with no GUI.
# use pygame_main.py for GUI display.


# NOTES

# Steps:
# Produce item → add to buffer.
# Show buffer state.
# Consume item → feed → digest.
# Show buffer state.
# Repeat.

# Requirements:
# Producer - adds to the buffer (only add when slots are empty, stop when it is full)
# Consumer - consumes slots (only consumer when it is full.)

# Semaphores:

# Mutex - represents a lock whether they can produce or consume (binary semaphore)
# Empty - represents the number of empty slots, set to the initial number of empty slots, decrement when produce is called. (counting semaphore)
# Full - initial value is 0, once more are produced increment this. (counting semaphore)

while start_loop:
    action = random.choice(['produce', 'consume'])
    # producer logic
    if action == 'produce' and len(buffer.slots) < buffer.size:
        buffer.produce_item()
        if buffer.is_full():
            print('buffer is full')

    # consumer logic
    if action == 'consume' and len(buffer.slots) > 0:
        buffer.consume_item()
        if buffer.is_empty():
            print('buffer is empty')
    print(f'current slots: {buffer.slots}')
    time.sleep(0.5)
