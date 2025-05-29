# UI Definitions

GTK UI definitions can be written in [Blueprint](https://jwestman.pages.gitlab.gnome.org/blueprint-compiler/) or XML.


Elements:

-   [`interface`](https://docs.gtk.org/gtk4/class.Builder.html#structure-of-ui-definitions) is the top-level elemtn
-   [`requires`](https://docs.gtk.org/gtk4/class.Builder.html#requirements) specifies target toolkit versions
-   [`object`](https://docs.gtk.org/gtk4/class.Builder.html#objects) elements are typically UI widgets defined by their class attribute. They can contain:
    -   `property` elements to define properties
    -   `signal` elements connect signals to handlers
    -   `child` elements describe child objects. 
        Generic containers such as `GtkBox` use the child element containing an object element to describe the child.
        Other widgets use a property element to define children.
