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

score.load_high_score()

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
                elif buttons.Settings.settings.collidepoint(event.pos):
                    game_state = "settings"

            elif game_state == 'settings':
                if buttons.Settings.Difficulties.difficulty_easy.collidepoint(event.pos):
                    matrix.set_difficulty("Easy")
                elif buttons.Settings.Difficulties.difficulty_normal.collidepoint(event.pos):
                    matrix.set_difficulty("Normal")
                elif buttons.Settings.Difficulties.difficulty_hard.collidepoint(event.pos):
                    matrix.set_difficulty("Hard")
                elif buttons.Settings.back.collidepoint(event.pos):
                    game_state = "Home"

            elif game_state == 'playing':
                if buttons.home_button.collidepoint(event.pos):
                    game_state = "Home"
                elif matrix.game_over:
                    if buttons.restart_button.collidepoint(event.pos):
                        matrix.restart()
                elif buttons.pause.collidepoint(event.pos):
                    matrix.toggle_pause()

    if game_state == 'playing':
        matrix.update()

    screen.fill(config.Theme.BG)

    mouse_pos = pygame.mouse.get_pos()

    if game_state == 'Home':
        title_rect = menus_config.Home.TITLE.get_rect(center=(config.SCREEN_SIZE[0] // 2, 200))
        screen.blit(menus_config.Home.TITLE, title_rect)

        start_color = config.Theme.BUTTON_HOVER if buttons.start.collidepoint(mouse_pos) else config.Theme.BUTTON_START
        pygame.draw.rect(screen, config.Theme.BUTTON_BG, buttons.start, border_radius=6)
        pygame.draw.rect(screen, start_color, buttons.start, width=2, border_radius=6)
        start_text = config.Font.BUTTON_FONT.render("Start", True, start_color)
        text_rect = start_text.get_rect(center=buttons.start.center)
        screen.blit(start_text, text_rect)

        settings_color = config.Theme.BUTTON_HOVER if buttons.Settings.settings.collidepoint(mouse_pos) else config.Theme.TEXT_SECONDARY
        pygame.draw.rect(screen, config.Theme.BUTTON_BG, buttons.Settings.settings, border_radius=6)
        pygame.draw.rect(screen, settings_color, buttons.Settings.settings, width=2, border_radius=6)
        settings_text = config.Font.BUTTON_FONT.render("Settings", True, settings_color)
        text_rect = settings_text.get_rect(center=buttons.Settings.settings.center)
        screen.blit(settings_text, text_rect)

    elif game_state == 'settings':
        title_rect = menus_config.Settings.TITLE.get_rect(center=(config.SCREEN_SIZE[0] // 2, 120))
        screen.blit(menus_config.Settings.TITLE, title_rect)

        label_rect = menus_config.Settings.LABEL.get_rect(center=(config.SCREEN_SIZE[0] // 2, 190))
        screen.blit(menus_config.Settings.LABEL, label_rect)

        difficulty_options = [
            ("Easy", buttons.Settings.Difficulties.difficulty_easy),
            ("Normal", buttons.Settings.Difficulties.difficulty_normal),
            ("Hard", buttons.Settings.Difficulties.difficulty_hard),
        ]
        for label, rect in difficulty_options:
            is_selected = matrix.difficulty == label
            if rect.collidepoint(mouse_pos):
                border_color = config.Theme.BUTTON_HOVER
            elif is_selected:
                border_color = config.Theme.ACCENT
            else:
                border_color = config.Theme.TEXT_SECONDARY
            pygame.draw.rect(screen, config.Theme.BUTTON_BG, rect, border_radius=6)
            pygame.draw.rect(screen, border_color, rect, width=2, border_radius=6)
            text = config.Font.BUTTON_FONT.render(label, True, border_color)
            text_rect = text.get_rect(center=rect.center)
            screen.blit(text, text_rect)

        back_color = config.Theme.BUTTON_HOVER if buttons.Settings.back.collidepoint(mouse_pos) else config.Theme.TEXT_SECONDARY
        pygame.draw.rect(screen, config.Theme.BUTTON_BG, buttons.Settings.back, border_radius=6)
        pygame.draw.rect(screen, back_color, buttons.Settings.back, width=2, border_radius=6)
        back_text = config.Font.BUTTON_FONT.render("Back", True, back_color)
        text_rect = back_text.get_rect(center=buttons.Settings.back.center)
        screen.blit(back_text, text_rect)

    else:
        # sidebar panel background, distinct from the board
        pygame.draw.rect(screen, config.Theme.PANEL_BG,
                          (config.SIDEBAR_X, 0, config.SIDEBAR_WIDTH, config.SCREEN_SIZE[1]))

        matrix.draw_grid(screen)

        # thin accent border around the play area
        pygame.draw.rect(screen, config.Theme.ACCENT, (0, 0, config.BOARD_WIDTH, config.SCREEN_SIZE[1]), 2)

        score_text = config.Font.IN_GAME_FONT.render(f"Score: {score.SCORE}", True, config.Theme.TEXT_PRIMARY)
        high_text = config.Font.IN_GAME_FONT.render(f"High: {score.HIGH_SCORE}", True, config.Theme.TEXT_SECONDARY)
        screen.blit(score_text, (config.SIDEBAR_X + 30, 190))
        screen.blit(high_text, (config.SIDEBAR_X + 30, 230))

        pause_color = config.Theme.BUTTON_HOVER if buttons.pause.collidepoint(mouse_pos) else config.Theme.BUTTON_PAUSE
        pygame.draw.rect(screen, config.Theme.BUTTON_BG, buttons.pause, border_radius=6)
        pygame.draw.rect(screen, pause_color, buttons.pause, width=2, border_radius=6)
        label = "Resume" if matrix.paused else "Pause"
        btn_text = config.Font.BUTTON_FONT.render(label, True, pause_color)
        text_rect = btn_text.get_rect(center=buttons.pause.center)
        screen.blit(btn_text, text_rect)

        home_color = config.Theme.BUTTON_HOVER if buttons.home_button.collidepoint(mouse_pos) else config.Theme.TEXT_SECONDARY
        pygame.draw.rect(screen, config.Theme.BUTTON_BG, buttons.home_button, border_radius=6)
        pygame.draw.rect(screen, home_color, buttons.home_button, width=2, border_radius=6)
        home_text = config.Font.BUTTON_FONT.render("Home", True, home_color)
        text_rect = home_text.get_rect(center=buttons.home_button.center)
        screen.blit(home_text, text_rect)

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

            restart_color = config.Theme.BUTTON_HOVER if buttons.restart_button.collidepoint(mouse_pos) else config.Theme.BUTTON_RESTART
            pygame.draw.rect(screen, config.Theme.BUTTON_BG, buttons.restart_button, border_radius=6)
            pygame.draw.rect(screen, restart_color, buttons.restart_button, width=2, border_radius=6)
            restart_text = config.Font.BUTTON_FONT.render("Restart", True, restart_color)
            text_rect = restart_text.get_rect(center=buttons.restart_button.center)
            screen.blit(restart_text, text_rect)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
