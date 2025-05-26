private void update_dimensions () {
    if (theme == null)
        return;

    var width = get_width ();
    var height = get_height ();

    /* Shrink border width at smaller window size (mobile screens) */
    var h_border = (float) width / 220;
    var v_border = (float) height / 560;
    var map_width = game.map.width + (game.map.h_overhang / 4) + h_border;
    var map_height = (game.map.height + (game.map.v_overhang / 4) + v_border) * theme_aspect;

    /* Scale the map to fit */
    var unit_width = (int) double.min (width / map_width, height / map_height);
    var unit_height = (int) (unit_width * theme_aspect);

    /* The size of one tile is two units wide, and the correct aspect ratio */
    tile_width = unit_width * 2;
    tile_height = unit_height * 2;

    /* Offset the tiles when on a higher layer (themes must use these hard-coded ratios) */
    tile_layer_offset_x = tile_width / 7;
    tile_layer_offset_y = tile_height / 10;

    /* Center the map */
    x_offset = (int) (width - ((game.map.width + (game.map.h_overhang / 4)) * unit_width)) / 2;
    y_offset = (int) (height - ((game.map.height * unit_height) - ((game.map.v_overhang * unit_height) / 8))) / 2;

    /* The images are bigger than the tile as they contain the isometric extension in the z-axis */
    tile_pattern_width = tile_width + tile_layer_offset_x;
    tile_pattern_height = tile_height + tile_layer_offset_y;

    /* Store the exact width the theme should be rendered at */
    rendered_theme_width = tile_pattern_width * 43;
    rendered_theme_height = tile_pattern_height * 2;
}
