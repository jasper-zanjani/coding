<div class="grid cards" markdown>


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


            ```rs title="src/main.rs" hl_lines="1-2 4-5"
            mod input;
            mod output;

            pub use input::get_name;
            pub use output::display_name;

            fn main() -> Result<(), std::io::Error> {
                get_name().and_then(display_name)?;
                Ok(())
            }
            ```

            When separating modules into their own files, the filename of the module must match the name provided after **mod**.
            Folders can also be used, in which case the folder name must match.

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
    
#### Caesar cipher
:   
    ''' rs
    pub mod encryptor {
        pub trait Encryptable {
            fn encrypt(&self) -> String;
        }

        pub struct Rot13(pub String);

        impl Encryptable for Rot13 {
            fn encrypt(&self) -> String {
                self.0
                    .chars()
                    .map(|ch| match ch {
                        'a'..='m' | 'A'..='M' => (ch as u8 + 13) as char,
                        'n'..='z' | 'N'..='Z' => (ch as u8 - 13) as char,
                        _ => ch,
                    })
                    .collect()
            }
        }
    }

    use encryptor::Encryptable;

    fn main() {
        println!("Input the string you want to encrypt:");
        let mut user_input = String::new();

        std::io::stdin()
            .read_line(&mut user_input)
            .expect("Cannot read input!");
        println!(
            "Your encrypted string: {}",
            encryptor::Rot13(user_input).encrypt()
        );
    }
    '''