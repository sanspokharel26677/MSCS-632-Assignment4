# MSCS-632-Assignment4

---

### **README for Python Implementation** (`README_Python.md`)

# Employee Shift Scheduler - Python Implementation

## Overview

The **Employee Shift Scheduler** is a Python-based CLI application that efficiently assigns employees to shifts across a week. The program ensures:

- Each employee can work **up to 5 days**.
- Each shift (Morning, Afternoon, Evening) has **at most 2 employees**.
- The total number of employees is at least **12** to ensure full shift coverage.
- Employees can **pick their shifts**, or get **randomly assigned** if left blank.
- **Validation ensures shifts are not overbooked**.
- A **neatly formatted weekly schedule** is generated at the end.

## Features

- **Interactive CLI** for scheduling.
- **Automatic conflict resolution** (no shift overbooking).
- **Random shift assignment** when employees don’t provide preferences.
- **At least 12 employees** needed for full coverage.
- **Clear and structured output**.

## Requirements

- Python **3.x**
- Works on Windows, macOS, and Linux

## Installation & Running the Program

### **Step 1: Install Python (if not installed)**
Ensure Python 3 is installed:
python3 --version
If not installed, download it from Python.org

### **Step 2: Run the program **.
python3 scheduler_app.py

## Usage

    1.    Enter the number of employees (must be at least 12 for full coverage).
    2.    Enter the name of each employee.
    3.    Assign shifts interactively:
    •    Employees pick their preferred shifts.
    •    If a shift is full, they must pick another.
    •    If they leave it blank, a random shift is assigned.
    4.    Final schedule is displayed.
    
## Example Output

How many employees do you want to schedule? 12
Enter name for Employee #1: Alice
Enter name for Employee #2: Bob
...

=== Assigning shifts for Alice ===
Alice, pick a shift for MONDAY (MORNING/AFTERNOON/EVENING) or leave blank if no preference.
Your choice: MORNING
Alice assigned to MORNING on MONDAY

...

===== FINAL WEEKLY SCHEDULE =====
--- MONDAY ---
  MORNING: Alice, Bob
  AFTERNOON: John, David
  EVENING: Eve, Kevin

...

## Notes

    •    If fewer than 12 employees are provided, a warning is displayed.
    •    Each employee can work up to 5 days.
    •    Employees cannot work multiple shifts in a single day.

## Licnese
This project is open-source and can be modified freely.



