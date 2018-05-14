"""Engine Module

"""

import time

import pygame


class GameEngine:

    """Manages all global state (ex. paused, game_over, clock)

    The highest authority on the game state machine, and the entity right below the game loop itself

    """

    def __init__(self):
        self.frame_rate = 60
        self.clock = pygame.time.Clock()

        self.screen_height = 900
        self.screen_width = 720
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        self.paused = False
        # paused_manual_frame_tick: Variable to move one frame forward while in paused mode
        self.paused_manual_frame_tick = False

        self.game_over = False
        # total_frames: Number of frames since game began
        self.total_frames = 0
        # total_frames_played: Excludes paused and game-over frames
        self.total_frames_played = 0
        self.started_time = time.time()

        self.generic_font = pygame.font.SysFont('Courier', 30)

    def restart(self):
        """Reinitialize engine

        """

        self.total_frames = 0
        self.total_frames_played = 0
        self.started_time = time.time()
        self.game_over = False

    def _get_fps(self):
        return format(self.clock.get_fps(), '.2f')

    def _get_elapsed_time(self):
        return time.time() - self.started_time

    def update(self):
        '''Advance the system by one frame, locked at 60 FPS'''
        self.total_frames += 1

        if (not self.paused or self.paused_manual_frame_tick) and not self.game_over:
            self.total_frames_played += 1

        self.clock.tick(60)

    def draw(self):
        '''Draws general system/game information to screen'''
        RED = (255, 0, 0)
        font = self.generic_font
        screen = self.screen

        if self.game_over:
            screen.fill((0, 0, 0))
            game_over_surface = self.generic_font.render('Game Over', False, RED)
            gos_x = self.screen_width // 2 - game_over_surface.get_width() // 2
            gos_y = self.screen_height // 2 - game_over_surface.get_height() // 2
            screen.blit(game_over_surface, (gos_x, gos_y))
        else:
            if self.paused:
                paused_surface = font.render('Paused', False, RED)
                ps_x = self.screen_width // 2  - paused_surface.get_width()  // 2
                ps_y = self.screen_height // 2 - paused_surface.get_height() // 2
                screen.blit(paused_surface, (ps_x, ps_y))

            fps_surface = font.render('FPS: ' + str(self._get_fps()), False, RED)
            screen.blit(fps_surface, (self.screen_width - fps_surface.get_width(), 0))
