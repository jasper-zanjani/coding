Custom drawing in GTK4 is primarily handled by overriding the `vfunc_snapshot()` virtual method of the widget (?).

[GtkSnapshot](https://docs.gtk.org/gtk4/class.Snapshot.html) assists in creating [GskRenderNode](https://docs.gtk.org/gsk4/class.RenderNode.html)s for widgets

GTK Scene Graph Kit (1) is the rendering and scene graph API for GTK.
A [scene graph](https://en.wikipedia.org/wiki/Scene_graph) is the data structure commonly used to represent vector-based graphics.
{: .annotate }

1.  === "Resources"

        -   [Wikipedia](https://en.wikipedia.org/wiki/GTK_Scene_Graph_Kit)

## Cairo

A [Context](https://pycairo.readthedocs.io/en/latest/reference/context.html) is the main object used when drawing with cairo.
