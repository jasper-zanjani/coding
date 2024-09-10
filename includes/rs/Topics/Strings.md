There are two main string implementations in Rust:

<div class="grid cards" markdown>

-   #### &[str][std::str] ("string slice")

    ---

    Immutable string slice representing a view into a sequence of bytes

-   #### [String](https://doc.rust-lang.org/stable/std/string/struct.String.html)

    ---

    Owned, mutable string type that allows modification of contents.

    Methods:

    === "into_bytes"

        ```rs hl_lines="8"
        #[derive(Debug)]
        struct BinaryData {
            data: Vec<u8>
        }

        impl From<String> for BinaryData {
            fn from(input: String) -> Self {
                let data: Vec<u8> = input.into_bytes();
                BinaryData { data }
            }
        }
        ```

</div>

Strings can be concatenated using various methods:

<div class="grid cards" markdown>

-   An initial String can be concatenated with an additional &str using the `+` operator

    ```rs
    println!("{}", String::from("Hello, ") + "World!");
    ```

-   The [**format** macro](https://doc.rust-lang.org/stable/std/macro.format.html) can be used.

    ```rs
    println!("{}", format!("{}{}", "Hello, ", "World!"));
    ```

</div>

Assembling strings from a single, repeated character

<div class="grid cards" markdown>

-   Using repeat method on a string

    ```rs
    println!("{}", "-".repeat(w as usize));
    ```


-   Using formatting parameters provides a more verbose implementation.

    ```rs
    println!("{}", format!("{:-<1$}", "", w as usize));
    ```

-   Specifying a char from a Unicode code point, then converting to string

    ```rs
    let char_str = char::from_u32(0x2500)
        .unwrap()
        .to_string()
        .repeat(w as usize)
    println!("{}", char_str);
    ```
</div>

Strings are typically processed as other types using the **parse** method.

```rs
let string = String::from("16");
if let number = string.parse::<usize>().unwrap();
```