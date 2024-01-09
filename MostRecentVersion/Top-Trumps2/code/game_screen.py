import pygame
import os
pygame.init()

FPS = 60
WIDTH = 800
HEIGHT = 800

# path_MinecraftRegular = os.path.join("Top-Trumps2", "assets", "fonts", "MinecraftRegular-Bmg3.otf")
# path_MinecraftBoldItalic = os.path.join("Top-Trumps2","assets","fonts", "MinecraftBold-nMK1.otf")
# path_start_screen = os.path.join("Top-Trumps2", "assets", "fotos", "start_screen.jpg")
# path_background = os.path.join("Top-Trumps2", "assets", "fotos", "background_topTrumps.JPG")
# path_voorkant = os.path.join("Top-Trumps2", "assets", "fotos", "voorkant_kaart.jpg")
# path_achterkant = os.path.join("Top-Trumps2", "assets", "fotos", "achterkant_kaart.jpg")
# path_eind_screen = os.path.join("Top-Trumps2", "assets", "fotos", "achterkant_kaart.jpg")

path_start_screen = "../assets/fotos/start_screen.jpg"
path_eind_screen = "../assets/fotos/eind_screen.jpg"
path_background = "../assets/fotos/background_topTrumps.JPG"
path_voorkant = "../assets/fotos/voorkant_kaart.jpg"
path_achterkant= "../assets/fotos/achterkant_kaart.jpg"
path_MinecraftRegular = "../assets/fonts/MinecraftRegular-Bmg3.otf"
path_MinecraftBoldItalic = "../assets/fonts/MinecraftBoldItalic-1y1e.otf"

# Minecraft Font :)
FONT = pygame.font.Font(path_MinecraftRegular, int(WIDTH // 40))
MEDIUMFONT = pygame.font.Font(path_MinecraftRegular, int(WIDTH // 17.4))
GROOTFONT = pygame.font.Font(path_MinecraftRegular, int(WIDTH // 10))
FONTSPELUITLEG = pygame.font.Font(path_MinecraftBoldItalic, int(WIDTH // 45))

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (169, 169, 169)

# Set up display



screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top Trumps")
clock = pygame.time.Clock()

startscreen = pygame.image.load(path_start_screen)
startscreen = pygame.transform.scale(startscreen, (WIDTH, HEIGHT))

endscreen = pygame.image.load(path_eind_screen)
endscreen = pygame.transform.scale(endscreen, (WIDTH, HEIGHT))

background = pygame.image.load(path_background)
background = pygame.transform.scale(background, (WIDTH, HEIGHT + 20))

ttFront = pygame.image.load(path_voorkant)
ttFront = pygame.transform.scale(ttFront, (WIDTH // 3.333, HEIGHT // 2.5))

ttBack = pygame.image.load(path_achterkant)
ttBack = pygame.transform.rotate(ttBack, 180)
ttBack = pygame.transform.scale(ttBack, (WIDTH // 3.333, HEIGHT // 2.5))

# path_animalcards = os.path.join("Top-Trumps2", "assets", "fotos","animal_cards", "start_screen.jpg") #word nergens gebruikt???  dus mss f-strings werken wel????

def display_in_a_match(card, hoger_lager, aantal_player_kaarten):
    player_kaarten = f"{aantal_player_kaarten}"
    x1, x2 = WIDTH // 2.025, WIDTH // 1.616
    ylist = [HEIGHT // 1.161, HEIGHT // 1.117, HEIGHT // 1.0796, HEIGHT // 1.0376]
    screen.blit(background, (0, 0 - HEIGHT * 0.02))
    screen.blit(ttFront, ((WIDTH // 2) - (ttFront.get_width() // 2), HEIGHT - ttFront.get_height()))
    screen.blit(ttBack, ((WIDTH // 2) - (ttBack.get_width() // 2), 0))
    image = pygame.image.load(f"../assets/fotos/animals_cards/{card.naam}.JPG")
    image = pygame.transform.scale(image, (WIDTH // 4.4, HEIGHT // 6.7))
    screen.blit(image, (WIDTH // 2.556, HEIGHT // 1.48))
    for y in ylist:
        pygame.draw.line(screen, WHITE, (x1, y), (x2, y))

    if hoger_lager:
        hoger_lager_text = "Hoger"
    else:
        hoger_lager_text = "Lager"
    hoger_lager_text = MEDIUMFONT.render(hoger_lager_text, True, WHITE)
    screen.blit(hoger_lager_text, (WIDTH * 0.8, HEIGHT * 0.06))

    name_text = FONT.render(card.naam, True, (255, 255, 255))
    screen.blit(name_text, (WIDTH // 2 - (WIDTH // 10.666), HEIGHT * 0.64))

    for i in range(4):
        attr_value = f"{card.attr_list[i]}"
        attr_surface = FONT.render(attr_value, True, WHITE)
        x_offset = len(attr_value) * WIDTH // 72.727
        screen.blit(attr_surface,
                    ((WIDTH // 2) + (WIDTH // 8) - x_offset, HEIGHT * (0.83 + (i * 0.035))))
    player_aantal = FONT.render(player_kaarten, True, WHITE)
    screen.blit(player_aantal, ((WIDTH // 2) + (WIDTH // 15), HEIGHT * 0.625))

    pygame.display.flip()


def won_lost_screen(player_kaart, com_kaart, gewonnen_verloren, player_aantal, com_aantal, hoger_lager, choice):
    running = True
    player_kaarten = f"{player_aantal}"
    com_kaarten = f"{com_aantal}"
    keuze = f"{choice}"
    display_in_a_match(player_kaart, hoger_lager, player_aantal)
    x1, x2, y1, y2 = WIDTH // 3.2, WIDTH // 1.454, HEIGHT // 2.424, HEIGHT // 1.7
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if x1 <= mouse_x <= x2 and y1 <= mouse_y <= y2:
                    running = False
        screen.blit(ttFront, ((WIDTH / 2) - (ttBack.get_width() / 2), 0))

        name_text = FONT.render(com_kaart.naam, True, WHITE)
        screen.blit(name_text, (WIDTH // 2 - (WIDTH // 10.666), HEIGHT * 0.04))
        image = pygame.image.load(f"../assets/fotos/animals_cards/{com_kaart.naam}.JPG")
        image = pygame.transform.scale(image, (WIDTH // 4.4, HEIGHT // 6.7))
        screen.blit(image, (WIDTH // 2.556, HEIGHT // 14.545))
        for i in range(4):
            attr_value = f"{com_kaart.attr_list[i]}"
            x_offset = len(attr_value) * WIDTH // 72.727
            attr_surface = FONT.render(attr_value, True, WHITE)
            screen.blit(attr_surface,
                        ((WIDTH // 2) + (WIDTH // 8) - x_offset, HEIGHT * (0.23 + (i * 0.035))))

        if gewonnen_verloren == 1:
            gewonnen_verloren_txt = "Gewonnen"
            gewonnen_verloren_txt = MEDIUMFONT.render(gewonnen_verloren_txt, True, GREEN)
        elif gewonnen_verloren == -1:
            gewonnen_verloren_txt = "Verloren"
            gewonnen_verloren_txt = MEDIUMFONT.render(gewonnen_verloren_txt, True, RED)
        else:
            gewonnen_verloren_txt = "Gelijk"
            gewonnen_verloren_txt = MEDIUMFONT.render(gewonnen_verloren_txt, True, YELLOW)
        next = GROOTFONT.render("Verder", True, WHITE)
        screen.blit(next, (WIDTH // 2 - WIDTH // 6.145, HEIGHT // 2 - HEIGHT // 20))
        screen.blit(gewonnen_verloren_txt, (WIDTH * 0.72, HEIGHT * 0.01))
        # player_aantal = FONT.render(player_kaarten, True, WHITE)
        com_aantal = FONT.render(com_kaarten, True, WHITE)
        screen.blit(com_aantal, ((WIDTH // 2) + (WIDTH // 15), HEIGHT * 0.025))
        # screen.blit(player_aantal, ((WIDTH // 2) + (WIDTH // 15), HEIGHT * 0.625))

        keuzeTekst = GROOTFONT.render(keuze, True, WHITE)
        screen.blit(keuzeTekst, (WIDTH * 0.86, HEIGHT // 2 - HEIGHT // 20))
        pygame.display.flip()




def timer_clock(timer_seconds, kaart, hoger_lager, player_aantal):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # sc.fill(BLACK)
        display_in_a_match(kaart, hoger_lager, player_aantal)
        timer_text = GROOTFONT.render(str(timer_seconds), True, WHITE)
        text_rect = timer_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(timer_text, text_rect)

        pygame.display.flip()
        clock.tick(1)
        timer_seconds -= 1

        if timer_seconds < 0:
            running = False


def draw_difficulty_boxes(selected_difficulty):
    difficulties = ["Easy", "Medium", "Hard"]
    box_width, box_height = 200, 50
    margin = 20

    for i, difficulty in enumerate(difficulties):
        rect = pygame.Rect((WIDTH - box_width) // 2, i * (box_height + margin) + 580, box_width, box_height)
        color = GREEN if selected_difficulty == difficulty else GRAY

        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)

        text = MEDIUMFONT.render(difficulty, True, BLACK)
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)

def spel_uitleg():
    speluitleg_tekst = "Spelregels: Versla je tegenstander door alle"
    speluitleg_tekst2 = "kaarten van het spel te bemachtigen! Wanneer"
    speluitleg_tekst3 = "het jouw beurt is, kijk dan goed of het een"
    speluitleg_tekst4 = "hoge of lage ronde is. Kies vervolgens de"
    speluitleg_tekst5 = "eigenschap van jouw dier waarvan je denkt"
    speluitleg_tekst6 = "dat deze hoger / lager is dan die van jouw"
    speluitleg_tekst7 = "tegenstander. De ronde winnaar blijft aan"
    speluitleg_tekst8 = "beurt en krijgt alle gespeelde kaarten."
    speluitleg_tekst9 = "Leer zo alle dieren kennen om optimale"
    speluitleg_tekst10 = "keuzes te maken en te winnen tegen een"
    speluitleg_tekst11 = "makkelijke, gemiddelde of moeilijke tegenstander."

    text = FONTSPELUITLEG.render(speluitleg_tekst, True, BLACK)  # Adjust color as needed
    screen.blit(text, (140, 220))
    text2 = FONTSPELUITLEG.render(speluitleg_tekst2, True, BLACK)
    screen.blit(text2, (140, 240))
    text3 = FONTSPELUITLEG.render(speluitleg_tekst3, True, BLACK)
    screen.blit(text3, (140, 260))
    text4 = FONTSPELUITLEG.render(speluitleg_tekst4, True, BLACK)
    screen.blit(text4, (140, 280))
    text5 = FONTSPELUITLEG.render(speluitleg_tekst5, True, BLACK)
    screen.blit(text5, (140, 300))
    text6 = FONTSPELUITLEG.render(speluitleg_tekst6, True, BLACK)
    screen.blit(text6, (140, 320))
    text7 = FONTSPELUITLEG.render(speluitleg_tekst7, True, BLACK)
    screen.blit(text7, (140, 340))
    text8 = FONTSPELUITLEG.render(speluitleg_tekst8, True, BLACK)
    screen.blit(text8, (140, 360))
    text9 = FONTSPELUITLEG.render(speluitleg_tekst9, True, BLACK)
    screen.blit(text9, (140, 380))
    text10 = FONTSPELUITLEG.render(speluitleg_tekst10, True, BLACK)
    screen.blit(text10, (140, 400))
    text11 = FONTSPELUITLEG.render(speluitleg_tekst11, True, BLACK)
    screen.blit(text11, (140, 420))
