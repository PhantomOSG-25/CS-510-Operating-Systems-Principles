# Reflecting on Key Learnings and Future Applications

Looking back over this course, the biggest change for me is that I now see an operating system as a connected system instead of a collection of separate topics. Process scheduling, memory management, file systems, I/O, security, and resource allocation all affect how a computer behaves. That matters because real users do not report that a scheduler is inefficient. They report that the computer is slow, an application freezes, or something does not work.

## Challenges

One of my biggest challenges was moving from understanding a concept to making it work in Python. I can usually read code and follow what it is doing, but deciding how to build a solution is still something I am strengthening. The psutil activities helped because they turned CPU, memory, process, and disk concepts into something I could actually see.

Project Two pushed that further by combining resource monitoring, threading, error handling, and formatted output into one program. I also ran into problems with VS Code, file paths, and getting projecttwo.txt to work correctly. Instead of changing everything at once, I learned to isolate the failing section, read the error, verify what the program was actually doing, make one controlled change, and test again.

## Applying What I Learned

The knowledge I expect to use the most is resource monitoring, process management, memory management, and structured troubleshooting. Those areas fit the technology roles I am pursuing, especially application support, technical support, and systems analysis.

What surprised me most was how much operating-system material connects to work outside traditional software development. I can see some of the same ideas while operating the mini-slitter at Hankook Tire. A production machine and an operating system are obviously different, but both depend on limited resources being managed, work happening in the correct order, and one problem not being allowed to stop everything else.

## Operating System Principles and Best Practices

The assignments gave me several chances to apply the concepts instead of only describing them. The semaphore activity showed how synchronization can control access to limited resources and reduce deadlock risk. The resource-monitoring activities used psutil to inspect real system information. Project Two brought several ideas together by organizing the program into functions, using two threads, handling an intentional exception without crashing, and testing each section as it was completed.

The best practice I want to carry forward is that a working solution should be organized, readable, testable, and able to handle problems. Whether I am debugging Python, supporting an application, or troubleshooting another technical system, I can use the same approach: understand the problem, isolate the failure, verify the facts, make one change, and test again.
