[std][std]::[sync][std::sync]::[atomic](https://doc.rust-lang.org/stable/std/sync/atomic/index.html) provides thread-safe types modeled on the [atomics](https://doc.rust-lang.org/stable/nomicon/atomics.html) of C++20.
This model introduces the concept of **atomic accesses** which tell the hardware and compiler what ordering it has with relation to other accesses. 
This largely boils down to preventing reordering of instructions and determining how writes are propagated to other threads.

[std][std]::[sync][std::sync]::[RwLock](https://doc.rust-lang.org/stable/std/sync/struct.RwLock.html) is a **reader-writer lock**, which allows a number of readers or at most one writer at any point in time.
A **Mutex**, by comparison, does not distinguish between readers or writers and blocks any threads waiting for the lock to become available.

```rs
let lock = std::sync::RwLock::new(1);
```

**write** attempts to acquire the rwlock with exclusive write access and returns a [std][std]::[sync](https://doc.rust-lang.org/stable/std/sync/)::[LockResult](https://doc.rust-lang.org/stable/std/sync/type.LockResult.html) (really a type alias for Result).

```rs
let mut n = lock.write().unwrap();
*n = 2;
```

[std][std]::[sync][std::sync]::[RwLock](https://doc.rust-lang.org/stable/std/sync/struct.RwLock.html).[try\_read](https://doc.rust-lang.org/stable/std/sync/struct.RwLock.html) attempts to acquire the RwLock with shared read access.

```rs
assert!(lock.try_read().is_err());
```