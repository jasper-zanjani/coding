Contacts (obviously) uses a [NavigationSplitView][Adw.NavigationSplitView].

-   The sidebar is named "list-pane" and contains a [Stack][Gtk.Stack], apparently for displaying a [Spinner][Adw.Spinner] while loading the list of contacts.
-   The content is named "contact-pane" and also uses a Stack to switch between editing and viewing modes (StackPages are named "contact-sheet-page" and "contact-editor-page".
    The editing view uses [Overlay][Gtk.Overlay] to organize the widgets in the avatar.


!!! info "Application properties"

    -   `this.list_view`: ListView created by ContactList
    -   `this.editor`: ContactEditor created by ContactPane

ContactList (src/contacts-contact-list.vala) is a subclass of [AdwBin][Adw.Bin] (which is also the type of `contacts_list_container`). 
It creates a [ListView][Gtk.ListView] with a SignalListItemFactory, wrapped in a ScrolledWindow and assigns it to `this.list_view`.
In code it is instantiated in the constructor of the Contacts.MainWindow class (src/contacts-main-window.vala) by a call to `create_list_pane`.

-   The factory's `setup` handler creates a ContactListRow and wraps it in a ListItem.
-   The factory's `bind` handler assigns an Individual object to the row's `individual` property to serve as the data model.

ContactSheet (defined in src/contacts-contact-sheet.vala) is used for viewing contacts.

ContactPane (1)
{: .annotate }

1.  

    --8<-- "includes/pygobject/projects/contacts-contact-pane.md"

ContactEditor (src/contacts-contact-editor.vala)
