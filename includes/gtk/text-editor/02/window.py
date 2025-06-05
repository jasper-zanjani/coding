from gi.repository import Adw
from gi.repository import Gtk
from gi.repository import Gio

@Gtk.Template(resource_path='/org/gnome/Example/window.ui')
class TextEditorWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'TextEditorWindow'

    textview = Gtk.Template.Child()
    open_button = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        open_action = Gio.SimpleAction(name="open")
        open_action.connect("activate", self.open_file_dialog)
        self.add_action(open_action)

    def open_file_dialog(self, action, _):
        self._native = Gtk.FileChooserNative(
            title="Open File",
            transient_for=self,
            action=Gtk.FileChooserAction.OPEN,
            accept_label="_Open",
            cancel_label="_Cancel",
        )
        self._native.connect("response", self.on_open_response)
        self._native.show()

    def on_open_response(self, dialog, response):
        if response == Gtk.ResponseType.ACCEPT:
            self.open_file(dialog.get_file())
        self._native = None

    def open_file(self, file):
        print("open_file fired!")
