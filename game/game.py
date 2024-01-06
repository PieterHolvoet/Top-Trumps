import csv
import sys
import pygame
import random
import math

pygame.init()

FPS = 60

# Set up display
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Top Trumps")
clock = pygame.time.Clock()

game_bg = pygame.image.load('/Users/ridhakareem/Documents/GitHub/Top-Trumps/fotos/TTGame.jpg')
game_bg = pygame.transform.scale(game_bg, (width + 80, height + 80))

ttFront = pygame.image.load('/Users/ridhakareem/Documents/GitHub/Top-Trumps/fotos/TTFrontCard.jpg')
ttFront = pygame.transform.scale(ttFront, (240, 320))

ttBack = pygame.image.load('/Users/ridhakareem/Documents/GitHub/Top-Trumps/fotos/TTBackCard.jpg')
ttBack = pygame.transform.rotate(ttBack, 180)
ttBack = pygame.transform.scale(ttBack, (240, 320))

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

kleur1 = (244, 247, 190)
kleur2 = (229, 247, 125)
kleur3 = (222, 186, 111)
kleur4 = (130, 48, 56)
benazwart = (43, 43, 43)

font = pygame.font.Font('/Users/ridhakareem/Documents/GitHub/Top-Trumps/fonts/MinecraftRegular-Bmg3.otf', 20)


def game_loop():
    while player.is_niet_einde(com):
        clock.tick(60)
        bonus_stapel = []
        boolean = True
        while boolean:
            print("Player beurt")
            screen.blit(game_bg, (0, 0))  # Fill the screen with a black background
            pygame.display.flip()
            hoger_lager = (random.randint(1, 100) % 2 == 0)  # EVEN == HOGER
            if hoger_lager:
                print("Deze Ronde is het hoger")
                rotation_angle = 0
                arrow_color = green
            else:
                print("Deze Ronde is het lager")
                rotation_angle = 180
                arrow_color = red
            print()
            tekenArrow(arrow_color, rotation_angle)
            player_kaart = player.pak_bovenste_kaart()
            display_card(player_kaart, True)
            com_kaart = com.pak_bovenste_kaart()
            pygame.display.flip()

            print(
                f"{player_kaart.naam}::: {attr1}: {player_kaart.attr1_waarde}, {attr2}: {player_kaart.attr2_waarde}, {attr3}: {player_kaart.attr3_waarde}, {attr4}: {player_kaart.attr4_waarde}")
            print("VOOR TEST ===V")
            print(
                f"{com_kaart.naam}::: {attr1}: {com_kaart.attr1_waarde}, {attr2}: {com_kaart.attr2_waarde}, {attr3}: {com_kaart.attr3_waarde}, {attr4}: {com_kaart.attr4_waarde}")
            keuze = get_selected_number(player_kaart, hoger_lager)
            print(keuze)
            if player_kaart.isgelijk(com_kaart, keuze):
                bonus_stapel.append(player_kaart)
                bonus_stapel.append(com_kaart)
                player.kaart_verwijderen_deck(player_kaart)
                com.kaart_verwijderen_deck(com_kaart)
                continue
            gewonnen = player.battle_andere_speler(com, keuze, bonus_stapel, hoger_lager)
            won_lost_screen(player_kaart, com_kaart, gewonnen)
            boolean = False
        bonus_stapel = []
        boolean = True
        if player.is_niet_einde(com):
            while boolean:
                print("Com Beurt")
                screen.fill((0, 0, 0))  # Fill the screen with a black background
                pygame.display.flip()
                hoger_lager = (random.randint(1, 100) % 2 == 0)  # EVEN == HOGER
                if hoger_lager:
                    print("Deze Ronde is het hoger")
                    rotation_angle = 0
                    arrow_color = green
                else:
                    print("Deze Ronde is het lager")
                    rotation_angle = 180
                    arrow_color = red
                print()
                tekenArrow(arrow_color, rotation_angle)
                player_kaart = player.pak_bovenste_kaart()
                display_card(player_kaart, True)
                com_kaart = com.pak_bovenste_kaart()
                pygame.display.flip()

                print(
                    f"{player_kaart.naam}::: {attr1}: {player_kaart.attr1_waarde}, {attr2}: {player_kaart.attr2_waarde}, {attr3}: {player_kaart.attr3_waarde}, {attr4}: {player_kaart.attr4_waarde}")
                print("VOOR TEST ===V")
                print(
                    f"{com_kaart.naam}::: {attr1}: {com_kaart.attr1_waarde}, {attr2}: {com_kaart.attr2_waarde}, {attr3}: {com_kaart.attr3_waarde}, {attr4}: {com_kaart.attr4_waarde}")
                keuze = rank_kaart_attr(com_kaart, hoger_lager)
                print(keuze)
                if player_kaart.isgelijk(com_kaart, keuze):
                    bonus_stapel.append(player_kaart)
                    bonus_stapel.append(com_kaart)
                    player.kaart_verwijderen_deck(player_kaart)
                    com.kaart_verwijderen_deck(com_kaart)
                    continue
                timer_clock(5, player_kaart)
                gewonnen = player.battle_andere_speler(com, keuze, bonus_stapel, hoger_lager)
                won_lost_screen(player_kaart, com_kaart, gewonnen)
                boolean = False


# Call the start screen function
start_screen()

# Quit the game
pygame.quit()
sys.exit()
