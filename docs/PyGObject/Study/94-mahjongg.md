# GNOME Mahjongg

--8<-- "includes/pygobject/links.md"

!!! info "Project structure"

    -   **game-view.vala** contains [GameView](#gameview) which handles visual representation of the game board, including tile rendering

    -   **map.vala** handles the tile layout

    -   **gnome-mahjongg.vala** implements GTK action system for commands like new game, undo, redo

    -   **game-save.vala** implements saving and loading game states (even though this doesn't appear to be available when using the application itself)

## GameView

GameView extends Gtk.Widget.
The key methods for custom drawing in GameView are:

-   [`snapshot()`](#snapshot) the main drawing method where all custom rendering happens
-   `resize_theme()` handles loading and scaling of tile textures
-   `get_tile_position()` calculates screen coordinates for each tile

#### snapshot

Custom rendering in GTK4 starts by overriding `snapshot()`
