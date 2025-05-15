
First the resource bundle must be registered using [Gio.Resource][Gio.Resource].
This represents a file path relative from the current working directory at the time of invocation and must be present.

```py
Gio.Resource._register(Gio.Resource.load("gresources.gresource"))
```

Within a PyGObject application, the class definition for the custom widget defined in the template must be decorated with [Gtk.Template][Gtk.Template], and the resource path must be specified.

```py hl_lines="3"
@Gtk.Template(resource_path="/org/gtk/Example/main.ui")
class Window(Adw.ApplicationWindow):
    __gtype_name__ = "Window"
```

Note that the Python identifier of the decorated class **need not** match that of the widget specified in markup, however the variable `__gtype_name__` must be assigned to a string value that **does** match.

