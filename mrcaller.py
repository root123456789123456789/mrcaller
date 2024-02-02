from pynput import keyboard,mouse

def on_mouve(x,y):
    print("Pointer mouved to {}".format(x,y))

def on_click(x,y,button,pressed):
    print("{} at {}".format('Pressed' if pressed else 'Realed',(x,y)))
    if not pressed:
        return False
'''
def get_key(key):
    if isinstance(key,keyboard.KeyCode):
        return key.char
    else:
        return str(key)


def press(key):
    name_key = get_key(key)
    print("key {} presse".format(name_key))

def release(key):
    name_key = get_key(key)
    print("key {} release".format(name_key))
    if key == keyboard.Key.esc:
        print("Exiting...")
        return False

with keyboard.Listener(
    on_press=press,
    on_release=release) as listener:
    listener.join()
'''
with mouse.Listener(
    on_mouve = on_mouve,
    on_click = on_click
    ) as listener:
    listener.join()