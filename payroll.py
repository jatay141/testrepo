"""
Program: Payroll Calculation
Author: Austin Taylor
Date: 2025-04-03
Description: This program reads a payroll file containing employee names, hourly wages, and hours worked,
             calculates the wages paid, and displays the results in a formatted table.
             It handles errors such as file not found, invalid numeric format, and incorrect line structure.

"""


filename = input("Enter the payroll filename: ")

try:
    payroll_file = open(filename, 'r')
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    exit()

print(f"{'Employee Name':<15} {'Hours Worked':<15} {'Wages Paid':<15}")
print("-" * 45)

for line in payroll_file:
    parts = line.strip().split()
    if len(parts) == 3:
        last_name, hourly_wage_str, hours_worked_str = parts
        try:
            hourly_wage = float(hourly_wage_str)
            hours_worked = float(hours_worked_str)
            wages_paid = hourly_wage * hours_worked
            print(f"{last_name:<15} {hours_worked:<15.2f} {wages_paid:<15.2f}")
        except ValueError:
            print(f"Warning: Skipping line due to invalid numeric format - '{line.strip()}'")
            continue
    else:
        print(f"Warning: Skipping invalid line - '{line.strip()}'")

payroll_file.close()