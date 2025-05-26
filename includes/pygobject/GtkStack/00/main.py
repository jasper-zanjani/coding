import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw

class MyApp(Adw.Application):
    def do_activate(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("main.ui")

        win = self.props.active_window
        if not win:
            win = self.builder.get_object("main_window")
        win.set_application(self)
        win.present()

        self.button = self.builder.get_object("toggle_button")
        self.button.connect("toggled", self.on_toggled_button)

    def on_toggled_button(self, button):
        stack = self.builder.get_object("stack")
        if self.button.get_active(): 
            stack.set_visible_child_name("enabled_page")
        else:
            stack.set_visible_child_name("disabled_page")

if __name__ == "__main__":
    app = MyApp()
    app.run()
