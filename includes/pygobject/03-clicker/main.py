import gi;
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw

class ClickerApp(Adw.Application):
    def do_activate(self):
        builder = Gtk.Builder()
        builder.add_from_file("main.ui")

        button_inc = builder.get_object("button_inc")
        button_dec = builder.get_object("button_dec")
        self.label = builder.get_object("label")
        button_inc.connect("clicked", self.button_inc_clicked)
        button_dec.connect("clicked", self.button_dec_clicked)

        self.number = 0
        self.label.set_label(f"{self.number}")

        win = self.props.active_window
        if not win:
            win = builder.get_object("main_window")
        win.set_application(self)
        win.present()

    def button_inc_clicked(self, button):
        self.number += 1
        self.label.set_label(f"{self.number}")

    def button_dec_clicked(self, button):
        self.number -= 1
        self.label.set_label(f"{self.number}")



if __name__ == "__main__":
    app = ClickerApp()
    app.run()
