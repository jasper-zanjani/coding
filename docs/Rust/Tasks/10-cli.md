# Command-line arguments

--8<-- "includes/rs/links.md"

--8<-- "includes/rs/cli/info.md"


args() yields Strings, so it has to be cast to a string slice in the match statement because match arms can't have function calls.
Note that looping through the iterator requires the first item to be skipped.

```rs
--8<-- "includes/rs/cli/cat/cat-single-arg/src/main.rs"
```
