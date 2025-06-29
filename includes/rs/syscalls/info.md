In Rust, the **nix** crate can be used for syscalls, but depending on the type, the proper feature flag must be used (i.e. "process" for `getpid`, etc)

```rs title="src/main.rs"
--8<-- "includes/rs/syscalls/syscalls0.rs"
```

1.  

    ```c title="C equivalent"
    --8<-- "includes/c/syscalls/syscalls0.c"
    ```


```toml title="Cargo.toml"
--8<-- "includes/rs/syscalls/syscalls0.toml"
```

