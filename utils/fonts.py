from math import floor, ceil
import pygame
import json

with open('assets/fonts/info.json') as f:
    DATA = json.load(f)

class Font:
    def __init__(self, name):
        if name not in DATA:
            raise ValueError(
                f'Name of font "{name}" not in known fonts!'
            )
        data = DATA[name]
        self.img = pygame.image.load('assets/fonts/'+data['fname'])
        self.chars = data['chars']
        self.replaces = data['replace']
    
    def render(self, txt, max_width=None):
        sur = pygame.Surface(((max_width if max_width is not None and len(txt)>max_width else len(txt))*8, 
                              ceil(len(txt)/(max_width or len(txt)))*8))
        sur.set_colorkey((255, 0, 255))
        sur.fill((255, 0, 255))

        x = 0
        y = 0
        for let in txt:
            idx = self.chars.index(let)
            sur.blit(self.img.subsurface((idx*8)%self.img.get_width(), 
                                         floor(idx/(self.img.get_width()/8))*8, 
                                         8, 8), (x*8, y*8))
            x += 1
            if max_width is not None and x >= max_width:
                x = 0
                y += 1
        
        return sur
