import gi
gi.require_version('Gtk', '3.0')
gi.require_version("WebKit2", "4.1")
from gi.repository import Gtk, Adw, WebKit

class MyApp(Adw.Application):
    def do_activate(self):
        builder = Gtk.Builder()
        builder.add_from_file("main.ui")

        win = self.props.active_window
        if not win:
            win = builder.get_object("main_window")
        win.set_application(self)
        win.present()

if __name__ == "__main__":
    app = MyApp()
    app.run()
