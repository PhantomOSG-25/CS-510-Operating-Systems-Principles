# Project Two Documentation: OS Performance and Optimization Simulator

For Project Two, I built a Python system-monitoring application that reports disk, CPU, memory, process, and threading information and demonstrates fault handling. I think of it like a dashboard: before trying to optimize a system, I need to see where the resources are going. The psutil module makes that possible by providing direct access to operating-system resource statistics (psutil, 2026).

## Effectiveness of Algorithmic Optimizations

The main optimization approach is to keep each task separate, collect only the information needed, and handle failures without stopping the program. Disk, CPU, memory, threading, and error handling are each placed in their own function, which makes the application easier to test and maintain.

The threading section starts two threads and uses `join()` so both tasks complete before the program continues. The divide-by-zero test also proves that the program can catch a fault, explain it, and still finish normally instead of crashing.

## OS Performance Metrics

My successful test run reported 8 physical CPU cores, 16 logical cores, about 4.1 GHz CPU frequency, and 16.9% CPU utilization. It also showed 31.56 GB of total memory, 15.95 GB used, and 15.61 GB available. Disk statistics showed 930.43 GB total and 707.87 GB free.

These measurements help identify whether CPU, memory, or storage is becoming the limiting resource.

## Memory Management and Scheduling

For memory management, I used a monitoring-based approach. The application reports physical memory and virtual or swap usage instead of trying to force memory allocation itself. If available memory drops or swap usage rises, that is a warning that workloads may need to be reduced or redistributed.

For scheduling, two Python threads execute different functions while the operating system handles the actual scheduling. The program uses `start()` and `join()` to control the work and make sure both threads finish before moving on.

## Improving System Security and Stability

The program improves stability by monitoring resource pressure and by avoiding unnecessary system changes. It reads statistics but does not terminate processes, change security settings, or alter operating-system configuration. Error handling adds another layer of protection because expected faults can be caught instead of causing an application failure.

## Resource Allocation

The resource-allocation strategy is intentionally lightweight. CPU usage is sampled for one second, only a small process sample is displayed, and the threading demonstration uses two short-lived threads. This keeps monitoring overhead low while still showing how the operating system is using its resources.

## References

psutil. (2026). *psutil documentation*. https://psutil.readthedocs.io/stable/

Python Software Foundation. (2026). *threading - Thread-based parallelism*. Python 3.14 documentation. https://docs.python.org/3.14/library/threading.html
