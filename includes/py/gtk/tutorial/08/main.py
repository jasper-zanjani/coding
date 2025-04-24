import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Things will go here
        self.box1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.button = Gtk.Button(label="Hello")
        self.button.connect('clicked', self.hello)

        socrates_check = Gtk.CheckButton(label="Socrates")
        socrates_check.greet_name = "Socrates"
        socrates_check.connect("toggled", self.radio_toggled)

        plato_check = Gtk.CheckButton(label="Plato")
        plato_check.greet_name = "Plato"
        plato_check.connect("toggled", self.radio_toggled)
        plato_check.set_group(socrates_check)

        aristotle_check = Gtk.CheckButton(label="Aristotle")
        aristotle_check.greet_name = "Aristotle"
        aristotle_check.connect("toggled", self.radio_toggled)
        aristotle_check.set_group(socrates_check)

        self.set_child(self.box1)
        self.box1.append(self.box2)
        self.box1.append(self.box3)
        self.box2.append(self.button)
        self.box2.append(socrates_check)
        self.box2.append(plato_check)
        self.box2.append(aristotle_check)
        self.set_default_size(600, 250)
        self.set_title("MyApp")

    def radio_toggled(self, button):
        self.greet_name = button.greet_name

    def hello(self, button):
        print(f"Hello, {self.greet_name}!")

class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

app = MyApp(application_id="com.example.GtkApplication")
app.run(sys.argv)
