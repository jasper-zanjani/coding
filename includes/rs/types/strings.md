--8<-- "includes/rs/docs/std.md"

There are two main string implementations in Rust:


-   [`&str`][str] ("string slice"): an immutable string slice representing a view into a sequence of bytes

-   [`String`][String]: an owned, mutable string type that allows modification of contents.


<div class="grid cards" markdown>

-   #### Concatenation

    ---

    Strings can be concatenated using various methods:

    -   **`+`** operator can concatenate an initial String to another string slice. (1)
        {: .annotate }


        1. 

            ```rs
            println!("{}", String::from("Hello, ") + "World!");
            ```

    -   [**format** macro](https://doc.rust-lang.org/stable/std/macro.format.html) (1)
        {: .annotate }

        1.  

            ```rs
            println!("{}", format!("{}{}", "Hello, ", "World!"));
            ```

-   #### Repeating characters

    ---

    Assembling strings from a single, repeated character

    -   [repeat](https://doc.rust-lang.org/std/primitive.str.html#method.repeat) method on string slice (1)
        {: .annotate }

        1. 

            ```rs
            println!("{}", "-".repeat(w as usize));
            ```

    -   formatting parameters (1)
        {: .annotate }

        1. 

            ```rs
            println!("{}", format!("{:-<1$}", "", w as usize));
            ```

    -   Specifying a char from a Unicode code point (1)
        {: .annotate }

        1. 

            ```rs
            let char_str = char::from_u32(0x2500)
                .unwrap()
                .to_string()
                .repeat(w as usize)
            println!("{}", char_str);
            ```

-   #### Casting

    ---

    Strings are cast into other types using the **parse** method.

    ```rs
    let string = String::from("16");
    if let number = string.parse::<usize>().unwrap();
    ```

    A String can be converted to a string slice by using [`as_str`][as_str].

</div>
