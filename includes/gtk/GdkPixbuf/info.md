In PyGObject, Pixbuf is in its own module, [GdkPixbuf][GdkPixbuf].

A separate class, [PixbufLoader][GdkPixbuf.PixbufLoader].

## Examples

<div class="grid cards" markdown>

-   **Gtasks**

    ```py title="main.py"
    icon_data = pkgutil.get_data(__package__, ICON)
    if icon_data:
        icon_pixbuf = GdkPixbuf.PixbufLoader.new_with_type('png')
        icon_pixbuf.write(icon_data)
        icon_pixbuf.close()
        self.set_icon(icon_pixbuf.get_pixbuf())
    ```

</div>
