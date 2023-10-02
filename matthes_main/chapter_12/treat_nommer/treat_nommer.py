import pygame
import sys

class TreatNommer:
    '''overall class, manages game assets and behavior'''
    def __init__(self):
        '''initialize game, create resources'''
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Treat Nommer")

        self.cosmo = Cosmo(self)

        # set the background color
        self.bg_color = (100, 180, 200)

    def run_game(self):
        '''start the main loop for the game'''
        while True:
            # watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #redraw the screen during each pass through the loop
            self.screen.fill(self.bg_color)
            self.cosmo.blitme()

            # make the most recently drawn screen visible
            pygame.display.flip()
            self.clock.tick(60)

class Cosmo:
    '''class with all properties for the cosmo sprite'''
    def __init__(self, tn_game):
        # initialize the cosmo image, and its starting position
        self.screen = tn_game.screen
        self.screen_rect = tn_game.screen.get_rect()

        # load the cosmo image and get its rect
        self.image = pygame.image.load("/Users/andrew/Developer/vscode/02_matthes_exercises/matthes_main/chapter_12/treat_nommer/cosmo.png")
        self.rect = self.image.get_rect()

        # start each new cosmo at the bottom of center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        '''draw the cosmo sprite at its current location'''
        self.screen.blit(self.image, self.rect)


if __name__ == "__main__":
    # make a game instance, and run the game
    tn = TreatNommer()
    tn.run_game()