# Python Security Tools

This folder contains small Python scripts I wrote to practice security automation and log analysis.  
The goal is to show that I can read, write, and modify simple Python tools that help with basic security tasks.

## Project 1 – Simple log filter

Description:
- Reads a log file line by line.
- Looks for suspicious keywords (for example: "error", "fail", "denied", "invalid").
- Prints only the matching lines, so it is easier to see potential issues.

Skills practiced:
- Working with files in Python.
- Basic string matching and filtering.
- Writing simple, reusable command-line tools.

## How to run

Example usage:

```bash
python log_filter.py sample.log
```

This will:
- Read `sample.log`.
- Print only the lines that contain keywords like "error", "fail", "denied", "invalid", or "warning".
