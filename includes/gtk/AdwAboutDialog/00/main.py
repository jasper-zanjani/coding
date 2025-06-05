import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw

class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        builder = Gtk.Builder()
        builder.add_from_file("main.ui")

        if not self.props.active_window:
            win = builder.get_object("main_window")
        win.set_application(self)
        win.present()

        button = builder.get_object("button")
        dialog = builder.get_object("about")
        button.connect("clicked", lambda x: dialog.present(win) )

app = MyApp()
app.run()
