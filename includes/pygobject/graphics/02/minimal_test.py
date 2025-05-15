import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Gdk', '4.0')
from gi.repository import Gtk, Gdk, GObject
import cairo
import math

# 1. Define the Custom Widget
class MinimalDrawer(Gtk.Widget):
    __gtype_name__ = 'MinimalDrawer'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._color = Gdk.RGBA(0.8, 0.2, 0.2, 1.0) # Red
        self.set_vexpand(True)
        self.set_hexpand(True)
        self.set_visible(True) # Explicitly set visible
        print("[MinimalDrawer] __init__ called.")

    def do_vfunc_measure(self, orientation, for_size):
        print(f"[MinimalDrawer] do_vfunc_measure CALLED - Orientation: {'H' if orientation == Gtk.Orientation.HORIZONTAL else 'V'}")
        if orientation == Gtk.Orientation.HORIZONTAL:
            return (50, 100) # min_width, natural_width
        else:
            return (50, 100) # min_height, natural_height

    def do_vfunc_snapshot(self, snapshot):
        width = self.get_allocated_width()
        height = self.get_allocated_height()
        print(f"[MinimalDrawer] do_vfunc_snapshot CALLED - Size: {width}x{height}")

        if width <= 0 or height <= 0:
            print("[MinimalDrawer] Skipping snapshot due to zero size.")
            return

        bounds = Gdk.Rectangle(x=0, y=0, width=width, height=height)
        cr = snapshot.append_cairo(bounds) # Get Cairo context from snapshot

        Gdk.cairo_set_source_rgba(cr, self._color)
        
        # Draw a simple rectangle filling the widget
        cr.rectangle(0, 0, width, height)
        cr.fill()
        print("[MinimalDrawer] Rectangle drawn.")

# 2. Define a simple Application class
class TestApplication(Gtk.Application):
    def __init__(self):
        super().__init__(application_id='com.example.minimaldrawer')
        print("[TestApplication] __init__")

    def do_activate(self):
        print("[TestApplication] do_activate")
        window = Gtk.ApplicationWindow(application=self, title="Minimal Drawer Test")
        
        drawing_area = MinimalDrawer()
        
        window.set_child(drawing_area)
        window.set_default_size(200, 200)
        window.present()
        print("[TestApplication] Window presented.")

# 3. Run the Application
if __name__ == '__main__':
    print("Starting application...")
    app = TestApplication()
    exit_status = app.run(None)
    print(f"Application finished with status: {exit_status}")
