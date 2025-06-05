import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Gsk', '4.0')
gi.require_version('Graphene', '1.0')
from gi.repository import Gtk, Gsk, Gdk, GLib, Graphene

class AppWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_default_size(200, 150)
        self.set_title("Gsk.Renderer Hello")

        self.drawing_area = Gtk.DrawingArea()
        self.drawing_area.set_draw_func(self.on_draw)
        self.set_child(self.drawing_area)
        self.gsk_renderer = None

    def on_draw(self, drawing_area, cr, width, height):
        red_color = Gdk.RGBA()
        red_color.red = 1.0
        red_color.green = 0.0
        red_color.blue = 0.0
        red_color.alpha = 1.0
        # color_node = Gsk.ColorNode.new(red_color, Gdk.Rectangle(x=0, y=0, width=width, height=height))
        color_node = Gsk.ColorNode.new(red_color, Graphene.Rect(x=0, y=0, width=width, height=height))
        root_node = color_node
        snapshot = cr
        snapshot.append_node(root_node)

class HelloGskApp(Gtk.Application):
    def __init__(self, **kwargs):
        super().__init__(application_id="org.example.hellogsk", **kwargs)
        self.connect("activate", self.on_activate)

    def on_activate(self, app):
        self.win = AppWindow(application=self)
        self.win.present()

if __name__ == "__main__":
    app = HelloGskApp()
    app.run(None)
