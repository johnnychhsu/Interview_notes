## Http and Http2
Http is an application-level protocol for distributed hyper-media information system. Some basic features : 
1. Connectionless : Client and server know each other only during current request and response.
2. Media independent : Any type of data can be sent by Http as long as both client and server know how to handle the data content.  
3. Stateless

### Http messages
```command
<Request> | <Response> ; HTTP/1.1 messages
```
Http request and response message format consist of following part : 
1. A start line
2. Header fields followed by CRLF(carriage return '\r' + line feed '\n') indicating the end of line
3. Empty line
4. Message body

**Request message** \n
The start line is like : 
```command
Method Request-URL HTTP-Version CRLF
```
1. Method : GET, POST, PUT, DELETE ...
2. Requested-URL : The resource identifier link, where data we want resides
3. Request header fields : Some other information about the request


