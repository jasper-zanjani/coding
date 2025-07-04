The Blueprint [bind expression](https://gnome.pages.gitlab.gnome.org/blueprint-compiler/reference/values.html#bindings) (1) is used to bind widget values to data.
{: .annotate }

1.  

    ```blueprint hl_lines="11" title="data-binding/blp-bind"
    --8<-- "includes/gtk/data-binding/blp-bind/main.blp"
    ```

In this example, note the single bind declaration saves the need to wire up a signal handler in code.

=== ":simple-gtk: Blueprint"

    <div class="grid cards" markdown>

    ```blueprint hl_lines="27" title="02-scale"
    --8<-- "includes/pygobject/02-scale/main.blp"
    ```

    ```blueprint hl_lines="27-29" title="02-scale-bind"
    --8<-- "includes/pygobject/02-scale-bind/main.blp"
    ```

    </div>

=== ":simple-python: PyGObject"

    <div class="grid cards" markdown>

    ```py title="02-scale"
    --8<-- "includes/pygobject/02-scale/main.py"
    ```

    ```py title="02-scale-bind"
    --8<-- "includes/pygobject/02-scale-bind/main.py"
    ```

    </div>


In this example it binds a Label to a ListStore.



```blueprint hl_lines="30" title="Demonstration of ListView (with BuilderListItemFactory)"
--8<-- "includes/gtk/GtkListView/BuilderListItemFactory/00/main.blp"
```
