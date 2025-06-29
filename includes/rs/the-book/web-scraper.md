In [chapter 17.1](https://doc.rust-lang.org/stable/book/ch17-01-futures-and-syntax.html) we create an asynchronous tool that fetches the HTML title provided by a website.
We write our first two asynchronous functions which can be chained into a single one.

```rs title="TRPL/70" hl_lines="4"
--8<-- "includes/rs/the-book/70-web-scraper/src/main.rs"
```

As we elaborate this example, first the author notes that Rust async code needs a _runtime_ (also called an _executor_), and any async Rust program has a section that manages the details of executing the asynchronous code.
This is different from most other languages which bundle a runtime.
In fact, Rust offers many different runtimes that offer different advantages.
In these examples, we use `trpl::run` which sets up a runtime that's used to run the future passed in.

In the updated code we can pass in two URLs and see which one completes first.
Because either one of these URLs could potentially finish first, a Result doesn't make sense; rather, we return a new type `trpl::Either`, which is similar to Result in that it has two enums but which avoids the implication that one or the other is a failure.
The wrapped value of the fastest request is returned.

```rs
--8<-- "includes/rs/the-book/71/src/main.rs"
```

Now we examine how to combine threads and futures.
We recall our first example where we count up on two separate threads (1).
{: .annotate }

1.  

    ```rs title="concurrency/01"
    --8<-- "includes/rs/concurrency/01/src/main.rs"
    ```


