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

        def on_setup(factory, li):
            label = Gtk.Label()
            bin = Adw.Bin()
            bin.set_child(label)
            li.set_child(bin)

        def on_bind(factory, li):
            bin = li.get_child()
            label = bin.get_child()
            simple_obj = li.get_item()
            label.set_text(simple_obj.get_string())

        # Create BuilderListItemFactory for ListView
        factory = Gtk.SignalListItemFactory()
        factory.connect('setup', on_setup)
        factory.connect('bind', on_bind)

        string_model = Gtk.StringList.new(['USS Enterprise', 'SSV Normandy', 'Millennium Falcon'])
        model = Gtk.SingleSelection(model = string_model)
        list_view = builder.get_object("list_view")
        list_view.set_model(model)
        list_view.set_factory(factory)


if __name__ == "__main__":
    app = MyApp()
    app.run()
