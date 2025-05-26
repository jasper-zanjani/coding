import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Adw, Gdk, GLib, Gio, Gtk, GObject

class Fruit(GObject.Object):
    name = GObject.Property(type=str)
    def __init__(self, name):
        super().__init__()
        self.name = name

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Things will go here
        self.grid = Gtk.GridView()

        fruits = ["Banana", "Apple", "Strawberry", "Pear", "Watermelon", "Blueberry"]

        self.ls = Gio.ListStore()
        for f in fruits:
            self.ls.append(Fruit(f))

        ss = Gtk.SingleSelection()
        ss.set_model(self.ls)
        ss.connect("selection-changed", self.on_selected_items_changed)
        self.grid.set_model(ss)

        factory = Gtk.SignalListItemFactory()

        def f_setup(fact, item):
            label = Gtk.Label(halign=Gtk.Align.START)
            label.set_selectable(False)
            item.set_child(label)

        factory.connect("setup", f_setup)
        
        def f_bind(fact, item):
            fruit = item.get_item()
            fruit.bind_property(
                "name", item.get_child(), "label",
                GObject.BindingFlags.SYNC_CREATE
            )
        factory.connect("bind", f_bind)

        self.grid.set_factory(factory)

        # Set app name
        GLib.set_application_name("My App")

        self.header = Gtk.HeaderBar()
        self.set_titlebar(self.header)
        self.open_button = Gtk.Button(label="Open")
        self.open_button.set_icon_name("document-open-symbolic")
        self.open_button.connect('clicked', self.show_open_dialog)
        self.open_dialog = Gtk.FileDialog.new()
        self.open_dialog.set_title("Select a file")

        f = Gtk.FileFilter()
        f.set_name("Image files")
        f.add_mime_type("image/jpeg")
        f.add_mime_type("image/png")

        filters = Gio.ListStore.new(Gtk.FileFilter)
        filters.append(f)

        self.open_dialog.set_filters(filters)
        self.open_dialog.set_default_filter(f)
        self.header.pack_start(self.open_button)

        # Create a new Action
        action = Gio.SimpleAction.new("something", None)
        action.connect("activate", self.print_something)
        self.add_action(action)

        # Create an action to run the show_about function
        action = Gio.SimpleAction.new("about", None)
        action.connect("activate", self.show_about)
        self.add_action(action)

        # Create a new menu, containing that action
        menu = Gio.Menu.new()
        menu.append("Do something", "win.something")
        menu.append("About", "win.about")

        # Create a popover
        self.popover = Gtk.PopoverMenu()
        self.popover.set_menu_model(menu)

        # Create a menu button
        self.hamburger = Gtk.MenuButton()
        self.hamburger.set_popover(self.popover)
        self.hamburger.set_icon_name("open-menu-symbolic")

        # Add menu button to the HeaderBar
        self.header.pack_start(self.hamburger)


        self.slider = Gtk.Scale()
        self.slider.set_digits(0)
        self.slider.set_range(0,10)
        self.slider.set_draw_value(True)
        self.slider.set_value(5)
        self.slider.connect('value-changed', self.slider_slid)

        css_provider = Gtk.CssProvider()
        css_provider.load_from_path('style.css')
        Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        self.box1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.button = Gtk.Button(label="Hello")
        self.button.connect('clicked', self.hello)

        socrates_check = Gtk.CheckButton(label="Socrates")
        socrates_check.greet_name = "Socrates"
        socrates_check.connect("toggled", self.radio_toggled)

        plato_check = Gtk.CheckButton(label="Plato")
        plato_check.greet_name = "Plato"
        plato_check.connect("toggled", self.radio_toggled)
        plato_check.set_group(socrates_check)

        aristotle_check = Gtk.CheckButton(label="Aristotle")
        aristotle_check.greet_name = "Aristotle"
        aristotle_check.connect("toggled", self.radio_toggled)
        aristotle_check.set_group(socrates_check)

        self.switch_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.switch = Gtk.Switch()
        self.switch.set_active(True)
        self.switch.connect("state-set", self.switch_switched)

        self.label = Gtk.Label(label="A switch")
        self.label.set_css_classes(['title'])
        self.switch_box.set_spacing(5)

        self.switch_box.append(self.switch)
        self.switch_box.append(self.label)
        self.box2.append(self.switch_box)

        self.set_child(self.box1)
        self.box1.append(self.box2)
        self.box1.append(self.box3)
        self.box2.append(self.button)
        self.box2.append(socrates_check)
        self.box2.append(plato_check)
        self.box2.append(aristotle_check)
        self.box2.append(self.slider)
        self.box3.append(self.grid)
        self.set_default_size(600, 250)
        self.set_title("MyApp")

    def on_selected_items_changed(selection, position, n_items):
        selected_item = selection.get_selected_item()
        if selected_item is not None:
            print(f"Selected item changed to: {selected_item.name}")

    def show_about(self, action, param):
        dialog = Adw.AboutWindow(transient_for=self)
        dialog.set_application_name("App name")
        dialog.set_version("1.0")
        dialog.set_developer_name("Developer")
        dialog.set_license_type(Gtk.License(Gtk.License.GPL_3_0))
        dialog.set_comments("Adw.AboutWindow example")
        dialog.set_website("https://localhost")
        # Icon must be uploaded to $HOME/.local/share/icons or /usr/share/icons
        dialog.set_application_icon("com.github.devname.appname")

        dialog.set_visible(True)

        # self.about = Gtk.AboutDialog()
        #
        # # Sets dialog in front of main window
        # self.about.set_transient_for(self)
        #
        # self.about.set_modal(True)
        #
        # self.about.set_authors(["Your Name"])
        # self.about.set_copyright("Copyright 2022 Your Full Name")
        # self.about.set_license_type(Gtk.License.GPL_3_0)
        # self.about.set_website("http://example.com")
        # self.about.set_website_label("My Website")
        # self.about.set_version("1.0")
        #
        # # This icon will have to be added to an appropriate location
        # # i.e. /usr/share/icons/hicolor/scalable/apps/org.example.example.svg
        # self.about.set_logo_icon_name("org.example.example")
        #
        # self.about.set_visible(True)
        #
    def print_something(self, action, param):
        print("Something!")

    def show_open_dialog(self, button):
        self.open_dialog.open(self, None, self.open_dialog_open_callback)

    def open_dialog_open_callback(self, dialog, result):
        try:
            file = dialog.open_finish(result)
            if file is not None:
                print(f"File path is {file.get_path()}")
        except GLib.Error as error:
            print(f"Error opening file: {error.message}")

    def slider_slid(self, slider):
        print(f"Slider changed to {int(slider.get_value())}")

    def switch_switched(self, switch, state):
        print(f"The switch has been switched {'on' if state else 'off'}")

    def radio_toggled(self, button):
        self.greet_name = button.greet_name

    def hello(self, button):
        print(f"Hello, {self.greet_name}!")

class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)
        self.win = None

    def on_activate(self, app):
        if not self.win:
            self.win = MainWindow(application=app)
        self.win.present()

app = MyApp(application_id="com.example.GtkApplication")
app.run(sys.argv)
