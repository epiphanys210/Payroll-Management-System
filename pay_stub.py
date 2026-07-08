from reportlab.pdfgen import canvas


def create_pay_stub(
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

    filename = f"{employee_name}_PayStub.pdf"

    pdf = canvas.Canvas(filename)

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(170, 780, "PAY STUB")

    pdf.setFont("Helvetica", 12)

    pdf.drawString(50, 740, f"Employee ID: {employee_id}")
    pdf.drawString(50, 720, f"Employee Name: {employee_name}")

    pdf.drawString(50, 690, f"Hourly Rate: ${hourly_rate:.2f}")
    pdf.drawString(50, 670, f"Hours Worked: {hours_worked}")

    pdf.drawString(50, 640, f"Gross Pay: ${gross_pay:.2f}")

    pdf.drawString(50, 610, f"Federal Tax: ${federal_tax:.2f}")
    pdf.drawString(50, 590, f"State Tax: ${state_tax:.2f}")
    pdf.drawString(50, 570, f"Social Security: ${social_security:.2f}")
    pdf.drawString(50, 550, f"Medicare: ${medicare:.2f}")

    pdf.drawString(50, 510, f"Net Pay: ${net_pay:.2f}")

    pdf.save()