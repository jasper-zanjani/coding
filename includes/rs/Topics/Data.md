Variable declarations are called **bindings** in Rust, and by convention variable names are in **snake\_case** (lower-case letters with words delimited by **\_**).
They are globally scoped by default unless they are declared in a code block.

<div class="grid cards" markdown>

-   #### Mutability

    ---

    Variables are immutable by default, so if their values are to change they must be marked with `mut`.
    However, immutable variables are distinct from constants declared using `const`, which cannot be made mutable at all.
    `const` identifiers are conventionally written in capitalized snake\_case.


    ```rs title="Immutable"
    let language = "&nbsp;";
    ```
    ```rs title="Mutable"
    let mut language = "&nbsp;";
    ```
    ```rs title="Constant"
    const language = "&nbsp;";
    ```

-   #### Type

    ---

    Data type is explicitly specified on initialization after colon, and this same syntax is used to type function parameters and return types:

    ```rs
    let language: String = "&nbsp;";
    ```

    !!! info "!"

        A special **`!`** type indicates that the function never returns

        ```rs
        // RIA p. 78
        fn read(f: &mut File, save_to: &mut Vec<u8>) -> ! {
            unimplemented!();
        }
        ```

</div>


--8<-- "includes/rs/links.md"