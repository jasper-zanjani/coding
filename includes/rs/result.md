**Result** (1) is the type used to return and propagate erros.
{: .annotate }

1.  **Resources**

    -   [Documentation](https://doc.rust-lang.org/std/result/)

    **Definition**

    ```rs
    enum Result<T, e> { Ok(T), Err(e) }
    ```


There are a variety of [methods](https://doc.rust-lang.org/std/result/#extracting-contained-values) on Result that allow flexible error handling.

Two methods cause a panic if the Result contains an error (and require E to implement Debug):

-   [`unwrap`](https://doc.rust-lang.org/stable/std/result/enum.Result.html#method.unwrap) (1) returns the contained Ok value, but will cause a panic in the case of Err.
    It is inferior to the use of **?** because it assumes that each fallible call will succeed.
    {: .annotate }

    1.  **Examples**

        ```rs hl_lines="4" title="Hello, World! (parameterized)"
        --8<-- "includes/rs/01-hello-world/01-parameterized/src/main.rs"
        ```

-   [`expect`](https://doc.rust-lang.org/std/result/enum.Result.html#method.expect) panics with a provided custom message

A family of methods allow graceful implementation of various behavior:

-   [`unwrap_or`](https://doc.rust-lang.org/stable/std/result/enum.Result.html#method.unwrap_or) returns the contained `Ok` value or a provided default. (1)
    {: .annotate }

    1.  

        ```rs title="iter/00"
        --8<-- "includes/rs/iter/00/src/main.rs"
        ```

        1.  

            ``` title="Output"
            results: [Ok(1), Err("bla"), Ok(2)]
            ```

        2.  

            ``` title="Output"
            values: [1, 0, 2]
            ```

        **Examples**

        ```rs title="Hello, World! (parameterized)" hl_lines="5"
        --8<-- "includes/rs/01-hello-world/02-param-unwrap_or/src/main.rs"
        ```

-   [`and_then`](https://doc.rust-lang.org/stable/std/result/enum.Result.html#method.and_then) calls a given function if the result is Ok or returns Err. (1)
    {: .annotate }

    1.  **Examples**

        ```rs title="Hello, World! (interactive)"
        --8<-- "includes/rs/01-hello-world/03-interactive-and_then/src/main.rs"
        ```

Transforming methods change `Result<T, E>` to Option:

-   [`err`](https://doc.rust-lang.org/std/result/enum.Result.html#method.err) transforms `Result<T, E>` to `Option<E>`, mapping `Err(e)` to `Some(e)` and `Ok(v)` to `None`

-   [`ok`](https://doc.rust-lang.org/std/result/enum.Result.html#method.ok) transforms `Result<T, E>` to `Option<T>`, mapping `Ok(v)` to `Some(v)` and `Err(e)` to `None`



-   [The question mark operator `?`](https://doc.rust-lang.org/std/result/#the-question-mark-operator-) (1) propagates errors up the call stack.
    {: .annotate }

    1.  I can't seem to get this example to work!

        ```rs hl_lines="5" title="Hello, World!"
        --8<-- "includes/rs/01-hello-world/09-question-mark-operator/src/main.rs"
        ```
