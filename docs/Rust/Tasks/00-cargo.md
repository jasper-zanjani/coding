# Cargo

#### Specify nightly build

```sh
rustup install nightly

# Ad hoc
cargo +nightly run

# Permanent
rustup override set nightly
```

#### Publishing

Some additional fields of the Cargo.toml are required before publishing:

```toml hl_lines="6-9"
[package]
name = "mdrend"
version = "0.1.0"
edition = "2018"
authors= ["Johnny Appleseed <johnny@apple.com>"]
license = "MIT"
keywords = [ "Parse", "markdown"]
repository = "https://github.com/..."
description = "Read a markdown file and return parsed HTML"

[dependencies]
clap = "2.34.0"
maud = "0.23.0"
pulldown-cmark = "0.8.0"
```

```sh
cargo login
cargo publish
```

