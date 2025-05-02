from pynput import keyboard

def on_press(key): #-> keyboard objects 
    try:
        print(f'alphanumeric key  pressed {key.char}')
    except AttributeError:
        print(f"special key {key}")

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    
# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener: # this chunk is creating a new thread, create a new thread and give it work to do
    listener.join() # threading operation on a thread, "I want to wait until this thread finishes its execution"
    
    "blocking opp becuase .join() method pauses operation on the mian thread until the listner thread finishes" 

print("I'm here")



""" # ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
    """ 