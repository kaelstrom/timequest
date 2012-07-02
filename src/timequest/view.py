'''
Created on Jun 22, 2012

@author: kaelstrom
'''

from graphic import Graphic
import timequest
import pygame

class View(object):
    '''
    classdocs
    '''
    def __init__(self):
        self.create_screen()
        
    def create_screen(self):   
        #fill whatever the current resolution is
        self.screen = pygame.display.set_mode((0,0) , pygame.FULLSCREEN)
        self.SCREEN_SIZE = (pygame.display.Info().current_w,pygame.display.Info().current_h)
        
    def draw(self):
        for obj in timequest.g.objects:
            obj.draw()