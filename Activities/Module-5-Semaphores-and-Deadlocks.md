# 5-2 Activity: Using Semaphores to Prevent Deadlocks

For this activity, I created a Python program that uses a semaphore to control access to a limited number of shared resources. I used a warehouse example because it made the idea easier for me to understand. The program has six workers, but only three forklifts are available. Each worker is represented by a thread, and the semaphore controls how many workers can use a forklift at the same time.

## Using the Semaphore

I initialized the semaphore with a value of three because the warehouse has three forklifts available. In the program, `threading.Semaphore(3)` means that up to three worker threads can enter the section of code that represents using a forklift. Any additional workers have to wait until one of the three forklifts is released.

Changing the initial semaphore value would directly change how many workers could use forklifts at the same time. If I changed the value from three to one, every worker would wait their turn. If I increased it to six, all six workers could enter at once.

## Deadlock Prevention and Synchronization

Deadlock prevention matters because a program can stop making progress when processes or threads are waiting on resources held by one another. A deadlock can occur when mutual exclusion, hold and wait, no preemption, and circular wait exist at the same time (zyBooks, 2026).

In this program, workers are not allowed to take one forklift and then wait while holding it for another resource. Each worker only needs one forklift, and the semaphore controls access to the available pool.

## Challenges and What I Learned

The biggest challenge was making the synchronization behavior easy to see instead of just making the code run. Adding a short delay gave me enough time to see that only three workers were using forklifts at once while the others waited.

The warehouse example made the semaphore concept easier to understand. A semaphore does not stop workers from doing their jobs. It controls access so more workers do not use a shared resource at the same time than the system can safely support.

## References

Python Software Foundation. (2026). *threading: Thread-based parallelism*. https://docs.python.org/3/library/threading.html

zyBooks. (2026). *Operating systems principles and applications*. Wiley zyBooks.
