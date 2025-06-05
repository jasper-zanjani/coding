private void resize_theme () {
    if (game == null || theme == null)
        return;

    if (rendered_theme_width == 0)
        return;

    /* Get size to load the next tile texture at */
    int new_theme_width, new_theme_height;
    get_theme_size (out new_theme_width, out new_theme_height);

    /* If texture size didn't change, avoid unnecessary work */
    if (new_theme_width == loaded_theme_width)
        return;

    /* Load texture at new size */
    this.loaded_theme_width = new_theme_width;
    this.loaded_theme_height = new_theme_height;

    try {
        Gdk.Pixbuf pixbuf;
        if (new_theme_width > initial_theme_width)
            pixbuf = new Gdk.Pixbuf.from_resource_at_scale (theme, new_theme_width, new_theme_height, false);
        else if (new_theme_width < initial_theme_width)
            pixbuf = this.pixbuf.scale_simple (new_theme_width, new_theme_height, Gdk.InterpType.TILES);
        else
            pixbuf = this.pixbuf;

        var rowstride = new_theme_width * 4;
        var new_texture = new Gdk.MemoryTexture (
            new_theme_width,
            new_theme_height,
            Gdk.MemoryFormat.R8G8B8A8,
            pixbuf.read_pixel_bytes (),
            rowstride
        );

        if (using_cairo) {
            var theme_surface = new Cairo.ImageSurface (Cairo.Format.ARGB32, new_theme_width, new_theme_height);
            new_texture.download (theme_surface.get_data (), rowstride);
            theme_surface.mark_dirty ();
            this.cairo_pattern = new Cairo.Pattern.for_surface (theme_surface);
        } else {
            this.texture = new_texture;
        }
        queue_draw ();
    } catch (Error e) {
        warning ("Could not load theme %s: %s", theme, e.message);
    }
}
