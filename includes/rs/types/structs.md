[Structs](https://doc.rust-lang.org/book/ch05-00-structs.html) are custom types that allow data to be packaged together, similar to the data attributes of an object in object-oriented languages.

A struct's type structure is defined before it is instantiated.


```rs
--8<-- "includes/rs/the-book/06-structs/src/main.rs"
```

Unlike other languages, Rust does not allow individual fields to be made mutable.

Rust does offer a "field init shorthand" to initialize structs from the arguments passed to functions when the struct fields are named exactly like the parameters.

```rs hl_lines="19 20" title="Field init shorthand"
--8<-- "includes/rs/the-book/07-structs/src/main.rs"
```

The "struct update syntax" allows one struct to be initialized from another struct without repetitively typing field names.


```rs hl_lines="13" title="Struct update syntax"
--8<-- "includes/rs/the-book/08-structs/src/main.rs"
```

New types can also be created using "tuple structs"

```rs title="Tuple structs"
struct Color(i32, i32, i32);
struct Point(i32, i32, i32);

fn main() {
    let black = Color(0, 0, 0);
    let origin = Point(0, 0, 0);
}
```

Methods or "associated functions" are defined in impl blocks.

```rs hl_lines="7-15"
--8<-- "includes/rs/the-book/13/src/main.rs"
```
