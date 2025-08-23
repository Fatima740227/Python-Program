import pygame 
import random
import sys
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_model((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 150, 255)
GREEN = (0, 200, 100)
RED = (255, 50, 50)
font = pygame.font.SysFont(None, 36)
background = pygame.Surface(WIDTH, HEIGHT)
background.fill((240, 240, 240))
class Button:
    def __init__ (self, text, x, y, w, h, color, action):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.action = action

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=10)
        text_surf = font.render(self.text, True, WHITE)
        text_rect = text_surf.get_rect(center-self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper' ):
           return "You win!"
    else:
            return "Computer wins!"
choices = ["Rock", "Paper", "Scissors"]
result = "Choose Rock, Paper, or Scissors"

buttons = [
     Button("Rock", 100, 300, 120, 50, BLUE,  "Rock"),
     Button("Paper", 240, 300, 120, 50, GREEN,  "Paper"), 
     Button("Scissors", 300, 300, 120, 50, RED,  "Scissors"),
]
running = True
while running:
     screen.blit(background, (0,0))
     title = font.render("Rock Paper Scissors", True, BLACK)
     screen.blit(title, (WIDTH//2 - title.get_width()//2,40))
     result_text = font.render(result, True, BLACK)
     screen.blit(result_text, (WIDTH//2 - result_text.get_width()//2,120))
for button in buttons:
     button.draw(screen)
     
            