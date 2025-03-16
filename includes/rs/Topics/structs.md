[**Structs**](https://doc.rust-lang.org/book/ch05-00-structs.html) are custom types that allow data to be packaged together, similar to the data attributes of an object in object-oriented languages.

A struct is defined and then instantiated

<div class="grid cards" markdown>

```rs title="Definition"
struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}
```

```rs title="Instantiation"
fn main() {
    let user1 = User {
        active: true,
        username: String::from("someusername123"),
        email: String::from("someone@example.com"),
        sign_in_count: 1,
    };
}
```

</div>
