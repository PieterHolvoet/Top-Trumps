import random
import pygame
import sys
import csv
import math
import game_screen as screen
import kaart as card
import player as pl
import os
import psycopg2

# Kies het path door van eerste tot laatste selecteren dan Ctrl+/
# Path Pieter
# path_music = os.path.join("Top-Trumps2","assets", "geluid", "music.mp3")
# path_eind_screen = os.path.join("Top-Trumps2","assets","fotos","eind_screen.jpg")
# path_MinecraftRegular = os.path.join("Top-Trumps2","assets", "fonts", "MinecraftRegular-Bmg3.otf")
# path_start_screen = os.path.join("Top-Trumps2","assets","fotos","start_screen.jpg")
# path_eind_screen = os.path.join("Top-Trumps2", "assets", "fotos", "achterkant_kaart.jpg")
# path_dierencsv = os.path.join("Top-Trumps2","assets","Dieren_TopTrumps.csv")
# path_MinecraftBoldItalic = os.path.join("Top-Trumps2","assets","fonts", "MinecraftBold-nMK1.otf")


# Path Joren/Ridha
path_MinecraftRegular = "../assets/fonts/MinecraftRegular-Bmg3.otf"
path_start_screen = "../assets/fotos/start_screen.jpg"
path_eind_screen = "../assets/fotos/eind_screen.jpg"
path_dierencsv = "../assets/Dieren_TopTrumps.csv"
path_MinecraftBoldItalic = "../assets/fonts/MinecraftBoldItalic-1y1e.otf"
path_music = "../assets/geluid/music.mp3"

# geluid
pygame.mixer.music.load(path_music)
pygame.mixer.music.play(-1)
#######
#######


FPS = 60
WIDTH = 800
HEIGHT = 800

FONT = pygame.font.Font(path_MinecraftRegular, int(WIDTH // 40))
FONTSPELUITLEG = pygame.font.Font(path_MinecraftBoldItalic, int(WIDTH // 45))
GROOTFONT = pygame.font.Font(path_MinecraftRegular, int(WIDTH // 10))

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (169, 169, 169)

sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top Trumps")
clock = pygame.time.Clock()

startscreen = pygame.image.load(path_start_screen)
startscreen = pygame.transform.scale(startscreen, (WIDTH, HEIGHT))

endscreen = pygame.image.load(path_eind_screen)
endscreen = pygame.transform.scale(endscreen, (WIDTH, HEIGHT))
def start_screen():
    pygame.init()
    x1, x2 = WIDTH // 2.8, WIDTH // 1.5
    y1, y2 = HEIGHT // 1.5625, HEIGHT // 1.4
    running = True
    selected_difficulty = "Easy"
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False
                    game_loop(selected_difficulty)  # Call the game loop function when Enter key is pressed
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print(mouse_x)
                print(mouse_y)
                print()
                if x1 <= mouse_x <= x2 and y1 <= mouse_y <= y2:
                    running = False
                    game_loop(selected_difficulty)
                # Check if any difficulty box is clicked
                difficulties = ["Easy", "Medium", "Hard"]
                for i, difficulty in enumerate(difficulties):
                    rect = pygame.Rect((WIDTH - 200) // 2, i * (50 + 20) + 580, 200, 50)
                    if rect.collidepoint(event.pos):
                        selected_difficulty = difficulty
        sc.fill(WHITE)
        sc.blit(startscreen, (0, 0))
        screen.draw_difficulty_boxes(selected_difficulty)
        screen.spel_uitleg()
        pygame.display.flip()

        # if com.aantal_kaarten == 30 or player.aantal_kaarten == 30:
        #     end_image = pygame.image.load(path_eind_screen)
        #     sc.blit(end_image,(0,0))

        pygame.time.Clock().tick(FPS)


def get_selected_number(kaart, hoger_lager, len_player_kaarten):
    selected_number = None
    timer_seconds = 30
    x1, x2 = WIDTH // 2.666, WIDTH // 1.616
    y1, y2, y3, y4, y5 = HEIGHT // 1.212, HEIGHT // 1.161, HEIGHT // 1.117, HEIGHT // 1.0796, HEIGHT // 1.0376
    while True:
        for event in pygame.event.get():
            mouse_x, mouse_y = pygame.mouse.get_pos()
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
        screen.display_in_a_match(kaart, hoger_lager, len_player_kaarten)
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
            return random.randint(1, 4)


DECK_DIEREN_CSV = []
with open(path_dierencsv, 'r') as csv_bestand:
    csv_lezer = csv.reader(csv_bestand)
    header = next(csv_lezer)
    attr1, attr2, attr3, attr4 = header[1], header[2], header[3], header[4]
    for rij in csv_lezer:
        attr_lijst = [float(rij[1]), float(rij[2]), float(rij[3]), float(rij[4])]
        dier = card.Kaart(rij[0], attr_lijst)
        DECK_DIEREN_CSV.append(dier)
# random.seed(1)
# random.shuffle(DECK_DIEREN_CSV)
# deck1 = []
# deck2 = []
# for i in range(2):  # 15 standaard
#     deck1.append(DECK_DIEREN_CSV[i])
#     deck2.append(DECK_DIEREN_CSV[i + 15])
# player = pl.Player(deck1)
# com = pl.Player(deck2)

# Stored-procedure sectie
# Update these variables with your PostgreSQL database credentials
db_credentials = {
    'host': 'localhost',
    'database': 'Toptrumpsdb',
    'user': 'postgres',
    'password': 'wachtwoord',
    'port': '5432',  # Default is 5432
}


def connect_to_database():
    try:
        # Establish a connection to the PostgreSQL database
        connection = psycopg2.connect(**db_credentials)
        cursor = connection.cursor()
        return connection, cursor

    except (Exception, psycopg2.Error) as error:
        print("Error connecting to PostgreSQL database:", error)
        return None, None


def call_stored_procedure(id, difficulty, higher_lower):
    connection, cursor = connect_to_database()

    if connection and cursor:
        try:
            # Execute a stored procedure
            cursor.callproc('get_computer_choice', (id, difficulty, higher_lower))  # Replace with actual parameters

            # Fetch the results if the stored procedure returns any
            results = cursor.fetchall()
            # Get the string value out of the tuple
            if results:
                actual_value = results[0]
                if isinstance(actual_value, tuple):
                    actual_value = actual_value[0]
                attribute_dict = {"Speed": 1, "Weight": 2, "Beauty": 3, "Killer Instinct": 4}

            return attribute_dict.get(actual_value)

        except (Exception, psycopg2.Error) as error:
            print("Error calling the stored procedure:", error)

        finally:
            # Close the cursor and connection
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed.")


animal_dict = {
    'Leeuw': 1,
    'Haai': 2,
    'Olifant': 3,
    'Bidsprinkhaan': 4,
    'Krokodil': 5,
    'Neushoorn': 6,
    'Panda': 7,
    'Eekhoorn': 8,
    'Zeearend': 9,
    'Orca': 10,
    'Mier': 11,
    'Tijger': 12,
    'Beer': 13,
    'Ijsbeer': 14,
    'Wolf': 15,
    'Python': 16,
    'Kraai': 17,
    'Impala': 18,
    'Schorpioen': 19,
    'Octopus': 20,
    'Siamese-kempvis': 21,
    'Blobvis': 22,
    'Gorilla': 23,
    'Chimpanzee': 24,
    'Eland': 25,
    'Hyena': 26,
    'Vos': 27,
    'Mammoet': 28,
    'Luiaard': 29,
    'Pinguin': 30
}


def game_loop(difficulty):
    player, com = shuffle_deal()
    while player.is_niet_einde(com):
        bonus_stapel = []
        boolean = True
        while boolean:
            if player.is_niet_einde(com):
                hoger_lager = (random.randint(1, 100) % 2 == 0)  # EVEN == HOGER
                player_kaart = player.pak_bovenste_kaart()
                com_kaart = com.pak_bovenste_kaart()
                screen.display_in_a_match(player_kaart, hoger_lager, len(player.deck))
                keuze = get_selected_number(player_kaart, hoger_lager, len(player.deck))
                if player_kaart.isgelijk(com_kaart, keuze):
                    bonus_stapel.append(player_kaart)
                    bonus_stapel.append(com_kaart)
                    player.kaart_verwijderen_deck(player_kaart)
                    com.kaart_verwijderen_deck(com_kaart)
                    screen.won_lost_screen(player_kaart, com_kaart, 0, len(player.deck), len(com.deck), hoger_lager,
                                           keuze)
                    continue
                gewonnen = player.battle_andere_speler(com, keuze, bonus_stapel, hoger_lager)
                bonus_stapel = []
                screen.won_lost_screen(player_kaart, com_kaart, gewonnen, len(player.deck), len(com.deck), hoger_lager,
                                       keuze)
                if gewonnen == 1:
                    continue
            boolean = False

        bonus_stapel = []
        boolean = True
        while boolean:
            if player.is_niet_einde(com):
                hoger_lager = (random.randint(1, 100) % 2 == 0)  # EVEN == HOGER
                player_kaart = player.pak_bovenste_kaart()
                com_kaart = com.pak_bovenste_kaart()
                screen.display_in_a_match(player_kaart, hoger_lager, len(player.deck))
                game_difficulty = 'Easy'  # dit is voorlopig hard-coded op easy, wanneer start keuze scherm gemaakt is dan waarde aan deze variabele toeschrijven
                print('com_kaart naam: ', com_kaart.naam)
                comp_kaart = com_kaart.naam
                comp_kaart_id = animal_dict.get(comp_kaart)
                print('kaart id: ', comp_kaart_id)
                keuze = call_stored_procedure(comp_kaart_id, difficulty, hoger_lager)
                if keuze is None:
                    keuze = card.rank_kaart_attr(com_kaart, hoger_lager)
                print('keuze: ', keuze)
                screen.timer_clock(5, player_kaart, hoger_lager, len(player.deck))
                if player_kaart.isgelijk(com_kaart, keuze):
                    bonus_stapel.append(player_kaart)
                    bonus_stapel.append(com_kaart)
                    player.kaart_verwijderen_deck(player_kaart)
                    com.kaart_verwijderen_deck(com_kaart)
                    screen.won_lost_screen(player_kaart, com_kaart, 0, len(player.deck), len(com.deck), hoger_lager,
                                           keuze)
                    continue
                gewonnen = player.battle_andere_speler(com, keuze, bonus_stapel, hoger_lager)
                bonus_stapel = []
                screen.won_lost_screen(player_kaart, com_kaart, gewonnen, len(player.deck), len(com.deck), hoger_lager,
                                       keuze)
                if gewonnen == -1:
                    continue

            boolean = False
    print("Einde")
    if len(player.deck) == 0:
        speler_gewonnen = False
    else:
        speler_gewonnen = True
    end_screen(speler_gewonnen)

def shuffle_deal():
    random.shuffle(DECK_DIEREN_CSV)
    deck1 = []
    deck2 = []
    for i in range(2):  # 15 standaard
        deck1.append(DECK_DIEREN_CSV[i])
        deck2.append(DECK_DIEREN_CSV[i + 15])
    player = pl.Player(deck1)
    com = pl.Player(deck2)
    return player, com
def end_screen(speler_gewonnen):
    box_width, box_height = 300, 80
    box_width2, box_height2 = 400, 80
    selected_difficulty = "Easy"
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    shuffle_deal()
                    running = False
                    game_loop(selected_difficulty)  # Call the game loop function when Enter key is pressed
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print(mouse_x)
                print(mouse_y)
                print()
                if (WIDTH-box_width)//2 <= mouse_x <= ((WIDTH-box_width)//2)+box_width and 400 <= mouse_y <= 400+box_height:
                    shuffle_deal()
                    running = False
                    game_loop(selected_difficulty)
                # Check if any difficulty box is clicked
                difficulties = ["Easy", "Medium", "Hard"]
                for i, difficulty in enumerate(difficulties):
                    rect = pygame.Rect((WIDTH - 200) // 2, i * (50 + 20) + 580, 200, 50)
                    if rect.collidepoint(event.pos):
                        selected_difficulty = difficulty
        # Draw background
        sc.blit(endscreen, (0, 0))
        screen.draw_difficulty_boxes(selected_difficulty)
        rect_gewonnen = pygame.Rect((WIDTH-box_width2)//2, box_height2 + 100, box_width2, box_height2)
        pygame.draw.rect(sc, GRAY, rect_gewonnen)
        pygame.draw.rect(sc, BLACK, rect_gewonnen, 2)
        if speler_gewonnen:
            gewonnen_text = GROOTFONT.render("Gewonnen", True, GREEN)
            gewonnen_rect = gewonnen_text.get_rect(center=rect_gewonnen.center)
        else:
            gewonnen_text = GROOTFONT.render("Verloren", True, RED)
            gewonnen_rect = gewonnen_text.get_rect(center=rect_gewonnen.center)
        sc.blit(gewonnen_text, gewonnen_rect)
        rect_start = pygame.Rect((WIDTH - box_width) // 2, box_height + 300, box_width, box_height)
        pygame.draw.rect(sc, GRAY, rect_start)
        pygame.draw.rect(sc, BLACK, rect_start, 2)

        start_text = GROOTFONT.render("Start", True, BLACK)
        start_rect = start_text.get_rect(center=rect_start.center)
        sc.blit(start_text, start_rect)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        pygame.time.Clock().tick(FPS)


start_screen()
