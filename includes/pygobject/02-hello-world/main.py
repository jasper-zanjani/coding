import gi;
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

class MyApp(Gtk.Application):
    def do_activate(self):
        builder = Gtk.Builder()
        builder.add_from_file("main.ui")

        win = self.props.active_window
        if not win:
            win = builder.get_object("main_window")
        win.set_application(self)
        win.present()

        button = builder.get_object("button")
        button.connect("clicked", self.button_clicked)

    def button_clicked(self, button):
        button.set_label("Hello, World!");
        

if __name__ == "__main__":
    app = MyApp()
    app.run()
