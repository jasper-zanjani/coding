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

        win = self.props.active_window
        if not win:
            win = builder.get_object("main_window")
        win.set_application(self)
        win.present()

        self.overlay = builder.get_object("overlay")

        self.label = builder.get_object("label")
        button = builder.get_object("button")
        button.connect("clicked", self.button_on_clicked)

    def button_on_clicked(self, button):
        toast = Adw.Toast()
        toast.set_title(f"Hello, {self.label.get_label()}!")
        self.overlay.add_toast(toast)

app = MyApp()
app.run()
