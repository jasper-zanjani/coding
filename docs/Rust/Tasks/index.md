# Tasks

<div class="grid cards" markdown>


-   #### Specify nightly build

    ---

    ```sh
    rustup install nightly

    # Ad hoc
    cargo +nightly run

    # Permanent
    rustup override set nightly
    ```

-   #### Publishing

    ---

    Some additional fields of the Cargo.toml are required before publishing:

    ```toml hl_lines="6-9"
    [package]
    name = "mdrend"
    version = "0.1.0"
    edition = "2018"
    authors= ["Johnny Appleseed <johnny@apple.com>"]
    license = "MIT"
    keywords = [ "Parse", "markdown"]
    repository = "https://github.com/..."
    description = "Read a markdown file and return parsed HTML"

    [dependencies]
    clap = "2.34.0"
    maud = "0.23.0"
    pulldown-cmark = "0.8.0"
    ```

    ```sh
    cargo login
    cargo publish
    ```

-   #### Hello, World!

    ---

    === "Parameterized"

        ```rs
        --8<-- "includes/rs/hello-world/parameterized.rs"
        ```

    === "Interactive"

        ```rs
        --8<-- "includes/rs/hello-world/interactive.rs"
        ```

    === "Modules"

        === "One file"

            ```rs hl_lines="1-2 9 19"
            use input::get_name;
            use output::display_name;

            fn main() -> Result<(), std::io::Error> {
                get_name().and_then(display_name)?;
                Ok(())
            }

            pub mod input {
                
                pub fn get_name() -> Result<String, std::io::Error> {
                    let mut name = String::new();
                    println!("What is your name? ");
                    std::io::stdin().read_line(&mut name)?;
                    Ok(name.trim().to_string())
                }
            }

            pub mod output {
                
                pub fn display_name(name: String) -> Result<(), std::io::Error> {
                    println!("Hello, {}!", name);
                    Ok(())
                }
            }
            ```

        === "Multiple files"

            When separating modules into their own files, the filename of the module must match the name provided after **mod**.
            Folders can also be used, in which case the folder name must match.

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

    
-   #### Caesar cipher

    ---
    ```rs
    --8<-- "includes/rs/caesar.rs"
    ```

-   #### Interactive echo

    ---

    ```rs
    --8<-- "includes/rs/echo-interactive.rs"
    ```


-   #### Weight on Mars

    ---

    ```rs
    --8<-- "includes/rs/mars.rs"
    ```

-   #### Fibonacci sequence

    ---

    === "Recursive"

        ```rs
        --8<-- "includes/rs/Tasks/fibonacci-recursive.rs"
        ```

    === "Memoized"

        ```rs
        --8<-- "includes/rs/Tasks/fibonacci-memoized.rs"
        ```

-   #### cat clone

    ---


    ```rs
    // Handling only one file (first argument)
    --8<-- "includes/rs/cat/1.rs"
    ```

    ```rs
    // Loop over every argument
    --8<-- "includes/rs/cat/2.rs"
    ```

-   #### starships

    ```rs
    --8<-- "includes/rs/starships/src/main.rs"
    ```

</div>