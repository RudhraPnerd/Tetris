import pygame
from pygame import SRCALPHA

pygame.init()

from game import config
import matrix
import score
import buttons
import menus_config

screen = pygame.display.set_mode(config.SCREEN_SIZE)
pygame.display.set_caption(config.SCREEN_TITLE)
clock = pygame.time.Clock()
game_state = 'Home'

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

            elif game_state == 'playing' and not matrix.paused and not matrix.game_over:
                if event.key == pygame.K_LEFT:
                    matrix.move(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    matrix.move(1, 0)
                elif event.key == pygame.K_UP:
                    matrix.rotate()
                elif event.key == pygame.K_DOWN:
                    matrix.soft_drop()
                elif event.key == pygame.K_SPACE:
                    matrix.hard_drop()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == 'Home':
                if buttons.start.collidepoint(event.pos):
                    game_state = "playing"

            elif matrix.game_over:
                if buttons.restart_button.collidepoint(event.pos):
                    matrix.restart()
            elif buttons.pause.collidepoint(event.pos):
                matrix.toggle_pause()

    if game_state == 'playing':
        matrix.update()

    screen.fill(config.SCREEN_BG)

    if game_state == 'Home':
        title_rect = menus_config.Home.TITLE.get_rect(center=(config.SCREEN_SIZE[0] // 2, 200))
        screen.blit(menus_config.Home.TITLE, title_rect)

        pygame.draw.rect(screen, (60, 60, 70), buttons.start)
        start_text = config.Font.BUTTON_FONT.render("Start", True, (240, 240, 240))
        screen.blit(start_text, (buttons.start.x + 30, buttons.start.y + 8))

    else:
        matrix.draw_grid(screen)

        score_text = config.Font.IN_GAME_FONT.render(f"Score: {score.SCORE}", True, (240, 240, 240))
        high_text = config.Font.IN_GAME_FONT.render(f"High: {score.HIGH_SCORE}", True, (240, 240, 240))
        screen.blit(score_text, (320, 40))
        screen.blit(high_text, (320, 80))

        pygame.draw.rect(screen, (200, 60, 60), buttons.pause)
        label = "Resume" if matrix.paused else "Pause"
        btn_text = config.Font.BUTTON_FONT.render(label, True, (240, 240, 240))
        screen.blit(btn_text, (buttons.pause.x + 10, buttons.pause.y + 8))

        if matrix.paused:
            overlay = pygame.Surface(config.SCREEN_SIZE, SRCALPHA)
            overlay.fill(menus_config.Pause.BG)
            screen.blit(overlay, (0, 0))

            title_rect = menus_config.Pause.PAUSE_TITLE.get_rect(
                center=(config.SCREEN_SIZE[0] // 2, config.SCREEN_SIZE[1] // 2 - 20))
            hint_rect = menus_config.Pause.RESUME_HINT.get_rect(
                center=(config.SCREEN_SIZE[0] // 2, config.SCREEN_SIZE[1] // 2 + 20))

            screen.blit(menus_config.Pause.PAUSE_TITLE, title_rect)
            screen.blit(menus_config.Pause.RESUME_HINT, hint_rect)

        if matrix.game_over:
            overlay = pygame.Surface(config.SCREEN_SIZE, SRCALPHA)
            overlay.fill(menus_config.GameOver.BG)
            screen.blit(overlay, (0, 0))

            title_rect = menus_config.GameOver.TITLE.get_rect(
                center=(config.SCREEN_SIZE[0] // 2, config.SCREEN_SIZE[1] // 2 - 40))
            hint_rect = menus_config.GameOver.HINT.get_rect(
                center=(config.SCREEN_SIZE[0] // 2, config.SCREEN_SIZE[1] // 2))
            screen.blit(menus_config.GameOver.TITLE, title_rect)
            screen.blit(menus_config.GameOver.HINT, hint_rect)

            pygame.draw.rect(screen, (60, 60, 70), buttons.restart_button)
            restart_text = config.Font.BUTTON_FONT.render("Restart", True, (240, 240, 240))
            screen.blit(restart_text, (buttons.restart_button.x + 15, buttons.restart_button.y + 8))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()