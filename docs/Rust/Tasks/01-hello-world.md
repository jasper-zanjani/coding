# Hello, World!

-   Naive (1)
    {: .annotate }

    1. The most basic Hello, World! is actually created by the cargo utility when creating a new project with `cargo new`.

        ```rs title="Naive"
        --8<-- "includes/rs/01-hello-world/00-naive/src/main.rs"
        ```

-   Parameterized (1)
    {: .annotate }

    1.  Rust's standard library provides a simple way of processing a command-line parameter.

        ```rs title="Parameterized"
        --8<-- "includes/rs/01-hello-world/01-parameterized/src/main.rs"
        ```

        The use of the `unwrap_or` method on Result allows a default value to be implemented.

        ```rs title="Parameterized (with unwrap_or)"
        --8<-- "includes/rs/01-hello-world/02-param-unwrap_or/src/main.rs"
        ```

-   Interactive (1)
    {: .annotate }

    1.  The standard library also allows for handling interactive text input.

        ```rs title="Interactive"
        --8<-- "includes/rs/01-hello-world/02-interactive/src/main.rs"
        ```

-   Modules (1)
    {: .annotate }

    1.  When separating modules into their own files, the filename of the module must match the name provided after **mod**.
        Folders can also be used, in which case the folder name must match.

        <div class="grid cards" markdown>

        ```rs title="src/main.rs"
        mod input;
        mod output;

        pub use input::get_name;
        pub use output::display_name;

        fn main() -> Result<(), std::io::Error> {
            get_name().and_then(display_name)?;
            Ok(())
        }
        ```

        ```rs title="src/input.rs"
        pub fn get_name() -> Result<String, std::io::Error> {
            let mut name = String::new();
            println!("What is your name? ");
            std::io::stdin().read_line(&mut name)?;
            Ok(name.trim().to_string())
        }
        ```

        ```rs title="src/output.rs"
        pub fn display_name(name: String) -> Result<(), std::io::Error> {
            println!("Hello, {}!", name);
            Ok(())
        }
        ```

        </div>

-   clap (1)
    {: .annotate }

    1.  

        ```rs title="Single argument"
        --8<-- "includes/rs/01-hello-world/10-clap/src/main.rs"
        ```

        ```rs title="Multiple arguments"
        --8<-- "includes/rs/01-hello-world/11-clap-append/src/main.rs"
        ```

        ```rs title="Delimited argument"
        --8<-- "includes/rs/01-hello-world/12-clap-delimiter/src/main.rs"
        ```

-   structopt (1)
    {: .annotate }

    1.  

        ```rs
        --8<-- "includes/rs/01-hello-world/20-structopt/src/main.rs"
        ```

-   Concurrent (1)
    {: .annotate }

    1.  

        --8<-- "includes/rs/01-hello-world/30/info.md"

        ```rs title="Hello, World! (concurrent)"
        --8<-- "includes/rs/01-hello-world/30/src/main.rs"
        ```
