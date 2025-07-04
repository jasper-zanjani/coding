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

        scale = builder.get_object("scale")
        scale.connect("value_changed", self.scale_value_changed)
        self.label = builder.get_object("label")

    def scale_value_changed(self, scale):
        self.label.set_label(f"{scale.get_value()}")

if __name__ == "__main__":
    app = MyApp()
    app.run()
