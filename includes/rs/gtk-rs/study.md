Implementing an activate signal handler allows us to create an empty window (note that the handler takes an _immutable reference_ to the Application instance).

```rs title="gtk-rs/00"
--8<-- "includes/rs/gtk-rs/00/src/main.rs"
```

Elaborating the activate signal handler, we create a button and pass a closure to handle the clicked signal.
Note that the button is made child to the ApplicationWindow by passing an _immutable reference_ to it.

This example recreates the typical Hello, World! using a button press to change its label.

```rs title="gtk-rs/01" hl_lines="12-18 21-23 28"
--8<-- "includes/rs/gtk-rs/01/src/main.rs"
```

Implementing a clicker app, we encounter an error when using a closure to increment a number.
Signal handlers in GTK require `'static` lifetimes for their references, so we cannot borrow a variable that lives only for the scope of the function `build_ui`.

However, the compiler's suggestion to move the number into the closure 
