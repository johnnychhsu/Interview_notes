## System Design
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