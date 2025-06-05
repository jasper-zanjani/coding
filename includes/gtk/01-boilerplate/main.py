import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw

class MyApp(Adw.Application): # (1)
    def do_activate(self): # (5)
        builder = Gtk.Builder()
        builder.add_from_file("main.ui")

        win = self.props.active_window # (3)
        if not win:
            win = builder.get_object("main_window")
        win.set_application(self) # (2)
        win.present()

app = MyApp() # (4)
app.run()
