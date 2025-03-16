# File handling

There are [various ways of accessing files](https://www.youtube.com/watch?v=jk5on2Rrwf4) in Rust:

- [std][std]::[fs][std::fs]::[read_to_string](https://doc.rust-lang.org/stable/std/fs/fn.read_to_string.html) reads directly to string and is convenient, but can only handle UTF-8 encoded text.

- std::fs::[read](https://doc.rust-lang.org/stable/std/fs/fn.read.html) returns a byte vector which can then be reencoded into text

- std::[io][std::io]::[BufReader](https://doc.rust-lang.org/std/io/struct.BufReader.html) adds buffering to any reader and is considered superior to read where larger, more infrequent reads optimize performance.
Filehandles and std::io::[stdin](https://doc.rust-lang.org/std/io/fn.stdin.html) both implement the BufRead trait.

- BufReader.bytes() is similar to allows bytewise control of file contents

=== "read\_to\_string"

    ```rs hl_lines="11"
    --8<-- "includes/rs/cat/cat-clap/src/main.rs"
    ```

=== "Byte vector"

    ```rs hl_lines="11 12"
    --8<-- "includes/rs/cat/cat-byte-vector/src/main.rs"
    ```

=== "Linewise"

    ```rs
    --8<-- "includes/rs/cat/cat-bufreader-lines/src/main.rs"
    ```

=== "Bytewise"

    ```rs
    --8<-- "includes/rs/cat/cat-bufreader-bytes/src/main.rs"
    ```

## Directories

```rs
--8<-- "includes/rs/dir/rdir-clap/src/main.rs"
```
