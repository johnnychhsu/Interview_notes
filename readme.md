## Notes for software engineer interview

### TCP/IP
The original OSI 7 layers model describe the function of internet very well, but it is too complicated to program. Hence, TCP/IP is proposed for the real world application, it is easier to program and still describe the internet model well.

TCP/IP is a protocol to enable point-to-point communication. There are too many things to do, thus it is separated into four layers. From top to bottom are : 

1. Application Layer
2. Transport Layer
3. Internet Layer
4. Link Layer

#### Link Layer
Wherer Ethernet protocol functions. The transmit unit is frame, consists of header and data. The length of header is 18 bytes, the length of data is between 46 ~ 1500 bytes. The header contains the source and destination MAC address. Each time a computer wants to send messages, it broadcast to the whole network(self and children).

#### Network Layer
We don't know which sub-network the intetnet card is in from MAC address, thus we needs this layer. IP is here, the header in this layer contains source IP and destination IP.

#### Transport Layer
After we know the IP address, there are many service in a computer, we need to know which service the data belongs to. Here we have the concept Port. The header contains the source port and destination port.
Examples like TCP, UDP.

#### Application Layer
Here we define the type of each application, such as http, mail, ... etc. The header depends on the type of service.

#### UDP & TCP
**UDP**
UDP packet contrain hearder and data. Header contrain port info. The sent order may be different from receive order. UDP don't care whether the reveiver receive or not.

**TCP**
1. Three times handshake : A send seq(x) to B for connection establishment. B reply with OK and seq(y), ack(x+1). x+1 means B reply to A because of reveiving A's message. Then A reply with ack(y+1), seq(z). The connection is established.
2. For data transmition : A send seq(x) with length 1024 bytes, B reply with ack(x+1024).
3. Disconnection : A send message to B says disconnect, B reply with OK. Then B send message to A says disconnect, A reply OK. (A send disconnect, but A can still receive, thus B has to send disconnect also.)
