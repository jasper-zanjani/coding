GNOME-Mahjong's GameView class extends Gtk.Widget and overrides the [`snapshot`](https://docs.gtk.org/gtk4/vfunc.Widget.snapshot.html) method.
Calls to `update_dimensions` and `resize_theme` are responsible for recalculating tile sizes and map scaling based on current window size.

=== "snapshot"

    ```vala
    --8<-- "includes/vala/99-mahjong/GameView.snapshot.vala"
    ```

=== "update_dimensions"

    ```vala
    --8<-- "includes/vala/99-mahjong/GameView.update_dimensions.vala"
    ```

=== "resize_theme"

    ```vala
    --8<-- "includes/vala/99-mahjong/GameView.resize_theme.vala"
    ```

