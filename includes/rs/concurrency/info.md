Rust's standard library uses a 1:1 model of thread implementation, whereby one thread defined in code corresponds to one operating system thread (alternatives exist).

This simple example illustrates spawning a single thread which is not joined, resulting in the spawned thread being terminated when the main loop ends.

```rs title="concurrency/01"
--8<-- "includes/rs/concurrency/01/src/main.rs"
```

The return type of `spawn` is `JoinHandle<T>`, an owned value that will wait for its thread to finish when the `join` method is called on it.
We do this in the next example, which allows the spawned thread to finish executing before exiting the program.

```rs title="concurrency/02"
--8<-- "includes/rs/concurrency/02/src/main.rs"
```

Placement of the join method call matters.
If the method call is placed above the main loop, then the spawned thread will finish and join before the loop even begins.
