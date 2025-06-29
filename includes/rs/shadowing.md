**Shadowing** and **masking** are terms that refer to using a locally scoped variable with the same identifier as a global variable.
When in the local variable's block, the local variable is said to be **masking** the global one, which conversely is **shadowing** the local.
Once the local scope is exited, the global variable's variable is accessible again and the local variable is destroyed.

Shadowing is used in the Guessing Game coding task to parse the input string as an integer.

```rs hl_lines="15" title="Guessing Game"
--8<-- "includes/rs/the-book/03-guessing-game/src/main.rs"
```
