[ToggleButton][Gtk.ToggleButton] emits the `toggled` signal every time its button is pressed.
For correct functionality, the signal handler must test for the state of the button (1).
{: .annotate }

1.  

    <div class="grid cards" markdown>

    ```blueprint
    --8<-- "includes/gtk/GtkStack/00/main.blp"
    ```

    ```py hl_lines="22-25"
    --8<-- "includes/gtk/GtkStack/00/main.py"
    ```

    </div>
