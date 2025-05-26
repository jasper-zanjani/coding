import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

class MyApp(Gtk.Application):
    def do_activate(self):
        win = Gtk.ApplicationWindow(application=app)
        win.set_default_size(200, 200)

        string_list = Gtk.StringList.new(['Plato', 'Aristotle', 'Socrates'])
        selection_model = Gtk.SingleSelection(model=string_list)

        def setup_cb(factory, list_item):
            label = Gtk.Label()
            list_item.set_child(label)

        def bind_cb(factory, list_item):
            label = list_item.get_child()
            simple_obj = list_item.get_item()
            label.set_text(simple_obj.get_string())

        factory = Gtk.SignalListItemFactory()
        factory.connect("bind", bind_cb)
        factory.connect("setup", setup_cb)

        list_view = Gtk.ListView.new(selection_model, factory)

        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_child(list_view)
        win.set_child(scrolled_window)
        win.present()

if __name__ == "__main__":
    app = MyApp(application_id="org.example.SimpleSignalListItemFactory")
    app.run(None)
