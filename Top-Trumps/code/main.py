import pygame
import random
import csv
import mekanics.game_mekanics

pygame.init()
FONT = pygame.font.Font('fonts/MinecraftRegular-Bmg3.otf', 20)

# # Minecraft Font :)
# FONT = pygame.FONT.Font('./fonts/MinecraftRegular-Bmg3.otf', 20)
#
# FPS = 60
# WIDTH = 800
# HEIGHT = 800
#
# # Colors
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
#
# # Set up display
#
# sc = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Top Trumps")
# clock = pygame.time.Clock()
#
# background = pygame.image.load("fotos/spel/background_topTrumps.JPG")
# background = pygame.transform.scale(background, (WIDTH, HEIGHT))
#
# ttFront = pygame.image.load('fotos/spel/voorkant_kaart.jpg')
# ttFront = pygame.transform.scale(ttFront, (WIDTH // 3.333, HEIGHT // 2.5))
#
# ttBack = pygame.image.load('fotos/spel/achterkant_kaart.jpg')
# ttBack = pygame.transform.rotate(ttBack, 180)
# ttBack = pygame.transform.scale(ttBack, (WIDTH // 3.333, HEIGHT // 2.5))




# def game_loop():
#     while player
mekanics.game_mekanics.start_screen()
