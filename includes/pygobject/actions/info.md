Actions (1) are a way to connect UI elements to callbacks and are functional only.
{: .annotate }

1.  === "Resources"

        -   [Actions](https://docs.gtk.org/gtk4/actions.html)
        -   [PyGObject tutorial - Actions](https://pygobject.gnome.org/tutorials/gtk4/application.html#actions)

Actions can be registered in subclasses of not only Application but also ApplicationWindow because they both implement the [Gio.ActionMap][Gio.ActionMap] interface.
Actions registered in either class are accessible using different namespaces ("app" for actions defined in Application and "win" for those defined in ApplicationWindow).

Actions can be added with `add_action` which adds a single Action to the map or with `add_action_entries` which takes a list of tuples.

-   Name (string, required)
-   Callback
-   [GVariant](https://api.pygobject.gnome.org/GLib-2.0/structure-VariantType.html) type string (only `"s"` is used)


Also note that the menu as a whole does not appear in code but is assigned to the `menu-model` property of the [MenuButton][Gtk.MenuButton] element. (1)
{: .annotate }

1.  

    ```blueprint hl_lines="11"
    template $TextEditorWindow: Adw.ApplicationWindow {
      content: Adw.ToolbarView {
        [top]
        Adw.HeaderBar {
          [start]
          Button open_button { /* ... */ }

          [end]
          MenuButton {
            // ...
            menu-model: primary_menu;
          }
        }
        // ...
      };
    }
    ```

```blueprint title="window.blp (excerpt)"
--8<-- "includes/pygobject/builder/menu-shorthand-annotated.blp"
```

1.  

    ```py title="window.py (excerpt)"
    save_action = Gio.SimpleAction(name="save-as")
    save_action.connect("activate", self.save_file_dialog)
    self.add_action(save_action)
    ```

2.  

    ```py title="main.py (excerpt)"
    self.create_action('preferences', self.on_preferences_action)
    ```

3. ??

4.  

    ```py title="main.py (excerpt)"
    self.create_action('about', self.on_about_action) l
    ```

