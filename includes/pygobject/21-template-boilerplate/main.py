import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gio, Adw, Gtk

Gio.Resource._register(Gio.Resource.load("gresources.gresource"))

@Gtk.Template(resource_path="/org/gtk/Boilerplate/template.ui")
class BoilerplateTemplate(Gtk.ApplicationWindow):
    __gtype_name__ = "BoilerplateTemplate"

class App(Adw.Application):
    def do_activate(self):
        if not self.props.active_window:
            win = BoilerplateTemplate(application=self)
        win.present()

if __name__ == "__main__":
    app = App()
    app.run()
