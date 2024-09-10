A trait can use the keyword **Self** as a type.


If two structs are of the same concrete type, then a method of one changing the other
can be implemented by using a mutable reference to Self, which refers to the parent type.


```rs
--8<-- "includes/rs/learning/learning-Self/src/main.rs"
```