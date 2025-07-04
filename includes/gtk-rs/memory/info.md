
Cloning appears to be necessary at points that seem strange to me.

For example, in the clicker example, we build an application with two buttons that much share ownership of the same value `number` as well as the label because they must have multiple ownership.
Within the signal handler of each button, we create a weak reference to the _other_ button in order to avoid a reference cycle.

```rs
--8<-- "includes/gtk-rs/03-clicker/src/main.rs"
```

However, in this example the signal emitter which is unique must be cloned because a move cannot take place on a borrowed value.

```rs title="02-scale" hl_lines="25"
--8<-- "includes/gtk-rs/02-scale/src/main.rs"
```

So a rule of thumb may be, if the signal emitter appears in the closure it must be cloned.

---

#### `glib::clone` or `clone`?

Although we were taught to use the `glib::clone` macro, it appears to be possible to use Rust's built-in `clone` to achieve similar results.


<div class="grid cards" markdown>

```rs title="02-scale" hl_lines="26-31"
--8<-- "includes/gtk-rs/02-scale/src/main.rs"
```

```rs title="02-scale-clone" hl_lines="25"
--8<-- "includes/gtk-rs/02-scale-clone/src/main.rs"
```
</div>
