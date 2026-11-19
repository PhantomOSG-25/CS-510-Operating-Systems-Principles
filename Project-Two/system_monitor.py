"""
Class:   CS-510
Author:  Michael Wood
Date:    11/19/2026

Description: This program demonstrates disk, CPU, memory, threading,
             and error-handling concepts using Python and psutil.
"""

import os
import psutil
import sys
import threading
from datetime import datetime


def printBlankLines(lines: int):
    for i in range(lines):
        print("")


def printMsg1(num):
    print("Thread 1 cubed: {}".format(num * num * num))


def printMsg2(num):
    print("Thread 2 squared: {}".format(num * num))


def getFileDiskUsageStatistics() -> None:
    # Display total/free disk space and basic attributes for a sample file.
    print("Getting Disk Statistics")
    file_name = "./projecttwo.txt"

    try:
        file_path = os.path.abspath(file_name)
        directory_path = os.path.dirname(file_path)

        disk_usage = psutil.disk_usage(directory_path)
        file_stats = os.stat(file_path)

        print("Disk Total Space: {:.2f} GB".format(
            disk_usage.total / (1024 ** 3)
        ))
        print("Disk Free Space: {:.2f} GB".format(
            disk_usage.free / (1024 ** 3)
        ))
        print("Disk Usage: {}%".format(disk_usage.percent))

        print("")
        print("File Information")
        print("----------------")
        print("File Name:", os.path.basename(file_path))
        print("File Path:", file_path)
        print("File Size:", file_stats.st_size, "bytes")
        print(
            "Last Modified:",
            datetime.fromtimestamp(file_stats.st_mtime).strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )
        print("Readable:", os.access(file_path, os.R_OK))
        print("Writable:", os.access(file_path, os.W_OK))

    except FileNotFoundError:
        print("Error: The file", file_name, "was not found.")
    except OSError as error:
        print("Disk/File Error:", error)

    printBlankLines(2)


def getMemoryStatistics() -> None:
    # Display total, used, available, and virtual/swap memory statistics.
    print("Getting Memory Statistics")

    memory = psutil.virtual_memory()
    swap = psutil.swap_memory()

    print("Total Memory: {:.2f} GB".format(
        memory.total / (1024 ** 3)
    ))
    print("Used Memory: {:.2f} GB".format(
        memory.used / (1024 ** 3)
    ))
    print("Available Memory: {:.2f} GB".format(
        memory.available / (1024 ** 3)
    ))
    print("Physical Memory Usage: {}%".format(memory.percent))
    print("Virtual/Swap Memory Total: {:.2f} GB".format(
        swap.total / (1024 ** 3)
    ))
    print("Virtual/Swap Memory Used: {:.2f} GB".format(
        swap.used / (1024 ** 3)
    ))
    print("Virtual/Swap Memory Usage: {}%".format(swap.percent))

    printBlankLines(2)


def getCpuStatistics() -> None:
    # Display CPU core count, frequency, utilization, and process information.
    print("Getting CPU Statistics")

    cpu_frequency = psutil.cpu_freq()

    print("Physical CPU Cores:", psutil.cpu_count(logical=False))
    print("Logical CPU Cores:", psutil.cpu_count(logical=True))

    if cpu_frequency is not None:
        print("Current CPU Frequency: {:.2f} MHz".format(
            cpu_frequency.current
        ))

    print("CPU Usage: {}%".format(psutil.cpu_percent(interval=1)))

    print("")
    print("Process Sample")
    print("--------------")

    process_count = 0

    for process in psutil.process_iter(["pid", "name", "cpu_percent"]):
        try:
            print(
                "PID: {} | Name: {} | CPU: {}%".format(
                    process.info["pid"],
                    process.info["name"],
                    process.info["cpu_percent"]
                )
            )

            process_count += 1

            if process_count == 5:
                break

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    printBlankLines(2)


def showThreadingExample() -> None:
    # Create two threads, run different functions, and show their lifecycle.
    print("Demonstrating Threading")

    thread1 = threading.Thread(
        target=printMsg1,
        args=(3,),
        name="CubeThread"
    )

    thread2 = threading.Thread(
        target=printMsg2,
        args=(4,),
        name="SquareThread"
    )

    print("Thread 1 created:", thread1.name)
    print("Thread 2 created:", thread2.name)

    thread1.start()
    thread2.start()

    print("Thread 1 executing with ID:", thread1.ident)
    print("Thread 2 executing with ID:", thread2.ident)

    thread1.join()
    print("Thread 1 destroyed:", not thread1.is_alive())

    thread2.join()
    print("Thread 2 destroyed:", not thread2.is_alive())

    print("Done With Threading!")

    printBlankLines(2)


def showErrorHandling() -> None:
    # Intentionally cause and catch an error so the program does not abort.
    print("Demonstrating Error Handling")

    try:
        res = 10 / 0

    except ZeroDivisionError:
        print("ZeroDivisionError: You can't divide by zero!")

    except MemoryError:
        print("MemoryError: The system ran out of available memory.")

    else:
        print("Result is", res)

    finally:
        print("Execution complete. The application handled the error.")

    printBlankLines(2)


def main() -> int:
    print("Starting Program")
    print("=============================")

    getFileDiskUsageStatistics()
    getCpuStatistics()
    getMemoryStatistics()
    showThreadingExample()
    showErrorHandling()

    return 0


if __name__ == '__main__':
    sys.exit(main())
