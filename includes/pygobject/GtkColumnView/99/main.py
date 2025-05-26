import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gio, GObject

starships = {   "USS Enterprise": ("NCC-1701", "TOS"),
                "USS Defiant": ("NX-74205", "DS9"),
                "SSV Normandy": ("SR-1", "ME"),
                "USS Cerritos": ("NCC-75567", "LD"), }

class Starship(GObject.Object):
    def __init__(self, name, registry, franchise):
        super().__init__()

        self._name = name
        self._registry = registry
        self._franchise = franchise

    @GObject.Property(type=str)
    def name(self) -> str:
        return self._name

    @GObject.Property(type=str)
    def registry(self) -> str:
        return self._registry

    @GObject.Property(type=int)
    def franchise(self) -> int:
        return self._franchise

class MyApp(Adw.Application):
    def do_activate(self):
        builder = Gtk.Builder()
        builder.add_from_file("main.ui")
        win = self.props.active_window
        if not win:
            win = builder.get_object("main_window")
        win.set_application(self)
        win.present()

        # Create the data model
        data_model = Gio.ListStore(item_type=Starship)
        for name, starship_info in starships.items():
            data_model.append(Starship(name=name, registry=starship_info[0], franchise=starship_info[1]))

        def _on_factory_setup(_factory, list_item):
            label = Gtk.Label()
            label.set_margin_top(12)
            label.set_margin_bottom(12)
            list_item.set_child(label)


        def _on_factory_bind(_factory, list_item, what):
            label_widget = list_item.get_child()
            book = list_item.get_item()
            label_widget.set_label(str(getattr(book, what)))


        column_view = builder.get_object("column_view")
        col1 = builder.get_object("col1")
        col2 = builder.get_object("col2")
        col3 = builder.get_object("col3")

        col1.get_factory().connect("setup", _on_factory_setup)
        col1.get_factory().connect("bind", _on_factory_bind, "name")
        col2.get_factory().connect("setup", _on_factory_setup)
        col2.get_factory().connect("bind", _on_factory_bind, "registry")
        col3.get_factory().connect("setup", _on_factory_setup)
        col3.get_factory().connect("bind", _on_factory_bind, "franchise")

        sorter_model = Gtk.SortListModel.new(model=data_model, sorter=column_view.get_sorter())
        selection = Gtk.SingleSelection.new(model=sorter_model)
        column_view.set_model(model=selection)

        col1_exp = Gtk.PropertyExpression.new(Starship, None, "name")
        col2_exp = Gtk.PropertyExpression.new(Starship, None, "registry")
        col3_exp = Gtk.PropertyExpression.new(Starship, None, "franchise")

        col1.set_sorter(Gtk.StringSorter.new(col1_exp))
        col2.set_sorter(Gtk.StringSorter.new(col2_exp))
        col3.set_sorter(Gtk.NumericSorter.new(col3_exp))


if __name__ == "__main__":
    app = MyApp()
    app.run()
