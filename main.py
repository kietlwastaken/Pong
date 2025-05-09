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


ball_vel_direction = 1

player_pos = pygame.Vector2((screen_width / 2) - 500, screen_height / 2)
player2_pos = pygame.Vector2((screen_width / 2) + 500, screen_height / 2)

ball_waiting = False

player_score = 0
player2_score = 0

ball_pos = pygame.Vector2((screen_width / 2), screen_height / 2)
ball_vel = pygame.Vector2(random.choice([1,-1]), random.choice([1,-1]))
ball_radius = 20
ball_speed = 300  # Adjust speed to suit your preference

player_height = 150
player_width = 20

player_speed = 400

ball_reset_time = 0  # Time at which to restart the ball


def reset_ball(direction):
    global ball_pos, ball_vel, ball_waiting, ball_reset_time
    ball_pos = pygame.Vector2(screen_width / 2, screen_height / 2)
    ball_vel = pygame.Vector2(0, 0)
    ball_waiting = True
    ball_reset_time = pygame.time.get_ticks() + 2000  # Wait 2 seconds
    ball_vel_direction = direction


def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))

dt = clock.tick(60) / 1000  # Initialize dt with a valid value


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if ball_waiting and pygame.time.get_ticks() >= ball_reset_time:
        ball_vel = pygame.Vector2(1 if ball_vel_direction == 1 else -1, random.uniform(-0.5, 0.5)).normalize()
        ball_waiting = False


    screen.fill("black")

    player = pygame.Rect(player_pos.x, player_pos.y, player_width, player_height)
    player2 = pygame.Rect(player2_pos.x, player2_pos.y, player_width, player_height)

    pygame.draw.rect(screen, (255, 0, 136), player)
    pygame.draw.rect(screen, (174, 122, 191), player2)

    pygame.draw.circle(screen, "white", ball_pos, ball_radius, width=0)

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

    if not ball_waiting:  # Only move the ball if it's not waiting
        ball_pos += ball_vel * dt * ball_speed

        if ball_pos.x - ball_radius <= 0 or ball_pos.x + ball_radius >= screen_width:
            ball_vel.x *= -1
        if ball_pos.y - ball_radius <= 0 or ball_pos.y + ball_radius >= screen_height:
            ball_vel.y *= -1

    ball_rect = pygame.Rect(ball_pos.x - ball_radius, ball_pos.y - ball_radius, ball_radius * 2, ball_radius * 2)

    if ball_rect.colliderect(player) and ball_vel.x < 0:
        offset = (ball_pos.y - player.centery) / (player_height / 2)
        y_dir = clamp(offset, -0.7, 0.7)
        ball_vel = pygame.Vector2(1, y_dir).normalize()
        winner = 255, 0, 136

    if ball_rect.colliderect(player2) and ball_vel.x > 0:
        offset = (ball_pos.y - player2.centery) / (player_height / 2)
        y_dir = clamp(offset, -0.7, 0.7)
        ball_vel = pygame.Vector2(-1, y_dir).normalize()
        winner = (174, 122, 191)

    # Scoring and resetting the ball
    if ball_pos.x <= 0 + ball_radius:
        player2_score += 1
        reset_ball(-1)

            
    if ball_pos.x >= screen_width - ball_radius:
        player_score += 1
        reset_ball(1)


    ball_speed += 2 * dt

    score_text_player1 = font.render(f"{player_score}", True, pygame.Color(255, 0, 136))
    score_text_player2 = font.render(f"{player2_score}", True, pygame.Color(174, 122, 191))
    separator_text = font.render("  -  ", True, pygame.Color(winner))

    screen.blit(score_text_player1, (screen_width / 2 - score_text_player1.get_width() - 100, 30))  # Player 1 score
    screen.blit(separator_text, (screen_width / 2 - separator_text.get_width() / 2, 30))  # Separator
    screen.blit(score_text_player2, (screen_width / 2 + 100, 30))  # Player 2 score


    pygame.display.flip()

    dt = clock.tick(60) / 1000  # Update dt for frame rate independence

pygame.quit()
