**ContactPane**{: #contactpane } (1) corresponds to the `$ContactsContactPane` UI template. It contains a [Stack][Gtk.Stack] with two [StackPages][Gtk.StackPage] (`contact_sheet_page` and `contact_editor_page`).
It is instantiated by `MainWindow.create_contact_pane()` and assigned to its `contact_pane` property.
{: .annotate }

1.  **Source**
    
    -   src/contacts-contact-pane.vala (ContactPane class)
    -   data/ui/contacts-contact-pane.ui (ContactsContactPane template)

    ---

    **Properties**

    -   `contact_editor_box` is a Box that appends the [ContactEditor](#contacteditor) widget created by `create_contact_editor()`
    -   `contact_sheet_clamp`
    -   `selection_model`

    ---

    **Methods**

    -   `create_contact_editor()` creates a new [ContactEditor](#contacteditor) and assigns to `this.editor` as well as `this.contact_editor_box`.
        It is called by various other ContactPane methods, usually right before setting the visible StackPage with `this.stack.set_visible_child_name()` (i.e. `edit_contact()` and `new_contact()`.


