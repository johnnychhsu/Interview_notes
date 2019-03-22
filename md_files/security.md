## Security issues
### MD5 (Message Digest Algorithm)
1. Variable length data as input, output 128 bits value.
2. There is vulnerabilities, thus should not be used for high security device.
3. Can be used as checksum, to make sure that files haven't be modified by others during tranmitting.

### SHA (Secure Hash Algorithm)
1. SHA 1~3.

### TLS (Transport Layer Security)
1. The connection is private because symmetric cryptography is used to encrypt data transmitted.

Client indicate the server to setup of a TLS connection, for example, https. Once client and server have agreed to use TLS, they negotiated a stateful connection by using a handshaking procedure. The whole procedure is like : 
1. The handshake begins with a cilent connection to a TLS-enabled server requesting connection with supported cipher suites.
2. Server pick a cipher and hash function that it also supports and notifies the client of the decision.
3. The server usually then provide identification in the form of a digital certificate, containing server name and the server's public encryption key.
4. The client confirm the validity of the certificate before proceeding.
5. To generate the session key used for this connection, the client either:
    1. encrypt a random number with the server's public key and sends the results to the server.
    2. use Diffie-Hellman key exchange.

### Symmetric cryptography v.s. Public Key cryptography (Asymmetric)
**Symmetric cryptography** <br />
Both sender and receiver use the same key.
1. Block cipher or stream cipher

**Security issue** <br />
1. Once the unauthorized third party knows the key, they can modify the content and send it again.
2. How to deliver the private key to receiver?

**Asymmetric cryptography** <br />
The public key can be distributed
1. Use different key

**Security issue** <br />
1. Current computer architecture's calculation is based on binary manipulation. Thus it needs lots of lots of time to find the private key given the public key.

### How to prevent DoS?
1. Firewall : Some firewalls are stateful. They not just forward the packets but validates the packets with the client.
2. Switch : Some of the preventions are delayed binding (TCP splicing).
3. Router : Rate limiting.

### DDoS
1. SYN Flooding : Bad clients send multiple SYN to server, the server will send SYN-ACK, then keep waiting for the ACK that will never be sent by the attacker.
