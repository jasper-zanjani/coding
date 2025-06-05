import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
gi.require_version("GObject", "2.0")
from gi.repository import Gtk, Adw, GObject, Gio

class Starship(GObject.Object):
    def __init__(self, name, registry, crew):
        super().__init__()

        self._name = name
        self._registry = registry
        self._crew = crew

    @GObject.Property(type=str)
    def name(self) -> str:
        return self._name

    @GObject.Property(type=str)
    def registry(self) -> str:
        return self._registry

    @GObject.Property(type=int)
    def crew(self) -> str:
        return self._crew

class MyApp(Adw.Application):
    def get_data(self):
        output = Gio.ListStore(item_type=Starship)
        ships = {"USS Enterprise": ('NCC-1701', 203), 'USS Defiant': ('NX-74205', 50), 'USS Reliant': ('NCC-1864', 35), 'SSV Normandy': ('SR-1', 20), }
        for (name, (registry, crew)) in ships.items():
            output.append(Starship(name, registry, crew))
        return output

    def do_activate(self):
        builder = Gtk.Builder()
        builder.add_from_file("main.ui")

        win = self.props.active_window
        if not win:
            win = builder.get_object("main_window")
        win.set_application(self)
        win.present()

        def on_setup(factory, li):
            label = Gtk.Label()
            bin = Adw.Bin()
            bin.set_child(label)
            li.set_child(bin)

        def on_bind(factory, li):
            bin = li.get_child()
            label = bin.get_child()
            simple_obj = li.get_item()
            label.set_text(simple_obj.name)

        factory = Gtk.SignalListItemFactory()
        factory.connect('setup', on_setup)
        factory.connect('bind', on_bind)

        starships_data = self.get_data()

        model = Gtk.SingleSelection(model = starships_data)
        list_view = builder.get_object("list_view")
        list_view.set_model(model)
        list_view.set_factory(factory)


if __name__ == "__main__":
    app = MyApp()
    app.run()
