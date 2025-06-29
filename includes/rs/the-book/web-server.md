This very simple example will print a short message whenever a connection is attempted to the specified port.

```rs
--8<-- "includes/rs/the-book/90-web-server/src/main.rs"
```

Adding a BufReader to read each request stream.
Each nonempty line of the incoming HTTP request (1) is unwrapped and collected into a vector which is then displayed.
{: .annotate }

1.  

    --8<-- "includes/rs/http-request.md"

```rs
--8<-- "includes/rs/the-book/91/src/main.rs"
```

Send back a successful HTTP response to prevent the error about an empty response.

```rs hl_lines="24 26"
--8<-- "includes/rs/the-book/92/src/main.rs"
```

Implement file reading with `read_to_string` in order to return a HTML file.

```rs hl_lines="24-26 28-29"
--8<-- "includes/rs/the-book/93/src/main.rs"
```

Implementing 404 error page.

```rs hl_lines="29-39"
--8<-- "includes/rs/the-book/94/src/main.rs"
```

Refactoring to reduce repetitiveness:

```rs hl_lines="20-24"
--8<-- "includes/rs/the-book/95/src/main.rs"
```

Changing flow control to match statement, and incorporating `sleep` to simulate slow response

```rs
```
