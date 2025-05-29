**App** (1) 
{: .annotate }

1.  === "Source"

        -   src/contacts-app.vala

    === "Properties"

        Most application properties are set by helper methods called in the constructor.

        Property        | Type          | Method    | Description
        ---             | ---           | ---       | ---
        `contacts_list` | ContactsList
        `editor`        | ContactEditor |
        `list_view`     | ListView      | 

    === "Methods"

        App exposes various methods that create dialogs or other windows.
        These usually begin with `show_` and construct a widget in code.
        The widget's `present` method is then called, passing `this.window` as argument.
        These callbacks are provided in the ActionEntry list passed to `add

        Method          | Return type                                           
        ---             | ---
        [`command_line`](#app-command_line)  | [ApplicationCommandLine][Gio.ApplicationCommandLine] 
        `create_actions` | void


