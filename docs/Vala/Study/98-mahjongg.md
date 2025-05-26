# GNOME Mahjongg

--8<-- "includes/pygobject/links.md"

!!! info "Project structure"

    -   **game-view.vala** contains [GameView](#gameview) which handles visual representation of the game board, including tile rendering

    -   **map.vala** handles the tile layout

    -   **gnome-mahjongg.vala** implements GTK action system for commands like new game, undo, redo

    -   **game-save.vala** implements saving and loading game states (even though this doesn't appear to be available when using the application itself)

--8<-- "includes/vala/99-mahojng/info.md"

## Graphics

--8<-- "includes/vala/99-mahjong/gfx.md"
