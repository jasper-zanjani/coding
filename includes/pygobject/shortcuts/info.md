**Keyboard accelerators** can be specified in menu items by prepending `_` to a letter in the display text.

Application exposes [`set_accels_for_action`](https://api.pygobject.gnome.org/Gtk-4.0/class-Application.html#gi.repository.Gtk.Application.set_accels_for_action) to set keyboard accelerators.

## Examples

<div class="grid cards" markdown>

-   **Builder**

    --8<-- "includes/pygobject/projects/Builder/keyboard.md"

    ```blueprint title="primary_menu (decompiled from src/window.ui)"
    --8<-- "includes/pygobject/projects/Builder/menu-shorthand.blp"
    ```

</div>
