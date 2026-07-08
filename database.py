import sqlite3


def create_database():

    connection = sqlite3.connect("payroll.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS payroll (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        employee_id TEXT,

        employee_name TEXT,

        hourly_rate REAL,

        hours_worked REAL,

        gross_pay REAL,

        federal_tax REAL,

        state_tax REAL,

        social_security REAL,

        medicare REAL,

        net_pay REAL
    )
    """)

    connection.commit()
    connection.close()


def save_payroll(
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
):

    connection = sqlite3.connect("payroll.db")
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO payroll
    (
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

    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
    (
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
    ))

    connection.commit()
    connection.close()


def get_payroll_history():

    connection = sqlite3.connect("payroll.db")
    cursor = connection.cursor()

    cursor.execute("""
SELECT employee_id,
       employee_name,
       hourly_rate,
       hours_worked,
       gross_pay,
       net_pay
FROM payroll
""")

    records = cursor.fetchall()

    connection.close()

    return records