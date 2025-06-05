**ContactList** (1) is a subclass of [AdwBin][Adw.Bin] (which is also the type of `contacts_list_container`). 
It creates a [ListView][Gtk.ListView] with a SignalListItemFactory, wrapped in a ScrolledWindow and assigns it to `this.list_view`.
A ContactList is created in `MainWindow.create_list_pane()` and assigned to `this.contacts_list`  as well as made the child of `contacts_list_container`.
{: .annotate }

1.  **Sources**

    -   src/contacts-contact-list.vala

    **Implementation**

    -   The factory's `setup` handler creates a ContactListRow and wraps it in a ListItem.
    -   The factory's `bind` handler assigns an Individual object to the row's `individual` property to serve as the data model.

