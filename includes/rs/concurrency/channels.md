_Message passing_ is one approach to ensuring safe concurrency that is gaining popularity.
Toward this, the standard library implements _channels_, a general programming concept by which data is sent from one thread to another.
A channel has a transmitter ("producer") and a receiver ("consumer").

A new channel can be created by using [`mpsc::channel()`](https://doc.rust-lang.org/stable/std/sync/mpsc/fn.channel.html), which returns the transmitter and receiver (conventionally abbreviated `tx` and `rx` in other fields) as a tuple.

```rs title="concurrency/04"
--8<-- "includes/rs/concurrency/04/src/main.rs"
```

Now we pass the transmitter into a spawned thread and send a string to allow communication with the main thread.
The use of the `move` keyword moves `tx` into the closure so that the spawned thread owns it.

-   `send` returns a Result that contains an error if the receiver has already been dropped.
-   The receiver has two useful methods: 

    -   `recv` which blocks the main thread's execution and waits for a value to be received, returning a Result.
    -   `try_recv` which does not block but returns a Result immediately and Err if there is not message available.

```rs hl_lines="9 12" title="concurrency/05"
--8<-- "includes/rs/concurrency/05/src/main.rs"
```

Attempting to access a moved value after it has been sent to another thread results in a compiler error. (1)
{: .annotate }

1.  

    ```rs hl_lines="10" title="concurrency/06"
    --8<-- "includes/rs/concurrency/06/src/main.rs"
    ```

We can watch the receiver waiting for values (note that we are not calling `recv` explicitly anymore but treating rx as an iterator):

```rs title="concurrency/07"
--8<-- "includes/rs/concurrency/07/src/main.rs"
```

We create multiple producers by cloning the transmitter.

```rs title="concurrency/08"
--8<-- "includes/rs/concurrency/08/src/main.rs"
```
