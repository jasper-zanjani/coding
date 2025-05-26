import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Adw, Gdk, GLib, Gio, Gtk, GObject

class Fruit(GObject.Object):
    name = GObject.Property(type=str)
    def __init__(self, name):
        super().__init__()
        self.name = name

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Things will go here
        self.grid = Gtk.GridView()

        fruits = ["Banana", "Apple", "Strawberry", "Pear", "Watermelon", "Blueberry"]

        self.ls = Gio.ListStore()
        for f in fruits:
            self.ls.append(Fruit(f))

        ss = Gtk.SingleSelection()
        ss.set_model(self.ls)
        ss.connect("selection-changed", self.on_selected_items_changed)
        self.grid.set_model(ss)

        factory = Gtk.SignalListItemFactory()

        def f_setup(fact, item):
            label = Gtk.Label(halign=Gtk.Align.START)
            label.set_selectable(False)
            item.set_child(label)

        factory.connect("setup", f_setup)
        
        def f_bind(fact, item):
            fruit = item.get_item()
            fruit.bind_property(
                "name", item.get_child(), "label",
                GObject.BindingFlags.SYNC_CREATE
            )
        factory.connect("bind", f_bind)

        self.grid.set_factory(factory)

