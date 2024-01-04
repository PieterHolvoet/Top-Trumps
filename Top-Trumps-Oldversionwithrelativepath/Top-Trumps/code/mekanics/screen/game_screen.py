import pygame

pygame.init()

# Minecraft Font :)
FONT = pygame.font.Font('.././fonts/MinecraftRegular-Bmg3.otf', 20)
MEDIUMFONT = pygame.font.Font('.././fonts/MinecraftRegular-Bmg3.otf', 46)
GROOTFONT = pygame.font.Font('.././fonts/MinecraftRegular-Bmg3.otf', 80)
FPS = 60
WIDTH = 800
HEIGHT = 800

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up display

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top Trumps")
clock = pygame.time.Clock()

startscreen = pygame.image.load(".././fotos/spel/start_screen.jpg")
startscreen = pygame.transform.scale(startscreen, (WIDTH, HEIGHT))

background = pygame.image.load(".././fotos/spel/background_topTrumps.JPG")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

ttFront = pygame.image.load('.././fotos/spel/voorkant_kaart.jpg')
ttFront = pygame.transform.scale(ttFront, (WIDTH // 3.333, HEIGHT // 2.5))

ttBack = pygame.image.load('.././fotos/spel/achterkant_kaart.jpg')
ttBack = pygame.transform.rotate(ttBack, 180)
ttBack = pygame.transform.scale(ttBack, (WIDTH // 3.333, HEIGHT // 2.5))


def display_in_a_match(card, hoger_lager):
    x1, x2 = 395, 495
    ylist = [689, 716, 741, 771]
    screen.blit(background, (0, 0 - HEIGHT * 0.02))
    screen.blit(ttFront, ((WIDTH / 2) - (ttFront.get_width() / 2), HEIGHT - ttFront.get_height()))
    screen.blit(ttBack, ((WIDTH / 2) - (ttBack.get_width() / 2), 0))
    image = pygame.image.load(f".././fotos/dieren/{card.naam}.JPG")
    image = pygame.transform.scale(image, (WIDTH // 4.4, HEIGHT // 6.7))
    screen.blit(image, (313, 540))
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
        screen.blit(attr_surface,
                    ((WIDTH // 2) + (WIDTH // 15), HEIGHT * (0.83 + (i * 0.035))))
    pygame.display.flip()


def won_lost_screen(player_kaart, com_kaart, gewonnen_verloren, player_aantal, com_aantal, hoger_lager, choice):
    running = True
    player_kaarten = f"{player_aantal}"
    com_kaarten = f"{com_aantal}"
    keuze = f"{choice}"
    display_in_a_match(player_kaart, hoger_lager)
    x1, x2, y1, y2 = 250, 550, 330, 470
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
        image = pygame.image.load(f".././fotos/dieren/{com_kaart.naam}.JPG")
        image = pygame.transform.scale(image, (WIDTH // 4.4, HEIGHT // 6.7))
        screen.blit(image, (313, 55))
        for i in range(4):
            attr_value = f"{com_kaart.attr_list[i]}"
            attr_surface = FONT.render(attr_value, True, WHITE)
            screen.blit(attr_surface,
                        ((WIDTH // 2) + (WIDTH // 15), HEIGHT * (0.23 + (i * 0.035))))

        if gewonnen_verloren:
            gewonnen_verloren_txt = "Gewonnen"
            gewonnen_verloren_txt = MEDIUMFONT.render(gewonnen_verloren_txt, True, GREEN)
        else:
            gewonnen_verloren_txt = "Verloren"
            gewonnen_verloren_txt = MEDIUMFONT.render(gewonnen_verloren_txt, True, RED)
        next = GROOTFONT.render("Verder", True, WHITE)
        screen.blit(next, (WIDTH // 2 - 130, HEIGHT // 2 - 40))
        screen.blit(gewonnen_verloren_txt, (WIDTH * 0.72, HEIGHT * 0.01))
        player_aantal = FONT.render(player_kaarten, True, WHITE)
        com_aantal = FONT.render(com_kaarten, True, WHITE)
        screen.blit(com_aantal, ((WIDTH // 2) + (WIDTH // 15), HEIGHT * 0.025))
        screen.blit(player_aantal, ((WIDTH // 2) + (WIDTH // 15), HEIGHT * 0.625))
        keuzeTekst = GROOTFONT.render(keuze, True, WHITE)
        screen.blit(keuzeTekst, (WIDTH * 0.86, HEIGHT // 2 - 40))
        pygame.display.flip()


# def start_screen():
#     x1, x2 = sc.get_width() // 2.8, sc.get_width() // 1.5
#     y1, y2 = sc.get_height() // 1.5625, sc.get_height() // 1.4
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_RETURN:
#                     running = False
#                     game_loop()  # Call the game loop function when Enter key is pressed
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_x, mouse_y = pygame.mouse.get_pos()
#                 print(mouse_x)
#                 print(mouse_y)
#                 print()
#                 if x1 <= mouse_x <= x2 and y1 <= mouse_y <= y2:
#                     running = False
#                     game_loop()
#         # Draw background
#         sc.blit(startscreen, (0, 0))
#
#         # Update the display
#         pygame.display.flip()
#
#         # Cap the frame rate
#         pygame.time.Clock().tick(FPS)


def timer_clock(timer_seconds, kaart, hoger_lager):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # sc.fill(BLACK)
        display_in_a_match(kaart, hoger_lager)
        timer_text = GROOTFONT.render(str(timer_seconds), True, WHITE)
        text_rect = timer_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(timer_text, text_rect)

        pygame.display.flip()
        clock.tick(1)
        timer_seconds -= 1

        if timer_seconds < 0:
            running = False
