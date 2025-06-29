```rs
--8<-- "includes/rs/the-book/10-rectangle-area/src/main.rs"
```

Adding outer attribute to implement Display trait.

```rs hl_lines="1 14"
--8<-- "includes/rs/the-book/11/src/main.rs"
```

Reimplementing area function as a method (or rather "associated function") on Rectangle.
Note that the method takes a reference to `self`, however methods can take ownership of self (rare) or a mutable borrow.

```rs hl_lines="7-11"
--8<-- "includes/rs/the-book/12/src/main.rs"
```

Implementing another associated function that takes another Rectangle.

```rs hl_lines="12-14"
--8<-- "includes/rs/the-book/13/src/main.rs"
```

