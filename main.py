import pygame

# pygame setup
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
dt = 0


player_pos = pygame.Vector2((screen.get_width() / 2) - 500, screen.get_height() / 2)
player2_pos = pygame.Vector2((screen.get_width() / 2) + 500, screen.get_height() / 2)

ball_pos = pygame.Vector2((screen_width() / 2) + 500, screen.get_height() / 2)

player_height = 100
player_width = 20

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    
    player = pygame.Rect(player_pos.x, player_pos.y, player_width, player_height)
    player2 = pygame.Rect(player2_pos.x, player2_pos.y, player_width, player_height)

    pygame.draw.rect(screen, "white", player)
    pygame.draw.rect(screen, "white", player2)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_UP]:
        player2_pos.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        player2_pos.y += 300 * dt

    if player_pos.y >= screen_height - player_height:
        player_pos.y = screen_height - player_height
    if player_pos.y <= 0:
        player_pos.y = 0
    
    if player2_pos.y >= screen_height - player_height:
        player2_pos.y = screen_height - player_height
    if player2_pos.y <= screen_height:
        player2_pos.y = screen_height
    


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
