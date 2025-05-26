# Projects

--8<-- "includes/pygobject/links.md"

## Apps

#### [Gradia](https://github.com/AlexanderVanhee/Gradia)

PyGObject

#### Contacts

Contacts (obviously) uses a [NavigationSplitView][Adw.NavigationSplitView].

-   The sidebar is named "list-pane" and contains a [Stack][Gtk.Stack], apparently for displaying a [Spinner][Adw.Spinner] while loading the list of contacts.
-   The content is named "contact-pane" and also uses a Stack to switch between editing and viewing modes (StackPages are named "contact-sheet-page" and "contact-editor-page".
    The editing view uses [Overlay][Gtk.Overlay] to organize the widgets in the avatar.


ContactList is defined in-code (src/contacts-contact-list.vala) as a subclass of [AdwBin][Adw.Bin] (which is also the type of `contacts_list_container`). 
It creates a [ListView][Gtk.ListView] with a SignalListItemFactory, wrapped in a ScrolledWindow and assigns it to `this.list_view`.
In code it is instantiated in the constructor of the Contacts.MainWindow class (src/contacts-main-window.vala) by a call to `create_list_pane`.

-   The factory's `setup` handler creates a ContactListRow and wraps it in a ListItem.
-   The factory's `bind` handler assigns an Individual object to the row's `individual` property to serve as the data model.

ContactSheet (defined in src/contacts-contact-sheet.vala) is used for viewing contacts.

## Other projects

#### [antipatico/gtk\_gtasks](https://github.com/antipatico/gtk_gtasks)

-   Gtk 3.0 using [WebView][WebKit.WebView] 4.1

-   Blueprint UI compiles but then the Python doesn't like WebKitWebView.. possibly why author went with GTK3 instead of GTK 4?

#### [funinka/Gnome-OCR-Screenshot](https://github.com/funinkina/Gnome-OCR-Screenshot)

-   PyGObject application

Can't seem to get it working.. I messaged the [developer](https://www.reddit.com/user/ashtraxk/) on [Reddit](https://www.reddit.com/r/gnome/comments/1ktis0x/comment/mtvdo8d/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) 

#### [tfuxu/Halftone](https://github.com/tfuxu/Halftone)

#### [qwersyk/Newelle](https://github.com/qwersyk/Newelle)

## Extensions

It may be worthwhile to learn GJS since there are so many [GNOME extensions][GNOME-extensions] available.

-   [ChatGPT-GNOME-Extension](https://github.com/macdaddyaz20/ChatGPT-GNOME-Extension)
-   [Voluble](https://github.com/QuantiusBenignus/voluble)
-   [Blur my Shell](https://github.com/aunetx/blur-my-shell)
-   [Dash to Dock](https://github.com/micheleg/dash-to-dock)
