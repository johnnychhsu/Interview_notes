## OS related notes
### Process and threads
A progress is a program in execution. <br />
![Process](./process_components.jpg)
1. Stack : Contains method/function parameters, return address
2. Heap : Dynamically allocated memory to process during its run time.
3. Text : Contains program counter and progress register.
4. Data : Contains global and static variables.

**Process Control Block** <br />
It is a data structure maintained by OS. The PCB is identified by PID. A PCB keeps all the information needed to keep track of a process as listed below : 
1. Process state
2. Process privileges
3. Process ID
4. Pointer : point to parent
5. Program counter : the address of the next instruction to be executed by the process.
6. More  

![Process Image](./process_image.jpg)

**Inter Process Communication (IPC)** <br />
Communication can be of two types : 
1. Between process and its parent
2. Between unrelated process

Different way of IPC : 
1. Pipe
2. Named pipe
3. Shared memory
4. Message queue
5. Semaphore
6. Signal
7. Memory mapping

**Pipe** <br />
It is half duplex, one process can only read or write to a pipe. If we need both, then we need to pipes.
```c
#include<stdio.h>
#include<unistd.h>

int main() {
   int pipefds[2];
   int returnstatus;
   int pid;
   char writemessages[2][20]={"Hi", "Hello"};
   char readmessage[20];
   returnstatus = pipe(pipefds);
   if (returnstatus == -1) {
      printf("Unable to create pipe\n");
      return 1;
   }
   pid = fork();
   
   // Child process
   if (pid == 0) {
      read(pipefds[0], readmessage, sizeof(readmessage));
      printf("Child Process - Reading from pipe – Message 1 is %s\n", readmessage);
      read(pipefds[0], readmessage, sizeof(readmessage));
      printf("Child Process - Reading from pipe – Message 2 is %s\n", readmessage);
   } else { //Parent process
      printf("Parent Process - Writing to pipe - Message 1 is %s\n", writemessages[0]);
      write(pipefds[1], writemessages[0], sizeof(writemessages[0]));
      printf("Parent Process - Writing to pipe - Message 2 is %s\n", writemessages[1]);
      write(pipefds[1], writemessages[1], sizeof(writemessages[1]));
   }
   return 0;
}
```


**Fork()** <br />
Once `fork()` is called, it will return :
1. 0 for child process
2. Child PID for parent process
3. < 0 if error occur
```c
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main() {
   pid_t pid, mypid, myppid;
   pid = getpid();
   printf("Before fork: Process id is %d\n", pid);
   pid = fork();

   if (pid < 0) {
      perror("fork() failure\n");
      return 1;
   }

   // Child process
   if (pid == 0) {
      printf("This is child process\n");
      mypid = getpid();
      myppid = getppid();
      printf("Process id is %d and PPID is %d\n", mypid, myppid);
   } else { // Parent process 
      sleep(2);
      printf("This is parent process\n");
      mypid = getpid();
      myppid = getppid();
      printf("Process id is %d and PPID is %d\n", mypid, myppid);
      printf("Newly created process id or child pid is %d\n", pid);
   }
   return 0;
}
```

**Wait()** <br />
If parent process finish early than child, then the child's parent becomes init process, whose PID is 1.
```c
#include<stdio.h>

int main() {
   int pid;
   int status;
   pid = fork();
   
   // Child process
   if (pid == 0) {
      system("ps -ef");
      sleep(10);
      system("ps -ef");
      return 3; //exit status is 3 from child process
   } else {
      sleep(3);
      wait(&status);
      printf("In parent process: exit status from child is decimal %d, hexa %0x\n", status, status);
   }
   return 0;
}
```

**Orphan process and Zombie process** <br />
1. Orphan process : parent process finish early than child, than init process will become parent of the orphan process
2. Zombie process : child process is finished, but parent process is not ready to clean up the child process.

**Daemon process** <br />
Processes that are not associated with any terminal or shell. Run in the background, usually ends up with 'd', for example, 'sshd'.

**Threads** <br />
Thread is similar to process, thus also called light weight process. However, thread share some resource such as open files and signal, data segment.

Why we need multi-thread programming ? Because it can improve efficiency of program through parallel. Threads operate faster than process because : 
1. Thread creation is much faster.
2. Context switching between threads is much faster.
3. Threads can be terminated easily.
4. Communication between threads is faster.

```cpp
void *myThreadFun(void *vargp) 
{ 
    sleep(1); 
    printf("Printing GeeksQuiz from Thread \n"); 
    return NULL; 
} 
   
int main() 
{ 
    pthread_t thread_id; 
    printf("Before Thread\n"); 
    pthread_create(&thread_id, NULL, myThreadFun, NULL); 
    pthread_join(thread_id, NULL); 
    printf("After Thread\n"); 
    exit(0); 
}
```
 
### Critical Section
Piece of codes that need to be executed atomically, shcu as accessing recourse. A simple solution is as follow : 
```cpp
acquireLock();
process critical section;
releaseLock();
```

Check the codes below : 
```cpp
pthread_t tid[2]; 
int counter; 
  
void* trythis(void *arg) 
{ 
    unsigned long i = 0; 
    counter += 1; 
    printf("\n Job %d has started\n", counter); 
  
    for(i=0; i<(0xFFFFFFFF);i++); 
    printf("\n Job %d has finished\n", counter); 
  
    return NULL; 
} 
  
int main(void) 
{ 
    int i = 0; 
    int error; 
  
    while(i < 2) 
    { 
        error = pthread_create(&(tid[i]), NULL, &trythis, NULL); 
        if (error != 0) 
            printf("\nThread can't be created : [%s]", strerror(error)); 
        i++; 
    } 
  
    pthread_join(tid[0], NULL); 
    pthread_join(tid[1], NULL); 
  
    return 0; 
} 
```

The result might be : 
```command
Job 1 has started
Job 2 has started
Job 2 has finished
Job 2 has finished
```

**Why this happen ?**
Before thread 1 finish, thread 2 might be scheduled, and context switch happen. Thus before thread 1 finish, thread 2 start and modify the global value, thus thread 1 finish with the value set to 2.

**Mutex**

To solve this problem, we can use **Mutex**. It is a lock for critical region, in this case is the `trythis()`.
1. Mutex is a lock that we set before we use shared resource and release after using it.
2. When the lock is set, no other thread can access the lock region. Context switch still happen, but no threads can execute except for the thread has the lock.

Following codes use mutex lock : 
```cpp
pthread_t tid[2]; 
int counter; 
pthread_mutex_t lock; 
  
void* trythis(void *arg) 
{ 
    pthread_mutex_lock(&lock); 
  
    unsigned long i = 0; 
    counter += 1; 
    printf("\n Job %d has started\n", counter); 
  
    for(i=0; i<(0xFFFFFFFF);i++); 
  
    printf("\n Job %d has finished\n", counter); 
  
    pthread_mutex_unlock(&lock); 
  
    return NULL; 
} 
  
int main(void) 
{ 
    int i = 0; 
    int error; 
  
    if (pthread_mutex_init(&lock, NULL) != 0) 
    { 
        printf("\n mutex init has failed\n"); 
        return 1; 
    } 
  
    while(i < 2) 
    { 
        error = pthread_create(&(tid[i]), NULL, &trythis, NULL); 
        if (error != 0) 
            printf("\nThread can't be created :[%s]", strerror(error)); 
        i++; 
    } 
  
    pthread_join(tid[0], NULL); 
    pthread_join(tid[1], NULL); 
    pthread_mutex_destroy(&lock); 

    return 0;
}
```

**Semaphore** <br />
It is a variable. There two kinds of semaphore : 
1. Binary semaphore : 
    It is like mutex. When it is zero, wait. When it is one, operate the critical section.
2. Counter semaphore : 
    There might me multiple units of one resource, thus semaphore can be more than one. Consider following codes : 
    ```cpp
    P(Semaphore s) 
    { 
        s = s - 1; 
        if (s < 0) { 
            // add process to queue 
            block(); 
        } 
    } 
  
    V(Semaphore s) 
    { 
        s = s + 1; 
        if (s >= 0) { 
            // remove process p from queue 
            wakeup(p); 
        } 
    } 
    ```
    When there are no available resource, the process is put into a queue by calling `block()`, wait for the semaphore. Once there are semaphores, the process is resumed by calling `wakeup()`.
    This implementation is more efficient than using a while loop to check.

**The difference between mutex and semaphore**
**Mutex** is a lock mechanism, while semaphore is a signal mechanism. Mutex itself is a lock, it can only owned by a single process or thread at the same time. Also, only the owner can release the lock, this is used to assure atomic operation.

**Semaphore** is a different concept, although the implementation of binary semaphore is similar to mutex. Semaphore can be multiple, thus once there is a room for it, the waiting process can join. 

### Memory Management
**Process Address Space** <br />
The process address space is the set of logical addresses that a process references in its code.
1. Symbolic address <br />
    The addresses used in a source code. The variable names, constants, and instruction labels are the basic elements of the symbolic address space.
2. Relative address <br /> 
    At the time of compilation, a compiler converts symbolic addresses into relative addresses.
3. Physical address <br />
    The loader generates these addresses at the time when a program is loaded into main memory.

**Static & Dynamic Loading** <br />
1. Static loading : 
    If we have to load your program statically, then at the time of compilation, the complete programs will be compiled and linked without leaving any external program or module dependency.
2. Dynamic loading : 
    If we are using dynamic loading, dynamic routines of the library are stored on a disk in relocatable form and are loaded into memory only when they are needed by the program.

**Swapping** <br />
Swapping is a mechanism in which a process can be swapped temporarily out of main memory (or move) to secondary storage (disk) and make that memory available to other processes.
<br />

![Swapping](./process_swapping.jpg)

**Fragmentation** <br />
As precesses are loaded and removed from memory, the free memory space are broken into pieces. These pieces are not continuous thus the left space might be enough, but no continuous space can be fitted for a new progress.
1. External fragmentation : 
    Total memory space is enough to satisfy a request or to reside a process in it, but it is not contiguous, so it cannot be used.
2. Internal fragmentation : 
    Memory block assigned to process is bigger. Some portion of memory is left unused, as it cannot be used by another process.
![Fragmentation](./memory_fragmentation.jpg)

External fragmentation can be solved by memory compaction or shuffle memory contents to place all free memory together in one large block.
<br />

**Paging** <br />
Paging is a memory management technique in which process address space is broken into blocks of the same size called pages. The size of the process is measured in the number of pages. <br />
Similarly, main memory is divided into small fixed-sized blocks of (physical) memory called frames and the size of a frame is kept the same as that of a page to have optimum utilization of the main memory and to avoid external fragmentation. <br />

![Page map](./page_map_table.jpg)
<br />
**Address Translation** <br />
1. Page address is called logical address. 
    `Logical Address = Page number + page offset`
2. Frame address is calledphysical address. 
    `Physical Address = Frame number + page offset`

**Advantages and Disadvantages of Paging** <br />
1. Paging reduces external fragmentation, but still suffer from internal fragmentation.
2. Page table requires extra memory space, so may not be good for a system having small RAM.

**Segmentation** <br />
Segmentation is a memory management technique in which each job is divided into several segments of different sizes, one for each module that contains pieces that perform related functions. Each segment is actually a different logical address space of the program.
<br />
Segmentation memory management works very similar to paging but here segments are of variable-length where as in paging pages are of fixed size.
<br />
![Segmentation map](./segment_map_table.jpg)

**Address Binding** <br />
1. Compile Time : <br />
This allocates a space in memory to the machine code of a computer when the program is compiled to an executable binary file. 
2. Load Time : 
If memory allocation is designated at the time the program is allocated, then no program can ever transfer from one computer to another in its compiled state. This is because the executable code will contain memory allocations that may already be in use by other programs on the new computer. In this instance, the program's logical addresses are not bound to physical addresses until the program is invoked and loaded into memory.
3. Execution Time : 
Execution time address binding usually applies only to variables in programs and is the most common form of binding for scripts, which don't get compiled. In this scenario, the program requests memory space for a variable in a program the first time that variable is encountered during the processing of instructions in the script.

**Demand Paging** <br />
Definition : 
1. Page Fault : If a program references a page which is not in the main memory.
For demand paging, Pages are only loaded when needed. <br />
Advantages :
    1. More efficient use of memory.
    2. Large virtual memory.
Disadvantages : 
    1. Number of tables and the amount of processor overhead for handling page interrupts are greater than in the case of the simple paged management techniques.

**Reference String** <br />
The string of memory references. <br />
For a given page size, we only need to consider the page number. 

**Page Replacement Algorithm** <br />
1. LRU (Least Recently Used)
2. MFU (Most Frequently Used)
3. LFU (Least Frequently Used)
4. Page Buffering

### Scheduler
1. Job queue : all process in the system
2. Ready queue : a set of process reside in the main memory, ready and waiting to be executed
3. IO waiting queue

**Two state process model** <br />
1. Running 
2. Not running
Each entry in a queue is a pointer points to a process. <br />


**Scheduler** <br />
1. Long-Term Scheduler <br />
   Also called job scheduler, it selects process from queue and load them into main memory for execution. The primary objective of job scheduler is to provide a balanced mix of jobs, such as IO bound or processor bound. 
2. Short-Term Scheduler <br />
    Also called CPU scheduler, dispatcher, select process from ready queue to execute.
3. Medium-Term Scheduler <br />
    Part of swapping. It removes process from the memory, because some process might become suspended if it makes IO requests.

**Context Switch** <br />
To store and restore the state or context of a CPU in Process Control Block(PCB), so that a process execution can be resumed from the same point at a later time.

**Schedule Algorithm** <br />
1. First Come First Serve : Non-preemptive.
2. Shortest Job Next : Shortest waiting time, but only for tasks that we know its execution time before enter CPU. Non-preemptive.
3. Priority Schedule : Non-preemptive.
4. Shortest Remaining Time : It's preemptive version of SJN.
5. Round Robin : Preemptive. Each process is provided a fix time to execute, called quantum.
6. Multi-level Queue : Combine with above algorithm.

```command
wait time = Service time - Arrival time
```


### Reference
1. [Memory Management](https://www.tutorialspoint.com/operating_system/os_memory_management.htm)
2. [Virtual Memory](https://www.tutorialspoint.com/operating_system/os_virtual_memory.htm)
