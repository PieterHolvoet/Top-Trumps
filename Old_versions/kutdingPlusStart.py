import csv
import sys
import pygame
import random
import math

pygame.init()

FPS = 60

# Set up display
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Top Trumps")
clock = pygame.time.Clock()

game_bg = pygame.image.load('fotos/New-img/background_topTrumps.JPG')
game_bg = pygame.transform.scale(game_bg, (width, height))

ttFront = pygame.image.load('fotos/TTFrontCard.jpg')
ttFront = pygame.transform.scale(ttFront, (screen.get_width() // 3.333, screen.get_height() // 2.5))

ttBack = pygame.image.load('fotos/TTBackCard.jpg')
ttBack = pygame.transform.rotate(ttBack, 180)
ttBack = pygame.transform.scale(ttBack, (screen.get_width() // 3.333, screen.get_height() // 2.5))

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

kleur1 = (244, 247, 190)
kleur2 = (229, 247, 125)
kleur3 = (222, 186, 111)
kleur4 = (130, 48, 56)
benazwart = (43, 43, 43)

font = pygame.font.Font('fonts/MinecraftRegular-Bmg3.otf', 20)


class Kaart:
    def __init__(self, naam, attr1_waarde, attr2_waarde, attr3_waarde, attr4_waarde, imageCard):
        self.naam = naam
        self.attr1_waarde = attr1_waarde
        self.attr2_waarde = attr2_waarde
        self.attr3_waarde = attr3_waarde
        self.attr4_waarde = attr4_waarde
        self.imageCard = pygame.image.load(imageCard)

    def isgelijk(self, other, attr):
        if attr == 1:
            return self.attr1_waarde == other.attr1_waarde
        elif attr == 2:
            return self.attr2_waarde == other.attr2_waarde
        elif attr == 3:
            return self.attr3_waarde == other.attr3_waarde
        elif attr == 4:
            return self.attr4_waarde == other.attr4_waarde

    def isgroter(self, other, attr):
        if attr == 1:
            return self.attr1_waarde > other.attr1_waarde
        elif attr == 2:
            return self.attr2_waarde > other.attr2_waarde
        elif attr == 3:
            return self.attr3_waarde > other.attr3_waarde
        elif attr == 4:
            return self.attr4_waarde > other.attr4_waarde


deck_dieren_excel = []
with open('Dieren_TopTrumps.csv', 'r') as csv_bestand:
    csv_lezer = csv.reader(csv_bestand)
    header = next(csv_lezer)
    attr1, attr2, attr3, attr4 = header[1], header[2], header[3], header[4]
    for rij in csv_lezer:
        dier = Kaart(rij[0], float(rij[1]), float(rij[2]), float(rij[3]), float(rij[4]), 'fotos/leeuwen.jpg')
        deck_dieren_excel.append(dier)

sorted_attr1 = []
sorted_attr2 = []
sorted_attr3 = []
sorted_attr4 = []

for kaart in deck_dieren_excel:
    sorted_attr1.append(kaart.attr1_waarde)
    sorted_attr2.append(kaart.attr2_waarde)
    sorted_attr3.append(kaart.attr3_waarde)
    sorted_attr4.append(kaart.attr4_waarde)
sorted_attr1 = sorted(sorted_attr1)
sorted_attr2 = sorted(sorted_attr2)
sorted_attr3 = sorted(sorted_attr3)
sorted_attr4 = sorted(sorted_attr4)


def rank_kaart_attr(kaart, hoger_lager):
    waarde1, waarde2, waarde3, waarde4 = kaart.attr1_waarde, kaart.attr2_waarde, kaart.attr3_waarde, kaart.attr4_waarde
    rank1 = sorted_attr1.index(waarde1)
    rank2 = sorted_attr2.index(waarde2)
    rank3 = sorted_attr3.index(waarde3)
    rank4 = sorted_attr4.index(waarde4)
    rank_list = [rank1, rank2, rank3, rank4]
    if hoger_lager:  # True==Hoger
        wanted_rank = max(rank_list)
    else:
        wanted_rank = min(rank_list)
    return rank_list.index(wanted_rank) + 1


def display_card(card, player):
    # if player:
    #     x = 50
    # else:
    #     x = 450
    screen.blit(game_bg, (0, 0 - screen.get_height() * 0.02))
    screen.blit(ttFront, ((width / 2) - (ttFront.get_width() / 2), height - ttFront.get_height()))
    screen.blit(ttBack, ((width / 2) - (ttBack.get_width() / 2), 0))

    name_text = font.render(card.naam, True, (255, 255, 255))
    screen.blit(name_text, (screen.get_width() // 2 - (screen.get_width() // 10.666), screen.get_height() * 0.64))
    attr_value = f"{card.attr1_waarde}"
    attr_surface = font.render((attr_value), True, (255, 255, 255))
    screen.blit(attr_surface, ((screen.get_width() // 2) + (screen.get_width() // 15), screen.get_height() * 0.83))

    # text_y = 300
    #
    # # Display card name
    # name_text = font.render(card.naam, True, (255, 255, 255))
    # screen.blit(name_text, (x, text_y))
    # text_y += 50
    #
    # button1 = Button(2, text_y - 12, 46, 46, "", kleur1, white)
    # button1.draw()
    # attribute_text = f"{attr1}: {card.attr1_waarde}"
    # attribute_surface = font.render(attribute_text, True, (255, 255, 255))
    # screen.blit(attribute_surface, (x, text_y))
    # text_y += 50
    #
    # button2 = Button(2, text_y - 12, 46, 46, "", kleur2, white)
    # button2.draw()
    # attribute_text = f"{attr2}: {card.attr2_waarde}"
    # attribute_surface = font.render(attribute_text, True, (255, 255, 255))
    # screen.blit(attribute_surface, (x, text_y))
    # text_y += 50
    #
    # button3 = Button(2, text_y - 12, 46, 46, "", kleur3, white)
    # button3.draw()
    # attribute_text = f"{attr3}: {card.attr3_waarde}"
    # attribute_surface = font.render(attribute_text, True, (255, 255, 255))
    # screen.blit(attribute_surface, (x, text_y))
    # text_y += 50
    #
    # button4 = Button(2, text_y - 12, 46, 46, "", kleur4, white)
    # button4.draw()
    # attribute_text = f"{attr4}: {card.attr4_waarde}"
    # attribute_surface = font.render(attribute_text, True, (255, 255, 255))
    # screen.blit(attribute_surface, (x, text_y))
    # text_y += 50


#
# import csv
# import sys
# import pygame
# import random
# import math
#
# pygame.init()
#
# FPS = 60
#
# # Set up display
# width, height = 800, 800
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Top Trumps")
# clock = pygame.time.Clock()
#
# game_bg = pygame.image.load('fotos/TTGame.jpg')
# game_bg = pygame.transform.scale(game_bg, (width + 80, height + 80))
#
# ttFront = pygame.image.load('fotos/TTFrontCard.jpg')
# ttFront = pygame.transform.scale(ttFront, (240, 320))
#
# ttBack = pygame.image.load('fotos/TTBackCard.jpg')
# ttBack = pygame.transform.rotate(ttBack, 180)
# ttBack = pygame.transform.scale(ttBack, (240, 320))
#
# black = (0, 0, 0)
# white = (255, 255, 255)
# green = (0, 255, 0)
# red = (255, 0, 0)
#
# kleur1 = (244, 247, 190)
# kleur2 = (229, 247, 125)
# kleur3 = (222, 186, 111)
# kleur4 = (130, 48, 56)
# benazwart = (43, 43, 43)
#
# font = pygame.font.Font('./fonts/MinecraftRegular-Bmg3.otf', 20)


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
                print()
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


class Button:
    def __init__(self, x, y, width, height, text, background_color, text_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.background_color = background_color
        self.text_color = text_color

    def draw(self):
        pygame.draw.rect(screen, self.background_color, self.rect)
        text = font.render(self.text, True, self.text_color)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def get_coords(self):
        return self.rect.x, self.rect.y, self.rect.width, self.rect.height


class Player:
    def __init__(self, deck):
        self.deck = deck

    def aantal_kaarten(self):
        return len(self.deck)

    def pak_bovenste_kaart(self):
        kaart = self.deck[0]
        return kaart

    def kaart_toevoegen_deck(self, kaart):
        self.deck.append(kaart)
        return

    def kaart_verwijderen_deck(self, kaart):
        self.deck.remove(kaart)
        return

    def bonus_krijgen(self, kaarten):
        for kaart in kaarten:
            self.kaart_toevoegen_deck(kaart)

    def battle_andere_speler(self, other, attr, bonus, bool_hoger_lager):
        eigen_kaart, andere_kaart = self.pak_bovenste_kaart(), other.pak_bovenste_kaart()
        if bool_hoger_lager:
            if eigen_kaart.isgroter(andere_kaart, attr):
                self.kaart_verwijderen_deck(eigen_kaart)
                self.kaart_toevoegen_deck(eigen_kaart)
                self.kaart_toevoegen_deck(andere_kaart)
                other.kaart_verwijderen_deck(andere_kaart)
                self.bonus_krijgen(bonus)
                print("Player is gewonnen")
                print(f"PlayerRes: {len(self.deck)}     ComRes:{len(other.deck)}")
                return True
            else:
                self.kaart_verwijderen_deck(eigen_kaart)
                other.kaart_verwijderen_deck(andere_kaart)
                other.kaart_toevoegen_deck(andere_kaart)
                other.kaart_toevoegen_deck(eigen_kaart)
                other.bonus_krijgen(bonus)
                print("Com is gewonnen")
                print(f"PlayerRes: {len(self.deck)}     ComRes:{len(other.deck)}")
                return False
        else:
            if eigen_kaart.isgroter(andere_kaart, attr):
                self.kaart_verwijderen_deck(eigen_kaart)
                other.kaart_verwijderen_deck(andere_kaart)
                other.kaart_toevoegen_deck(andere_kaart)
                other.kaart_toevoegen_deck(eigen_kaart)
                other.bonus_krijgen(bonus)
                print("Com is gewonnen")
                print(f"PlayerRes: {len(self.deck)}     ComRes:{len(other.deck)}")
                return False
            else:
                self.kaart_verwijderen_deck(eigen_kaart)
                self.kaart_toevoegen_deck(eigen_kaart)
                self.kaart_toevoegen_deck(andere_kaart)
                other.kaart_verwijderen_deck(andere_kaart)
                self.bonus_krijgen(bonus)
                print("Player is gewonnen")
                print(f"PlayerRes: {len(self.deck)}     ComRes:{len(other.deck)}")
                return True

    def is_niet_einde(self, other):
        if self.deck and other.deck:
            return True
        else:
            return False


def get_selected_number(kaart, hoger_lager):
    selected_number = None
    timer_seconds = 30
    button_zijde = 46
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
                if 2 <= mouse_x <= 2 + button_zijde and 350 <= mouse_y <= 350 + button_zijde:
                    selected_number = 1
                if 2 <= mouse_x <= 2 + button_zijde and 400 <= mouse_y <= 400 + button_zijde:
                    selected_number = 2
                if 2 <= mouse_x <= 2 + button_zijde and 450 <= mouse_y <= 450 + button_zijde:
                    selected_number = 3
                if 2 <= mouse_x <= 2 + button_zijde and 500 <= mouse_y <= 500 + button_zijde:
                    selected_number = 4
        # If a number is selected, break out of the loop and return the value
        if selected_number is not None:
            print(selected_number)
            return selected_number
        angle = 360 * (timer_seconds / 5)
        screen.fill(black)

        display_card(kaart, True)
        # Draw the circle
        pygame.draw.arc(screen, white, (width - 100, height - 100, 100, 100), math.radians(0), math.radians(angle), 5)

        # Draw the timer text
        timer_text = font.render(str(timer_seconds), True, white)
        text_rect = timer_text.get_rect(center=(width - 50, height - 50))
        screen.blit(timer_text, text_rect)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(1)

        # Update the timer
        timer_seconds -= 1

        # Check if the timer has reached 0
        if timer_seconds < 0:
            return rank_kaart_attr(kaart, hoger_lager)


random.seed(42)
random.shuffle(deck_dieren_excel)
deck1 = []
deck2 = []
for i in range(15):
    deck1.append(deck_dieren_excel[i])
    deck2.append(deck_dieren_excel[i + 15])
player = Player(deck1)
com = Player(deck2)

example_card = deck_dieren_excel[0]

# Create the screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Top Trumps Game")

# Load background image (replace 'background.jpg' with your image file)
background = pygame.image.load('fotos/start_screen.jpg')
background = pygame.transform.scale(background, (width, height))


# Fonts


def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


def start_screen():
    x1, x2 = screen.get_width() // 2.8, screen.get_width() // 1.5
    y1, y2 = screen.get_height() // 1.5625, screen.get_height() // 1.4
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
        screen.blit(background, (0, 0))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        pygame.time.Clock().tick(FPS)


def won_lost_screen(player_kaart, com_kaart, gewonnen_verloren):
    button_width, button_height = 150, 50
    button_x, button_y = (width - button_width) // 2, (height - button_height) - 5

    # Run the game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                    running = False

        screen.fill(black)
        display_card(player_kaart, True)
        display_card(com_kaart, False)
        # Draw the button
        pygame.draw.rect(screen, benazwart, (button_x, button_y, button_width, button_height))
        if gewonnen_verloren:
            button_text = font.render("Gewonnen", True, green)
        else:
            button_text = font.render("Verloren", True, red)
        button_text_rect = button_text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
        screen.blit(button_text, button_text_rect)

        # Update the display
        pygame.display.flip()


def timer_clock(timer_seconds, kaart):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(black)
        display_card(kaart, True)
        # Calculate the angle for the arc
        angle = 360 * (timer_seconds / 5)

        # Draw the circle
        pygame.draw.arc(screen, white, (screen.get_width()//2, screen.get_height()//2, 100, 100), math.radians(0), math.radians(angle), 5)

        # Draw the timer text
        timer_text = font.render(str(timer_seconds), True, white)
        text_rect = timer_text.get_rect(center=(width //2, height //2))
        screen.blit(timer_text, text_rect)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(1)

        # Update the timer
        timer_seconds -= 1

        # Check if the timer has reached 0
        if timer_seconds < 0:
            running = False


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
