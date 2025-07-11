
An **iterator** is any value that implements [Iterator](https://doc.rust-lang.org/stable/std/iter/trait.Iterator.html).
A value is described as **iterable** if it implements [IntoIterator](https://doc.rust-lang.org/stable/std/iter/trait.IntoIterator.html) and the method **into\_iter**.

```rs
let v = vec!["antimony", "arsenic", "aluminum", "selenium"];
for element in &v {
    println!("{}", element); // (1)
}
```

1.  

    Under the hood, every **for** loop is syntactic sugar for calls to IntoIterator and Iterator methods.
    Here, the for loop uses IntoIterator::into\_iter to convert the operand &v into an iterator and then calls Iterator::next until the operand is exhausted.

    ```rs
    let mut iterator = (&v).into_iter();
    while let Some(element) = iterator.next() {
        println!("{}", element);
    }
    ```


For example, a [RangeInclusive](https://doc.rust-lang.org/stable/std/ops/struct.RangeInclusive.html) value is an iterator.

There are [three common ways](https://doc.rust-lang.org/stable/std/iter/index.html#the-three-forms-of-iteration) of creating iterators from collections:

<div class="grid cards" markdown>

-   

    - **iter()** iterates over **`&T`**
    - **iter\_mut()** iterates over **`&mut T`**
    - **into\_iter()** iterates over **`T`**

```mermaid
graph LR;
    subgraph Iterable;
    Collection;
    end;
    Collection --> |iter|Iterator;
    Collection --> |iter_mut|Iterator;
    Collection --> |into_iter|Iterator;
```

</div>


Triangle number

<div class="grid cards" markdown>


```rs
--8<-- "includes/rs/triangle-number/triangle-number-naive/src/lib.rs"
```

```rs
--8<-- "includes/rs/triangle-number/triangle-number-fold/src/lib.rs"
```

</div>

Methods that call next are referred to as **consuming adaptors**.

-   [**`collect`**][collect] transforms an Iterator into a collection.

-   [`chain`][chain] takes two iterators and creates a new iterator over both in sequence.

-   [`join`][join] flattens a slice into a single value, placing a given separator between each value. (1)

    1.  **Examples**

        ```rs
        --8<-- "includes/rs/vector/00/src/main.rs"
        ```

