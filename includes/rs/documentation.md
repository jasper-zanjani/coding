Rust uses C-style line comments using **`//`** and block comments using **`/*`**, **`*/`**

**Doc comments** support markdown and are used to generate documentation with the use of **cargo doc**.

Markdown code blocks containing test cases are known as **doc tests** and can be run with **cargo test**, for library crates only.
Note that markdown code blocks in Rust doc comments don't need a language annotation.

- **Outer doc comments** are preceded by **`///`** and are written immediately preceding the code blocks they document
- **Inner doc comments** are preceded by **`//!`** and are written within code blocks, similar to docstrings in Python