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
        self.current_home = "Shed"  # Initialize current home
        self.home_costs = {"Shed": 10, "Apartment": 100, "House": 500, "Mansion": 2000}  # Add cost of different homes

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        money_text = font.render(f"${int(self.money)}", 1, WHITE)
        win.blit(money_text, (self.x + 10, self.y + 10))
        home_text = font.render(f"Current Home: {self.current_home}", 1, WHITE)
        win.blit(home_text, (200, 50))

    def is_clicked(self, pos):
        return pos[0] > self.x and pos[0] < self.x + self.width and pos[1] > self.y and pos[1] < self.y + self.height

    def click_me(self):
        self.money += self.click_damage

    def apply_idle_income(self):
        self.money += self.idle_income

    def apply_upgrades(self):
        for upgrade in self.upgrades:
            upgrade.apply_effect()

    def buy_home(self, home):
        if self.money >= self.home_costs[home]:
            self.money -= self.home_costs[home]
            self.current_home = home
            # Update idle income based on new home
            self.idle_income = self.home_costs[home] // 10
