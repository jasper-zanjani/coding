# File handling

--8<-- "includes/rs/links.md"

There are [various ways of accessing files](https://www.youtube.com/watch?v=jk5on2Rrwf4) in Rust:

-   [`read_to_string`][read_to_string] is the simplest method but can only handle UTF-8 encoded text. (1)
    {: .annotate }

    1.  

        ```rs hl_lines="3" title="cat/00"
        --8<-- "includes/rs/50-cat/00/src/main.rs"
        ```

        `read_to_string` was also used in The Book's web server project.

        ```rs hl_lines="25"
        --8<-- "includes/rs/the-book/93/src/main.rs"
        ```

-   [`read`](https://doc.rust-lang.org/stable/std/fs/fn.read.html) returns a byte vector which can then be reencoded into text (1)
    {: .annotate }

    1.  

        ```rs hl_lines="11 12"
        --8<-- "includes/rs/cli/cat/cat-byte-vector/src/main.rs"
        ```

-   Opening a [File](https://doc.rust-lang.org/stable/std/fs/struct.File.html) handle with [`open`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.open) and passing it to [BufReader](https://doc.rust-lang.org/std/io/struct.BufReader.html). (1)
    {: .annotate }

    1.  

        ```rs
        --8<-- "includes/rs/cli/cat/cat-bufreader-lines/src/main.rs"
        ```

-   The [`bytes`](https://doc.rust-lang.org/std/io/trait.Read.html#method.bytes) method on BufReader is similar but allows bytewise control of file contents (1)
    {: .annotate }

    1.  

        ```rs
        --8<-- "includes/rs/cli/cat/cat-bufreader-bytes/src/main.rs"
        ```

## Directories

```rs
--8<-- "includes/rs/dir/rdir-clap/src/main.rs"
```
