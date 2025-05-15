import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Gdk', '4.0')
# GLib is good practice to import if using GObject.Property, though often available via GObject
from gi.repository import Gtk, Gdk, GObject, GLib 

import cairo 
import math

class MyCircleWidget(Gtk.Widget):
    __gtype_name__ = 'MyCircleWidget'

    def __init__(self, **kwargs):
        # Initialize the backing field for the GObject property *before* super().__init__().
        # This ensures self._color exists if any part of GObject/GTK construction tries to access it early
        # via the property's getter, even though direct setting by GObject default happens later.
        self._color = Gdk.RGBA(0.9, 0.1, 0.1, 1.0) # A distinct initial red for self._color
        print(f"[MyCircleWidget MODIFIED PROP] self._color initialized to: {self._color.to_string()} before super")

        super().__init__(**kwargs) # GObject construction happens here.
        
        print(f"[MyCircleWidget MODIFIED PROP] __init__ called (after super).")
        # self._color should still be the red we set, unless super somehow changed it (unlikely for Gtk.Widget)
        
        self.set_vexpand(True)
        self.set_hexpand(True)
        self.set_visible(True) 
        
        print(f"[MyCircleWidget MODIFIED PROP] Initial vexpand: {self.get_vexpand()}, hexpand: {self.get_hexpand()}, visible: {self.get_visible()}")
        print(f"[MyCircleWidget MODIFIED PROP] self._color in __init__ (after super): {self._color.to_string()}")
        
        self.connect("map", self._on_mapped)
        self.connect("unmap", self._on_unmapped)
        print(f"[MyCircleWidget MODIFIED PROP] __init__ finished. Current self._color: {self._color.to_string()}")


    def _on_mapped(self, widget):
        print(f"[MyCircleWidget MODIFIED PROP] Widget has been MAPPED. Parent: {self.get_parent()}")
        # At this point, the widget is in the scene. Properties from Blueprint should have been applied.
        # self._color should reflect what Blueprint set, or the initial __init__ value if Blueprint didn't set 'color'.
        print(f"[MyCircleWidget MODIFIED PROP] self._color on map: {self._color.to_string()}")
        self.queue_resize() 
        print(f"[MyCircleWidget MODIFIED PROP] Called queue_resize() on map.")

    def _on_unmapped(self, widget):
        print(f"[MyCircleWidget MODIFIED PROP] Widget has been UNMAPPED.")

    # MODIFICATION: Removed 'default=Gdk.RGBA(...)' from the decorator.
    # The "default" value of this property will now effectively be whatever self._color
    # is initialized to in __init__(), until the setter is called (e.g. by Blueprint).
    @GObject.Property(type=Gdk.RGBA, 
                      nick="Color",
                      blurb="The fill color of the circle")
    def color(self):
        # self._color should always exist due to __init__
        print(f"[MyCircleWidget MODIFIED PROP] color property GET returning: {self._color.to_string()}")
        return self._color

    @color.setter
    def color(self, value: Gdk.RGBA): # Added type hint for clarity
        print(f"[MyCircleWidget MODIFIED PROP] color property SET called with: {value.to_string() if value else 'None'}")
        if not isinstance(value, Gdk.RGBA):
             print(f"[MyCircleWidget MODIFIED PROP] WARNING: Invalid type for color property: {type(value)}. Ignoring.")
             return

        # Compare with current self._color. self._color is guaranteed to exist by __init__.
        if not self._color.equal(value):
            self._color = value
            print(f"[MyCircleWidget MODIFIED PROP] Color changed to {self._color.to_string()}, calling queue_draw().")
            self.queue_draw()
        else:
            print(f"[MyCircleWidget MODIFIED PROP] Color set to same value ({self._color.to_string()}), no redraw needed by setter.")

    def do_vfunc_snapshot(self, snapshot: Gtk.Snapshot): # Added type hint
        width = self.get_allocated_width()
        height = self.get_allocated_height()
        
        # self._color should be a valid Gdk.RGBA due to __init__ and property setter logic.
        current_color_str = self._color.to_string()
        
        print(f"[MyCircleWidget MODIFIED PROP] >>>>>>> do_vfunc_snapshot CALLED! width={width}, height={height}, color={current_color_str}")

        if width <= 0 or height <= 0:
            print("[MyCircleWidget MODIFIED PROP] Skipping draw: width or height is zero/negative.")
            return

        bounds = Gdk.Rectangle(x=0, y=0, width=width, height=height)
        cr = snapshot.append_cairo(bounds)
        
        Gdk.cairo_set_source_rgba(cr, self._color) # Use self._color directly
        # For now, draw the rectangle to confirm drawing. Then we'll switch to circle.
        cr.rectangle(0, 0, width, height) 
        cr.fill()
        print(f"[MyCircleWidget MODIFIED PROP] Filled rectangle from (0,0) to ({width},{height}) with {current_color_str}")

        # --- Circle Drawing (to be uncommented once rectangle works reliably) ---
        # radius = min(width, height) / 3.0
        # center_x = width / 2.0
        # center_y = height / 2.0
        # print(f"[MyCircleWidget MODIFIED PROP] Circle params: radius={radius}, cx={center_x}, cy={center_y}")
        # cr.arc(center_x, center_y, radius, 0, 2 * math.pi)
        # cr.fill() # Fill the arc
        # print(f"[MyCircleWidget MODIFIED PROP] Attempted to draw and fill circle with {current_color_str}")


    def do_vfunc_measure(self, orientation, for_size):
        print(f"[MyCircleWidget MODIFIED PROP] >>>>>>> do_vfunc_measure CALLED! orientation={'H' if orientation == Gtk.Orientation.HORIZONTAL else 'V'}, for_size={for_size}")
        min_size, nat_size = (50, 100) # Original tutorial values
        print(f"[MyCircleWidget MODIFIED PROP] do_vfunc_measure reporting min={min_size}, natural={nat_size}")
        return (min_size, nat_size)

# The if __name__ == "__main__": block for direct testing can be added back if needed,
# similar to the simplified version, but adapted to set the 'color' property.
# For now, we are focusing on making it work with main_app.py and window.ui.
