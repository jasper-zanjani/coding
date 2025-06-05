import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw

class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        builder = Gtk.Builder()
        builder.add_from_file("main.ui")
        
        win = self.props.active_window
        if not win:
            win = builder.get_object("main_window")
        win.set_application(self)
        win.present()


        dw = Gtk.DrawingArea()

        dw.set_hexpand(True)
        dw.set_vexpand(True)

        dw.set_draw_func(self.draw, None)
        box3 = builder.get_object("box3")
        box3.append(dw)

    def draw(self, area, c, w, h, data):
        # c is a Cairo context

        # Fill background with a color
        c.set_source_rgb(0, 0, 0)
        c.paint()

        # Draw a line
        c.set_source_rgb(0.5, 0, 0.5)
        c.set_line_width(3)
        c.move_to(10, 10)
        c.line_to(w - 10, h - 10)
        c.stroke()

        # Draw a rectangle
        c.set_source_rgb(0.8, 0.8, 0)
        c.rectangle (20, 20, 50, 20)
        c.fill()

        # Draw some text
        c.set_source_rgb(0.1, 0.1, 0.1)
        c.select_font_face("Sans")
        c.set_font_size(13)
        c.move_to(25, 35)
        c.show_text("Test")


app = MyApp()
app.run()
