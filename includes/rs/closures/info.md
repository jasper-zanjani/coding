A closure is used in the `giveaway` method.

```rs hl_lines="10"
--8<-- "includes/rs/closures/00/src/main.rs"
```

A closure implements various traits depending on how it is used.

-   `FnOnce` applies to closures that can be called once, that is. All closures implement at least this trait.
    A closure that moves captured values out of its body will implement only `FnOnce` and none of the others.

-   `FnMut` applies to closure that don't move the captured value but might mutate it.

-   `Fn` applies to closures that neither move nor mutate captured values, as well as closures that capture nothing from their environment.

--8<-- "includes/rs/closures/gtk.md"
