# GTK

!!! info "Quick Reference"

    === "Resources"

        --8<-- "includes/gtk/resources.md"

    === "API"

        --8<-- "includes/py/gtk/links.md"

        -   **Adw**
            -   AboutWindow
            -   Application

        -   **Gio**
            -   ListStore
            -   Menu
            -   SimpleAction

        -  **GObject** 
            -   Object

        -   **GLib**
            -   Error

        -   **Gtk**
            -   AboutDialog
            -   [Box][Gtk.Box]
            -   [Button][Gtk.Button]
            -   [CheckButton][Gtk.CheckButton]
            -   [CssProvider][Gtk.CssProvider]
            -   [FileDialog][Gtk.FileDialog]
            -   [FileFilter][Gtk.FileFilter]
            -   [GridView][Gtk.GridView]
            -   [HeaderBar][Gtk.HeaderBar]
            -   License
            -   PopoverMenu
            -   [Scale][Gtk.Scale]
            -   SignalListItemFactory
            -   SingleSelection

    === "Projects"

        -   [GTK Google Tasks](https://github.com/antipatico/gtk_gtasks): GTK 3.0 wrapper around Google Tasks

    === "Board games"

        --8<-- "includes/gtk/board-games.md"

Plan

1.  Get comfortable with XML files first. You can use pug to simplify the presentation for yourself.
2.  

GTK 4 user interfaces can be written in [Blueprint](https://jwestman.pages.gitlab.gnome.org/blueprint-compiler/) or XML.

```pug 
--8<-- "includes/pug/gtk/00.pug"
```

```xml
--8<-- "includes/gtk/tutorial.ui"
```
