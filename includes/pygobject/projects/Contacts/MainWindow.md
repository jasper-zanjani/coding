MainWindow (1) ("`content_box`") uses a [NavigationSplitView][Adw.NavigationSplitView].
{: .annotate }

1.  === "Source"

        -   src/contacts-main-window.vala

<!-- -->

-   The sidebar is named "list-pane" and contains a [Stack][Gtk.Stack], apparently for displaying a [Spinner][Adw.Spinner] while loading the list of contacts.
-   The content is named "contact-pane" and also uses a Stack to switch between editing and viewing modes (StackPages are named "contact-sheet-page" and "contact-editor-page".
    The editing view uses [Overlay][Gtk.Overlay] to organize the widgets in the avatar.

Actions are defined with a GLib.ActionEntry list which are then passed to the [`add_action_entries`][Gio.ActionMap] method.
This is not defined in code, nor is it found in the documentation for [Application][Gtk.Application].
The code for the MainWindow creates properties for Settings, OperationList, App, and Store.
