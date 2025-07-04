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

=== ":material-tools: Config"

    [Cargo configuration](https://doc.rust-lang.org/cargo/reference/config.html) is processed as cargo crawls up the directory tree looking for **.cargo/config.toml**.

    ```toml
    # Define custom target directory
    [build]
    target-dir = /path/to/target
    ```

    A third party tool, **sccache** can be installed to [cache dependencies](https://doc.rust-lang.org/cargo/reference/config.html#buildrustc-wrapper) that have already been downloaded.

    ```toml
    [build]
    rustc-wrapper = "sccache"
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


