The `move` keyword is often used with closures passed to `spawn`.
This allows the closure to take ownership of the values it uses from the environment and allowing ownership to be transferred from thread to thread.

This example will fail to compile because the closure may outlive the borrowed vector value _v_, although it is captured by the closure because it is used within it.
There is the possibility that the thread would be placed in the background without running at all while the main thread drops v.
This would result in an invalid reference, and the compiler does not allow this possibility.

Using `move` resolves the problem and allows the example to compile.

```rs hl_lines="6"
--8<-- "includes/rs/concurrency/03/src/main.rs"
```

