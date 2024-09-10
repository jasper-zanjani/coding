[The Rust Rand Book](https://rust-random.github.io/book/)

Use rand::[thread\_rng](https://docs.rs/rand/latest/rand/fn.thread_rng.html) to create a [thread-local random number generator](https://docs.rs/rand/latest/rand/rngs/struct.ThreadRng.html)

```rs
// random integer using ThreadRng
let mut rng = rand::thread_rng();

let x: u8 = rng.gen();

// random integer from range
let y: u8 = rng.gen_range(0..20);
```

```rs title="Random sampling"
--8<-- "includes/rs/sampling/src/main.rs"
```

The rand::[random](https://docs.rs/rand/latest/rand/fn.random.html) function is in fact a shortcut to `thread_rng().gen()`

```rs
// generate a boolean
let randbool = rand::random();

// random unicode character
let randchar = rand::random::<char>();

// random integer
let randint = random::<u8>();
```