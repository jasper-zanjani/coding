In the [Contacts][GNOME-Contacts] application, actions are defined as lists of [Gio.ActionEntry][Gio.ActionEntry] (1) and passed to `add_action_entries` in the constructor for both App and MainWindow.
 
1.  

    ```vala title="src/contacts-main-window.vala (excerpt)"
    private const GLib.ActionEntry[] ACTION_ENTRIES = {
      { "cancel", cancel_action },
      { "new-contact", new_contact },
      { "edit-contact", edit_contact },
      { "edit-contact-save", edit_contact_save },
      { "focus-search", focus_search },
      { "mark-favorite", mark_favorite },
      { "unmark-favorite", unmark_favorite },
      { "cancel-selection", cancel_selection_action },
      { "link-marked-contacts", link_marked_contacts },
      { "delete-marked-contacts", delete_marked_contacts },
      { "export-marked-contacts", export_marked_contacts },
      { "show-contact-qr-code", show_contact_qr_code },
      { "unlink-contact", unlink_contact },
      { "delete-contact", delete_contact },
      { "sort-on", null, "s", "'surname'", sort_on_changed },
      { "undo-operation", undo_operation_action, "s" },
      { "cancel-operation", cancel_operation_action, "s" },
    };
    ```

These are then wired to menus where appropriate in the UI

-   data/ui/contacts-main-window.ui
    -   "sort-on" is wired twice in `primary_menu_popover`, each time with different values for `target`, reflecting whether to organize based on first name or surname.
    -   "mark-favorite", "unmark-favorite", "show-contact-qr-code", and "delete-contact" are wired in `contact_hamburger_menu_popover`

