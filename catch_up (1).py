import pygame
import random

pygame.init()


BACKGROUND = (30, 30, 60) 

win = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 52)

left_pad  = pygame.Rect(24, 210, 14, 80)
right_pad = pygame.Rect(662, 210, 14, 80)
ball      = pygame.Rect(338, 238, 24, 24)

ball_x = 5
ball_y = random.choice([-3, 3])
left_score  = 0
right_score = 0
WIN_SCORE = 7  

while True:
    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]    and left_pad.top    > 0:    left_pad.y  -= 5
    if keys[pygame.K_s]    and left_pad.bottom < 500:  left_pad.y  += 5
    if keys[pygame.K_UP]   and right_pad.top   > 0:    right_pad.y -= 5
    if keys[pygame.K_DOWN] and right_pad.bottom < 500: right_pad.y += 5

    if left_score < WIN_SCORE and right_score < WIN_SCORE:
        ball.x += ball_x
        ball.y += ball_y

        if ball.top <= 0 or ball.bottom >= 500:
            ball_vy *= -1

        if ball.colliderect(left_pad) and ball_x < 0:
            ball_x *= -1
            ball.left = left_pad.right

        if ball.colliderect(right_pad) and ball_x > 0:
            ball_x *= -1
            ball.right = right_pad.left

        if ball.left <= 0:
            right_score += 1
            ball.center = (350, 250)
            ball_x = 5
            ball_y = random.choice([-3, 3])

        if ball.right >= 700:
            left_score += 1
            ball.center = (350, 250)
            ball_x = -5
            ball_y = random.choice([-3, 3])

    win.fill(BACKGROUND)
    pygame.draw.rect(win, (255, 255, 255), left_pad,  border_radius=4)
    pygame.draw.rect(win, (255, 255, 255), right_pad, border_radius=4)
    pygame.draw.circle(win, (200, 212, 0), ball.center, 12)

    win.blit(font.render(str(left_score),  True, (255, 255, 255)), (290, 16))
    win.blit(font.render(str(right_score), True, (255, 255, 255)), (390, 16))

    if left_score >= WIN_SCORE:
        win.blit(font.render("Left Wins!", True, (255, 255, 0)), (230, 220))
    if right_score >= WIN_SCORE:
        win.blit(font.render("Right Wins!", True, (255, 255, 0)), (220, 220))

    pygame.display.flip()