# Blueprint syntax

--8<-- "includes/gtk/links.md"

??? info "Reference"

    --8<-- "includes/gtk/callout.md"

!!! info "Note"

    While examining the source code of the demos found in Workbench, it seems that I will not be able to run them outside of the app without introducing some scaffolding.
    I'll study how Builder projects are structured to see if I can find a way.

Blueprint (1) documents can be compiled to XML using [blueprint-compiler](https://gitlab.gnome.org/GNOME/blueprint-compiler).
{: .annotate }

1.  

    --8<-- "includes/gtk/blueprint/callout.md"

Every Blueprint document (with file name extension .blp) begins with a [GTK declaration](https://gnome.pages.gitlab.gnome.org/blueprint-compiler/reference/document_root.html#document-root) and one or more imports.
[Objects](https://gnome.pages.gitlab.gnome.org/blueprint-compiler/reference/objects.html), which are the basic building blocks of a GTK interface, follow.
The type names of objects must include the namespace (i.e. `Adw.Leaflet`), but objects in the Gtk namespace may omit them.
Also note that the compiler will throw an error if the empty braces are not present.

<div class="grid cards" markdown>

```blueprint
--8<-- "includes/gtk/01-boilerplate/main.blp"
```

```xml
--8<-- "includes/gtk/01-boilerplate/main.xml"
```

</div>

Property names and values are provided as `key: value`.
Note that the integer value for [GtkOrientation](https://docs.gtk.org/gtk4/enum.Orientation.html) is compiled to 1 because that is the value of the enum in C.

Also note that the blueprint file abstracts the parent-child relationship of elements by nesting elements.

<div class="grid cards" markdown>

```blueprint hl_lines="6"
--8<-- "includes/gtk/taiko/04/main.blp"
```

```xml hl_lines="12"
--8<-- "includes/gtk/taiko/04/main.ui"
```

</div>

[Child types](https://gnome.pages.gitlab.gnome.org/blueprint-compiler/reference/objects.html#children) are specified by brackets as shown for [HeaderBar][Gtk.HeaderBar] below.


<div class="grid cards" markdown>

```blueprint hl_lines="5-6"
--8<-- "includes/gtk/ui-examples/10-HeaderBar/main.blp"
```

```xml hl_lines="10-11"
--8<-- "includes/gtk/ui-examples/10-HeaderBar/main.ui"
```

</div>

#### Templates

--8<-- "includes/gtk/templates/blueprint.md"

#### Menu

--8<-- "includes/gtk/menu/blueprint.md"
