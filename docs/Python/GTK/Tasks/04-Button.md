# Button

[Adding](https://github.com/Taiko2k/GTK4PythonTutorial/tree/main?tab=readme-ov-file#add-a-button) a [Button](https://api.pygobject.gnome.org/Gtk-4.0/class-Button.html) that prints "Hello, World!" to the terminal.

We also change the Box's orientation to vertical.

=== "Builder"

    ```py
    --8<-- "includes/py/gtk/tutorial/04/builder.py"
    ```

    1.  

        ```xml
        --8<-- "includes/py/gtk/tutorial/04/layout.ui"
        ```

=== "Procedural"

    ```py hl_lines="11 14-19"
    --8<-- "includes/py/gtk/tutorial/04/main.py"
    ```
