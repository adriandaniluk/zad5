class Pokretlo():
    ilosc_wcisniec_wszystkich_pokretel = 0
    def __init__(self, arg_x, arg_y, arg_r):
        self.obrot = 0
        self.wcisniety = False 
        self.x = arg_x
        self.y = arg_y
        self.r = arg_r

    def rysuj(self):
        arc(self.x, self.y, self.r, self.r, 0+radians(self.obrot+45), PI+ radians(self.obrot+45), PIE)
        arc(self.x, self.y, self.r, self.r, 0+radians(self.obrot+45), PI+ radians(self.obrot+270), PIE)
    def obroc(self, stopnie):
        self.obrot += stopnie
    def wcisnij(self):
        Pokretlo.ilosc_wcisniec_wszystkich_pokretel +=1
        self.wcisniety = not self.wcisniety
        background(100)

def setup():
    size(400, 400)
    global pokretlo_piekarnika
    pokretlo_piekarnika = Pokretlo(width/2, height/2, 200)
def mouseClicked():
    pokretlo_piekarnika.wcisnij()
def mouseWheel(event):
    pokretlo_piekarnika.obroc(10)
def draw():
    background(300)
    pokretlo_piekarnika.rysuj()
         
