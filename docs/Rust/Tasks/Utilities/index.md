# Overview

The success of [ripgrep](https://github.com/BurntSushi/ripgrep) has inspired many ports of other GNU utilities to Rust.

Porting grep to Rust provides the opportunity to explore various ways of using [iterators](/Rust/Glossary#iterator), evolving from a naive `for in` loop to the [**`filter()`**](/Rust/Glossary#filter) iterator method using a [closure](/Rust/Glossary#closure).


#### To-do

- Implement using clap
    - mkdir
    - rmdir
- Paste in grep implementations
    - grep-lite
    - mini-grep
