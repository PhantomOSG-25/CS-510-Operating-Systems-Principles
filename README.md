# CS-510 Operating Systems Principles

This repository contains selected coursework and project artifacts from **CS-510: Operating Systems Principles** at Southern New Hampshire University.

The course focused on how operating systems manage processes, threads, memory, storage, I/O, synchronization, security, and system resources. My goal with this repository is to show both the concepts I learned and how I applied them through Python-based system monitoring, synchronization exercises, operating-system evaluation, and reflective technical writing.

## Skills Demonstrated

- Python system monitoring with `psutil`
- CPU, memory, disk, and process inspection
- Multithreading and concurrency
- Semaphores, synchronization, and deadlock prevention
- Exception handling and fault tolerance
- Virtual memory and resource-management concepts
- File-system and I/O management
- Operating-system security, reliability, and performance evaluation
- Incremental debugging and validation
- Technical documentation and analysis

## Repository Structure

### `Journals/`
Course reflections connecting operating-system concepts to practical troubleshooting and professional applications.

### `Activities/`
Selected hands-on coursework, including synchronization and semaphore-based deadlock prevention.

### `Project-One/`
An operating-system recommendation report evaluating an enterprise Linux platform for a fictional financial-technology environment. The report focuses on security, stability, resource management, reliability, distributed environments, and performance.

### `Project-Two/`
A Python system-monitoring application that collects and displays operating-system metrics and demonstrates threading and exception handling.

The application includes:

- Disk total/free space and file attributes
- CPU core count, frequency, utilization, and process information
- Physical and virtual/swap memory statistics
- Two-thread concurrency demonstration
- Intentional error generation and exception handling

## Running Project Two

Requirements:

```bash
pip install psutil
```

Run the program from the `Project-Two` directory so that `projecttwo.txt` is available to the application:

```bash
python system_monitor.py
```

## Validation and Testing

Project Two was tested incrementally instead of waiting until the full application was complete.

Validation included:

1. Running the program from the project directory and confirming that `projecttwo.txt` was found.
2. Verifying that disk statistics and file attributes were displayed without path errors.
3. Confirming CPU core counts, utilization, and process data were returned by `psutil`.
4. Confirming physical and virtual/swap memory statistics were displayed.
5. Verifying both threads were created, executed, joined, and reported as no longer active.
6. Triggering a `ZeroDivisionError` intentionally and confirming the exception was caught without terminating the application.
7. Confirming the program completed normally after the handled error.

During testing, a Windows path issue was isolated to passing a file path directly to `psutil.disk_usage()`. The solution was to resolve the file's absolute path, extract its directory, and pass the directory path to `psutil.disk_usage()`. This reinforced an important troubleshooting practice: isolate the failing component, verify the actual input, make one controlled correction, and retest.

## What I Took From the Course

The most useful lesson from CS-510 was learning to look at an operating system as a connected system rather than a collection of separate topics. CPU scheduling, memory, processes, storage, I/O, concurrency, and security all affect how applications behave.

That perspective is especially useful for the technical-support, application-support, systems, and implementation roles I am pursuing because users rarely describe a problem in operating-system terms. They report symptoms. Understanding the system underneath the application gives me more places to investigate and a more structured way to troubleshoot.

## Author

**Michael Wood**  
B.S. Computer Science, Software Engineering Concentration  
Graduate student, Computer Science
