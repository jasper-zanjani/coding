public override void snapshot (Gtk.Snapshot snapshot) {
    if (game == null)
        return;

    update_dimensions ();
    resize_theme ();

    if (texture == null && cairo_pattern == null)
        return;

    Gsk.RenderNode? texture_node = null;

    /* Scale the tile texture */
    if (texture != null) {
        var texture_snapshot = new Gtk.Snapshot ();
        texture.snapshot (texture_snapshot, rendered_theme_width, rendered_theme_height);

        texture_node = texture_snapshot.free_to_node ();
    }

    foreach (unowned var tile in game.tiles) {
        if (!tile.visible)
            continue;

        /* Select image for this tile, or blank image if paused */
        var tile_number = game.paused ? -1 : tile.number;
        var texture_x = get_image_offset (tile_number) * tile_pattern_width;
        var texture_y = tile.highlighted ? tile_pattern_height : 0;

        /* Draw the tile */
        int tile_x, tile_y;
        get_tile_position (tile, out tile_x, out tile_y);

        var tile_rect = Graphene.Rect ();
        tile_rect.init (tile_x, tile_y, tile_pattern_width, tile_pattern_height);

        snapshot.push_clip (tile_rect);

        if (texture_node != null) {
            snapshot.translate (Graphene.Point () {
                x = tile_x - texture_x,
                y = tile_y - texture_y
            });
            snapshot.append_node (texture_node);
        } else {
            /* Cairo fallback */
            var ctx = snapshot.append_cairo (tile_rect);
            var matrix = Cairo.Matrix.identity ();

            matrix.scale (
                (double)loaded_theme_width / (double)rendered_theme_width,
                (double)loaded_theme_height / (double)rendered_theme_height
            );
            matrix.translate (texture_x - tile_x, texture_y - tile_y);

            cairo_pattern.set_matrix (matrix);
            ctx.set_source (cairo_pattern);

            ctx.rectangle (tile_x, tile_y, tile_pattern_width, tile_pattern_height);
            ctx.fill ();
        }
        snapshot.pop ();
    }
}
