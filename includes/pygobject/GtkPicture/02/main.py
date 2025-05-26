import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, GdkPixbuf, Gio

class MyApp(Adw.Application):
    def do_activate(self):
        builder = Gtk.Builder()
        builder.add_from_file("main.ui")

        win = self.props.active_window
        if not win:
            win = builder.get_object("main_window")
        win.set_application(self)
        win.present()

        with open("image.jpg", 'rb') as f:
            image_bytes = f.read()
        loader = GdkPixbuf.PixbufLoader()
        loader.write(image_bytes)
        loader.close()
        image_pixbuf = loader.get_pixbuf()
        picture = builder.get_object("picture")
        picture.set_pixbuf(image_pixbuf)

if __name__ == "__main__":
    app = MyApp()
    app.run()
