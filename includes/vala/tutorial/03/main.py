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

        self.spin_box = builder.get_object("spin_box")
        self.spin_box.connect("value_changed", self.on_value_changed_spin_box)
        self.slider = builder.get_object("slider")
        self.slider.connect("value_changed", self.on_value_changed_slider)

    def on_value_changed_spin_box(self, spinbox):
        self.slider.set_value(spinbox.get_value())

    def on_value_changed_slider(self, slider):
        self.spin_box.set_value(slider.get_value())

app = MyApp()
app.run()
