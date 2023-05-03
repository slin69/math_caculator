import pygame
import random
try:
    from Point import point

except:
    from graph.Point import point
class Graph:
    def __init__(self,width=400,height=400):
        self.width=width
        self.height=height
        self.points=[]
        self.coor=[]
        self.currentframe=[-self.width,self.width]
        self.screen=pygame.display.set_mode((self.width,self.height))
        self.ysp=[[0,-self.width],[0,self.width]]
        self.xsp=[[self.height,self.width],[-self.height,self.width]]
        self.change=0.04
    def coor_to_points(self):
        for c in self.coor:
            self.points.append(point(c[0],c[1],self.width/100,self.height/100,c[0],c[1]))
    def draw_oglines(self):
        pygame.draw.line(self.screen,(115,165,128),self.ysp[0],self.ysp[1])
        pygame.draw.line(self.screen,(115,165,128),self.xsp[0],self.xsp[1])
    def move(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_a]:
            for p in self.points:
                p.x+=self.change
            self.ysp[0][0]+=self.change
            self.ysp[1][0]+=self.change
        if keys[pygame.K_d]:
            for p in self.points:
                p.x-=self.change
            self.ysp[0][0]-=self.change
            self.ysp[1][0]-=self.change

        if keys[pygame.K_w]:
            for p in self.points:
                p.y+=self.change
            self.xsp[0][1]+=self.change
            self.xsp[1][1]+=self.change
        if keys[pygame.K_s]:
            for p in self.points:
                p.y-=self.change
            self.xsp[0][1]-=self.change
            self.xsp[1][1]-=self.change

    def test_random(self):
        for i in range(20):
            x=random.randint(-100,100)
            y=random.randint(-100,100)
            w,h=self.width/100,self.width/100
            p=point(x,y,w,h,x,y)
            self.points.append(p)
        #self.points.append(point(0,0,self.width/100,self.width/100,0,0))
    def render(self):
        for p in self.points:
            p.render(self.screen)
    def main(self):
        run=True
        #self.test_random()
        self.coor_to_points()
        while run:
            self.screen.fill((0,0,0))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
            self.draw_oglines()
            self.render()
            self.move()
            pygame.display.update()
        pygame.quit()



if __name__=='__main__':
    Graph().main()