
# Payroll Calculator
# Calculates gross pay, overtime, taxes, and net pay


# Get employee information
employee_name = input("Enter employee name: ")

hourly_rate = float(input("Enter hourly rate: "))

hours_worked = float(input("Enter hours worked: "))


# Payroll rules
regular_hours = 40
overtime_rate = 1.5


# Calculate regular pay and overtime pay
if hours_worked > regular_hours:

    overtime_hours = hours_worked - regular_hours

    regular_pay = regular_hours * hourly_rate

    overtime_pay = overtime_hours * hourly_rate * overtime_rate

else:

    regular_pay = hours_worked * hourly_rate

    overtime_pay = 0


# Calculate gross pay
gross_pay = regular_pay + overtime_pay


# Tax rates (example rates)
federal_tax_rate = 0.12
state_tax_rate = 0.04
social_security_rate = 0.062
medicare_rate = 0.0145


# Calculate deductions
federal_tax = gross_pay * federal_tax_rate

state_tax = gross_pay * state_tax_rate

social_security = gross_pay * social_security_rate

medicare = gross_pay * medicare_rate


# Total deductions
total_deductions = (
    federal_tax
    + state_tax
    + social_security
    + medicare
)


# Calculate net pay
net_pay = gross_pay - total_deductions


# Display paycheck
print("----------------------")
print("PAYROLL SUMMARY")
print("----------------------")

print("Employee:", employee_name)

print("Regular Pay: $", round(regular_pay, 2))

print("Overtime Pay: $", round(overtime_pay, 2))

print("Gross Pay: $", round(gross_pay, 2))

print("----------------------")

print("Federal Tax: $", round(federal_tax, 2))

print("State Tax: $", round(state_tax, 2))

print("Social Security: $", round(social_security, 2))

print("Medicare: $", round(medicare, 2))

print("Total Deductions: $", round(total_deductions, 2))

print("----------------------")

print("Net Pay: $", round(net_pay, 2))

print("----------------------")