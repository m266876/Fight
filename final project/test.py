import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BAR_WIDTH = 400
BAR_HEIGHT = 50
BAR_COLOR = (0, 128, 255)
FPS = 60

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fill Up Bar")

clock = pygame.time.Clock()

def main():
    bar_width = 0
    start_time = pygame.time.get_ticks()
    duration = 5000  # 5 seconds in milliseconds

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Calculate the elapsed time
        elapsed_time = pygame.time.get_ticks() - start_time

        # Update the bar width based on elapsed time
        if elapsed_time < duration:
            bar_width = int((elapsed_time / duration) * BAR_WIDTH)
        else:
            bar_width = BAR_WIDTH

        # Clear the screen
        screen.fill((255, 255, 255))

        # Draw the bar
        pygame.draw.rect(screen, BAR_COLOR, (WIDTH // 2 - BAR_WIDTH // 2, HEIGHT // 2 - BAR_HEIGHT // 2, bar_width, BAR_HEIGHT))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

        # Check if the duration has passed, and exit the loop
        if elapsed_time >= duration + 1000:  # Add an extra second before exiting
            break

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
