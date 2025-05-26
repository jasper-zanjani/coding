import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw

class MyApp(Adw.Application):
    def do_activate(self):
        builder = Gtk.Builder()
        builder.add_from_file("main.ui")

        if not self.props.active_window:
            win = builder.get_object("main_window")
        win.set_application(self)
        win.present()

        self.button = builder.get_object("button")
        self.button.connect("clicked", self.button_clicked)

    def button_clicked(self, button):
        self.button.set_label("Clicked!")

if __name__ == "__main__":
    app = MyApp()
    app.run()
