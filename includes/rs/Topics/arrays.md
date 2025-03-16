There are various collection types available in Rust, the most C-like of which is the **array**, which is a collection of objects of the same type `T`, stored in contiguous memory.
Arrays are limited because their length must be known at compile-time.
If the size and type cannot be inferred, the length is placed after a semicolon within the type signature.

```rs
let array [u8; 5] = [1, 2, 3, 4, 5];
```

They cannot be built directly from iterators, but a conversion method must be used.

```rs
// Error
let array: [u8; 5] = (1..5).collect();

let array: [u8; 5] = (1..6).collect::<Vec<u8>>().try_into().expect("Error");
```

Array slices use the range operator, but are similar to other slices in that they store references to the index of the first and last element of the slice.

```rs
let slice = &array[1..3]; // [2, 3, 4]
```
