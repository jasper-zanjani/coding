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

        # Create BuilderListItemFactory for ListView
        string_model = Gtk.StringList.new(['USS Enterprise', 'SSV Normandy', 'Millennium Falcon'])
        model = Gtk.SingleSelection(model = string_model)
        list_view = builder.get_object("list_view")
        list_view.set_model(model)


        # starships_listview = Gtk.ListView()

if __name__ == "__main__":
    app = MyApp()
    app.run()
