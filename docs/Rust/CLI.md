# Reimplementing CLI utilities


=== "TODO"

    - Implement using clap
        - mkdir
        - rmdir
    - Paste in grep implementations
        - grep-lite
        - mini-grep

=== "cat"

    ```rs
    --8<-- "includes/rs/rcat/rcat1/src/main.rs"
    ```

=== "git"

    ```rs
    --8<-- "includes/rs/cli/git-clap/src/main.rs"
    ```

=== "grep"

    === "grep-lite"

        TODO: Paste most complete implementation of grep from *Rust in Action*...

    === "minigrep"

        TODO: Paste most complete implementation of grep from *The Rust Programming Language*

=== "mkdir"

    ```rs
    --8<-- "includes/rs/dir/rdir-clap/src/main.rs"
    ```

    [std][std]::[fs][std::fs]::[create\_dir](https://doc.rust-lang.org/stable/std/fs/fn.create_dir.html) creates a new directory at the provided path and returns a Result.

    ```rs
    --8<-- "includes/rs/cli/mkdir/rmkdir0/src/main.rs"
    ```

    [std][std]::[path][std::path]::[Path](https://doc.rust-lang.org/stable/std/path/struct.Path.html) provides a way to check for existence of the directory.

    ```rs title="Validation"
    --8<-- "includes/rs/cli/mkdir/rmkdir2/src/main.rs"
    ```

    In fact, create\_dir already returns checks for the existence of the directory and returns an Error.
    In this even more simplified implementation, the main function returns a Return type.

    ```rs
    --8<-- "includes/rs/cli/mkdir/rmkdir3/src/main.rs"
    ```

=== "rmdir"

    ```rs
    --8<-- "includes/rs/cli/rrmdir/src/main.rs"
    ```


