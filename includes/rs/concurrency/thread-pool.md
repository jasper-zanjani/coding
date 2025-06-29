A _thread pool_ is a group of spawned threads that are waiting to handle a task.

In the following example, a new thread is spawned for every request that arrives.
This is dangerous because there is no limit to the number of threads created.

<div class="grid cards" markdown>

```rs
--8<-- "includes/rs/the-book/96/src/main.rs"
```

```rs
--8<-- "includes/rs/the-book/97/src/main.rs"
```

</div>

We implement a thread pool (which apparently isn't available in the standard library) as follows:

-   The `execute` method is modeled on [`thread::spawn`](https://doc.rust-lang.org/stable/std/thread/fn.spawn.html) which uses several bounds on the type parameter F.

    -   `FnOnce` is appropriate because the thread running a request will only execute that request's closure one time.
        The `()` are necessary because this FnOnce represents a closure that takes no parameters and returns the unit type `()`.
    -   `Send` allows the closure to be transfered from one thread to another.
        The closure must be passed _by value_ from the thread where it is spawned to the new thread, and its return value must be passed from the new thread to the thread where it is `join`ed.
    -   The lifetime bound `'static` is needed because we don't know how long the thread will take to execute.
        The closure and its return must have a lifetime of the whole program execution.

```rs
--8<-- "includes/rs/the-book/98/src/main.rs"
```
