class Unit():
    def __init__(self, name="",hp=10):
        self.name = name 
        self.HP = hp 
        self.block = 5
        self.isAlive = True
        print(f"{self.name} is online")

#get
    def getHP(self):
        return self.HP


    def getBlock(self):
        return self.block
    

    def getName(self):
        return self.name
    
    def isAlive(self):
        return self.isAlive
    
#set
    def setHP(self, n):
        self.HP = n
    
    def die(self):
        print(f"{self.name} is dead")
        self.isAlive = False 
        
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
