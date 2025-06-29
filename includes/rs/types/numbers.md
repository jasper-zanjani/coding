Numbers can be typed by appending the data type to the value itself. Digits can be separated with \_

```rs
let x = 255i8;
let y = 1_024_i16;
```

Because implicit integer conversions are a well-known source of bugs and security holes, conversion must be explicit using the **as** keyword:

```rs
do_something(x as i32);
```

Common mathematical calculations are implemented as methods, which can be called directly on variables or literals or as associated functions of the type:

```rs
let x = (4.5_f64).floor()

let y = 4.0_f64;
let z = y.sqrt();

let a = f64::sqrt(4.0);
```

Common constants can be found in each type's **consts** module, i.e. [std][std]::f32::consts.
Other values like `MIN`, `MAX`, `INFINITY`, `NEG_INFINITY`, and `NAN` (not-a-number) are also implemented as consts.

Integers can be fixed-length or variable-length.
Fixed-size integers can be signed (`i`) or unsigned (`u`) and 8, 16, 32, or 64 bits: i.e. `i8`, `u64` etc.
Variable-size integers can be **pointer-sized signed** `isize` or **pointer-sized unsigned** `usize`, the size of both of which depend on the architecture of the host system.