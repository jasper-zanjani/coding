HTTP is a text-based protocol, and a request takes the following format:

-   Each line is concluded by `CRLF`

    -   Request line: method (i.e. `GET`, `POST`, etc.), URI, and HTTP version (i.e. `HTTP/1.1`)

    -   Headers: key-value pairs delimited by colon. 
        Header names are case-insensitive according to the HTTP specification (i.e. `User-Agent`, `Host`, `Accept-Language`, `Connection`, `Content-Type`, etc.)

    -   Empty line

    -   Body (JSON document)



```http title="Example HTTP request"
POST /users HTTP/1.1
User-Agent: curl/7.16.3
Host: www.tutorialspoint.com
Accept-Language: en-us
Connection: Keep-Alive
Content-Type: application/json

{ "firstName": "Tutorials", "lastName": "Point", "email": "Tutorialspoint@example.com" }
```


