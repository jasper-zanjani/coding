import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1') # Optional, for Adwaita application class
from gi.repository import Gtk, Adw, Gio, GObject

# IMPORTANT: Python needs to know about MyCustomDrawer before the UI is loaded.
from my_custom_drawer import MyCustomDrawer

@Gtk.Template(filename='window.ui')
class MyApplicationWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MyApplicationWindow'

    # Get a reference to our custom widget from the Blueprint file
    custom_drawing_area = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # You could set an initial color here if desired, e.g.:
        # self.custom_drawing_area.set_circle_color(1.0, 0.5, 0.0) # Orange

    @Gtk.Template.Callback()
    def on_color_button_clicked(self, button):
        print("Button clicked! Changing circle color to green.")
        # Call the method on our custom widget instance
        if self.custom_drawing_area:
            self.custom_drawing_area.set_circle_color(0.1, 0.7, 0.1) # Green
        else:
            print("Error: custom_drawing_area not found!")

class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(application_id="com.example.simplecustomdrawer", **kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MyApplicationWindow(application=app)
        self.win.present()

if __name__ == "__main__":
    # It's good practice to ensure the custom widget type is registered if loaded
    # from a separate module, though the import and __gtype_name__ usually suffice.
    # If you encounter issues where GTK can't find 'MyCustomDrawer', uncommenting this
    # GObject.type_register(MyCustomDrawer) before app = MyApp() might be needed.
    # However, try without it first as it's typically handled automatically.
    
    app = MyApp()
    app.run(None)
