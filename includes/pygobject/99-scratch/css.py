import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw


class MyWindow(Adw.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app)
        self.set_title("Box with Border")
        self.set_default_size(200, 100)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.set_content(box)

        # Add a CSS class to the box
        box.add_css_class("bordered-box")

        # Create a CssProvider and load CSS
        css_provider = Gtk.CssProvider()
        css = """
        .bordered-box {
            border: 2px solid red;
            background-color: lightblue;
            margin: 5px; # Optional: add some margin outside the border
            padding: 5px; # Optional: add some padding inside the border
        }
        """
        css_provider.load_from_data(css.encode())

        # Apply the CSS to the box's style context
        style_context = box.get_style_context()
        style_context.add_provider(css_provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)

        label = Gtk.Label(label="This box has a border.")
        box.append(label)


class MyApp(Adw.Application):
    def __init__(self):
        super().__init__(application_id="com.example.BoxWithBorder")

    def do_activate(self):
        window = MyWindow(self)
        window.present()


if __name__ == "__main__":
    app = MyApp()
    app.run()
