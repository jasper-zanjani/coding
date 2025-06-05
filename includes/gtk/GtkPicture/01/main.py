import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gdk, Gio

class MyApp(Adw.Application):
    def do_activate(self):
        builder = Gtk.Builder()
        builder.add_from_file("main.ui")

        win = self.props.active_window
        if not win:
            win = builder.get_object("main_window")
        win.set_application(self)
        win.present()

        image_file = Gio.File.new_for_path("image.jpg")
        picture = builder.get_object("picture")
        texture = Gdk.Texture.new_from_file(image_file)
        picture.set_paintable(texture)

if __name__ == "__main__":
    app = MyApp()
    app.run()
