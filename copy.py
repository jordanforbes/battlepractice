from pynput import keyboard 

def punch():
    print("punch!")

def on_press(key):
    try: 
        if key.char == 'f':
            punch()
        else:
            print(f'key pressed: {key.char}')

    except AttributeError: 
        print(f'special key pressed: {key}')
        
def on_release(key):
    print(f'Key released: {key}')
    if key == keyboard.Key.esc:
        return False 
    
#collect events until released 
with keyboard.Listener(
        on_press=on_press, 
        on_release=on_release) as listener: 
    listener.join()