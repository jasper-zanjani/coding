# grep

```rs title="Loop"
fn main() {
    let mut results = Vec::new();

    for line in contents.lines() {
        if line.contains(query) {
            results.push(line);
        }
    }
    results
}
```

```rs title="filter"
fn main() {
    contents.lines()
        .filter(|line| line.contains(query))
        .collect()
}
```

#### grep-lite

--8<-- "includes/rs/cli/grep/grep-lite.md"

#### minigrep

--8<-- "includes/rs/cli/grep/minigrep.md"

