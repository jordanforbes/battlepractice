import PySimpleGUI as sg 
from pynput import keyboard
from Card import Card
from Unit import Unit


    
######   
p = Unit("player")
e = Unit("enemy")
punch = Card("punch")    

global gameOn
gameOn = True

#####
def attack(key,p=p,e=e):
    if key.char == "f":
        punch.use(p,e)
        
    elif key.char =="e":
        gameOn = False
        

def endGame():
    gameOn = False


with keyboard.Listener(on_press=attack) as listener: 
    while gameOn == True:    
        listener.join()
        
print("GAME OVER")