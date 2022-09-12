import pygame
import pygame_menu

from src.music import load as music_load
from src.music import play as music_play
from src.music import MAIN_SONG as music_MAIN_SONG


from src.GameViewFactory import GameView
# import music

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
        music_load()
        music_play(music_MAIN_SONG)

        return screen

    def menuStart(self):

        running = True
        blue = (0, 0, 205)
        while running:
            surface = pygame.display.set_mode((800, 600))

            def start_the_game():

                pass

            def select_level(value):
                # level 1 \
                # level.someFunc
                # level 2
                # print("levels selected")
                # print(value)
                levelTup = ("Regular", 1)
                curGameView = GameView(levelTup[0], levelTup[1], pygame.display.get_surface())
                curGameView.runGame()

            def settings_menu():
                pass

            menu = pygame_menu.Menu('Welcome', self.resolution[0], self.resolution[1],
                                    theme=pygame_menu.themes.THEME_BLUE)

            menu.add.button('Start', start_the_game)

            menu.add.dropselect("Levels", [("Regular-1", 1)], onselect=select_level)
            #menu.add.button('Levels', select_level)
            menu.add.button('Settings', settings_menu)
            menu.add.button('Quit', pygame_menu.events.EXIT)

            menu.mainloop(surface)









    # def start(self):
    #     """Main loop for the whole game.
    #     :return: nothing
    #     """
    #     self.__initialize_display()
    #     self.__mainMenuObj.run()
    #
    #     #waiting for user to select a level...
    #     (GameEngine.selected_Level_Type, GameEngine.selected_Level_Num) = \
    #         GameEngine.__UserInputObj.getInput("main_menu")
    #
    #     #Running the level:
    #     # GameEngine.__gameViewObj = GameViewFactory.generateGameView()

