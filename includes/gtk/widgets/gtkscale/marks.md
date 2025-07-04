Blueprint offers extended syntax for Scale offering the ability to define marks.
The [`marks`](https://gnome.pages.gitlab.gnome.org/blueprint-compiler/reference/extensions.html#syntax-extscalemarks) block allows the definition of one or more `mark` with up to three arguments: origin (required, position within the range defined by the scale's adjustment property), label position (optional, `top`, `bottom`, `left`, or `right`) and label contents (optional).
Note that marks uses square brackets and not a brace to define its contents, similar to an array.

```rs hl_lines="26-30" title="02-scale-marks"
--8<-- "includes/gtk-rs/02-scale-marks/main.blp"
```
