Unlike regular interface descriptions, [templates](https://docs.gtk.org/gtk4/class.Widget.html#building-composite-widgets-from-template-xml) expect a `template` tag as a direct child of the toplevel `interface` tag.
The template's `class` attribute must specify the type name of the widget, and optionally the `parent` widget can be specified (this is ignored by GtkBuilder).
The template can take `property` and `child` tags and its content behaves as if it were added to the object tag defining the widget itself.
Unlike `object`, template does not take an `id` attribute.
