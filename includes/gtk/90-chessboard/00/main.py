import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
gi.require_version("Gdk", "4.0")
from gi.repository import Adw, Gtk, Gdk, Graphene, Gsk
from chessboard import Chessboard


class MyApp(Adw.Application):
    def do_activate(self):
        builder = Gtk.Builder()
        builder.add_from_file("main.ui")

        win = self.props.active_window
        if not win:
            win = builder.get_object("main_window")
        win.set_application(self)
        win.present()
        label = builder.get_object('label')
        box = builder.get_object('box')
        chessboard = Chessboard(hexpand = True, vexpand = True)
        box.insert_child_after(chessboard, label)

if __name__ == "__main__":
    app = MyApp()
    app.run()
