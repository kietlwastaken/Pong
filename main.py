import pygame
import random
import time

# pygame setup
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
dt = 0


# font setup
font = pygame.font.Font(None, 74)  
largefont = pygame.font.Font(None, 80)

screen_width_center = screen_width / 2
screen_height_center = screen_height / 2
screen_center = (screen_width_center, screen_height_center)

# player variables
player_pos = pygame.Vector2((screen_width_center) - 500, screen_height_center)
player2_pos = pygame.Vector2((screen_width_center) + 500, screen_height_center)

player_height = 150
player_width = 20

player_score = 0
player2_score = 0

player_speed = 400


# ball variables
ball_pos = pygame.Vector2(screen_center)
ball_vel = pygame.Vector2(random.choice([1,-1]), random.choice([1,-1]))
ball_radius = 20
ball_speed = 300

ball_reset_time = 2000

ball_waiting = False
ball_vel_direction = 0


# move ball to center screen upon scoring
def reset_ball(direction):
    global ball_pos, ball_vel, ball_waiting, ball_reset_time
    ball_pos = pygame.Vector2(screen_center)
    ball_vel = pygame.Vector2(0, 0)
    ball_waiting = True
    ball_reset_time = pygame.time.get_ticks() + 2000  # Wait 2 seconds
    ball_vel_direction = direction


# if value higher than n set to n
def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))


# win
def win(winnercol):
    screen.fill(winnercol)
    screen.blit(wintext, (screen_center))  # you win!!!
    screen.blit(wintextbg, (screen_center))  # you win!!! bg

dt = clock.tick(60) / 1000  # Initialize dt with a valid value

winner = (0,0,0)
player_col = (255, 0, 136)
player2_col = (174, 122, 191)

# main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ball 2 second wait
    if ball_waiting and pygame.time.get_ticks() >= ball_reset_time:
        ball_vel = pygame.Vector2(1 if ball_vel_direction == 1 else -1, random.uniform(-0.5, 0.5)).normalize()
        ball_waiting = False


    screen.fill("black")

    
    # player rect creation
    player = pygame.Rect(player_pos.x, player_pos.y, player_width, player_height)
    player2 = pygame.Rect(player2_pos.x, player2_pos.y, player_width, player_height)

    
    # drawing player and ball
    pygame.draw.rect(screen, player_col, player)
    pygame.draw.rect(screen, player2_col, player2)

    pygame.draw.circle(screen, "white", ball_pos, ball_radius, width=0)
    

    # movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= player_speed * dt
    if keys[pygame.K_s]:
        player_pos.y += player_speed * dt

    if keys[pygame.K_UP]:
        player2_pos.y -= player_speed * dt
    if keys[pygame.K_DOWN]:
        player2_pos.y += player_speed * dt
    

    # no going off screen
    if player_pos.y >= screen_height - player_height:
        player_pos.y = screen_height - player_height
    if player_pos.y <= 0:
        player_pos.y = 0
    
    if player2_pos.y >= screen_height - player_height:
        player2_pos.y = screen_height - player_height
    if player2_pos.y <= 0:
        player2_pos.y = 0


    # move the ball
    if not ball_waiting:
        ball_pos += ball_vel * dt * ball_speed
        
        # wall bouncing
        if ball_pos.x - ball_radius <= 0 or ball_pos.x + ball_radius >= screen_width:
            ball_vel.x *= -1
        if ball_pos.y - ball_radius <= 0 or ball_pos.y + ball_radius >= screen_height:
            ball_vel.y *= -1
    

    # ball collision box
    ball_rect = pygame.Rect(ball_pos.x - ball_radius, ball_pos.y - ball_radius, ball_radius * 2, ball_radius * 2)


    # ball x player collision
    if ball_rect.colliderect(player) and ball_vel.x < 0:
        offset = (ball_pos.y - player.centery) / (player_height / 2)
        y_dir = clamp(offset, -0.7, 0.7)
        ball_vel = pygame.Vector2(1, y_dir).normalize()
        winner = player_col

    if ball_rect.colliderect(player2) and ball_vel.x > 0:
        offset = (ball_pos.y - player2.centery) / (player_height / 2)
        y_dir = clamp(offset, -0.7, 0.7)
        ball_vel = pygame.Vector2(-1, y_dir).normalize()
        winner = player2_col


    # Scoring and resetting the ball
    if ball_pos.x <= 0 + ball_radius:
        player2_score += 1
        reset_ball(-1)

    if ball_pos.x >= screen_width - ball_radius:
        player_score += 1
        reset_ball(1)


    # slowly speed up ball
    ball_speed += 2 * dt


    # score text
    score_text_player1 = font.render(f"{player_score}", True, pygame.Color(player_col))
    score_text_player2 = font.render(f"{player2_score}", True, pygame.Color(player2_col))
    separator_text = font.render("  -  ", True, pygame.Color(winner))
    wintext = font.render(f"you win!!!!!!!!!!!!!!!!!!!!!", True, pygame.Color(winner))
    wintextbg = largefont.render(f"you win!!!!!!!!!!!!!!!!!!!!!", True, pygame.Color(0,0,0))

    screen.blit(score_text_player1, (screen_width_center - score_text_player1.get_width() - 100, 30))  # Player 1 score
    screen.blit(separator_text, (screen_width_center - separator_text.get_width() / 2, 30))  # Separator
    screen.blit(score_text_player2, (screen_width_center + 100, 30))  # Player 2 score


    # winning
    if player_score >= 5:
        win(player_col)
    if player2_score >= 5:
        win(player2_col)


    pygame.display.flip()

    dt = clock.tick(60) / 1000  # Update dt for frame rate independence

pygame.quit()
