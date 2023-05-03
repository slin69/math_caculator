import pygame

class point:
    def __init__(self,x,y,width,height,relativex,relativey):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.relativex=relativex
        self.relativey=relativey
    def render(self,window):
        pygame.draw.rect(window,(115,165,0),pygame.Rect(self.x,self.y+400,self.width,self.height))