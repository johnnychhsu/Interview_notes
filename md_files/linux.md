## Linux
### Init system
#### System V
We can use 
```
service --status-all
```
to check running deamon.

#### System d
We can use
```
systemctl list-units --type service
```
to check running deamon.

### /dev/tty
Those device connect to our computer. We can use `2 > /dev/tty` to pass the number to our device.

### /dev/null
We can redirect error message to /dev/null, so that the error message will be missed.
