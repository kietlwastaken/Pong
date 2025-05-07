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

ball_pos = pygame.Vector2((screen.get_width / 2), screen.get_height() / 2)
ball_vel = pygame.Vector2(1,0)
ball_radius = 20

player_height = 150
player_width = 20

player_speed = 400

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
        player_pos.y -= player_speed * dt
    if keys[pygame.K_s]:
        player_pos.y += player_speed * dt
    if keys[pygame.K_UP]:
        player2_pos.y -= player_speed * dt
    if keys[pygame.K_DOWN]:
        player2_pos.y += player_speed * dt

    if player_pos.y >= screen_height - player_height:
        player_pos.y = screen_height - player_height
    if player_pos.y <= 0:
        player_pos.y = 0
    
    if player2_pos.y >= screen_height - player_height:
        player2_pos.y = screen_height - player_height
    if player2_pos.y <= 0:
        player2_pos.y = 0

    
    ball_pos += ball_vel * dt

    if ball_pos.x - ball_radius <= 0 or ball_pos.x + ball_radius >= screen_width:
        ball_vel.x *= -1
    if ball_pos.y - ball_radius <= 0 or ball_pos.y + ball_radius >= screen_height:
        ball_vel.y *= -1

    ball_rect = pygame.Rect(ball_pos.x - ball_radius, ball_pos.y - ball_radius, ball_radius * 2, ball_radius * 2)

    # Bounce off paddles
    if ball_rect.colliderect(player) and ball_vel.x < 0:
        ball_vel.x *= -1
    if ball_rect.colliderect(player2) and ball_vel.x > 0:
        ball_vel.x *= -1

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
