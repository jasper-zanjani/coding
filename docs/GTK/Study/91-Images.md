# Images

--8<-- "includes/gtk/links.md"

There is more than one widget used to display images.

Widget                  | File path (str)   | [GFile](#giofile) | [Pixbuf](#gdkpixbuf)
---                     | ---               | ---               | ---
[Picture](#gtkpicture)  | ?                 | `set_file`        | ~~`set_pixbuf`~~
[Image](#gtkimage)      | `set_from_file`   | ?                 | ~~`set_from_pixbuf`~~


<div class="grid cards" markdown>

-   **[GtkPicture][Gtk.Picture]**

    ---

    [GtkPicture][Gtk.Picture] was introduced with GTK4 and is what is used to display images in the [HTTP Image](https://github.com/workbenchdev/demos/tree/main/src/HTTP%20Image), [Avatar](https://github.com/workbenchdev/demos/tree/main/src/Avatar), and [Picture](https://github.com/workbenchdev/demos/tree/main/src/Picture) demos on [Workbench][Workbench-git].

    -   The simplest way of using Picture is to pass in a [GFile](#giofile) to the `set_file` method. (1)
        {: .annotate }

        1.  

            ```py hl_lines="17-19" title="GtkPicture with GFile"
            --8<-- "includes/gtk/GtkPicture/00/main.py"
            ```
    
    -   Another, more circuitous route is to take the File and then pass that to [Texture][Gdk.Texture].
        This texture is then passed as argument to the Picture's `set_paintable` method (1).
        This is the method used in the HTTP Image demo.
        {: .annotate }

        1.  

            ```py hl_lines="17-20" title="GtkPicture with GtkTexture"
            --8<-- "includes/gtk/GtkPicture/01/main.py"
            ```
    
    -   It is also possible to create a Picture from a [GdkPixbuf](#gdkpixbuf) using the deprecated method `set_pixbuf` (1).
        Documentation indicates that `set_paintable` is to be preferred but it appears that a Pixbuf cannot be passed as argument to this method.
        {: .annotate }

        1.  

            ```py hl_lines="17-24" title="GtkPicture with GdkPixbuf"
            --8<-- "includes/gtk/GtkPicture/02/main.py"
            ```

-   **[GtkImage][Gtk.Image]**
    
    ---

    In Workbench demos, [GtkImage][Gtk.Image] is used mostly for displaying icons, since it can take an `icon-name` property.

    -   A file path can be passed to `set_from_file` (1), but it requires a string (unlike `Picture.set_file` which requires a GFile).
        {: .annotate }

        1.  

            ```py hl_lines="18"
            --8<-- "includes/gtk/GtkImage/00/main.py"
            ```

    -   A [Pixbuf](#gdkpixbuf) can be passed to `set_from_pixbuf` (like `Picture.set_pixbuf` also deprecated since 4.12) (1)
        {: .annotate }

        1.  

            ```py hl_lines="17-24"
            --8<-- "includes/gtk/GtkImage/01/main.py"
            ```

</div>

#### GdkPixbuf

--8<-- "includes/gtk/GdkPixbuf/info.md"

<div class="grid cards" markdown>

This is about as simple an example as is possible with GdkPixbuf.
A [PixbufLoader][GdkPixbuf.PixbufLoader] is instantiated which uses the [**`write` method**](https://api.pygobject.gnome.org/GdkPixbuf-2.0/class-PixbufLoader.html#gi.repository.GdkPixbuf.PixbufLoader.write) to read from an open file.

```py hl_lines="11"
--8<-- "includes/gtk/GdkPixbuf/00/main.py"
```

More robust error handling is implemented in the entrypoint here:

```py hl_lines="4 17-22"
--8<-- "includes/gtk/GdkPixbuf/01/main.py"
```


A Pixbuf can be displayed with [Image][Gtk.Image]

```py
--8<-- "includes/gtk/GdkPixbuf/02/main.py"
```

</div>

#### GioFile

--8<-- "includes/gtk/GioFile/info.md"
