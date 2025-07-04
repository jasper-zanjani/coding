```rs title="00"
--8<-- "includes/rs/the-book/00/src/main.rs"
```

Todo: function that returns Result

```rs title="01"
--8<-- "includes/rs/the-book/01/src/main.rs"
```

```rs title="02"
--8<-- "includes/rs/the-book/02/src/main.rs"
```

In order to incorporate the **cmp** module to use the Ordering enum, we must be able to parse the user's guess to a number type.
This example also demonstrates shadowing.

```rs hl_lines="15-18" title="03"
--8<-- "includes/rs/the-book/03/src/main.rs"
```

Infinite [loop](https://doc.rust-lang.org/stable/std/keyword.loop.html)

```rs hl_lines="10 26" title="04"
--8<-- "includes/rs/the-book/04/src/main.rs"
```

A match statement to beef up the parsing behavior and prevent panic on invalid input:

```rs hl_lines="26-29" title="05"
--8<-- "includes/rs/the-book/05/src/main.rs"
```

