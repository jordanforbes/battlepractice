import PySimpleGUI as sg 

class GUI():
    def __init__(self,title="gui"):
        self.title=title 
    
    layout = [ 
              [sg.Text("hello")]
              ]
    
    win = sg.Window("GUI").Layout(layout)
    
    e, v = win.Read()
    if e == sg.WIN_CLOSED or e == 'Close':
        win.Close()

g = GUI()