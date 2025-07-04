!!! info "Resources"

    --8<-- "includes/rs/gtk-rs/resources.md"

Implementing an activate signal handler allows us to create an empty window (note that the handler takes an _immutable reference_ to the Application instance).

```rs title="gtk-rs/00"
--8<-- "includes/gtk-rs/99/00/src/main.rs"
```

Elaborating the activate signal handler, we create a button and pass a closure to handle the clicked signal.
Note that the button is made child to the ApplicationWindow by passing an _immutable reference_ to it.

This example recreates the typical Hello, World! using a button press to change its label.

```rs title="gtk-rs/01" hl_lines="12-18 21-23 28"
--8<-- "includes/gtk-rs/99/01/src/main.rs"
```

Implementing a clicker app, we encounter an error when using a closure to increment a number.
Signal handlers in GTK require `'static` lifetimes for their references, so we cannot borrow a variable that lives only for the scope of the function `build_ui`.

```rs title="gtk-rs/02" hl_lines="21"
--8<-- "includes/gtk-rs/99/02/src/main.rs"
```

However, `number` is a captured variable within the `Fn` closure and may not be assigned to, even after following the compiler's suggestion and using `move`.

```rs title="gtk-rs/03" hl_lines="21"
--8<-- "includes/gtk-rs/99/03/src/main.rs"
```

In order to modify `number` we need a data type with _interior mutability_ (1) like [`Cell`][Cell] (for types that implement `Copy`) or [`RefCell`][RefCell].
{: .annotate }

1.  

    --8<-- "includes/rs/atomics-locks/interior-mutability.md"


```rs title="gtk-rs/04" hl_lines="22"
--8<-- "includes/gtk-rs/99/04/src/main.rs"
```

In order to have two buttons able to modify the same number, we have to implement [`Rc`][Rc], which counts the number of strong references created via clone.
Here we use the `glib::clone` macro, which was made specifically to reduce the boilerplate required for passing references into signal handler closures.

```rs title="gtk-rs/05" hl_lines="32-39"
--8<-- "includes/gtk-rs/99/05/src/main.rs"
```

Because GObjects are reference-counted and mutable, we do not need to wrap them in `Rc` but only use the `glib::clone` macro to create a weak copy of the button to pass it into the closure.
In this bizarre example, we clone the _other_ button in each button's signal handler.

In fact, because both buttons hold _strong references_ to the other, this is a _reference cycle_ which is an antipattern.

```rs title="gtk-rs/07"
--8<-- "includes/gtk-rs/99/07/src/main.rs"
```

With weak references, we avoid a reference cycle:

```rs title="gtk-rs/08" hl_lines="35-36 45-46"
--8<-- "includes/gtk-rs/99/08/src/main.rs"
```

Using weak references with the `glib::clone` macro, we can implement the canonical clicker example.

```rs title="gtk-rs/06" hl_lines="29 38 46"
--8<-- "includes/gtk-rs/99/06/src/main.rs"
```

---

