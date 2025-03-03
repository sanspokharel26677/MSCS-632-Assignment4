# MSCS-632-Assignment4

# Employee Shift Scheduler - Java Implementation

## Overview

The **Employee Shift Scheduler** is a command-line application written in **Java** that allows businesses to efficiently schedule employees for shifts throughout the week. The program ensures that:

- Each employee can work **up to 5 days**.
- Each shift (Morning, Afternoon, Evening) has **at most 2 employees**.
- The total number of employees is at least **12** to guarantee full shift coverage.
- Employees can choose their preferred shifts, and the program ensures no conflicts.
- If an employee leaves their preference blank, they are assigned randomly to an available shift.
- The system prevents over-scheduling beyond the allowed limits.

## Features

- Interactive **CLI-based** scheduling.
- **Validation checks** to prevent over-scheduling.
- **Random assignment** for employees who don't provide shift preferences.
- Ensures a **minimum of 12 employees** for full shift coverage.
- **Neatly formatted** weekly schedule output.

## Requirements

- Java **JDK 8+**
- A terminal or command prompt

## Installation & Running the Program

### Step 1: Compile the Code
javac SchedulerApp.java

###  Run the program
java SchedulerApp

## Usage

    1.    Enter the number of employees (must be at least 12 for full coverage).
    2.    Enter the name of each employee.
    3.    Assign shifts interactively:
    •    Employees choose their preferred shifts for each day.
    •    If a shift is full, they are prompted to pick another.
    •    If they leave it blank, they are randomly assigned.
    4.    View the final schedule after all employees have been assigned.
    
### Example output

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

    •    If fewer than 12 employees are provided, a warning is displayed, indicating possible incomplete shift coverage.
    •    Each employee can work up to 5 days.
    •    Employees cannot work multiple shifts in a single day.

## License
This project is open-source and can be modified freely
