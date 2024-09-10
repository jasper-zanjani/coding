The [convert][std::convert] module contains two main traits for converting data types:

- [From](https://doc.rust-lang.org/stable/std/convert/trait.From.html) and the from method serves as a generic constructor for producing an instance of a type from some other single value.
- [Into](https://doc.rust-lang.org/stable/std/convert/trait.Into.html) is intended for conversion to types outside the current crate.

In fact by implementing the From trait for any type, the into method becomes usable as well.
However, implementing Into does not allow use of the from method.

Implementing From on a new type allows us to generate types arbitrarily.

<div class="grid cards" markdown>

-   From a comma-separated string:

    ```rs
    struct Person {
        name: String,
        age: usize
    }

    impl From<&str> for Person {
        fn from(s: &str) -> Self {
            Person {

            }
        }
    }

    fn main() {
        let p1 = Person::from("Mark,20");
        let p2 = "Gerald,70".into();
    }
    ```

</div>

From is used in error types.