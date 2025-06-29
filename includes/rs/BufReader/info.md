[BufReader](https://doc.rust-lang.org/stable/std/io/struct.BufReader.html) performs large, infrequent reads and maintains an in-memory buffer of the results.
It is used in both file or network read calls.

<div class="grid cards" markdown>

```rs hl_lines="17 18" title="Web Server"
--8<-- "includes/rs/the-book/91/src/main.rs"
```

```rs hl_lines="11" title="cat Clone using BufReader"
--8<-- "includes/rs/50-cat/cat-bufreader-bytes/src/main.rs"
```

</div>
