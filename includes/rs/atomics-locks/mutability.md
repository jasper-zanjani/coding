In Rust, the distinction between [mutable and immutable borrowing](https://marabos.nl/atomics/basics.html#borrowing-and-races) is intended to fully prevent _data races_, where one thread mutates data while the other concurrently accesses it.
Data races are generally [_undefined behavior_](https://marabos.nl/atomics/basics.html#undefined-behavior), meaning the compiler will optimistically assume these situations will not occur.
Undefined behavior is only possible in Rust when using `unsafe` code, which means the compiler is not validating the safety of the code.
