Tests are functions annotated with the **`#[test]`** [attribute](#attribute).
Tests fail when the test function panics.

```rs
#[test]
fn math_works() {
    assert_eq!(2+2, 4);
}

#[test]
fn fails() {
    panic!("This test will fail");
}
```

Tests can also be incorporated in documentation as markdown code blocks.

```rs title="echor"
---8<-- "includes/rs/echor/tests/cli.rs"
```