By replacing the `Rc` which is not thread-safe with `Arc`, the example works.

```rs title="concurrency/12"
--8<-- "includes/rs/concurrency/12/src/main.rs"
```

The concept of _atomic accesses_, introduced by C++20, involves instructing the hardware and compiler what ordering it has with relation to other accesses. 
This entails preventing the reordering of instructions and determining how writes are propagated to other threads.
Rust implements thread-safe types modeled on these atomics in the [atomic](https://doc.rust-lang.org/stable/std/sync/atomic/index.html) module.

-   [`RwLock`](https://doc.rust-lang.org/stable/std/sync/struct.RwLock.html) is a _reader-writer lock_, which allows a number of readers or at most one writer at any point in time (by comparison, a mutex does not distinguish between readers or writers and blocks any threads waiting for the lock to become available).

-   `write` attempts to acquire the rwlock with exclusive write access and returns a `LockResult`

-   [`try_read`](https://doc.rust-lang.org/stable/std/sync/struct.RwLock.html) attempts to acquire the RwLock with shared read access.

```rs
let lock = std::sync::RwLock::new(1);
```

```rs
let mut n = lock.write().unwrap();
*n = 2;
```

```rs
assert!(lock.try_read().is_err());
```

