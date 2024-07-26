# Import the pygame library and initialise the game engine
import pygame
from random import randint

pygame.init()
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BRIGHT_YELLOW = (255, 255, 100)

# Set the height and width of the screen
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rags to Riches: Idle Clicker")

# Load the font
font = pygame.font.SysFont('Monospace Regular', 32)
small_font = pygame.font.SysFont('Monospace Regular', 20)

# Clock to control frame rate
clock = pygame.time.Clock()

# Player class


class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = YELLOW
        self.click_damage = 1
        self.money = 0
        self.idle_income = 0
        self.upgrades = []

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        money_text = font.render(f"${int(self.money)}", 1, WHITE)
        win.blit(money_text, (self.x + 10, self.y + 10))

    def is_clicked(self, pos):
        return pos[0] > self.x and pos[0] < self.x + self.width and pos[1] > self.y and pos[1] < self.y + self.height

    def click_me(self):
        self.money += self.click_damage

    def apply_idle_income(self):
        self.money += self.idle_income

    def apply_upgrades(self):
        for upgrade in self.upgrades:
            upgrade.apply_effect()

# Upgrade class


class Upgrade:
    def __init__(self, name, cost, damage, income_increase):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.income_increase = income_increase
        self.active = False

    def draw(self, win):
        if self.active:
            color = BRIGHT_YELLOW
        else:
            color = YELLOW

        pygame.draw.rect(win, color, (300, self.y, 200, 50))
        upgrade_text = font.render(f"{self.name} - ${self.cost}", 1, WHITE)
        win.blit(upgrade_text, (310, self.y + 10))
        effect_text = small_font.render(f"+{self.damage} click damage, +${self.income_increase} income", 1, WHITE)
        win.blit(effect_text, (310, self.y + 30))

    def is_hovered(self, pos):
        return pos[0] > 300 and pos[0] < 500 and pos[1] > self.y and pos[1] < self.y + 50

    def buy(self, player):
        if player.money >= self.cost:
            player.money -= self.cost
            self.active = True
            player.upgrades.append(self)

    def apply_effect(self):
        player.click_damage += self.damage
        player.idle_income += self.income_increase


# Create upgrade instances
upgrade_1 = Upgrade("Mouse Upgrade", 50, 2, 1)
upgrade_2 = Upgrade("Computer Upgrade", 100, 5, 5)
upgrade_3 = Upgrade("Laptop Upgrade", 200, 10, 10)
upgrades = [upgrade_1, upgrade_2, upgrade_3]

# Position the upgrades
y_offset = 100
for i, upgrade in enumerate(upgrades):
    upgrade.y = 100 + i * y_offset


player = Player(200, 400, 100, 50)

# Storyline variables
story_texts = [
    "Welcome to 'Rags to Riches: Idle Clicker'!",
    "You start from the bottom, working a low-paying job.",
    "Click to earn money, and aim to become wealthy.",
    "Use your money wisely to buy upgrades and increase your income."
]
current_story_index = 0

# Keep looping until the user x button is clicked
running = True
while running:
    # Did the user click the close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
            mouse_pos = pygame.mouse.get_pos()
            # Check if the player clicked the button
            if player.is_clicked(mouse_pos):
                player.click_me()

            # Check for upgrade clicks
            for upgrade in upgrades:
                if upgrade.is_hovered(mouse_pos) and not upgrade.active:
                    upgrade.buy(player)

    # Update the player's income and apply upgrades
    player.apply_idle_income()
    player.apply_upgrades()

    # Fill the background with black
    win.fill(BLACK)

    # Draw the button
    player.draw(win)

    # Render the text
    income_text = font.render(f"Idle Income: ${player.idle_income}/s", 1, WHITE)
    win.blit(income_text, (300, 40))
    fps_text = font.render(f"FPS: {int(clock.get_fps())}", 1, WHITE)
    win.blit(fps_text, (50, 10))

    # Draw upgrade buttons
    for upgrade in upgrades:
        upgrade.draw(win)

    # Display storyline text
    story_text = font.render(story_texts[current_story_index], 1, WHITE)
    win.blit(story_text, (100, 550))

    # Next story text when space is pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        current_story_index = (current_story_index + 1) % len(story_texts)

    # Update display
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)
pygame.quit()
