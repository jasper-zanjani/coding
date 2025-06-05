In the Contacts app, `bind_property` is used a lot, especially in the 

-   `ContactList.on_setup_item()` (1)
    {: .annotate }

    1.  This binding apparently sets the checkmark when selecting one or more contacts.

        ```vala hl_lines="15-16"
        --8<-- "includes/gtk/projects/Contacts/ContactList.on_setup_item.vala"
        ```

-   
