"""Unittests for engine/engine.py

"""

from unittest import TestCase

import pygame

from engine import GameEngine

class TestGameEngine(TestCase):

    def setUp(self):
        pygame.init()
        self.engine = GameEngine()

    def tearDown(self):
        pygame.quit()

    def test_update(self):
        self.engine.update()
        self.assertEqual(1, self.engine.total_frames)

    def test_restart(self):
        self.engine.update()
        self.engine.game_over = True
        self.engine.restart()
        self.assertEqual(0, self.engine.total_frames)
        self.assertEqual(0, self.engine.total_frames_played)

if __name__ == '__main__':
    unittest.main()
