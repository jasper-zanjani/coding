[ListStore][Gio.ListStore] works as a collection of GObjects.
In fact it is the main implementation of the [ListModel interface](https://api.pygobject.gnome.org/Gio-2.0/interface-ListModel.html#gi.repository.Gio.ListModel). (1)
{: .annotate }


1.  !!! info "Note"

        ListStore was used in [Taiko's tutorial](https://github.com/Taiko2k/GTK4PythonTutorial/?tab=readme-ov-file#using-gridview) as the data model for the list of fruit.
        For some reason, I wasn't able to get this working when I was studying the implementation of [ListView][Gtk.ListView].


        In my (non-working) example, I created a custom GObject subclass and attempted to populate a [ListStore][Gio.ListStore] with three items.
        My mistake was to attempt to instantiate it with a kwarg when the subclass constructor only took an arg.


        ```py hl_lines="2 15" title="Doesn't work!"
        class Philosopher(GObject.Object):
            def __init__(self, name):
                super().__init__()
                self._name = name

            @GObject.Property(type=str)
            def name(self)-> str:
                return self._name

        # ...

        philosophers = ['Plato', 'Aristotle', 'Socrates']
        list_store = Gio.ListStore(item_type=Philosopher)
        for p in philosophers:
            list_store.append(Philosopher(name=p))
        ```

        Rather, care must be taken to remember to instantiate the class using a positional parameter rather than keyword parameter unless the constructor accepts a kwarg.

```py hl_lines="30 33-35"
--8<-- "includes/gtk/GioListStore/main.py"
```
