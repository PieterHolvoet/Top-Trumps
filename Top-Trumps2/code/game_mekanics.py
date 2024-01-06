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


#geluid
path_music = os.path.join("Top-Trumps2","assets", "geluid", "music.mp3")
path_music_v2 = "../assets/geluid/music.mp3"
pygame.mixer.music.load(path_music)
pygame.mixer.music.play(-1)
#######
path_eind_screen = os.path.join("Top-Trumps2","assets","fotos","eind_screen.jpg")
path_eind_screen_V2 = "../assets/fotos/eind_screen.jpg"
#######

path_MinecraftRegular = os.path.join("Top-Trumps2","assets", "fonts", "MinecraftRegular-Bmg3.otf")
path_MinecraftRegular_V2 = "../assets/fonts/MinecraftRegular-Bmg3.otf"
path_start_screen = os.path.join("Top-Trumps2","assets","fotos","start_screen.jpg")
path_start_screen_V2 = "../assets/fotos/start_screen.jpg"
path_dierencsv = os.path.join("Top-Trumps2","assets","Dieren_TopTrumps.csv")
path_dierencsv_V2 = "../assets/Dieren_TopTrumps.csv"
path_MinecraftBoldItalic = os.path.join("Top-Trumps2","assets","fonts", "MinecraftBold-nMK1.otf")
path_MinecraftBoldItalic_V2 = "../assets/fonts/MinecraftBoldItalic-1y1e.otf"




FPS = 60
WIDTH = 800
HEIGHT = 800


FONT = pygame.font.Font(path_MinecraftRegular, int(WIDTH//40))
FONTSPELUITLEG = pygame.font.Font(path_MinecraftBoldItalic, int(WIDTH//45))
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


speluitleg_tekst = "Spelregels: Versla je tegenstander door alle"
speluitleg_tekst2 = "kaarten van het spel te bemachtigen! Wanneer"
speluitleg_tekst3 = "het jouw beurt is, kijk dan goed of het een"
speluitleg_tekst4 = "hoge of lage ronde is. Kies vervolgens de"
speluitleg_tekst5 = "eigenschap van jouw dier waarvan je denkt"
speluitleg_tekst6 = "dat deze hoger / lager is dan die van jouw"
speluitleg_tekst7 = "tegenstander. De ronde winnaar blijft aan"
speluitleg_tekst8 = "beurt en krijgt alle gespeelde kaarten."
speluitleg_tekst9 = "Leer zo alle dieren kennen om optimale"
speluitleg_tekst10= "keuzes te maken en te winnen tegen een"
speluitleg_tekst11= "makkelijke, gemiddelde of moeilijke tegenstander."


def start_screen():
    pygame.init()
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
        # Draw background and text
                    
        sc.blit(startscreen, (0, 0))

        # text speluitleg
        text = FONTSPELUITLEG.render(speluitleg_tekst, True, (0, 0, 0))  # Adjust color as needed
        sc.blit(text, (140,220))
        text2 = FONTSPELUITLEG.render(speluitleg_tekst2, True, (0, 0, 0))
        sc.blit(text2,(140,240))
        text3 = FONTSPELUITLEG.render(speluitleg_tekst3, True, (0, 0, 0))
        sc.blit(text3,(140,260))
        text4 = FONTSPELUITLEG.render(speluitleg_tekst4, True, (0, 0, 0))
        sc.blit(text4,(140,280))
        text5 = FONTSPELUITLEG.render(speluitleg_tekst5, True, (0, 0, 0))
        sc.blit(text5,(140,300))
        text6 = FONTSPELUITLEG.render(speluitleg_tekst6, True, (0, 0, 0))
        sc.blit(text6,(140,320))
        text7 = FONTSPELUITLEG.render(speluitleg_tekst7, True, (0, 0, 0))
        sc.blit(text7,(140,340))
        text8 = FONTSPELUITLEG.render(speluitleg_tekst8, True, (0, 0, 0))
        sc.blit(text8,(140,360))
        text9 = FONTSPELUITLEG.render(speluitleg_tekst9, True, (0, 0, 0))
        sc.blit(text9,(140,380))
        text10 = FONTSPELUITLEG.render(speluitleg_tekst10, True, (0, 0, 0))
        sc.blit(text10,(140,400))
        text11 = FONTSPELUITLEG.render(speluitleg_tekst11, True, (0, 0, 0))
        sc.blit(text11,(140,420))

        # if com.aantal_kaarten == 30 or player.aantal_kaarten == 30:
        #     end_image = pygame.image.load(path_eind_screen)
        #     sc.blit(end_image,(0,0))
        

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
        screen.display_in_a_match(kaart, hoger_lager, len(player.deck))
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
            return random.randint(1,4)


DECK_DIEREN_CSV = []
with open(path_dierencsv, 'r') as csv_bestand:
    csv_lezer = csv.reader(csv_bestand)
    header = next(csv_lezer)
    attr1, attr2, attr3, attr4 = header[1], header[2], header[3], header[4]
    for rij in csv_lezer:
        attr_lijst = [float(rij[1]), float(rij[2]), float(rij[3]), float(rij[4])]
        dier = card.Kaart(rij[0], attr_lijst)
        DECK_DIEREN_CSV.append(dier)
random.seed(1)
random.shuffle(DECK_DIEREN_CSV)
deck1 = []
deck2 = []
for i in range(15):
    deck1.append(DECK_DIEREN_CSV[i])
    deck2.append(DECK_DIEREN_CSV[i + 15])
player = pl.Player(deck1)
com = pl.Player(deck2)



#Stored-procedure sectie
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
                attribute_dict = {"Speed":1, "Weight":2, "Beauty":3, "Killer Instinct": 4}


            return attribute_dict.get(actual_value)

        except (Exception, psycopg2.Error) as error:
            print("Error calling the stored procedure:", error)

        finally:
            # Close the cursor and connection
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed.")

animal_dict = {
'Leeuw':1,
'Haai':2,
'Olifant':3,
'Bidsprinkhaan':4,
'Krokodil':5,
'Neushoorn':6,
'Panda':7,
'Eekhoorn':8,
'Zeearend':9,
'Orca':10,
'Mier':11,
'Tijger':12,
'Beer':13,
'Ijsbeer':14,
'Wolf':15,
'Python':16,
'Kraai':17,
'Impala':18,
'Schorpioen':19,
'Octopus':20,
'Siamese-kempvis':21,
'Blobvis':22,
'Gorilla':23,
'Chimpanzee':24,
'Eland':25,
'Hyena':26,
'Vos':27,
'Mammoet':28,
'Luiaard':29,
'Pinguin':30
}


def game_loop():
    while player.is_niet_einde(com):
        bonus_stapel = []
        boolean = True
        while boolean:
            if player.is_niet_einde(com):
                hoger_lager = (random.randint(1, 100) % 2 == 0)  # EVEN == HOGER
                player_kaart = player.pak_bovenste_kaart()
                com_kaart = com.pak_bovenste_kaart()
                screen.display_in_a_match(player_kaart, hoger_lager, len(player.deck))
                keuze = get_selected_number(player_kaart, hoger_lager)
                if player_kaart.isgelijk(com_kaart, keuze):
                    bonus_stapel.append(player_kaart)
                    bonus_stapel.append(com_kaart)
                    player.kaart_verwijderen_deck(player_kaart)
                    com.kaart_verwijderen_deck(com_kaart)
                    screen.won_lost_screen(player_kaart, com_kaart, 0, len(player.deck), len(com.deck), hoger_lager, keuze)
                    continue
                gewonnen = player.battle_andere_speler(com, keuze, bonus_stapel, hoger_lager)
                bonus_stapel = []
                screen.won_lost_screen(player_kaart, com_kaart, gewonnen, len(player.deck), len(com.deck), hoger_lager, keuze)
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
                game_difficulty = 'Easy'    # dit is voorlopig hard-coded op easy, wanneer start keuze scherm gemaakt is dan waarde aan deze variabele toeschrijven
                print('com_kaart naam: ', com_kaart.naam)
                comp_kaart = com_kaart.naam
                comp_kaart_id = animal_dict.get(comp_kaart)
                print('kaart id: ', comp_kaart_id)
                keuze = call_stored_procedure(comp_kaart_id, game_difficulty, hoger_lager)
                #keuze = card.rank_kaart_attr(com_kaart, hoger_lager)
                print('keuze: ', keuze)
                screen.timer_clock(5, player_kaart, hoger_lager, len(player.deck))
                if player_kaart.isgelijk(com_kaart, keuze):
                    bonus_stapel.append(player_kaart)
                    bonus_stapel.append(com_kaart)
                    player.kaart_verwijderen_deck(player_kaart)
                    com.kaart_verwijderen_deck(com_kaart)
                    screen.won_lost_screen(player_kaart, com_kaart, 0, len(player.deck), len(com.deck), hoger_lager, keuze)
                    continue
                gewonnen = player.battle_andere_speler(com, keuze, bonus_stapel, hoger_lager)
                bonus_stapel = []
                screen.won_lost_screen(player_kaart, com_kaart, gewonnen, len(player.deck), len(com.deck), hoger_lager, keuze)
                if gewonnen == -1:
                    continue

                boolean = False
                



start_screen()


