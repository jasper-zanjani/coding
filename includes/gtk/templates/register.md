First the resource bundle must be registered using `GioResource` (1).
This represents a file path relative from the current working directory at the time of invocation and must be present.
{: .annotate }

1.  

    --8<-- "includes/gtk/GioResource/callout.md"

```py
Gio.Resource._register(Gio.Resource.load("gresources.gresource"))
```

Within a PyGObject application, the class definition for the custom widget defined in the template must be decorated with `GtkTemplate` (1), and the resource path must be specified.
{: .annotate }

1.  

    --8<-- "includes/gtk/GtkTemplate/callout.md"

```py hl_lines="3"
@Gtk.Template(resource_path="/org/gtk/Example/main.ui")
class Window(Adw.ApplicationWindow):
    __gtype_name__ = "Window"
```

Note that the Python identifier of the decorated class **need not** match that of the widget specified in markup, however the variable `__gtype_name__` must be assigned to a string value that **does** match.

