The socket module is Python's standard interface for the transport layer.
Sockets can be classified by family and type:

<div class="grid cards" markdown>

-   **Family** 

    - `AF_INET` Internet
    - `AF_UNIX` UNIX sockets

-   **Type**

    - `SOCK_STREAM` TCP
    - `SOCK_DGRAM` UDP

</div>

These enum values are required upon initialization of a socket object:

```py
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

<div class="grid cards" markdown>


```py title="TCP server"
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
```

```py title="TCP client"
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
```


```py title="UDP server"
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST,PORT))
```

```py title="UDP client"
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto("Hello, world!".encode(), (HOST,PORT))
```

</div>

```py
# Define port on which to listen for connections.
serversocket.bind(('localhost',80))

# Connect to a remote socket in one direction
client_socket.connect(('www.packtpub.com',80))

# Convert a domain name into IPv4 address
socket.gethostbyname('packtpub.com') # '83.166.169.231'

# Defaults to **localhost** with no arguments
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))

# Get protocol name from port number
socket.getservbyport(80) # 'http'

# Listen to a maximum of 10 connections
serversocket.listen(10)

# Receive bytestream from server
msg = s.recv(1024)
print(msg.decode('utf-8'))
```


??? info "Resources"

    [Sockets tutorial](https://youtu.be/Lbfe3-v7yE0)
