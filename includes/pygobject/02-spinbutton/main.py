import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw

class MyApp(Adw.Application):
    def do_activate(self):
        builder = Gtk.Builder()
        builder.add_from_file("main.ui")

        win = self.props.active_window
        if not win:
            win = builder.get_object("main_window")
        win.set_application(self)
        win.present()

        spin = builder.get_object("spin")
        spin.connect("value_changed", self.spin_value_changed)
        self.label = builder.get_object("label")

    def spin_value_changed(self, spin):
        self.label.set_label(f"{spin.get_value()}")

if __name__ == "__main__":
    app = MyApp()
    app.run()
