import pygame

class Ship:
    '''a class to manage the ship'''

    def __init__(self, ai_game):
        '''initialize the ship and set its starting position'''
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect
        self.image = pygame.image.load("/Users/andrew/Developer/vscode/02_matthes_exercises/matthes_main/chapter_12/alien_invasion/images/ship.bmp")
        self.rect = self.image.get_rect()

        # start each new ship at the bottom of center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # store a float for the ship's exact horizontal position
        self.x = float(self.rect.x)

        # movement flag; start with a ship that's not moving
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''Update the ship's position based on movement flags'''
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        # update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        '''draw the ship at its current location'''
        self.screen.blit(self.image, self.rect)