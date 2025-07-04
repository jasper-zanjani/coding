Data binding in GTK can apparently be done in several ways.

--8<-- "includes/gtk/blp/bind.md"

#### bind\_property

[`bind_property`](https://api.pygobject.gnome.org/GObject-2.0/class-Object.html#gi.repository.GObject.Object.bind_property) is a property exposed by all GObjects.

In Taiko's tutorial, `bind_property` is used in the SignalListItemFactory to bind the name of fruit to the Label. (1)
{: .annotate }

1.  

    ```py hl_lines="12-15"
    factory = Gtk.SignalListItemFactory()

    def f_setup(fact, item):
        label = Gtk.Label(halign=Gtk.Align.START)
        label.set_selectable(False)
        item.set_child(label)

    factory.connect("setup", f_setup)

    def f_bind(fact, item):
        fruit = item.get_item()
        fruit.bind_property(
            "name", item.get_child(), "label",
            GObject.BindingFlags.SYNC_CREATE
        )
    factory.connect("bind", f_bind)
    ```

