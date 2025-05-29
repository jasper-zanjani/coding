**ContactList** (1) is a subclass of [AdwBin][Adw.Bin] (which is also the type of `contacts_list_container`). 
It creates a [ListView][Gtk.ListView] with a SignalListItemFactory, wrapped in a ScrolledWindow and assigns it to `this.list_view`.
{: .annotate }

1.  === "Source"

        -   src/contacts-contact-list.vala

    === "Implementation"

        -   The factory's `setup` handler creates a ContactListRow and wraps it in a ListItem.
        -   The factory's `bind` handler assigns an Individual object to the row's `individual` property to serve as the data model.

