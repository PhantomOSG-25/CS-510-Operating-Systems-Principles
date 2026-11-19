# Project Two Validation Notes

## Purpose

These notes document how the Python system-monitoring application was validated during development.

## Test Environment

The application was run from a Windows development environment using Python 3.14 and `psutil` 7.2.2.

## Validation Performed

### Disk and File Reporting
- Confirmed `projecttwo.txt` was located when the program was run from the project directory.
- Confirmed total disk space, free disk space, disk usage, file size, file path, modification time, and read/write access were displayed.
- Corrected a Windows-specific path issue by passing the containing directory to `psutil.disk_usage()` instead of the file path itself.

### CPU Reporting
- Confirmed physical and logical CPU core counts were displayed.
- Confirmed current CPU frequency and CPU utilization were returned.
- Confirmed sample process IDs and names were displayed.

### Memory Reporting
- Confirmed total, used, and available physical memory were displayed.
- Confirmed physical-memory utilization and virtual/swap-memory metrics were displayed.

### Threading
- Confirmed two separate threads were created.
- Confirmed each thread called a different function.
- Confirmed thread identifiers were available during execution.
- Confirmed both threads were joined and no longer active afterward.

### Error Handling
- Intentionally triggered a divide-by-zero error.
- Confirmed `ZeroDivisionError` was caught.
- Confirmed the application displayed a clear error message and continued to the `finally` block instead of aborting.

## Result

The completed application ran successfully through all required sections and returned normally after the error-handling demonstration.
