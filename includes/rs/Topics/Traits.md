A **trait** tells the compiler about functionality a particular type has and can share with other types.
The methods that can be called on the type define its behavior.
Trait definitions allow method signatures to be grouped together to define a set of behaviors needed across multiple types.
Rust doesn't support inheritance, but the trait system offers a way to implement the behavior of OOP while maintaining type- and object-safety.

Various traits exist in the standard library to convert values.


- [AsRef](https://doc.rust-lang.org/stable/std/convert/trait.AsRef.html) to create immutable references

- [Deref](https://doc.rust-lang.org/stable/std/ops/trait.Deref.html) for explifict dereferencing as well as 

- [AsMut](https://doc.rust-lang.org/stable/std/convert/trait.AsMut.html) to create mutable references

- [Borrow](https://doc.rust-lang.org/stable/std/borrow/trait.Borrow.html)