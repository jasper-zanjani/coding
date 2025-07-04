import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gio, Adw, Gtk
from template import BoilerplateTemplate

Gio.Resource._register(Gio.Resource.load("gresources.gresource"))

class App(Adw.Application):
    def do_activate(self):
        self.window = BoilerplateTemplate(application=self)
        self.window.present()

if __name__ == "__main__":
    app = App()
    app.run()
