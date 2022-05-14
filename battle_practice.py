import PySimpleGUI as sg 
from pynput import keyboard
from Card import Card

class Unit():
    def __init__(self, name="",hp=10):
        self.name = name 
        self.HP = hp 
        self.block = 5
        print(f"{self.name} is online")

#hp
    def getHP(self):
        return self.HP

#block
    def getBlock(self):
        return self.block
    
#name
    def getName(self):
        return self.name
    
#sethp
    def setHP(self, n):
        self.HP = n
        
    def takeDamage(self,n):
        print(f'{self.name} took {n} damage!')
        hp = self.getHP()
        self.setHP(hp-n)
        self.vitals()
        return self 
    
    def dealDamage(self,target,n):
        print(f'{self.name} attacked {target.name}')
        target.takeDamage(n)
        return self         
    
    def block(self,n):
        block = self.getBlock()
        dmg -= block 
        if dmg < 0:
            dmg = 0 
        return dmg 
    
#deathCheck
    def vitals(self):
        if self.getHP() <=0:
            self.die()
            return self 
        else: 
            return self 
    
    def die(self):
        print(f"{self.name} is dead")
        gameOn = False
        return self
    
    
######   
p = Unit("player")
e = Unit("enemy")
punch = Card("punch")    

#####
def attack(key,p=p,e=e):
    if key.char == "f":
        punch.use(p,e)
        
gameOn = True 
while gameOn == True:
    with keyboard.Listener(on_press=attack) as listener: 
        listener.join()
    p.vitals()
    e.vitals()
        
print("GAME OVER")