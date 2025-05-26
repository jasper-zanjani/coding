import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw


class MyApp(Adw.Application):
    def do_activate(self):
        builder = Gtk.Builder()
        builder.add_from_file("main.ui")

        if not self.props.active_window:
            win = builder.get_object("main_window")
        win.set_application(self)
        win.present()

        string_list = Gtk.StringList.new(['Plato', 'Aristotle', 'Socrates'])
        selection_model = Gtk.SingleSelection.new(string_list)

        def setup_cb(factory, list_item):
            label = Gtk.Label()
            list_item.set_child(label)

        def bind_cb(factory, list_item):
            label = list_item.get_child()
            simple_obj = list_item.get_item()
            label.set_text(simple_obj.get_string())

        factory = Gtk.SignalListItemFactory()
        factory.connect('bind', bind_cb)
        factory.connect('setup', setup_cb)

        list_view = builder.get_object("list_view")
        list_view.set_model(selection_model)
        list_view.set_factory(factory)


if __name__ == "__main__":
    app = MyApp()
    app.run()
