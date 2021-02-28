import pygame,math,sys,time,random

class Sorting_algo():

    def Shuffle(self):
        for x in range(0,len(self.list)-1):
            ran = random.randint(0,len(self.list)-1)
            self.list[x],self.list[ran] = self.list[ran],self.list[x]
        self.mode = "class"

    def Class_tick(self):
        if self.cursor-1 > 0:self.cursor-=1
        else:
            self.cursor = size_sorting-1
        if self.list[self.cursor-1] > self.list[self.cursor]: self.list[self.cursor-1], self.list[self.cursor] = self.list[self.cursor], self.list[self.cursor-1]

    def __init__(self,nb):
        self.repeat = 100
        self.cursor = size_sorting-1
        self.mode = "shuffle"
        self.list = []
        for x in range(nb):
            self.list.append(x)

w,h = 400,400
#w,h = int(input("w ? => ")),int(input("h ? => "))
size_sorting = int(input("size ? => "))
tt = float(input("time ticks ? => "))
pygame.init()
screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()
sorting = Sorting_algo(size_sorting)

while True:

    for event in pygame.event.get():
        if event.type==pygame.QUIT: pygame.quit(); sys.exit()
        if event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE: pygame.quit(); sys.exit()

    screen.fill((0,0,0))
    if sorting.mode == "shuffle": sorting.Shuffle()
    else: sorting.Class_tick()

    y =w
    z = 0
    for x in sorting.list:
        x*=(w/len(sorting.list))
        color = (255,255,255)
        if z+1 == sorting.cursor: color = (0,255,0)
        if z+2 == sorting.cursor: color = (255,0,0)
        pygame.draw.polygon(screen,color,((y,x),(y-w/len(sorting.list),x),(y-w/len(sorting.list),w),(y,w)))
        y-=w/len(sorting.list)
        z+=1
    pygame.display.flip()
    time.sleep(tt)
