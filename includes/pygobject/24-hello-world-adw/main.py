import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gio, Adw
from template import BoilerplateTemplate

Gio.Resource._register(Gio.Resource.load("gresources.gresource"))

APP_ID = "com.example.BoilerplateTemplateApplication"

class App(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect("activate", self.on_activate)

    def on_activate(self, app):
        win = BoilerplateTemplate(application=app)
        win.present()


if __name__ == "__main__":
    app = App(application_id=APP_ID)
    app.run()
