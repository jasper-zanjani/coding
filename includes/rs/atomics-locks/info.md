--8<-- "includes/rs/links.md"

Ownership of values can be passed to spawned threads by using the `move` keyword in the closure passed to `spawn`.

```rs
--8<-- "includes/rs/atomics-locks/00/src/main.rs"
```

A _scoped thread_ is one that will not outlive its borrowed variables.
Scoped threads are implemented using the scoped spawn method `scope` (1) which does not have a `'static` bound on its argument type, allowing us to reference anything as long as it outlives the scope.
In this example, both of the new threads are concurrently accessing numbers, which is fine because neither of them modifies it.
{: .annotate }

1.  

    --8<-- "includes/rs/atomics-locks/leakpocalypse.md"

```rs title="01"
--8<-- "includes/rs/atomics-locks/01/src/main.rs"
```

However, changing the example to modify the example will produce compile-time errors because multiple mutable borrows cannot occur at the same time.


```rs title="02"
--8<-- "includes/rs/atomics-locks/02/src/main.rs"
```

There are various types of data that can be shared between threads that are not guaranteed to outlive the other.

-   [Static](https://marabos.nl/atomics/basics.html#statics) values (`'static`) can be referenced by multiple threads becaused they are owned by the entire process. (1)  
    {: .annotate }

    1.  

        ```rs hl_lines="4"
        use std::thread::spawn;

        fn main() {
            static X: [usize; 3] = [1, 2, 3];

            spawn(|| dbg!(&X));
            spawn(|| dbg!(&X));
        }
        ```

-   [Leaking](https://marabos.nl/atomics/basics.html#leaking) an allocation can be done deliberately using [`Box::leak`](https://doc.rust-lang.org/std/boxed/struct.Box.html#method.leak), which releases ownership of a Box promising never to drop it.
    The Box will live forever without an owner as long as the program runs, indicated by the `'static` lifetime. (1)
    {: .annotate }

    1.  

        ```rs hl_lines="5"
        use std::boxed::Box;
        use std::thread::spawn;

        fn main() {
            let x: &'static [usize; 3] = Box::leak(Box::new([1,2,3]));

            spawn(move || dbg!(x));
            spawn(move || dbg!(x));
        }
        ```

-   [Atomic reference counting](https://marabos.nl/atomics/basics.html#arc) allows us to make sure shared data gets dropped and deallocated.
    Rather than [`Rc`][Rc], which is not thread-safe, we must use [`Arc`][Arc] ("atomically reference counted") which is identical to Rc but guarantees that modifications to the reference counter are indivisible atomic operations, making it thread-safe. (1)
    {: .annotate }

    1.  

        ```rs hl_lines="5"
        use std::sync::Arc;
        use std::thread::spawn;

        fn main() {
            let a = Arc::new([1, 2, 3]);
            let b = a.clone();

            spawn(move || dbg!(a));
            spawn(move || dbg!(a));
        }
        ```


---

--8<-- "includes/rs/atomics-locks/atomics.md"
