# Templates

I have encountered Templates in various contexts, but especially in the Builder application where they are used to organize the application.
It seems to me to be rather undocumented, or rather I have not found very good documentation on the topic, at least coming to it as a learner.
Tutorials start with defining UI in code, and if anything they use XML UI definitions, like Taiko's tutorial.

So the jump from naive tutorials to production-grade applications appears to depend partly on this feature of GTK.

--8<-- "includes/gtk/templates/info.md"

#### Blueprint

--8<-- "includes/gtk/templates/blueprint.md"

#### GResource

--8<-- "includes/gtk/templates/gresources.md"

--8<-- "includes/gtk/templates/register.md"

#### Boilerplate

This pared-down example shows a "custom" subclass of `ApplicationWindow` (1) with no changes made.
Even the template class's constructor doesn't need to be overriden.
Running it produces an empty window indistinguishable from ApplicationWindow.
{: .annotate }

1.  

    --8<-- "includes/gtk/callouts/gtkapplicationwindow.md"

Note that unlike when using `Builder` (1), the XML markup is not referenced by the Python logic which loads only the resource bundle.
{: .annotate }

1.  

    --8<-- "includes/gtk/callouts/gtkbuilder.md"

<!-- -->

```py title="main.py"
--8<-- "includes/gtk/01-boilerplate-template/main.py"
```

```blueprint title="template.blp"
--8<-- "includes/gtk/01-boilerplate-template/template.blp"
```

```xml title="gresources.xml"
--8<-- "includes/gtk/01-boilerplate-template/gresources.xml"
```

#### Subclassing AdwApplicationWindow

A slightly more interesting variation on the example above (from [libadwaita-examples](https://github.com/FelisDiligens/libadwaita-examples)) shows how the template can package together the more complex `AdwApplicationWindow` (1) which requires `AdwToolbarView` (2) and `AdwHeaderBar` (3).
The end result, despite the increased complexity, looks the same.
{: .annotate }

1.  

    --8<-- "includes/gtk/callouts/adwapplicationwindow.md"

2.  

    --8<-- "includes/gtk/callouts/adwtoolbarview.md"

3.  

    --8<-- "includes/gtk/callouts/adwheaderbar.md"

Note that although we are now imitating GNOME convention by placing these files into a **src** directory, for the purposes of the application this has no effect, since the Python references only the resource bundle.

Also note that the custom subclass has been imported from another file, reflecting good modularization practices.


```py title="src/main.py"
--8<-- "includes/gtk/02-boilerplate-template-adw/main.py"
```

```py title="src/template.py"
--8<-- "includes/gtk/02-boilerplate-template-adw/template.py"
```

```blueprint title="src/template.blp"
--8<-- "includes/gtk/02-boilerplate-template-adw/template.blp"
```

```xml title="src/gresources.xml"
--8<-- "includes/gtk/02-boilerplate-template-adw/gresources.xml"
```

#### Adding widgets

Additional widgets, properties, and handlers can be added without much difficulty.

```py title="src/main.py"
--8<-- "includes/gtk/02-hello-world-adw/main.py"
```

```py title="src/template.py"
--8<-- "includes/gtk/02-hello-world-adw/template.py"
```

```blueprint title="src/template.blp"
--8<-- "includes/gtk/02-hello-world-adw/template.blp"
```

```xml title="src/gresources.xml"
--8<-- "includes/gtk/02-hello-world-adw/gresources.xml"
```

