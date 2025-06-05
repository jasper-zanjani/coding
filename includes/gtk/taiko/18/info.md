In [this step](https://github.com/Taiko2k/GTK4PythonTutorial/?tab=readme-ov-file#using-gridview), Taiko illustrates how to use a GridView to display a list of objects.

He notes that a [GridView][Gtk.GridView] needs both a **factory** to generate a child widget for each visible item as well as a **model** to hold the basis for the information.

```py hl_lines="7-11 17-55 165-168"
--8<-- "includes/gtk/taiko/18/main.py"
```

