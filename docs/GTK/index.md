# Overview

--8<-- "includes/gtk/links.md"

??? info "Reference"

    --8<-- "includes/gtk/callout.md"

GTK UI definitions can be written in Blueprint (1) or XML (2).
{: .annotate }

1.  

    --8<-- "includes/gtk/callouts/blueprint.md"

2.  Elements:

    -   [`interface`](https://docs.gtk.org/gtk4/class.Builder.html#structure-of-ui-definitions) is the top-level elemtn
    -   [`requires`](https://docs.gtk.org/gtk4/class.Builder.html#requirements) specifies target toolkit versions
    -   [`object`](https://docs.gtk.org/gtk4/class.Builder.html#objects) elements are typically UI widgets defined by their class attribute. They can contain:
        -   `property` elements to define properties
        -   `signal` elements connect signals to handlers
        -   `child` elements describe child objects. 
            Generic containers such as `GtkBox` use the child element containing an object element to describe the child.
            Other widgets use a property element to define children.

## Blueprint

--8<-- "includes/gtk/blp/info.md"

#### Templates

--8<-- "includes/gtk/templates/blueprint.md"

#### Menu

--8<-- "includes/gtk/menu/blueprint.md"

#### Layout


`AdwNavigationSplitView` (1) is the best way to implement the list-details pattern.
{: .annotate }

1.  

    --8<-- "includes/gtk/callouts/adwnavigationsplitview.md"

-   

    --8<-- "includes/gtk/GtkStack/00/info.md"

-   [Box][Gtk.Box] and [Bin][Adw.Bin] are distinguished by the fact that Bin accepts only a single child and has `get_child` and `set_child` methods that allow it to be defined in code.
    By contrast, Box only supports `append` and is meant to organize other widgets vertically or horizontally.

`AdwStatusPage` (1) is useful for demonstration purposes because it takes a `title` property which displays prominently and child widgets are vertically centered by default.
{: .annotate }

1.  

    --8<-- "includes/gtk/callouts/adwstatuspage.md"


```blueprint title="AdwStatusPage"
using Gtk 4.0;
using Adw 1;

Adw.StatusPage {
  title: _("Title");
  description: _("Description");

  Box {
    orientation: vertical;
    halign: center;
  }
}
```

## Widgets

??? info "GTK icon names"

    --8<-- "includes/gtk/icon-names.md"

#### AdwToastOverlay

-   The `AdwToastOverlay` is placed higher in the stack, just under `AdwApplicationWindow` (1). 
    This must be expected for Overlays.
    {: .annotate }

    1.  

        --8<-- "includes/gtk/callouts/adwapplicationwindow.md"

        ---

        ```blueprint
        --8<-- "includes/gtk/AdwToast/00/main.blp"
        ```

#### GtkButton

Both [Button][Gtk.Button] and [ToggleButton][Gtk.ToggleButton] support `icon-name`, but only Button supports `label`.
If Button has both icon-name and title assigned, title takes priority.


Button styling can be adjusted in a variety of standardized ways by specifying one or more styles.

-   `destructive-action` red
-   `suggested-action` highlighted
-   `pill`
-   `opaque`
-   `circular`
-   `flat`


--8<-- "includes/gtk/GtkToggleButton/info.md"

#### GtkListBox

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


#### GtkScale

--8<-- "includes/gtk/widgets/gtkscale/info.md"

#### GtkSpinButton

--8<-- "includes/gtk/widgets/gtkspinbutton/info.md"

## Data binding

--8<-- "includes/gtk/data-binding/info.md"
