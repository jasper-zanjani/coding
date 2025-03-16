# Command-line arguments

--8<-- "includes/rs/docs/std.md"

std::env::[args()](https://doc.rust-lang.org/std/env/fn.args.html) exposes an iterator that returns each command-line argument used to invoke the executable.


```rs
--8<-- "includes/rs/hello-world/hello-world-parameterized0/src/main.rs"
```

Here, if the first argument is "greet", it is interpreted as a subcommand that changes the Hello, World! message.

```rs
--8<-- "includes/rs/hello-world/hello-world-parameterized1/src/main.rs"
```

args() yields Strings, so it has to be cast to a string slice in the match statement because match arms can't have function calls.
Note that looping through the iterator requires the first item to be skipped.

```rs
--8<-- "includes/rs/cat/cat-single-arg/src/main.rs"
```
