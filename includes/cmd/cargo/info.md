=== "build"

    ```sh
    cargo build --release
    ```

=== "doc"

    ```sh
    # Generate docs
    cargo doc

    # Open documentation in browser
    cargo doc --open
    ```

=== "fmt"

    ```sh
    cargo fmt
    ```

=== "install"

    ```sh
    cargo install --git https://github.com/estin/simple-completion-language-server.git
    ```

=== "new"

    ```sh
    # Start a new crate without initializing a git repo
    cargo new --vcs none $CRATE
    ```

=== "run"

    ```sh
    cargo run --bin client
    ```

=== "tree"

    ```sh
    # Display tree of dependencies
    cargo tree
    ```

[Binary targets](https://doc.rust-lang.org/cargo/reference/cargo-targets.html#binaries) are executable programs that can be run after compilation.
The defualt binary filename is src/main.rs.
Additional binaries are stored in src/bin/ and the settings for each binary can be customized in the `[[bin]]` tables in the manifest.

Individual binaries can be specified with **--bin**

```toml
[[bin]]
name = "server"
path = "./src/server.rs"

[[bin]]
name = "client"
path = "./src/client.rs"
```
