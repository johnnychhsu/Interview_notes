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

### Http Header
HTTP header fields provide required imformation about the request or response, or about the object sent in the message body. There are four types of header : 
1. General header
2. Client request header
3. Server response header
4. Entity header

### Http Cache
It is used to improve the performance. Cache-control header allows server or client to transmit a variety of directive in either request or response. <br />
For example, in request cache header, we can use no-store to tell the server that the cache should not store anything about the client request and server response.
<br />
In response cache header, we can use public to indicate that this response can be cached by any cache.

### What happen after type in something in browser and hit enter?
The browser will first check the DNS cache in your browser. If there is no such entry, then it will check the OS DNS server. If still not, it will start to check the router cache. If still not, it will check ISP DNS. <br />
If the requested URL is not in the ISP DNS, it will initiates a DNS query to find the IP address of the server that host the URl. <br />
The DNS query will start to search multiple DNS server on the Internet till it finds the correct IP address. 
![DNS query search](./DNS.png) <br />
These requests are sent using small data packet which contains information such the content of the request and IP address it is destined for. These packets travel through many network equipments, which use routing table to figure out which way is the fastest way for the packets to its' destination. <br />
After we have the IP address, the browser establish a connection using TCP/IP. Then the browser will transfer data using HTTP. <br />
The detail checks the TCP/IP pages.

### Cookie and Session
1. Cookie is in saved in local browser, which is client side.
2. Session is save ion server. Request contain session ID, server will check whether there is a matching session for the request.

### HTTP2
Decrease latency to improve page load speed in web browser by considering : 
1. data compressed of http header
2. pipelining of requests
3. multiplexing multiple requests over a single TCP connection
4. Server push

**Difference between Http 2 and Http 1.x** <br />
1. Http 2 allow server to 'push' content. That is, allow server to respond with data more than the client requests. This allow server to supply data it knows a web browser will need to render a page without waiting for the browser to examine the first response, and without the overhead of an additional request cycle.
2. Avoid head-of-line blocking by multiplexing: When the first packets is block in a FIFO buffer, the rest packets behind it are all block. 

### Reference
[What happen when type in google.com in browser?](https://medium.com/@maneesha.wijesinghe1/what-happens-when-you-type-an-url-in-the-browser-and-press-enter-bb0aa2449c1a)
