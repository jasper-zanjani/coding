import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gio, Gtk, Adw, GObject

class Philosopher(GObject.Object):
    def __init__(self, name):
        super().__init__()
        self._name = name

    @GObject.Property(type=str)
    def name(self)-> str:
        return self._name

class MyApp(Adw.Application):
    def do_activate(self):
        builder = Gtk.Builder()
        builder.add_from_file("main.ui")

        win = self.props.active_window
        if not win:
            win = builder.get_object("main_window")
        win.set_application(self)
        win.present()

        philosophers = ['Plato', 'Aristotle', 'Socrates']
        list_store = Gio.ListStore(item_type=Philosopher)
        for p in philosophers:
            list_store.append(Philosopher(p))
        model = Gtk.SingleSelection(model=list_store)
        list_view = builder.get_object("list_view")
        list_view.set_model(model)

if __name__ == "__main__":
    app = MyApp()
    app.run()
