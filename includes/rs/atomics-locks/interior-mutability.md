[Interior mutability](https://marabos.nl/atomics/basics.html#interior-mutability) is a feature of some types that modifies borrowing rules to work better in concurrent applications.
An example is how Rc and Arc both mutate a reference counter, even though there may be multiple clones all using the same reference counter.
In essence, interior mutability represents a cutout in the traditional system of immutable and mutable references.
Some types with interior mutability:

-   [Cell](https://marabos.nl/atomics/basics.html#cell)
-   [RefCell](https://marabos.nl/atomics/basics.html#refcell)
-   [RwLock](https://marabos.nl/atomics/basics.html#mutex-and-rwlock)
-   Atomics
-   UnsafeCell
