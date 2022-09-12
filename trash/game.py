import pygame
import pygame_menu
import asyncio
import configs
import music


class Game:

    def __init__(self, dims, fps):
        self.dims = (800, 600)
        self.fps = 60

    def start(self):

        pygame.init()
        pygame.display.set_mode(self.dims)
        music.load()
        music.play(music.MAIN_SONG)

        running = True
        blue = (0, 0, 205)
        while running:
            surface = pygame.display.set_mode((800, 600))


            def start_the_game():
                # Do the job here !
                pass

            def select_level():
                # level 1 \
                # level.someFunc
                # level 2

                pass

            def settings_menu():
                pass

            menu = pygame_menu.Menu('Welcome', 800, 600,
                                    theme=pygame_menu.themes.THEME_BLUE)

            menu.add.button('Start', start_the_game)

            menu.add.button('Levels', select_level())
            menu.add.button('Settings', settings_menu)
            menu.add.button('Quit', pygame_menu.events.EXIT)

            menu.mainloop(surface)
