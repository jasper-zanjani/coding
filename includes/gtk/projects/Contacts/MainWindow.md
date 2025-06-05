**MainWindow**{: #mainwindow } (1) ("`content_box`") 
{: .annotate }

1.  **Sources**

    -   src/contacts-main-window.vala
    -   data/ui/contacts-main-window.ui

    **Properties**

    -   `contact_pane` ([ContactPane](#contactpane))

    **Methods**

    -   `create_contact_pane()` instantiates a ContactPane and assigns it to the `contact_pane` property
    -   `edit_contact()` is the callback for the "edit-contact" action, which is wired to the `edit_contact_button`. 
        It turns on the right headerbar's title setting and runs the `edit_contact()` method of [ContactPane](#contactpane)
        `ContactPane.edit_contact()` in turn runs `create_contact_editor()` and changes the StackPage shown to the user by running `this.stack.set_visible_child_name ("contact-editor-page")`

    **Implementation**
    
    MainWindow uses a [NavigationSplitView][Adw.NavigationSplitView] (`content_box`).

    -   The sidebar is a NavigationPage (`list_pane_page`, named "list-pane") and contains a [Stack][Gtk.Stack] (`list_pane_stack`):
        -   [Spinner][Adw.Spinner] while loading the list of contacts.
        -   Box containing [Adw.Bin][Adw.Bin] (`contacts_list_container`)

    -   The content is another NavigationPage (`contact_pane_page`, named "contact-pane") which corresponds with [ContactPane](#contactpane)

        The editing view uses [Overlay][Gtk.Overlay] to organize the widgets in the avatar.

    **Actions**

    Actions are defined with a GLib.ActionEntry list which are then passed to the [`add_action_entries`][Gio.ActionMap] method.
    This is not defined in code, nor is it found in the documentation for [Application][Gtk.Application].
    The code for the MainWindow creates properties for Settings, OperationList, App, and Store.

