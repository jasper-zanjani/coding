from gi.repository import Gtk, Adw

@Gtk.Template(resource_path="/org/gtk/Example/template.ui")
class BoilerplateTemplate(Adw.ApplicationWindow):
    __gtype_name__ = "BoilerplateTemplate"
    button = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.button.connect("clicked", self.on_button_clicked)

    def on_button_clicked(self, button):
        button.set_label("Hello World!")
