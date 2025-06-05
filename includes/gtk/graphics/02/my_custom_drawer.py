import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Gdk', '4.0')
from gi.repository import Gtk, Gdk, GObject
import cairo
import math

class MyCustomDrawer(Gtk.Widget):
    __gtype_name__ = 'MyCustomDrawer'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._draw_color = Gdk.RGBA(0.2, 0.2, 0.8, 1.0) # Default: A nice blue
        self.set_vexpand(True)
        self.set_hexpand(True)
        
        # --- Additions for Debugging ---
        self.set_visible(True) # Explicitly set widget to visible
        print(f"[MyCustomDrawer] __init__ called. Visible: {self.get_visible()}")
        self.connect("map", self._on_mapped)
        # --- End Additions ---

    # --- Added for Debugging ---
    def _on_mapped(self, widget):
        parent_type = type(self.get_parent()).__name__ if self.get_parent() else "None"
        print(f"[MyCustomDrawer] Widget has been MAPPED. Parent is '{parent_type}'.")
        self.queue_resize() # Request measure/allocate pass
        print("[MyCustomDrawer] Called queue_resize() on map.")
    # --- End Additions ---

    def set_circle_color(self, red, green, blue, alpha=1.0):
        print(f"[MyCustomDrawer] set_circle_color called with r={red}, g={green}, b={blue}, a={alpha}")
        self._draw_color.red = red
        self._draw_color.green = green
        self._draw_color.blue = blue
        self._draw_color.alpha = alpha
        self.queue_draw()

    def do_vfunc_measure(self, orientation, for_size):
        print(f"[MyCustomDrawer] >>>>>>> do_vfunc_measure CALLED for {'H' if orientation == Gtk.Orientation.HORIZONTAL else 'V'}, for_size={for_size}")
        if orientation == Gtk.Orientation.HORIZONTAL:
            min_w, nat_w = (50, 150)
            print(f"[MyCustomDrawer] Reporting for H: min={min_w}, natural={nat_w}")
            return (min_w, nat_w)
        else: # Gtk.Orientation.VERTICAL
            min_h, nat_h = (50, 150)
            print(f"[MyCustomDrawer] Reporting for V: min={min_h}, natural={nat_h}")
            return (min_h, nat_h)

    def do_vfunc_snapshot(self, snapshot):
        width = self.get_allocated_width()
        height = self.get_allocated_height()
        color_str = self._draw_color.to_string() if self._draw_color else "None"
        print(f"[MyCustomDrawer] >>>>>>> do_vfunc_snapshot CALLED. Size: {width}x{height}, Color: {color_str}")

        if width <= 0 or height <= 0:
            print("[MyCustomDrawer] Skipping snapshot: width or height is zero or negative.")
            return

        if not self._draw_color:
            print("[MyCustomDrawer] Skipping snapshot: _draw_color is None.")
            return
            
        bounds = Gdk.Rectangle(x=0, y=0, width=width, height=height)
        cr = snapshot.append_cairo(bounds)

        Gdk.cairo_set_source_rgba(cr, self._draw_color)

        radius = min(width, height) / 2.5
        center_x = width / 2.0
        center_y = height / 2.0
        cr.arc(center_x, center_y, radius, 0, 2 * math.pi)
        cr.fill()
        print("[MyCustomDrawer] Circle drawn.")
