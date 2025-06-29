[crossterm::event]:     https://docs.rs/crossterm/latest/crossterm/event
[crossterm::terminal]:  https://docs.rs/crossterm/latest/crossterm/terminal

# Crossterm

crossterm::[execute](https://docs.rs/crossterm/latest/crossterm/macro.execute.html) is a macro that executes one or more commands.

??? info "Terminal communications"

    <div class="grid cards" markdown>
    
    -   [**Terminal mode**](https://www.gnu.org/software/mit-scheme/documentation/stable/mit-scheme-ref/Terminal-Mode.html)

        ---

        A port that reads from or writes to a terminal has a terminal mode that is either **cooked** or **raw*; this is independent of the blocking mode.
        A terminal port in cooked mode provides some standard processing, reading from the terminal one line at a time and allowing editing within the line.
        A terminal port in raw mode disables all of that processing, and characters are read from and written to the device directly without any translation or interpretation by the operating system.
        Using raw mode removes certain sensible defaults that are typical to terminal usage, for example removing characters with ++backspace++, processing input on ++enter++, and interpreting ++ctrl+c++ with the terminal driver.

    -   [**Blocking mode**](https://www.gnu.org/software/mit-scheme/documentation/stable/mit-scheme-ref/Blocking-Mode.html)

        ---

        An interactive port is always in one of two modes: **blocking** or **non-blocking**; this is independent of the terminal mode.
        
        If an input port is in blocking mode, attempting to read from it when no input is available will cause Scheme to "block" or suspend itself until input is available.
        If an input port is in non-blocking mode, attempting to read from it when no input is available will cause the reading procedure to return immediately.

        An output port in blocking mode will block if the output device is not ready to accept output.
        In non-blocking mode it will return imediately after performing as much output as the device will allow.

    </div>

The alternate screen is a separate buffer that some terminals provide, distinct from the main screen. 
This allows the content of the original screen to be preserved.

<div class="grid cards" markdown>

-   #### Hello, World!

    ---

    Note that writing text can be done by using the [write](https://doc.rust-lang.org/std/io/trait.Write.html#tymethod.write) method on the stdout handle (so long as std::io::[Write](https://doc.rust-lang.org/std/io/trait.Write.html) is imported and you pass the string as bytes) or using crossterm::[style](https://docs.rs/crossterm/latest/crossterm/style/index.html)::[Print](https://docs.rs/crossterm/latest/crossterm/style/struct.Print.html).


    === "Naive"

        ```rs
        --8<-- "includes/rs/crossterm/hello-world/naive/src/main.rs"
        ```

    === "Centered"


        ```rs
        // Message is centered
        --8<-- "includes/rs/crossterm/hello-world/centered/src/main.rs"
        ```

    === "Border"


        ```rs
        // Message is centered with a magenta border.
        --8<-- "includes/rs/crossterm/hello-world/centered-with-border/src/main.rs"
        ```


-    #### Interactivity

    ---

    Interactivity is by looping over the result of [event][crossterm::event]::[read](https://docs.rs/crossterm/latest/crossterm/event/fn.read.html).

    ```rs
    loop {
        match read()? {
            // Event hooks
        }
    }
    ```

    Non-blocking read, using [event][crossterm::event]::[poll](https://docs.rs/crossterm/latest/crossterm/event/fn.poll.html)

    ```rs
    loop {
        if poll(Duration::from_millis(500))? {
            match read()? {
                // Event hooks
            }
        }
    }
    ```

    [event][crossterm::event]::[Event](https://docs.rs/crossterm/latest/crossterm/event/enum.Event.html) is an enum of various possible events

-   #### Raw mode

    ---




    Raw mode 

    - [terminal][crossterm::terminal]::[enable\_raw\_mode](https://docs.rs/crossterm/latest/crossterm/terminal/fn.enable_raw_mode.html)
    - [terminal][crossterm::terminal]::[disable\_raw\_mode](https://docs.rs/crossterm/latest/crossterm/terminal/fn.disable_raw_mode.html)

</div>


[QueueableCommand](https://docs.rs/crossterm/latest/crossterm/trait.QueueableCommand.html#tymethod.queue) is a trait that implements the **queue** method, which allows commands to be queued on types like std::io::stdout.

This allows the view to be built up procedurally.

[terminal][crossterm::terminal]::[enable\_raw\_mode](https://docs.rs/crossterm/latest/crossterm/terminal/fn.enable_raw_mode.html)