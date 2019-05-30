## System Design

### Overview
#### Some basic factors
1. Availability
    1. The uptime of a website is important. It is directly related to revenue. Thus it is important to design a system that can be constantly available and resilient to failure.
2. Performance
    1. High throughput, low latency.
3. Reliability 
    1. A request to data will consistently return the same data.
4. Scalability
5. Manageability
    1. Easy to maintain, operate, upgrade.
6. Cost

When it comes to system design, there are some things we should consider : what are the right pieces, how these pieces fit together, what are the right trade-off, etc.

#### Example : Image hosting application
#### Services
We can decouple the functionality and think about each part of the system as its own service with a clearly defined interface.

#### Cache
1. Each sevice node has a local cache. But because the cache is local, this may lead to cache miss.
2. Thus, we can use global cache or distribute cache.

#### Proxy
1. collapsed forwarding. 
2. Can also collapsed data. Utilize data locality.

#### Index
1. Index for file retrieval
2. Also we can use reverse index. For example, words as key, books as value.

#### Load balancer
1. Need to take care of problems like user-session-specific data.
2. The scheduling includes random picks a node, round robin, etc. Be careful of diagnosis cumbersome. Because one node might be high load instead of broken, but the load balancer will remove this node from its candidate pool.

### How to design google doc?
First dividing the big system into smaller components.

1. File storage
2. Online editing and formatting
3. Collaboration
4. Access control

**Concurrency control** <br />
1. Operational transformation.

### How to design twitter?


### Network @ Large


### Some Terms
**Thundering herd problem** <br />
When a large number of processes waiting for an event are awaken when the event occurs, but only one process is able to proceed at a time.

### Evolvable API design
1. [Evolvable API design](https://levelup.gitconnected.com/to-create-an-evolvable-api-stop-thinking-about-urls-2ad8b4cc208e)
Consider the state transition between client and server, we can first imagine how client will interact with you in the real life, then design the API like that.

### Reference
1. [Google doc design](http://blog.gainlo.co/index.php/2016/03/22/system-design-interview-question-how-to-design-google-docs/)
2. [HighScalability.com](http://highscalability.com/)
3. [Facebook network at large](https://code.fb.com/networking-traffic/networking-scale-may-2016-recap/)
4. [Scalable web architecture](http://www.aosabook.org/en/distsys.html)
