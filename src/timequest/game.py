'''
Created on Jun 22, 2012

@author: kaelstrom
'''
from timequest.view import View
import pygame

class Game(object):
    '''
    Class managing the input, logic, and view systems
    '''

    def __init__(self):
        self.view = View()
        self.objects = []
        self.is_running = False
        self.clock = pygame.time.Clock()
    
    def start(self):
        self.is_running = True
        self.game_loop()
    
    def game_loop(self):
        while self.is_running:
            self.clock.tick(60)
            self.handle_input()
            self.update_logic()
            self.draw()
        
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.is_running = False
            
    def update_logic(self):
        pass
    
    def draw(self):
        self.view.draw()
    