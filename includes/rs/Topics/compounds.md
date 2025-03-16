Arrays and Tuples are considered primitive data types, albeit **Compound** ones.
Integer and Float are considered **Numeric Scalars**, while Boolean and Chars are considered **Non-Numeric Scalars**.

- Floating point numbers can be single-precision `f32` or double-precision `f64`.
- Booleans are `true` or `false` (lower-case).

Arrays are **homogeneous** sequences of elements and must be of a fixed length, declared at initialization, although the type can be determined implicitly.

Type can be inferred by the compiler or explicitly annotated after a colon:

```rs
let var:u8 = 0;
let arr:[i32; 4] = [0, 0, 0, 0];
let person : (&str, i32, &str) = ("John", 35, "Doe");
```

Array length can be given by the `len()` method.

Array slicing 

```rs
let arr:[i32;4] = [1, 2, 3, 4]; 
let slice_array2:&[i32] = &arr[0..2];
```

Tuples, like arrays, are fixed-length.
But unlike arrays they are **heterogeneous** sequences of elements.

Tuples can be **destructured** (i.e. unpacked)
```rs
let person = ("John", 35, "Doe");
let (first_name, age, last_name) = person;
```

Tuples **can** be made mutable with the `mut` keyword.

Rust's standard library includes a number of collections

- A [**vector**](#vector) stores a variable number of values of a single type in a sequence
- A [**String**](#string) is a collection of characters
- A **hash map** is a key-value store

A collection can be built from an iterator using the [**collect**](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.collect) method so long as the collection type implements std::iter::[FromIterator](https://doc.rust-lang.org/std/iter/trait.FromIterator.html).

Most collection types provide iter and iter\_mut methods that return natural iterators over the type.