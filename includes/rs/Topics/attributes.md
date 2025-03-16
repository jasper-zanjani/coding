[**Attributes**](https://doc.rust-lang.org/reference/attributes.html) consist of a path to the attribute followed by an optional delimited token tree which is interpreted by the attribute itself.

The [**derive attribute**](https://doc.rust-lang.org/reference/attributes/derive.html) allows new items to be automatically generated for data structures.
This technique, called "deriving", is used to easily implement several [commonly-used traits](https://www.youtube.com/watch?v=Nzclc6MswaI) on new types.

<div class="grid cards" markdown>

-   #### [Debug](https://doc.rust-lang.org/stable/std/fmt/derive.Debug.html)

    ---

    By default, the template `:?` cannot be used to display a new type.
    However, by deriving Debug, the Debug template can be used to display the struct.

    ```rs hl_lines="1 8"
    #[derive(Debug)]
    enum Role {
        Admin,
        Standard,
        Guest,
    }

    #[derive(Debug)]
    struct User {
        id: u32,
        name: String,
        role: Role,
    }

    fn main() {
        user1 = User { 
            id: 1, 
            name: "John Doe", 
            role: Role::Admin 
        };
        println!("{:?}", user!);
    }
    ```



</div>

[Lint check attributes](https://doc.rust-lang.org/reference/attributes/diagnostics.html#lint-check-attributes) alter the default lint level

```rs
#[allow(dead_code)]
#[allow(unused_variables)]
```
