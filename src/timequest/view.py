'''
Created on Jun 22, 2012

@author: kaelstrom
'''

from graphic import Graphic
import timequest

class View(object):
    '''
    classdocs
    '''
    def __init__(self):
        pass
        
    def draw(self):
        for obj in timequest.g.objects:
            obj.draw()