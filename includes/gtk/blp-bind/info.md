The Blueprint [bind expression](https://gnome.pages.gitlab.gnome.org/blueprint-compiler/reference/values.html#bindings) (1) is used to bind widget values to data.
In this example it binds a Label to a ListStore.
{: .annotate }

1.

    ```blueprint hl_lines="11" title="Demonstration of bind expression"
    --8<-- "includes/gtk/blp-bind/main.blp"
    ```



```blueprint hl_lines="30" title="Demonstration of ListView (with BuilderListItemFactory)"
--8<-- "includes/gtk/GtkListView/BuilderListItemFactory/00/main.blp"
```
