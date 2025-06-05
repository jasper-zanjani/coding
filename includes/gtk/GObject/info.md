```py title="Canonical implementation" hl_lines="13 17 21"
--8<-- "includes/gtk/GObject/GObject.Property-decorator.py"
```

[GObject][GObject] [properties](https://api.pygobject.gnome.org/GObject-2.0/class-Property.html) can be created with the `GObject.Property` decorator: (1)
{: .annotate }

1.  

    ```py title="Equivalent" hl_lines="6-8"
    --8<-- "includes/gtk/GObject/GObject.Property.py"
    ```

## Examples

<div class="grid cards" markdown>

-   **WSelector**

    ```py title="wselector/models.py"
    class WallpaperGObject(GObject.Object):
        """GObject wrapper for WallpaperInfo."""
        __gtype_name__ = 'WallpaperGObject'
        
        id = GObject.Property(type=str)
        url = GObject.Property(type=str)
        thumbnail_url = GObject.Property(type=str)
        title = GObject.Property(type=str)
        category = GObject.Property(type=str)
        purity = GObject.Property(type=str)
        
        def __init__(self, wallpaper_info: WallpaperInfo):
            GObject.Object.__init__(self)
            self.id = wallpaper_info.id
            self.url = wallpaper_info.url
            self.thumbnail_url = wallpaper_info.thumbnail_url
            self.title = wallpaper_info.title
            self.category = wallpaper_info.category
            self.purity = wallpaper_info.purity
    ```

</div>
