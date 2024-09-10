Pointer types like [**`Box<T>`**](#box) and those internal to [String](#string) and [Vec](#vector) are **owning pointers**: when the owner is dropped the referent is deallocated.
Nonowning pointer types are called **references** and have no effect on their referents' lifetimes.

There are two types of reference:

- **Shared references** let you read but not modify the referent
Multiple shared references to the same value can be created.

- **Mutable references** allow both reading and modifying of the referent
To prevent **data races** only one mutable reference to a location in a scope can exist.

A mutable reference and an immutable one cannot coexist in the same scope.
Moves after a borrow are also forbidden, for this same reason.

Here, the call to **push()** causes the [vector](#vector) to be reallocated on the heap after an immutable borrow was made.

```rs
let mut data = vec![1, 2, 3];
let x = &data[0];
data.push(4);

println!("{}", x);
```

---

```rs title="Box"
type TestResult = Result<(), Box<dyn std::error::Error>>;
```