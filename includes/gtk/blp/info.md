Blueprint was [introduced](https://www.jwestman.net/2021/12/02/introducing-blueprint-a-new-way-to-craft-user-interfaces.html) in late 2021 as a more convenient syntax for defining GTK application UIs.
Blueprint documents can be compiled to XML using [blueprint-compiler](https://gitlab.gnome.org/GNOME/blueprint-compiler).

Every Blueprint document (with file name extension .blp) begins with a [GTK declaration](https://gnome.pages.gitlab.gnome.org/blueprint-compiler/reference/document_root.html#document-root) and one or more imports.
[Objects](https://gnome.pages.gitlab.gnome.org/blueprint-compiler/reference/objects.html), which are the basic building blocks of a GTK interface, follow.
The type names of objects must include the namespace (i.e. `Adw` for `Adw.Leaflet`), but objects in the `Gtk` namespace may omit them.
Abstracts the parent-child relationship of elements by nesting elements.

Property names and values are provided as `key: value;`.

```blueprint title="01-boilerplate"
--8<-- "includes/gtk/01-boilerplate/main.blp"
```

Note that the integer value for [GtkOrientation](https://docs.gtk.org/gtk4/enum.Orientation.html) is compiled to 1 because that is the value of the enum in C.
Also note that the compiler will throw an error if the empty braces are not present.

[Child types](https://gnome.pages.gitlab.gnome.org/blueprint-compiler/reference/objects.html#children) are specified by brackets as shown for `HeaderBar` (1) below.
{: .annotate }

1.  

    --8<-- "includes/gtk/callouts/gtkheaderbar.md"


```blueprint hl_lines="6-7"
--8<-- "includes/gtk/ui-examples/10-HeaderBar/main.blp"
```

