**Option** (1) serves as a wrapper around a value and serves as Rust's null-handling mechanism.
Rust doesn't have the same implementation of null values that other languages do because handling null values is complicated and when unexpected they cause bugs.
Rather than null values, Rust implements null as variant `None` of the enum `Option<T>`
{: .annotate }

1.  **Resources**

    -   [Documentation](https://doc.rust-lang.org/std/option/enum.Option.html)

    **Definition**

    ```rs
    enum Option<T> { Some(T), None }
    ```

The reason for this is because Rust conventionally handles enums in a [`match`](#match) statement, which requires **exhaustive** enumeration of all possible cases.
The compiler itself will raise an error if you compose a match statement which leaves some potential cases unhandled.

-   [`unwrap_or_default`](https://doc.rust-lang.org/std/option/enum.Option.html#method.unwrap_or_default) returns the wrapped value or the default value for that type (i.e. 0 for usize)

-   [`or_else`](https://doc.rust-lang.org/std/option/enum.Option.html#method.or_else) returns the option if it contains a value or calls the function

-   [`unwrap_or_else`](https://doc.rust-lang.org/std/option/enum.Option.html#method.unwrap_or_else) unwraps the value if ti exists or computes it from a closure. (1)
    {: .annotate }

    1.  

        ```rs hl_lines="10"
        --8<-- "includes/rs/closures/00/src/main.rs"
        ```
