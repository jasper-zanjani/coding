_Shared-state_ concurrency is another method that embraces sharing memory and features mutexes and locks.
Message-passing using channels is similar to single ownership, and shared-state concurrency is similar to multiple ownership.

A _mutex_ ("mutual exclusion") allows only one thread to access data at any given time.
This is done by means of a _lock_, a data structure that is part of the mutex that _guards_ the data it holds.
Mutexes are notorious for being difficult to use because you must remember two rules:

1.  The lock must first be _acquired_ before the data can be accessed.
2.  Once the operation has concluded the data must be unlocked to allow other threads to acquire the lock.

The analogy is similar to multiple panel speakers sharing a single microphone who must signal that they want to speak next.

This example illustrates how [`Mutex`](https://doc.rust-lang.org/std/sync/struct.Mutex.html) is used in a single-threaded context.

-   `Mutex<T>` is a smart pointer, and the call to `lock` returns another smart pointer called `MutexGuard` wrapped in a [`LockResult`](https://doc.rust-lang.org/stable/std/sync/type.LockResult.html) (really a type alias for Result).
    This call is blocking, so the current thread won't be able to do any work until the lock is acquired.
-   MutexGuard implements `Deref` to point at the inner data, and it also implements `Drop` that releases the lock automatically when it goes out of scope (at the end of the inner code block).
-   If the thread that has locked a mutex panics, causing the data to become inaccessible, the mutex is considered _poisoned_.

```rs title="concurrency/09"
--8<-- "includes/rs/concurrency/09/src/main.rs"
```

Now we spin up 10 threads and have them each increment a counter value by 1.

```rs title="concurrency/10"
--8<-- "includes/rs/concurrency/10/src/main.rs"
```

In fact, we find that this example does not compile because the counter is moved.
`Mutex<T>` does not implement the `Copy` trait and so using it between multiple threads requires _multiple ownership_.

First we attempt to give a value to multiple owners by wrapping the mutex in the smart pointer `Rc<T>`, however, this fails because we cannot send Rc between threads safely.

```rs hl_lines="6 10" title="concurrency/11"
--8<-- "includes/rs/concurrency/11/src/main.rs"
```

Rather we must use an _atomic referencing counting_ pointers.
