# Templates

I have encountered Templates in various contexts, but especially in the Builder application where they are used to organize the application.
It seems to me to be rather undocumented, or rather I have not found very good documentation on the topic, at least coming to it as a learner.
Tutorials start with defining UI in code, and if anything they use XML UI definitions, like Taiko's tutorial.

So the jump from naive tutorials to production-grade applications appears to depend partly on this feature of GTK.

--8<-- "includes/pygobject/templates/info.md"

#### Blueprint

--8<-- "includes/pygobject/templates/blueprint.md"

#### GResource

--8<-- "includes/pygobject/templates/gresources.md"

--8<-- "includes/pygobject/templates/register.md"

#### Boilerplate

This pared-down example shows a "custom" subclass of [Gtk.ApplicationWindow][Gtk.ApplicationWindow] with no changes made.
Even the template class's constructor doesn't need to be overriden.
Running it produces an empty window indistinguishable from Gtk.ApplicationWindow.

Note that unlike when using [Builder][Gtk.Builder], the XML markup is not referenced by the Python logic which loads only the resource bundle.


```py title="main.py"
--8<-- "includes/pygobject/21-template-boilerplate/main.py"
```

```blueprint title="template.blp"
--8<-- "includes/pygobject/21-template-boilerplate/template.blp"
```

```xml title="gresources.xml"
--8<-- "includes/pygobject/21-template-boilerplate/gresources.xml"
```

#### Subclassing Adw.ApplicationWindow

A slightly more interesting variation on the example above (from [libadwaita-examples](https://github.com/FelisDiligens/libadwaita-examples)) shows how the template can package together the more complex [Adw.ApplicationWindow][Adw.ApplicationWindow] which requires [Adw.ToolbarView][Adw.ToolbarView] and [Adw.HeaderBar][Adw.HeaderBar].
The end result, despite the increased complexity, looks the same.

Note that although we are now imitating GNOME convention by placing these files into a **src** directory, for the purposes of the application this has no effect, since the Python references only the resource bundle.

Also note that the custom subclass has been imported from another file, reflecting good modularization practices.


```py title="src/main.py"
--8<-- "includes/pygobject/22-template-boilerplate-adw/main.py"
```

```py title="src/template.py"
--8<-- "includes/pygobject/22-template-boilerplate-adw/template.py"
```

```blueprint title="src/template.blp"
--8<-- "includes/pygobject/22-template-boilerplate-adw/template.blp"
```

```xml title="src/gresources.xml"
--8<-- "includes/pygobject/22-template-boilerplate-adw/gresources.xml"
```

#### Adding widgets

Additional widgets, properties, and handlers can be added without much difficulty.

```py title="src/main.py"
--8<-- "includes/pygobject/24-hello-world-adw/main.py"
```

```py title="src/template.py"
--8<-- "includes/pygobject/24-hello-world-adw/template.py"
```

```blueprint title="src/template.blp"
--8<-- "includes/pygobject/24-hello-world-adw/template.blp"
```

```xml title="src/gresources.xml"
--8<-- "includes/pygobject/24-hello-world-adw/gresources.xml"
```

