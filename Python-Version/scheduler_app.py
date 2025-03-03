#!/usr/bin/env python3
import random
from enum import Enum

MAX_SHIFT_CAPACITY = 2          # At most 2 employees per (day, shift)
MAX_DAYS_PER_EMPLOYEE = 5       # Each employee can work up to 5 days
MIN_EMPLOYEES_REQUIRED = 12     # For guaranteed coverage

class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

class Shift(Enum):
    MORNING = 1
    AFTERNOON = 2
    EVENING = 3

class Employee:
    """Represents a single employee with a name and how many days they've been scheduled."""
    def __init__(self, name: str):
        self.name = name
        self.days_assigned = 0

    def increment_days_assigned(self):
        self.days_assigned += 1

class WeeklySchedule:
    """
    WeeklySchedule structure:
        { Day: { Shift: [Employee, Employee, ... up to 2] } }
    """

    def __init__(self):
        # Initialize the nested dict for each Day, each Shift -> empty list
        self.schedule = {}
        for day in Day:
            self.schedule[day] = {}
            for shift in Shift:
                self.schedule[day][shift] = []

    def count_employees(self, day: Day, shift: Shift) -> int:
        """Return how many employees are assigned to a given (day, shift)."""
        return len(self.schedule[day][shift])

    def assign(self, day: Day, shift: Shift, emp: Employee):
        """Assign an employee to a day-shift (no internal capacity checks)."""
        self.schedule[day][shift].append(emp)

    def print_schedule(self):
        """Print the final schedule in a neat format."""
        print("\n===== FINAL WEEKLY SCHEDULE =====")
        # We'll rely on the natural Day enum order
        for day in Day:
            print(f"\n--- {day.name} ---")
            for shift in Shift:
                emps = self.schedule[day][shift]
                # Collect each assigned employee's name
                if not emps:
                    print(f"  {shift.name}: No one assigned")
                else:
                    names_str = " ".join(e.name for e in emps)
                    print(f"  {shift.name}: {names_str}")


def main():
    # 1) Ask how many employees
    try:
        num_employees = int(input("How many employees do you want to schedule? ").strip())
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    # 1a) Check if we have enough employees to guarantee coverage
    if num_employees < MIN_EMPLOYEES_REQUIRED:
        print(f"\nWARNING: For full 7-day coverage with 2 employees per shift, "
              f"you need at least {MIN_EMPLOYEES_REQUIRED} employees each working "
              f"{MAX_DAYS_PER_EMPLOYEE} days.\nYou only have {num_employees} employees, "
              "so the schedule might be incomplete.\n")
    else:
        print(f"\nGreat! You have {num_employees} employees, which should be enough "
              f"to cover 7 days (2 employees per shift).")

    # 2) Gather employees
    employees = []
    for i in range(num_employees):
        name = input(f"Enter name for Employee #{i+1}: ").strip()
        emp = Employee(name)
        employees.append(emp)

    schedule = WeeklySchedule()

    # 3) For each employee, go day by day, ask user for shift.
    for emp in employees:
        print(f"\n=== Assigning shifts for {emp.name} ===")

        for day in Day:
            if emp.days_assigned >= MAX_DAYS_PER_EMPLOYEE:
                print(f"{emp.name} has already worked {MAX_DAYS_PER_EMPLOYEE} days. "
                      "Skipping remaining days.")
                break  # proceed to next employee

            print(f"\n{emp.name}, pick a shift for {day.name} "
                  "(MORNING/AFTERNOON/EVENING) or leave blank if no preference.\n"
                  "If all shifts are full or you type 'skip', you won't work this day.")

            while True:
                user_input = input("Your choice (or blank for no preference, 'skip' to skip day): ")
                choice = user_input.strip().upper()

                if choice == "SKIP":
                    print(f"Skipping {day.name} for {emp.name}")
                    break  # move on to next day

                # Blank => no preference => pick a random shift that isn't full
                if not choice:
                    available_shifts = []
                    for s in Shift:
                        if schedule.count_employees(day, s) < MAX_SHIFT_CAPACITY:
                            available_shifts.append(s)
                    if not available_shifts:
                        print(f"All shifts are full on {day.name}. No assignment possible.")
                    else:
                        chosen = random.choice(available_shifts)
                        schedule.assign(day, chosen, emp)
                        emp.increment_days_assigned()
                        print(f"{emp.name} assigned to {chosen.name} on {day.name}")
                    break  # done picking for this day

                # If user typed something else, try to parse as Shift
                try:
                    shift_choice = Shift[choice]  # e.g. "MORNING" -> Shift.MORNING
                except KeyError:
                    print("Invalid shift. Type MORNING, AFTERNOON, EVENING, blank, or 'skip'.")
                    continue  # re-prompt

                # Check if that shift is full
                if schedule.count_employees(day, shift_choice) >= MAX_SHIFT_CAPACITY:
                    print("That shift is already full. Pick another or skip.")
                else:
                    # Assign and move on
                    schedule.assign(day, shift_choice, emp)
                    emp.increment_days_assigned()
                    print(f"{emp.name} assigned to {shift_choice.name} on {day.name}")
                    break  # done for this day

    # 4) Print final schedule
    schedule.print_schedule()


if __name__ == "__main__":
    main()
