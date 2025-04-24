**scalar replacement of aggregates** (SROA): One of the core optimizations that a [C](#c) compiler performs; attempts to replace `struct`s and arrays with fixed lengths with individual variables, which allows the compiler to treat accesses as independent and elide operations entirely if it can prove the results are never visible, which also deletes padding sometimes.

