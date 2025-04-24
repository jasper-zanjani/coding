import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Adw, Gtk

class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        # Create a Builder
        builder = Gtk.Builder()
        builder.add_from_file("tutorial.ui")

        # Get button widget and connect it to a function
        button = builder.get_object("button1")
        button.connect("clicked", self.hello)
        

        # Get main window
        self.win = builder.get_object("main_window")
        self.win.set_application(self)
        self.win.present()

    def hello(self, button):
        print("Hello, World!")

app = MyApp(application_id="com.example.GtkApplication")
app.run(sys.argv)
