'''
Created on Jun 22, 2012

@author: kaelstrom
'''
from timequest.view import View

class Game(object):
    '''
    Class managing the input, logic, and view systems
    '''

    def __init__(self):
        self.view = View()
        self.objects = []
    
    def start(self):
        pass