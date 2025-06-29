There are many ways of processing CLI arguments in Rust.

Within the standard library, various methods on the `Args` struct returned by [`args`](https://doc.rust-lang.org/std/env/fn.args.html) provide access to CLI arguments.
Note that these methods are actually methods on [`Iterator`][Iterator] which Args implements.

-   [`nth`][nth] takes one argument specified by number (1)
    {: .annotate }

    1.  

        ```rs hl_lines="4" title="hw/01"
        --8<-- "includes/rs/01-hello-world/01-parameterized/src/main.rs"
        ```

-   [`skip`][skip] can be used to take all but the first argument (1)
    {: .annotate }

    1.  

        ```rs title="cat/00" hl_lines="2"
        --8<-- "includes/rs/50-cat/00/src/main.rs"
        ```

-   [`collect`][collect] collects all arguments into a Vector (1)
    {: .annotate }

    1.  

        ```rs hl_lines="12" title="TRPL/70"
        --8<-- "includes/rs/the-book/70-web-scraper/src/main.rs"
        ```

The clap crate is the preeminent CLI library in Rust.


```rs
--8<-- "includes/rs/01-hello-world/10-clap/src/main.rs"
```
