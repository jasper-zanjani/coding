**App** (1) 
{: .annotate }

1.  **Sources**

    -   src/contacts-app.vala

    ---

    **Properties**

    -   `contacts_list` (ContactsList)
    -   `editor` (ContactEditor)
    -   `list_view` (ListView)

    ---

    **Methods**

    App exposes various methods that create dialogs or other windows.
    These usually begin with `show_` and construct a widget in code.
    The widget's `present` method is then called, passing `this.window` as argument.
    These callbacks are provided in the ActionEntry list passed to `add

    -   [`command_line`](#app-command_line)  [ApplicationCommandLine][Gio.ApplicationCommandLine] 
    -   `create_actions`


