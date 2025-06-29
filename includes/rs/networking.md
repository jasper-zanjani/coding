A _stream_ represents an open connection between client and server.
[`TcpListener`](https://doc.rust-lang.org/stable/std/net/struct.TcpListener.html).[`incoming`](https://doc.rust-lang.org/stable/std/net/struct.TcpListener.html#method.incoming) is an iterator that returns each stream wrapped in Result.

A _connection_ is the name for the full request and response process after the TCP SYN-ACK-SYNACK handshake.

