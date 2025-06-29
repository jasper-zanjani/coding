[Atomic operations](https://marabos.nl/atomics/atomics.html) are the main building block for all other concurrency primitives, including mutexes and condition variables.
In Rust these operations are available as methods on the [standard atomic types][atomic] (`AtomicUsize`, etc).
Unlike other types, they have interior mutability and thus allow modification through a shared reference.
Atomic types all have the same interface for loading and storing values.

Atomic operations take an [`Ordering`][Ordering], an enum which defines the order of operations.
The simplest variant with the fewest guarantees is `Relaxed`, which guarantees consistency on a single atomic variable but provides no promises about the relative order of operations.
This chapter will use only `Relaxed` and explore other Orderings in Chapter 3.

The most basic atomic operations are `load` and `store`, both of which are methods on the atomic type and take an Ordering enum as argument.

The following example shows how an [`AtomicBool`][AtomicBool] can be used with an infinite loop to implement primitive shell-like functionality.
In this context it is being used as a _stop flag_, that is a signal to inform other threads to stop running.
Note that because `some_work()` is synchronous, the program will exit only after the function completes.

```rs title="03" hl_lines="6 10"
--8<-- "includes/rs/atomics-locks/03/src/main.rs"
```
