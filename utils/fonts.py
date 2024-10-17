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
        self.displace = data['displacement']
    
    def render(self, txt, max_width=None):
        for rep, repWith in self.replaces.items():
            txt = txt.replace(rep, repWith)

        w = (max_width if max_width is not None and len(txt)>max_width else len(txt))
        h = ceil(len(txt)/(max_width or len(txt)))
        sur = pygame.Surface((w*8+w*self.displace[0], h*8+h*self.displace[1]))
        sur.set_colorkey((255, 0, 255))
        sur.fill((255, 0, 255))

        x = 0
        y = 0
        for let in txt:
            idx = self.chars.index(let)
            sur.blit(self.img.subsurface((idx*8)%self.img.get_width(), 
                                         floor(idx/(self.img.get_width()/8))*8, 
                                         8, 8), (x*8+self.displace[0]*x, y*8+self.displace[1]*y))
            x += 1
            if max_width is not None and x >= max_width:
                x = 0
                y += 1
        
        return sur
