import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# Colors
BACKGROUND = (0, 0, 0)
USER_TEXT = (0, 128, 255)  # Change the user message color
AI_TEXT = (200, 200, 200)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Fonts
font = pygame.font.Font(None, 36)

# User input rectangle
user_input_rect = pygame.Rect(50, 450, 700, 50)

# Chat history rectangle
chat_history_rect = pygame.Rect(50, 50, 500, 350)

# Maximum width of chat bubble for text wrapping
bubble_width = chat_history_rect.width - 40

# Text input
user_input_text = ""
chat_history = []

# Clock for controlling frame rate
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_RETURN:
                user_message = f'You: {user_input_text}'
                chat_history.append(user_message)

                # Simulate AI chatbot response (replace this with your AI logic)
                ai_response = "This is the AI response.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
                ai_message = f'AI: {ai_response}'
                chat_history.append(ai_message)

                user_input_text = ""
            else:
                user_input_text += event.unicode

    # Clear the screen
    screen.fill(BACKGROUND)

    # Draw chat history with Android-style message bubbles
    bubble_radius = 10
    for i, message in enumerate(chat_history):
        if message.startswith('You:'):
            color = USER_TEXT
            x, y = chat_history_rect.x, chat_history_rect.y + i * 60
        else:
            color = AI_TEXT
            x, y = chat_history_rect.x + 200, chat_history_rect.y + i * 60
        pygame.draw.rect(screen, color, pygame.Rect(x, y, chat_history_rect.width, 40), 0, bubble_radius)
        text_surface = font.render(message, True, BACKGROUND if color == USER_TEXT else BACKGROUND)
        screen.blit(text_surface, (x + 20, y + 10))

    # Draw user input box
    pygame.draw.rect(screen, USER_TEXT, user_input_rect, 2)
    user_input_surface = font.render(user_input_text, True, USER_TEXT)
    screen.blit(user_input_surface, (user_input_rect.x + 5, user_input_rect.y + 5))

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

pygame.quit()
