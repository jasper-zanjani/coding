# Overview

<!-- 

Learning Rust has been exceptionally challenging for me, at least partly because the examples given
by teachers and books are very difficult. It seems that most people who take an interest in Rust 
already have familiarity with computer science topics that seem bizarre to me.

This is especially apparent in the Smart Pointers chapter of Klabnik (Chapter 15) where the section
on Rc<T> uses a scenario that assumes familiarity with "cons lists" from the Lisp programming lang-
uage. This is another unfortunate case of too many "dependencies" in the teaching material for a
technical topic. Klabnik also doesn't touch on Cells specifically but launches into RefCell<T>s and
uses the same cons list scenario he began in the beginning of the chapter. Unfortunately this is of 
very little use to anyone who is not familiar with that topic.

The Starships scenario provides a great case study on interior mutability. An immutable Starship
can be made partially mutable by changing a field to a Cell<T> type. This allows the crew complement
to be updated, which is a very intuitive and easy to understand application.


Cursive makes for an interesting use-case in learning closure semantics. This is especially true
when it comes to how some widgets do not implement the Nameable trait. This forces any retrieval
of the selection a user made to take place in a closure. Not only that, the `move` keyword must
be used because it must necessarily capture the environment of the current scope.

- Lifetime parameters and implementing std Traits was key in extending the Cursive Starships application.


Interactively discussing code may be best done using by pasting code into the styling generator here:
https://romannurik.github.io/SlidesCodeHighlighter/

Then pasting the output into Google Slides.

-->

> Rust's distinguishing feature as a programming language is its ability to prevent invalid data access at compile time.
> 
> &mdash;Tim McNamara

Rust offers **zero-cost abstractions**, where using the abstraction imposes no additional runtime overhead.

#### Iterators

--8<-- "includes/rs/Topics/Iterators.md"


## Tasks

<div class="grid cards" markdown>

-   #### Hello, World!

    === "std"

        === "Naive"

            ```rs
            --8<-- "includes/rs/hello-world/hello-world-naive/src/main.rs"
            ```

        === "Parameterized"

            ```rs
            --8<-- "includes/rs/hello-world/hello-world-parameterized1/src/main.rs"
            ```

        === "Interactive"

            ```rs
            --8<-- "includes/rs/hello-world/hello-world-interactive/src/main.rs"
            ```

    === "clap"

        === "Single argument"

            ```rs
            --8<-- "includes/rs/hello-world/hello-world-clap/src/main.rs"
            ```

        === "Multiple arguments"

            ```rs
            --8<-- "includes/rs/hello-world/hello-world-append/src/main.rs"
            ```

        === "Delimited argument"

            ```rs
            --8<-- "includes/rs/hello-world/hello-world-delimiter/src/main.rs"
            ```

    === "structopt"

        ```rs
        --8<-- "includes/rs/hello-world/hello-world-structopt/src/main.rs"
        ```

-   #### Triangle number

    ---

    $$
    \sum_{k=1}^{n}k = 1 + 2 + .. + n
    $$

    === "Naive"

        ```rs
        --8<-- "includes/rs/triangle-number/triangle-number-naive/src/lib.rs"
        ```

    === "Closure"

        ```rs
        --8<-- "includes/rs/triangle-number/triangle-number-fold/src/lib.rs"
        ```


-   #### Handling command-line arguments

    ---

    [std][std]::[env][std::env]::[args()](https://doc.rust-lang.org/std/env/fn.args.html) exposes an iterator that returns each command-line argument used to invoke the executable.
    

    ```rs
    --8<-- "includes/rs/hello-world/hello-world-parameterized0/src/main.rs"
    ```

    Here, if the first argument is "greet", it is interpreted as a subcommand that changes the Hello, World! message.

    ```rs
    --8<-- "includes/rs/hello-world/hello-world-parameterized1/src/main.rs"
    ```

    args() yields Strings, so it has to be cast to a string slice in the match statement because match arms can't have function calls.
    Note that looping through the iterator requires the first item to be skipped.

    ```rs
    --8<-- "includes/rs/cat/cat-single-arg/src/main.rs"
    ```


-   #### File handling

    ---

    There are [various ways of accessing files](https://www.youtube.com/watch?v=jk5on2Rrwf4) in Rust:

    - [std][std]::[fs][std::fs]::[read_to_string](https://doc.rust-lang.org/stable/std/fs/fn.read_to_string.html) reads directly to string and is convenient, but can only handle UTF-8 encoded text.
    
    - std::fs::[read](https://doc.rust-lang.org/stable/std/fs/fn.read.html) returns a byte vector which can then be reencoded into text
    
    - std::[io][std::io]::[BufReader](https://doc.rust-lang.org/std/io/struct.BufReader.html) adds buffering to any reader and is considered superior to read where larger, more infrequent reads optimize performance.
    Filehandles and std::io::[stdin](https://doc.rust-lang.org/std/io/fn.stdin.html) both implement the BufRead trait.
    
    - BufReader.bytes() is similar to allows bytewise control of file contents

    === "read\_to\_string"

        ```rs hl_lines="11"
        --8<-- "includes/rs/cat/cat-clap/src/main.rs"
        ```

    === "Byte vector"

        ```rs hl_lines="11 12"
        --8<-- "includes/rs/cat/cat-byte-vector/src/main.rs"
        ```

    === "Linewise"

        ```rs
        --8<-- "includes/rs/cat/cat-bufreader-lines/src/main.rs"
        ```

    === "Bytewise"

        ```rs
        --8<-- "includes/rs/cat/cat-bufreader-bytes/src/main.rs"
        ```


-   #### Directories

    ---


    ```rs
    --8<-- "includes/rs/dir/rdir-clap/src/main.rs"
    ```

-   #### Random sampling

    ---

    ```rs
    --8<-- "includes/rs/sampling/src/main.rs"
    ```


-   #### Rust versions

    ---

    [Rust 2021](https://doc.rust-lang.org/edition-guide/rust-2021/index.html)

    - A [migration lint](https://doc.rust-lang.org/edition-guide/rust-2021/reserving-syntax.html#migration) was introduced as part of the 2021 edition which aims to automate migration of Rust 2018 code bases.

    [Rust 2018](https://doc.rust-lang.org/edition-guide/rust-2018/index.html)
    
    - [`extern crate`](https://doc.rust-lang.org/edition-guide/rust-2018/path-changes.html#no-more-extern-crate) became unnecessary in most cases

-   #### Future research

    ---

    Watchlist:

    - [BTC price GUI](https://www.youtube.com/watch?v=z01c1hOr-kk&t=98s)
    - [Tim McNamara on Clap](https://www.youtube.com/watch?v=Y-LTWNciEks)
    - [std::fs](https://www.youtube.com/watch?v=0H3pg_pjyRE)

    Potential projects:

    - [COSMIC desktop environment](https://github.com/pop-os/cosmic) for Pop!_OS, in alpha development
    - [guilhermeprokisch/smd utility](https://github.com/guilhermeprokisch/smd) 
    - [Tetrs terminal game](https://github.com/Strophox/tetrs) 
    - [Linux kernel crate](https://www.kernel.org/doc/rustdoc/latest/kernel/)
        - [Setting up an environment for writing Linux kernel modules in Rust](https://www.youtube.com/watch?v=tPs1uRqOnlk)
        - [Writing Linux kernel modules in Rust](https://www.youtube.com/watch?v=-l-8WrGHEGI)
        - [Writing Linux kernel modules in safe Rust](https://www.youtube.com/watch?v=RyY01fRyGhM)
    - ratatui
        - [Tutorials](https://ratatui.rs/tutorials/)
        - [Rich terminal interfaces with ratatui](https://www.youtube.com/watch?v=pgFCjtwPBYI&pp=ygUMcnVzdCByYXRhdHVp)
        - [Introducing ratatui: a Rust library to cook up terminal user interfaces](https://www.youtube.com/watch?v=NU0q6NOLJ20&pp=ygUMcnVzdCByYXRhdHVp)


-   #### [std][std]

    ---

    - [**fmt**][std::fmt]:          [format](https://doc.rust-lang.org/std/fmt/fn.format.html)
    - [**fs**][std::fs]:            [read_to_string](https://doc.rust-lang.org/stable/std/fs/fn.read_to_string.html)  &bull;  [read](https://doc.rust-lang.org/stable/std/fs/fn.read.html)
    - [**io**][std::io]:            [stdin](https://doc.rust-lang.org/std/io/fn.stdin.html) [stdout](https://doc.rust-lang.org/stable/std/io/fn.stdout.html) [flush](https://doc.rust-lang.org/std/io/trait.Write.html#tymethod.flush) [Write](https://doc.rust-lang.org/std/io/trait.Write.html) 
    - [**iter**][std::iter]:        [Iterator](https://doc.rust-lang.org/stable/std/iter/trait.Iterator.html)
    - [**net**][std::net] implements the [Berkeley sockets](https://en.wikipedia.org/wiki/Berkeley_sockets) API
    - [**path**][std::path]:        [Path](https://doc.rust-lang.org/stable/std/path/struct.Path.html) &bull; [PathBuf](https://doc.rust-lang.org/stable/std/path/struct.PathBuf.html)
    - [**thread**][std::thread]:    [sleep](https://doc.rust-lang.org/stable/std/thread/fn.sleep.html)
    - [**time**][std::time]:        [Duration](https://doc.rust-lang.org/stable/std/time/struct.Duration.html)

    - Macros: [format!](https://doc.rust-lang.org/std/macro.format.html)


</div>



--8<-- "includes/rs/links.md"
