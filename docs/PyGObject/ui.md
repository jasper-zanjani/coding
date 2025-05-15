# UI Definitions

!!! info "Plan"

    1.  Get comfortable with XML files first. You can use pug to simplify the presentation for yourself.

GTK UI definitions can be written in [Blueprint](https://jwestman.pages.gitlab.gnome.org/blueprint-compiler/) or XML.

!!! info "Examples"

    Default window.ui created by Builder as part of a new project.
    Note that `object.AdwToolbarView` is actually a child of `property(name="content")`:

    === "pug"

        ```pug
        --8<-- "includes/pygobject/builder-window.pug"
        ```

    === "xml"

        ```xml
        --8<-- "includes/pygobject/builder/00/window.ui"
        ```

Elements:

-   [`interface`](https://docs.gtk.org/gtk4/class.Builder.html#structure-of-ui-definitions) is the top-level elemtn
-   [`requires`](https://docs.gtk.org/gtk4/class.Builder.html#requirements) specifies target toolkit versions
-   [`object`](https://docs.gtk.org/gtk4/class.Builder.html#objects) elements are typically UI widgets defined by their class attribute. They can contain:
    -   `property` elements to define properties
    -   `signal` elements connect signals to handlers
    -   `child` elements describe child objects. 
        Generic containers such as `GtkBox` use the child element containing an object element to describe the child.
        Other widgets use a property element to define children.
