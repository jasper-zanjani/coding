```rs
enum Result<T, e> { Ok(T), Err(e)}
```

Result is a type that is key to Rust's error-handling paradigm.

There are a menagerie of methods used to handle Results.

- **[Result](https://doc.rust-lang.org/stable/std/result/enum.Result.html)::[unwrap](https://doc.rust-lang.org/stable/std/result/enum.Result.html#method.unwrap)** returns the contained Ok value, but will cause a panic in the case of Err.
It is inferior to the use of **?** because it assumes that each fallible call will succeed.

```rs
--8<-- "includes/rs/hello-world/parameterized.rs"
```