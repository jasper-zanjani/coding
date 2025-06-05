Apparently [UriLauncher][Gtk.UriLauncher] is used to interact with the native GNOME help system.

## Examples

<div class="grid cards" markdown>

-   [**Contacts**][GNOME-Contacts]

    ```vala title="src/contacts-app.vala" hl_lines="2"
    public void show_help () {
      Gtk.UriLauncher help_launcher = new Gtk.UriLauncher ("help:gnome-help/contacts");
      help_launcher.launch.begin (this.window, null, (obj, res) => {
        try {
          help_launcher.launch.end (res);
        } catch (Error error) {
          warning ("Could not open help: %s", error.message);
        }
      });
    }
    ```

</div>
