**Keyboard accelerators** can be specified in menu items by prepending `_` to a letter in the display text.

[Application][Gtk.Application] exposes [`set_accels_for_action`](https://api.pygobject.gnome.org/Gtk-4.0/class-Application.html#gi.repository.Gtk.Application.set_accels_for_action) to set keyboard accelerators.

[ShortcutController][Gtk.ShortcutController] takes [Shortcut][Gtk.Shortcut] widgets.

## Examples

<div class="grid cards" markdown>

-   **Builder**

    --8<-- "includes/gtk/projects/Builder/keyboard.md"

    ```blueprint title="primary_menu (decompiled from src/window.ui)"
    --8<-- "includes/gtk/projects/Builder/menu-shorthand.blp"
    ```

-   **Contacts**

    ```blueprint title="data/ui/contacts-main-window.ui (decompiled excerpt)"
    ShortcutController {
      scope: global;

      Shortcut {
        trigger: "<Control>n";
        action: "action(win.new-contact)";
      }

      Shortcut {
        trigger: "<Control>f";
        action: "action(win.focus-search)";
      }

      Shortcut {
        trigger: "Escape";
        action: "action(win.cancel)";
      }

      Shortcut {
        trigger: "<Control>Return";
        action: "action(win.edit-contact-save)";
      }

      Shortcut {
        trigger: "<Control>Delete";
        action: "action(win.delete-marked-contacts)";
      }
    }
    ```


</div>
