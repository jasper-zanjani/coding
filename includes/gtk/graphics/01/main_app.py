import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1') # Optional: For Adwaita styles, if desired
from gi.repository import Gtk, Gio, GObject, Gdk, Adw

# Crucially, Python needs to know about MyCircleWidget *before* the UI is loaded
# if the UI directly instantiates it. Importing the module makes the class available.
from my_circle_widget import MyCircleWidget

# It's good practice to explicitly register types if they might not be
# automatically picked up, especially if they are in separate files.
# However, for PyGObject, defining __gtype_name__ and importing the module
# where the class is defined is usually sufficient for the type to be known.
# If you encounter issues, GObject.type_register(MyCircleWidget) can be used here.
# GObject.type_register(MyCircleWidget) # Usually not needed if imported correctly

@Gtk.Template(filename='window.ui')
class ExampleAppWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'ExampleAppWindow'

    # Access widgets defined in Blueprint by their ID
    my_custom_circle = Gtk.Template.Child()
    # change_color_button = Gtk.Template.Child() # No need to get it if only connecting signal

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @Gtk.Template.Callback()
    def change_color_button_clicked(self, button):
        print("Button clicked! Changing circle color.")
        current_color_str = self.my_custom_circle.props.color.to_string()
        print(f"Current color: {current_color_str}")

        # Create a Gdk.RGBA object for green
        green_color = Gdk.RGBA()
        green_color.red = 0.0
        green_color.green = 0.8
        green_color.blue = 0.2
        green_color.alpha = 1.0
        self.my_custom_circle.props.color = green_color # Set property
        # self.my_custom_circle.color = green_color # Or using the setter directly

        # Alternatively, parse from string
        # new_color = Gdk.RGBA()
        # new_color.parse("green")
        # self.my_custom_circle.props.color = new_color

        print(f"New color set to: {self.my_custom_circle.props.color.to_string()}")


class MyApp(Adw.Application): # Or Gtk.Application if not using Adwaita
    def __init__(self, **kwargs):
        super().__init__(application_id="com.example.customwidgetblueprint",
                         flags=Gio.ApplicationFlags.FLAGS_NONE,
                         **kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = ExampleAppWindow(application=app)
        self.win.present()

if __name__ == "__main__":
    # Ensure GObject knows about our custom widget type *before* any UI
    # referencing it is built. Importing the module usually does the trick.
    # If MyCircleWidget was in this file, its class definition would handle it.
    # If in doubt, uncommenting this won't hurt:
    # GObject.type_register(MyCircleWidget)

    app = MyApp()
    app.run(None)
