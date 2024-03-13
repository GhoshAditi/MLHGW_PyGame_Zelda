import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        pygame.display.set_caption('Zelda DarkSouls')
        self.clock = pygame.time.Clock()

        self.level = Level()

        # sound 
        main_sound = pygame.mixer.Sound('MLHGW_PyGame_Zelda/audio/main.ogg')
        main_sound.set_volume(0.5)
        main_sound.play(loops = -1)

        # splash screen
        self.show_splash_screen()

    def show_splash_screen(self):
        # Load splash screen image
        splash_image = pygame.image.load('MLHGW_PyGame_Zelda/images/splash2.png')

        # Draw splash screen
        self.screen.blit(splash_image, (0, 0))

        # Update display
        pygame.display.flip()

        # Wait for a certain amount of time
        pygame.time.wait(3000)  # 3000 milliseconds = 3 seconds

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()

            self.screen.fill(WATER_COLOR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()