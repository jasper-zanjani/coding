from gi.repository import Gtk, Adw

@Gtk.Template(resource_path="/org/gtk/Example/template.ui")
class BoilerplateTemplate(Adw.ApplicationWindow):
    __gtype_name__ = "BoilerplateTemplate"

