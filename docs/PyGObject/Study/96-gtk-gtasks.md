# [GTK Google Tasks](https://github.com/antipatico/gtk_gtasks)


--8<-- "includes/pygobject/links.md"

<div class="grid cards" markdown>

-   [GdkPixbuf][GdkPixbuf] is a module with several classes:

    -   [PixbufLoader](https://api.pygobject.gnome.org/GdkPixbuf-2.0/class-PixbufLoader.html)

```py title="main.py"
icon_data = pkgutil.get_data(__package__, ICON)
if icon_data:
    icon_pixbuf = GdkPixbuf.PixbufLoader.new_with_type('png')
    icon_pixbuf.write(icon_data)
    icon_pixbuf.close()
    self.set_icon(icon_pixbuf.get_pixbuf())
```


</div>


