[Stack][Gtk.Stack] and [StackPage][Gtk.StackPage] are often used with NavigationSplitView to implement the details pane. (1)
{: .annotate }

1.  In this example, a simple [ToggleButton][Gtk.ToggleButton] is used to flip between two StackPages.
    Note that StackPage takes a child property and does not accept a direct child.
    Also note that Stack's `set_visible_child_name` method takes the name of the StackPage as defined in its `name` property and **not** its id.

    <div class="grid cards" markdown>

    ```blueprint hl_lines="18 24"
    --8<-- "includes/gtk/GtkStack/00/main.blp"
    ```

    ```py hl_lines="23 25"
    --8<-- "includes/gtk/GtkStack/00/main.py"
    ```

    </div>
