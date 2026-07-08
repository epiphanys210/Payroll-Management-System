import tkinter as tk
from tkinter import messagebox
import csv
from database import create_database, save_payroll, get_payroll_history
from pay_stub import create_pay_stub

create_database()
last_employee_id = ""
last_employee_name = ""
last_hourly_rate = 0
last_hours_worked = 0
last_gross_pay = 0
last_federal_tax = 0
last_state_tax = 0
last_social_security = 0
last_medicare = 0
last_net_pay = 0

def exit_program():
    window.destroy()
def show_history():

    records = get_payroll_history()

    history_window = tk.Toplevel(window)
    history_window.title("Payroll History")
    history_window.geometry("700x400")

    text = tk.Text(history_window, width=90, height=20)
    text.pack(padx=10, pady=10)

    if len(records) == 0:
        text.insert(tk.END, "No payroll records found.")
        return

    text.insert(tk.END,
        "Employee ID | Employee | Rate | Hours | Gross | Net\n")
    text.insert(tk.END, "-" * 70 + "\n")

    for record in records:
        text.insert(
            tk.END,
            f"{record[0]} | {record[1]} | ${record[2]:.2f} | "
            f"{record[3]} | ${record[4]:.2f} | ${record[5]:.2f}\n"
        )
def generate_pay_stub():

    if last_employee_name == "":
        messagebox.showwarning(
            "No Payroll",
            "Please calculate payroll first."
        )
        return

    create_pay_stub(
        last_employee_id,
        last_employee_name,
        last_hourly_rate,
        last_hours_worked,
        last_gross_pay,
        last_federal_tax,
        last_state_tax,
        last_social_security,
        last_medicare,
        last_net_pay
    )

    messagebox.showinfo(
        "Success",
        "Pay Stub PDF created!"
    )


def export_csv():

    records = get_payroll_history()

    if len(records) == 0:
        messagebox.showwarning(
            "No Data",
            "No payroll records to export."
        )
        return

    with open("PayrollHistory.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Employee ID",
            "Employee Name",
            "Hourly Rate",
            "Hours Worked",
            "Gross Pay",
            "Net Pay"
        ])

        writer.writerows(records)

    messagebox.showinfo(
        "Success",
        "Payroll history exported to PayrollHistory.csv"
    )


def calculate_pay():


    global last_employee_id
    global last_employee_name
    global last_hourly_rate
    global last_hours_worked
    global last_gross_pay
    global last_federal_tax
    global last_state_tax
    global last_social_security
    global last_medicare
    global last_net_pay

    try:

        employee_id = id_entry.get()
        employee_name = name_entry.get()

        hourly_rate = float(rate_entry.get())
        hours_worked = float(hours_entry.get())

        regular_hours = 40
        overtime_rate = 1.5

        if hours_worked > regular_hours:

            overtime_hours = hours_worked - regular_hours

            regular_pay = regular_hours * hourly_rate

            overtime_pay = overtime_hours * hourly_rate * overtime_rate

        else:

            regular_pay = hours_worked * hourly_rate
            overtime_pay = 0

        gross_pay = regular_pay + overtime_pay

        federal_tax = gross_pay * 0.12
        state_tax = gross_pay * 0.04
        social_security = gross_pay * 0.062
        medicare = gross_pay * 0.0145

        total_deductions = (
            federal_tax
            + state_tax
            + social_security
            + medicare
        )

        net_pay = gross_pay - total_deductions

        last_employee_id = employee_id
        last_employee_name = employee_name
        last_hourly_rate = hourly_rate
        last_hours_worked = hours_worked
        last_gross_pay = gross_pay
        last_federal_tax = federal_tax
        last_state_tax = state_tax
        last_social_security = social_security
        last_medicare = medicare
        last_net_pay = net_pay

        save_payroll(
            employee_id,
            employee_name,
            hourly_rate,
            hours_worked,
            gross_pay,
            federal_tax,
            state_tax,
            social_security,
            medicare,
            net_pay
        )

        result_label.config(
            text=f"""
PAYROLL SUMMARY

Employee ID: {employee_id}

Employee: {employee_name}

Regular Pay: ${regular_pay:.2f}

Overtime Pay: ${overtime_pay:.2f}

Gross Pay: ${gross_pay:.2f}

Federal Tax: ${federal_tax:.2f}
State Tax: ${state_tax:.2f}
Social Security: ${social_security:.2f}
Medicare: ${medicare:.2f}

Total Deductions: ${total_deductions:.2f}

Net Pay: ${net_pay:.2f}
"""
        )

    except ValueError:

        messagebox.showerror(
            "Input Error",
            "Please enter valid numbers."
        )

# ---------------- WINDOW ----------------

window = tk.Tk()

window.title("Payroll Management System")

window.geometry("500x780")

window.configure(bg="#F4F6F8")


title = tk.Label(
    window,
    text="Payroll Management System",
    font=("Arial", 22, "bold"),
    bg="#F4F6F8",
    fg="#003366"
)

title.pack(pady=20)


tk.Label(
    window,
    text="Employee ID",
    bg="#F4F6F8",
    fg="black",
    font=("Arial",11)
).pack()

id_entry = tk.Entry(window,width=35)
id_entry.pack(pady=5)


tk.Label(
    window,
    text="Employee Name",
    bg="#F4F6F8",
    fg="black",
    font=("Arial",11)
).pack()

name_entry = tk.Entry(window,width=35)
name_entry.pack(pady=5)


tk.Label(
    window,
    text="Hourly Rate",
    bg="#F4F6F8",
    fg="black",
    font=("Arial",11)
).pack()

rate_entry = tk.Entry(window,width=35)
rate_entry.pack(pady=5)


tk.Label(
    window,
    text="Hours Worked",
    bg="#F4F6F8",
    fg="black",
    font=("Arial",11)
).pack()

hours_entry = tk.Entry(window,width=35)
hours_entry.pack(pady=5)


tk.Button(
    window,
    text="Calculate Payroll",
    width=30,
    height=2,
    bg="#007ACC",
    fg="white",
    font=("Arial", 11, "bold"),
    command=calculate_pay
).pack(pady=10)

tk.Button(
    window,
    text="View Payroll History",
    width=30,
    height=2,
    bg="#28A745",
    fg="white",
    font=("Arial", 11, "bold"),
    command=show_history
).pack(pady=10)


tk.Button(
    window,
    text="Generate Pay Stub",
    width=30,
    height=2,
    bg="#6F42C1",
    fg="white",
    font=("Arial", 11, "bold"),
    command=generate_pay_stub
).pack(pady=10)


result_label = tk.Label(
    window,
    text="Payroll Results Will Appear Here",
    bg="#F4F6F8",
    fg="black",
    justify="left",
    font=("Courier New",11)
)
result_label.pack(pady=20)
tk.Button(
    window,
    text="Export Payroll CSV",
    width=30,
    height=2,
    bg="#0F9D58",
    fg="white",
    font=("Arial", 11, "bold"),
    command=export_csv
).pack(pady=10)

tk.Button(
    window,
    text="Exit",
    width=30,
    height=2,
    bg="#DC3545",
    fg="white",
    font=("Arial", 11, "bold"),
    command=exit_program
).pack(pady=10)

window.mainloop()
