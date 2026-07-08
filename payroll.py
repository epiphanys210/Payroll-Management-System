def calculate_gross_pay(hourly_rate, hours_worked):

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


    return gross_pay