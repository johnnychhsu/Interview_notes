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

**Request message** <br />
The start line is like : 
```command
Method Request-URL HTTP-Version CRLF
```
1. Method : GET, POST, PUT, DELETE ...
2. Requested-URL : The resource identifier link, where data we want resides
3. Request header fields : Some other information about the request

**Response message** <br />
The status line is like : 
```command
HTTP-Version Status-code Reason-Phrase CRLF
```
1. Status code : 
    1. 1XX : Informational, received and processing
    2. 2XX : Success, received and accepted
    3. 3XX : Redirection, further action must be taken in order to complete the request
    4. 4XX : Client Error, the request contains incorrect syntax or cannot be fulfilled
    5. 5XX : Server Error, server failed to fulfill an apparently valid request

### Http method
Method are case-sensetive, should always and only be upper-case : 
1. GET : To receive data from the requested URL
2. HEAD : Similar to GET, but no entity-body (no content except header)
3. POST : To send data to server
4. PUT : To request server to store the included entity-body at a location specified by the given URL
5. DELETE : To request server to delete a file specified by the given URL
6. TRACE : To echo the content of a request from server back to the requester used for debugging



