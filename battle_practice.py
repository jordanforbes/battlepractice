import PySimpleGUI as sg 

class Unit():
    def __init__(self, name="",hp=100):
        self.name = name 
        self.HP = hp 
        self.block = 5
        print(f"{self.name} is online")
    def getHP(self):
        return self.HP
    
    def getBlock(self):
        return self.block
    
    def setHP(self, n):
        self.HP = n
        
    def takeDamage(self,n):
        hp = self.getHP()
        self.setHP(hp-n)
        return self 
    
    def dealDamage(self,target,n):
        target.takeDamage(n)
        return self         
    
    def block(self,n):
        block = self.getBlock()
        dmg -= block 
        if dmg < 0:
            dmg = 0 
        return dmg 
    
    
p = Unit("player")