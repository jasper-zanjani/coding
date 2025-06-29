This very simple example uses [`read_to_string`][read_to_string] to display the contents of any number of UTF-8 encoded files specified from the command-line.

```rs title="cat/00"
--8<-- "includes/rs/50-cat/00/src/main.rs"
```

The clap crate can be incorporated into our example by defining an application that takes one or more filenames.
In this example they are treated as Strings.

```rs title="cat/01"
--8<-- "includes/rs/50-cat/01/src/main.rs"
```

A more elaborated example uses [`value_parser`][value_parser] to parse the argument as a [`PathBuf`][PathBuf], which provides a bit more functionality appropriate to file paths.

```rs title="cat/02"
--8<-- "includes/rs/50-cat/02/src/main.rs"
```


```rs title="cat-bufreader-lines"
--8<-- "includes/rs/50-cat/cat-bufreader-lines/src/main.rs"
```

```rs title="cat-bufreader-bytes"
--8<-- "includes/rs/50-cat/cat-bufreader-bytes/src/main.rs"
```

```rs title="cat-byte-vector"
--8<-- "includes/rs/50-cat/cat-byte-vector/src/main.rs"
```

```rs title="cat/10"
--8<-- "includes/rs/50-cat/10/src/main.rs"
```

