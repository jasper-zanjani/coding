[ColumnView][Gtk.ColumnView] is more complicated than a list widget since each column must be handled separately, taking its own widget and Factory. (1)
Additionally, sorting by clicking on header columns is not possible without assigning a [StringSorter][Gtk.StringSorter] (which also requires [PropertyExpression][Gtk.PropertyExpression]. (2)
{: .annotate }

1.  

    ```blueprint hl_lines="23-36" title="ColumnViewColumns"
    --8<-- "includes/gtk/GtkColumnView/00/main.blp"
    ```

2.  

    ```py
    --8<-- "includes/gtk/GtkColumnView/sorting.py"
    ```

```py
--8<-- "includes/gtk/GtkColumnView/00/main.py"
```
