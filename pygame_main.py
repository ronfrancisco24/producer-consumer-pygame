import pygame
from pygame.locals import *
from buffer import Buffer
import sys
import random
from ui_components import Button

# use this to show GUI for producer-consumer problem

# TODO: modularize more of the ui_components.

# Constants
WIDTH, HEIGHT = 800, 600
BUTTON_WIDTH, BUTTON_HEIGHT = 250, 50
BUFFER_SLOT_SIZE = 70
BUFFER_SLOT_MARGIN = 20
FPS = 2
BUFFER_X, BUFFER_Y = 60, 200

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PINK = (254, 200, 200)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Producer-Consumer GUI")
clock = pygame.time.Clock()
FONT = pygame.font.Font(None, 36)

# Buffer instance
buffer = Buffer(size=8)

# Custom events
PRODUCE_CHANCE = 0.5  # 50% chance per frame
CONSUME_CHANCE = 0.5  # 50% chance per frame


# Flags for active producers/consumers
producer_active = False
consumer_active = False

# Button rectangles
producer_button = Button(120, 80, BUTTON_WIDTH, BUTTON_HEIGHT, PINK, 'START PRODUCER', BLACK, FONT)
consumer_button = Button(430, 80, BUTTON_WIDTH, BUTTON_HEIGHT, PINK, 'START CONSUMER', BLACK, FONT)


running = True
while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif producer_button.is_clicked(event):
            producer_active = not producer_active
            producer_button.color = GREEN if producer_active else PINK
            producer_button.text = 'STOP PRODUCER' if producer_active else 'START PRODUCER'
            producer_button.text_color = BLACK if producer_active else WHITE
        elif consumer_button.is_clicked(event):
            consumer_active = not consumer_active
            consumer_button.color = RED if consumer_active else PINK
            consumer_button.text = 'STOP CONSUMER' if consumer_active else 'START CONSUMER'
            consumer_button.text_color = BLACK if consumer_active else WHITE

    # producer and consumer logic.
    if producer_active and random.random() < PRODUCE_CHANCE:
        buffer.produce_item()

    if consumer_active and random.random() < CONSUME_CHANCE:
        buffer.consume_item()

    # draw buttons
    producer_button.draw_rect(screen)
    consumer_button.draw_rect(screen)

    # draw title
    title_text = FONT.render('Producer-Consumer GUI', True, BLACK)
    screen.blit(title_text, (260, 20))

    # draw the buffer slots

    # take the value for each index in buffer.slots
    for i, value in enumerate(buffer.slots):
        slot_rect = pygame.Rect(
            BUFFER_X + i * (BUFFER_SLOT_SIZE + BUFFER_SLOT_MARGIN),
            BUFFER_Y,
            BUFFER_SLOT_SIZE,
            BUFFER_SLOT_SIZE
        )
        pygame.draw.rect(screen, PINK, slot_rect)
        text = FONT.render(str(value), True, WHITE)
        text_rect = text.get_rect(center=slot_rect.center)
        screen.blit(text, text_rect)

    # show status texts
    status_y = BUFFER_Y + BUFFER_SLOT_SIZE + 50
    produced_text = FONT.render(f"Produced: {buffer.last_produced or 'None'}", True, BLACK)
    consumed_text = FONT.render(f"Consumed: {buffer.last_consumed or 'None'}", True, BLACK)
    screen.blit(produced_text, (50, status_y))
    screen.blit(consumed_text, (50, status_y + 40))

    # show buffer status if its full or not
    status_full = FONT.render("Buffer is FULL" if buffer.is_full() else "", True, GREEN)
    status_empty = FONT.render("Buffer is EMPTY" if buffer.is_empty() else "", True, RED)
    screen.blit(status_full, (540, status_y - 5))
    screen.blit(status_empty, (540, status_y - 5))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
