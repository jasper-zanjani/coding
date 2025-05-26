# Widgets

--8<-- "includes/pygobject/links.md"

??? info "GTK icon names"

    --8<-- "includes/pygobject/icon-names.md"

## Layout

-   [StatusPage][Adw.StatusPage] is useful for demonstration purposes because it takes a `title` property which displays prominently and child widgets are vertically centered by default. (1)
    {: .annotate }

    1.  In fact, the canonical layout used in [Workbench][Workbench-git] demos is:

        ```blueprint hl_lines="9"
        Adw.StatusPage {
          title: _("Title");
          description: _("Description");

          Box {
            orientation: vertical;
            halign: center;

            // Content
          }
        }
        ```

-   [NavigationSplitView][Adw.NavigationSplitView] is the best way to implement the list-details pattern.

    -   

        --8<-- "includes/pygobject/GtkStack/00/info.md"

-   [Box][Gtk.Box] and [Bin][Adw.Bin] are distinguished by the fact that Bin accepts only a single child and has `get_child` and `set_child` methods that allow it to be defined in code.
    By contrast, Box only supports `append` and is meant to organize other widgets vertically or horizontally.

## ListBox

[ListBox][Gtk.ListBox] is usually specified as `selection-mode: none` unless its items are meant to be selected.
It can take various row types:

-   [ListBoxRow][Gtk.ListBoxRow] is the superclass for all the other widgets below. Unlike other widgets which take label, these all take `title`.
-   [Adw.ActionRow][Adw.ActionRow] can take a title, subtitle, icon, as well as prefix and suffix widgets.
    -   [Adw.ComboRow][Adw.ComboRow] which takes a list of strings for its `model` property
    -   [Adw.SwitchRow][Adw.SwitchRow]
    -   [Adw.SpinRow][Adw.SpinRow]
-   [Adw.ButtonRow][Adw.ButtonRow] does not support subtitle or prefix or suffix children but does support an icon on the left or right with `start-icon-name` or `end-icon-name`.
-   [Adw.EntryRow][Adw.EntryRow] does support prefix and suffix children
-   [Adw.ExpanderRow][Adw.ExpanderRow]


#### Buttons

Both [Button][Gtk.Button] and [ToggleButton][Gtk.ToggleButton] support `icon-name`, but only Button supports `label`.
If Button has both icon-name and title assigned, title takes priority.


Button styling can be adjusted in a variety of standardized ways by specifying one or more styles.

-   `destructive-action` red
-   `suggested-action` highlighted
-   `pill`
-   `opaque`
-   `circular`
-   `flat`


--8<-- "includes/pygobject/GtkToggleButton/info.md"


#### Toast

-   The [ToastOverlay][Adw.ToastOverlay] is placed higher in the stack, just under [ApplicationWindow][Adw.ApplicationWindow] (1). 
    This must be expected for Overlays.
    {: .annotate }

    1.  

        ```blueprint
        --8<-- "includes/pygobject/AdwToast/00/main.blp"
        ```


