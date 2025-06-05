import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, GLib, Gdk

class TicTacToeWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app, title="Tic-Tac-Toe")

        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.game_over = False

        self.set_default_size(300, 350)
        self.set_resizable(False)

        main_vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.set_child(main_vbox)
        main_vbox.set_margin_top(10)
        main_vbox.set_margin_bottom(10)
        main_vbox.set_margin_start(10)
        main_vbox.set_margin_end(10)

        self.status_label = Gtk.Label(label=f"Player {self.current_player}'s turn")
        self.status_label.get_style_context().add_class("title-4") # Using a predefined style class for larger text
        main_vbox.append(self.status_label)

        grid = Gtk.Grid()
        grid.set_row_spacing(5)
        grid.set_column_spacing(5)
        grid.set_vexpand(True)
        grid.set_hexpand(True)
        main_vbox.append(grid)

        for r in range(3):
            for c in range(3):
                button = Gtk.Button(label="")
                button.set_size_request(80, 80) # Make buttons square-like
                button.get_style_context().add_class("font-scale-2") # Increase font size if possible
                button.connect("clicked", self.on_button_clicked, r, c)
                self.buttons[r][c] = button
                grid.attach(button, c, r, 1, 1)

        restart_button = Gtk.Button(label="Restart Game")
        restart_button.connect("clicked", self.on_restart_clicked)
        main_vbox.append(restart_button)

    def on_button_clicked(self, widget, r, c):
        if self.board[r][c] == "" and not self.game_over:
            self.board[r][c] = self.current_player
            widget.set_label(self.current_player)
            widget.set_sensitive(False) # Disable button after click

            if self.check_winner():
                self.status_label.set_label(f"Player {self.current_player} wins!")
                self.game_over = True
                self.disable_all_buttons()
            elif self.check_draw():
                self.status_label.set_label("It's a draw!")
                self.game_over = True
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.set_label(f"Player {self.current_player}'s turn")

    def check_winner(self):
        # Check rows
        for r in range(3):
            if self.board[r][0] == self.board[r][1] == self.board[r][2] == self.current_player:
                return True
        # Check columns
        for c in range(3):
            if self.board[0][c] == self.board[1][c] == self.board[2][c] == self.current_player:
                return True
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.current_player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == self.current_player:
            return True
        return False

    def check_draw(self):
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == "":
                    return False # If any cell is empty, game is not a draw
        return True # All cells are filled

    def disable_all_buttons(self):
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].set_sensitive(False)

    def on_restart_clicked(self, widget):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.game_over = False
        self.status_label.set_label(f"Player {self.current_player}'s turn")
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].set_label("")
                self.buttons[r][c].set_sensitive(True)

class TicTacToeApp(Gtk.Application):
    def __init__(self, **kwargs):
        super().__init__(application_id="org.example.tictactoe", **kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = TicTacToeWindow(self)
        self.win.present()

if __name__ == "__main__":
    # Add some CSS to make button text larger and center the status label
    css_provider = Gtk.CssProvider()
    css_provider.load_from_data(b"""
    button {
        font-size: 36px; /* Increase font size for X and O */
        font-weight: bold;
    }
    label {
        font-size: 16px; /* Default label size */
    }
    label.title-4 { /* Style for our status label */
        font-size: 20px;
        font-weight: bold;
        text-align: center; /* Note: text-align might not work directly on GtkLabel */
    }
    grid {
        margin-top: 10px;
        margin-bottom: 10px;
    }
    window {
        background-color: #f0f0f0; /* Light grey background for the window */
    }
    """)
    Gtk.StyleContext.add_provider_for_display(
        Gdk.Display.get_default(),
        css_provider,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )

    app = TicTacToeApp()
    app.run(None)
