In the [Contacts][GNOME-Contacts] application, actions are defined as lists of [Gio.ActionEntry][Gio.ActionEntry] and passed to `add_action_entries` in the constructor for both Contacts.App and Contacts.MainWindow.
These are placed into the "app" namespace (for actions defined for App) and are wired in the `primary_menu_popover` menu defined in data/ui/contacts-main-window.ui.

