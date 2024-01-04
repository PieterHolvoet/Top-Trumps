import random
import pygame
import sys
import csv
import math
import game_screen as screen
import kaart as card
import player as pl
import os


path_MinecraftRegular = os.path.join("Top-Trumps2","assets", "fonts", "MinecraftRegular-Bmg3.otf")
path_start_screen = os.path.join("Top-Trumps2","assets","fotos","start_screen.jpg")
path_dierencsv = os.path.join("Top-Trumps2","assets","Dieren_TopTrumps.csv")





FPS = 60
WIDTH = 800
HEIGHT = 800


FONT = pygame.font.Font(path_MinecraftRegular, int(WIDTH//40))
GROOTFONT = pygame.font.Font(path_MinecraftRegular, int(WIDTH//10))

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top Trumps")
clock = pygame.time.Clock()

startscreen = pygame.image.load(path_start_screen)
startscreen = pygame.transform.scale(startscreen, (WIDTH, HEIGHT))


def start_screen():
    x1, x2 = WIDTH // 2.8, WIDTH // 1.5
    y1, y2 = HEIGHT // 1.5625, HEIGHT // 1.4
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False
                    game_loop()  # Call the game loop function when Enter key is pressed
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print(mouse_x)
                print(mouse_y)
                print()
                if x1 <= mouse_x <= x2 and y1 <= mouse_y <= y2:
                    running = False
                    game_loop()
        # Draw background
        sc.blit(startscreen, (0, 0))
        pygame.display.flip()
        pygame.time.Clock().tick(FPS)


def get_selected_number(kaart, hoger_lager):
    selected_number = None
    timer_seconds = 30
    x1, x2 = WIDTH//2.666, WIDTH//1.616
    y1, y2, y3, y4, y5 = HEIGHT//1.212, HEIGHT//1.161, HEIGHT//1.117, HEIGHT//1.0796, HEIGHT//1.0376
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Check for key presses
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    selected_number = 1
                elif event.key == pygame.K_2:
                    selected_number = 2
                elif event.key == pygame.K_3:
                    selected_number = 3
                elif event.key == pygame.K_4:
                    selected_number = 4
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print("mouse_x:" + str(mouse_x) + "  mouse_y:" + str(mouse_y))
                if x1 <= mouse_x <= x2 and y1 <= mouse_y <= y2:
                    selected_number = 1
                if x1 <= mouse_x <= x2 and y2 <= mouse_y <= y3:
                    selected_number = 2
                if x1 <= mouse_x <= x2 and y3 <= mouse_y <= y4:
                    selected_number = 3
                if x1 <= mouse_x <= x2 and y4 <= mouse_y <= y5:
                    selected_number = 4
        # If a number is selected, break out of the loop and return the value
        if selected_number is not None:
            print(selected_number)
            return selected_number
        screen.display_in_a_match(kaart, hoger_lager)
        # Draw the timer text
        timer_text = GROOTFONT.render(str(timer_seconds), True, WHITE)
        text_rect = timer_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        sc.blit(timer_text, text_rect)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(1)

        # Update the timer
        timer_seconds -= 1

        # Check if the timer has reached 0
        if timer_seconds < 0:
            return card.rank_kaart_attr(kaart, hoger_lager)


DECK_DIEREN_CSV = []
with open(path_dierencsv, 'r') as csv_bestand:
    csv_lezer = csv.reader(csv_bestand)
    header = next(csv_lezer)
    attr1, attr2, attr3, attr4 = header[1], header[2], header[3], header[4]
    for rij in csv_lezer:
        attr_lijst = [float(rij[1]), float(rij[2]), float(rij[3]), float(rij[4])]
        dier = card.Kaart(rij[0], attr_lijst)
        DECK_DIEREN_CSV.append(dier)
random.seed(101)
random.shuffle(DECK_DIEREN_CSV)
deck1 = []
deck2 = []
for i in range(15):
    deck1.append(DECK_DIEREN_CSV[i])
    deck2.append(DECK_DIEREN_CSV[i + 15])
player = pl.Player(deck1)
com = pl.Player(deck2)


def game_loop():
    while player.is_niet_einde(com):
        bonus_stapel = []
        boolean = True
        while boolean:
            hoger_lager = (random.randint(1, 100) % 2 == 0)  # EVEN == HOGER
            player_kaart = player.pak_bovenste_kaart()
            com_kaart = com.pak_bovenste_kaart()
            screen.display_in_a_match(player_kaart, hoger_lager)
            keuze = get_selected_number(player_kaart, hoger_lager)
            if player_kaart.isgelijk(com_kaart, keuze):
                bonus_stapel.append(player_kaart)
                bonus_stapel.append(com_kaart)
                player.kaart_verwijderen_deck(player_kaart)
                com.kaart_verwijderen_deck(com_kaart)
                screen.won_lost_screen(player_kaart, com_kaart, 0, len(player.deck), len(com.deck), hoger_lager, keuze)
                continue
            gewonnen = player.battle_andere_speler(com, keuze, bonus_stapel, hoger_lager)
            screen.won_lost_screen(player_kaart, com_kaart, gewonnen, len(player.deck), len(com.deck), hoger_lager, keuze)
            boolean = False
        if player.is_niet_einde(com):
            bonus_stapel = []
            boolean = True
            while boolean:
                hoger_lager = (random.randint(1, 100) % 2 == 0)  # EVEN == HOGER
                player_kaart = player.pak_bovenste_kaart()
                com_kaart = com.pak_bovenste_kaart()
                screen.display_in_a_match(player_kaart, hoger_lager)
                keuze = card.rank_kaart_attr(com_kaart, hoger_lager)
                if player_kaart.isgelijk(com_kaart, keuze):
                    bonus_stapel.append(player_kaart)
                    bonus_stapel.append(com_kaart)
                    player.kaart_verwijderen_deck(player_kaart)
                    com.kaart_verwijderen_deck(com_kaart)
                    screen.won_lost_screen(player_kaart, com_kaart, 0, len(player.deck), len(com.deck), hoger_lager, keuze)
                    continue
                screen.timer_clock(5, player_kaart, hoger_lager)
                gewonnen = player.battle_andere_speler(com, keuze, bonus_stapel, hoger_lager)
                screen.won_lost_screen(player_kaart, com_kaart, gewonnen, len(player.deck), len(com.deck), hoger_lager, keuze)
                boolean = False


start_screen()
