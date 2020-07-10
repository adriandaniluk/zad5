import random

class Kwadraciki():
    kolory = ["#FFFF66", "#FFCC00",
              "#FF9900", "#FF0000"]
    def __init__(self, x, y, kwadratsSize):
        self.x = x
        self.y = y
        self.kwadratsSize = kwadratsSize
    
    def __rysujKwadrat(self, x, y):
        pushMatrix()
        strokeWeight(5)
        stroke(self.kolory[random.randrange(4)])
        fill(self.kolory[random.randrange(4)])
        rectMode(CENTER)
        rect(x, y, self.kwadratsSize, self.kwadratsSize)
        popMatrix()

    def rysuj(self):
        self.__rysujKwadrat(self.x-self.kwadratsSize/2, self.y-self.kwadratsSize/2)
        self.__rysujKwadrat(self.x-self.kwadratsSize/2, self.y+self.kwadratsSize/2)
        self.__rysujKwadrat(self.x+self.kwadratsSize/2, self.y-self.kwadratsSize/2)
        self.__rysujKwadrat(self.x+self.kwadratsSize/2, self.y+self.kwadratsSize/2)

def setup():
    size(700, 700)
    global listaKwadracikow
    listaKwadracikow = []
    
def draw():
    background(0)
    for i in listaKwadracikow:
        i.rysuj()
    
def mouseClicked():
    global listaKwadracikow
    listaKwadracikow.append(Kwadraciki(mouseX, mouseY, 100))
    
#2pkt
