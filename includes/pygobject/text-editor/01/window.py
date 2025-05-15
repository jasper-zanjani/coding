from gi.repository import Adw
from gi.repository import Gtk

@Gtk.Template(resource_path='/org/gnome/Example/window.ui')
class TextEditorWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'TextEditorWindow'

    textview = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
