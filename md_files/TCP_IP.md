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

#### TCP congestion control
To avoid network congestion, TCP has congestion control strategy. <br />
For each connection, TCP maintain a congestion window, limiting the total number of unacknowledged packets that may be in the trainsit end-to-end. TCP use a mechanism called slow start to increase the congestion window after a connection is initialized or a time-out. <br />
Although this is similar to sliding window of TCP flow control, actually they are different. 

#### UDP & TCP
**UDP**
UDP packet contrain hearder and data. Header contrain port info. The sent order may be different from receive order. UDP don't care whether the reveiver receive or not.

**TCP**
1. Three times handshake : A send seq(x) to B for connection establishment. B reply with OK and seq(y), ack(x+1). x+1 means B reply to A because of reveiving A's message. Then A reply with ack(y+1), seq(z). The connection is established.
2. For data transmition : A send seq(x) with length 1024 bytes, B reply with ack(x+1024).
3. Disconnection : A send message to B says disconnect, B reply with OK. Then B send message to A says disconnect, A reply OK. (A send disconnect, but A can still receive, thus B has to send disconnect also.)

### IPv4
Take data segment from TCP and divides it into packets. Each packet contains header and data.
![IP Header](../pic/ip_header.jpg)

**Mask** <br />
We can use mask to distinguish the network address and host address. Just do `and` operation to the address, the left non-zero is the network address.


### TCP details
TCP can be described as a sliding window protocol with cumulative positive acknowledgement.
#### Window of packets and sliding window
This mechanism can handle problems like how many packets are sent, how many are ACK, how many are still waiting.

#### Variable window : flow control and congestion control
1. Rate based flow control : sender is limited under a sending rate
2. Window based flow control : receiver will send window update to sender to update the window size

Above can control the transfer rate between sender and receiver. But what if the routers between senders and receivers have limited memory? This might cause packets lost.

Congestion control will take this into consideration. The window size should be update by not only explicit update from receiver, but also guess the network condition, and change the window size accordingly.

#### Retransmission rate
1. Round trip time estimation : usually the sample mean of a collection of RTTs.

#### Valid tcp packet
Only need to know the 4-tuple contining two end IP address and port, with valid sequence number within the sliding window are sufficient to ba a valid packet.

#### Interactive and bulk data
Both use the same packet format and TCP protocol. However, the time requirement is different. Think about online game, we need to react to users' action immediately. If we need to wait for ACK for every operation such as mouse clicking, this will harm the user experience.

We can disable Nagle algorithm to speed up for interactive transfer.

#### Congestion
Because the routers has limited buffer, thus if the receiving rate is higher than sending rate, there will be congestion.

A packet loss can be though as congestion. TCP need to know whether a packet loss is due to congestion or transmission error.

The window size is determined by `min(congestion window, advertised window)`. These two are estimmatd from network condition and from receiver.

Self-clock. Once the sender receives a ACK from receiver, it knows that it send another packet out.

Usually TCP begins a connection with slow start, eventually drops a packet, then settles into steady-state operation using congestion avoidance algorithn. Once the slow start threshold is established, TCP will run congestion avoidance algorithm.

SMSS (Sender Maximum Segment Size)
