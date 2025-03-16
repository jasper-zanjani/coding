# std

```rs title="Naive"
--8<-- "includes/rs/hello-world/hello-world-naive/src/main.rs"
```


```rs title="Parameterized"
--8<-- "includes/rs/hello-world/hello-world-parameterized1/src/main.rs"
```

```rs title="Interactive"
--8<-- "includes/rs/hello-world/hello-world-interactive/src/main.rs"
```


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

