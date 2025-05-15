import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Gdk', '4.0')
from gi.repository import Gtk, Gdk, GObject, GLib

import cairo # For drawing

class MyCircleWidget(Gtk.Widget):
    """
    A custom widget that draws a colored circle.
    """
    # Register the GObject type for our custom widget
    # This is crucial for GTK to recognize and use it, especially from Blueprint.
    __gtype_name__ = 'MyCircleWidget'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._color = Gdk.RGBA(1.0, 0.0, 0.0, 1.0) # Default to red
        self.set_vexpand(True) # Make it expand vertically
        self.set_hexpand(True) # Make it expand horizontally

    # --- GObject Properties ---
    # It's good practice to expose customizable aspects as properties.
    @GObject.Property(type=Gdk.RGBA)
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
        self.queue_draw() # Request a redraw when the color changes

    # --- Core Drawing Logic ---
    def do_vfunc_snapshot(self, snapshot):
        """
        This method is called when GTK needs to draw the widget.
        'snapshot' is a Gtk.Snapshot object.
        """
        # Get the allocated width and height of the widget
        width = self.get_allocated_width()
        height = self.get_allocated_height()

        if width <= 0 or height <= 0:
            return # Nothing to draw if no space

        # Determine circle parameters
        radius = min(width, height) / 3.0
        center_x = width / 2.0
        center_y = height / 2.0

        # Create a Cairo context from the snapshot
        # For simple drawing, append_color is often enough.
        # For more complex graphics, you might use snapshot.append_cairo()
        # and then work with a Cairo context.

        # Let's use snapshot.append_cairo() for a typical drawing example
        bounds = Gdk.Rectangle(x=0, y=0, width=width, height=height)
        cr = snapshot.append_cairo(bounds)

        # Set the drawing color from our property
        Gdk.cairo_set_source_rgba(cr, self._color)

        # Draw the circle
        cr.arc(center_x, center_y, radius, 0, 2 * 3.1415926535) # 2 * pi
        cr.fill()

        # It's important to restore the Cairo state if you modified it extensively,
        # though for this simple example, it's less critical.
        # cr.restore() # if you did cr.save() earlier

    # --- Size Request (Optional but good for layout) ---
    def do_vfunc_measure(self, orientation, for_size):
        """
        This method is called by GTK to determine the widget's preferred size.
        """
        # For this simple example, let's request a minimum size.
        # In a real application, this would be more dynamic.
        if orientation == Gtk.Orientation.HORIZONTAL:
            return (50, 100) # min_width, natural_width
        else: # Gtk.Orientation.VERTICAL
            return (50, 100) # min_height, natural_height

# --- Main Application (for testing) ---
class ExampleApp(Gtk.Application):
    def __init__(self, **kwargs):
        super().__init__(application_id="com.example.customwidgetapp", **kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        win = Gtk.ApplicationWindow(application=app, title="Custom Circle Widget Test")

        # Instantiate our custom widget
        circle_widget = MyCircleWidget()
        circle_widget.set_size_request(200, 200) # Request a specific size

        # You can set its properties directly
        # blue_color = Gdk.RGBA()
        # blue_color.parse("blue") # Using string parsing for color
        # circle_widget.props.color = blue_color

        win.set_child(circle_widget)
        win.present()

if __name__ == "__main__":
    # Register the custom widget type with GObject before creating any instance
    # This is often done at the module level or in the application's startup.
    # However, for simplicity in this single file, we can ensure it's "seen"
    # by GObject by virtue of the class definition. If you were loading this
    # widget from a separate module dynamically or using it in Glade/Blueprint
    # without prior Python instantiation, explicit registration might be needed
    # using GObject.type_register(MyCircleWidget).
    # For PyGObject, simply defining __gtype_name__ is usually sufficient for
    # automatic registration when the class is defined.

    app = ExampleApp()
    app.run(None)
