The key elements of asynchronous programming in Rust are _futures_ and Rust's `async` and `await` keywords.
A _future_ is a value that will be ready at some point in the future and in Rust it is built with the `Future` trait.

-   `async` is applied to blocks and functions to specify that they can be interrupted and resumed.

-   `await` is used to await a future

The function `page_title` is marked with async and the await keyword (not a method call but a "postfix keyword") is appended to `get()` and `text()`.

```rs
--8<-- "includes/rs/the-book/70-web-scraper/src/main.rs"
```

Like iterators, futures in Rust are lazy and will do nothing until you ask them with the `await` keyword.

When Rust sees a block marked with `async`, it compiles it into a unique, anonymous data type that implements the `Future` trait
A function marked with `async` is compiled into a non-async function whose body is an async block, and it returns the anonymous data type the compiler created for that block.
In other words, writing an async function is equivalent to writing a function that returns a future of the return type.

Every _await point_ (where code uses the await keyword) represents a place where control is handed back to the runtime.
In essence, the runtime is an invisible state machine managed by the Rust compiler.
An _executor_ refers to the part of a runtime responsible for executing the async code.


```rs
--8<-- "includes/rs/the-book/71/src/main.rs"
```

---

When combining async and concurrent code, care must be taken not to confuse the sometimes similar-looking APIs.

This simple example demonstrates concurrency without using the `join` method, resulting in the code stopping as soon as the for loop in the body of the main async block finishes.

```rs
--8<-- "includes/rs/concurrency/20/src/main.rs"
```

Using await instead of calling `join` provides similar results, except this way we don't have to spawn a thread, not even a task.

```rs
--8<-- "includes/rs/concurrency/21/src/main.rs"
```
