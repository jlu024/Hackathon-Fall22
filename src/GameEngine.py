import pygame
import pygame_menu
from pygame_menu import Theme

import src.music as music
import src.config as config

from src.GameViewFactory import GameView


class GameEngine:
    resolution = None
    screen = None

    def __init__(self, resolutionP, fpsP=60, debug="True"):
        self.resolution = resolutionP
        self.fps = fpsP
        self.screen = None

    def mainLoop(self):
        self.screen = self.__initialize_display_and_music()
        self.menuStart()
        # curGameView = GameView(levelTup[0], levelTup[1], pygame.display.get_surface())
        # curGameView.runGame()
        # (isSuccess, score) = curGameView.

    def __initialize_display_and_music(self):
        """Creating the main pygame display.
        Update this to contain all base configuration for the visual
        :return: no return value
        """
        pygame.init()
        screen = pygame.display.set_mode(self.resolution)

        clock = pygame.time.Clock()
        pygame.display.set_caption("Demo Test")
        # music
        music.load()
        music.play(music.MAIN_SONG)
        pygame.mixer.music.set_volume(config.SOUND_VOLUME)

        return screen

    def menuStart(self):

        running = True

        while running:
            surface = pygame.display.set_mode((800, 600))

            def start_the_game():
                if config.GAME_MODE == 1:
                    levelTup = ("Regular", 1)
                    curGameView = GameView(levelTup[0], levelTup[1], pygame.display.get_surface())
                    curGameView.runGame()
                elif config.GAME_MODE == 2:
                    pass

            def select_mode(mode, value):
                config.GAME_MODE = value

            # def music_setting(value):
            # not able to mute music because music is playing outside the loop

            font = pygame_menu.font.FONT_8BIT
            my_theme = Theme(widget_font=font)

            background_image = pygame_menu.baseimage.BaseImage(
                image_path="images/candyWallBackground.png",
                drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
            )
            my_theme.background_color = background_image
            menu = pygame_menu.Menu('Gem Crush', self.resolution[0], self.resolution[1],
                                    theme=my_theme)

            menu.add.button('Start', start_the_game)

            menu.add.selector('Game Mode :', [('Regular', 1), ('Fruit', 2)], onchange=select_mode)
            # menu.add.button('Levels', select_level)
            # menu.add.toggle_switch("Music", [0,True], onchange=music_setting())
            menu.add.button('Quit', pygame_menu.events.EXIT)

            menu.mainloop(surface)
