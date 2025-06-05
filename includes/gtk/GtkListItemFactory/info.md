[ListItemFactory][Gtk.ListItemFactory] creates widgets for items taken from a [ListModel][Gio.ListModel] and is commonly used with [list widgets](#list-widgets).
There are two ListItemFactory subclasses:

-   [BuilderListItemFactory][Gtk.BuilderListItemFactory] instantiates Builder UI templates. 
    A [Blueprint template block](https://gnome.pages.gitlab.gnome.org/blueprint-compiler/reference/extensions.html#syntax-extlistitemfactory) defines the template that will be used to create list items (which must be of type [ListItem][Gtk.ListItem] [ColumnViewRow][Gtk.ColumnViewRow], or [ColumnViewCell][Gtk.ColumnViewCell]).
    These must extend classes that the parent widget expects (i.e. [ListItem][Gtk.ListItem]s for [ListView][Gtk.ListView]).

-   [SignalListItemFactory][Gtk.SignalListItemFactory] emits signals to manage list items. The examples from Workbench mostly use SignalListItemFactory

Uniquely within Blueprint, this template block defines a completely separate UI section for each list item which may not reference objects in the main blueprint or vice-versa.
