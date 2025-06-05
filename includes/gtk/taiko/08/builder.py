import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw

class MyApp(Adw.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        builder = Gtk.Builder()
        builder.add_from_file('main.ui')

        win = self.props.active_window
        if not win:
            win = builder.get_object('main_window')
        win.set_application(self)
        win.present()

        button = builder.get_object('button_hello')
        button.connect('clicked', self.hello)

        socrates = builder.get_object('socrates')
        socrates.greet_name = "Socrates"
        socrates.connect('toggled', self.on_toggle_radio)
        self.greet_name = socrates.greet_name

        plato = builder.get_object('plato')
        plato.greet_name = "Plato"
        plato.connect('toggled', self.on_toggle_radio)

        aristotle = builder.get_object('aristotle')
        aristotle.greet_name = "Aristotle"
        aristotle.connect('toggled', self.on_toggle_radio)

    def on_toggle_radio(self, button):
        self.greet_name = button.greet_name

    def hello(self, button):
        print(f'Hello, {self.greet_name}!')

app = MyApp()
app.run()
