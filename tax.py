def calculate_federal_tax(gross_pay):

    federal_tax_rate = 0.12

    return gross_pay * federal_tax_rate



def calculate_state_tax(gross_pay):

    state_tax_rate = 0.04

    return gross_pay * state_tax_rate



def calculate_social_security(gross_pay):

    social_security_rate = 0.062

    return gross_pay * social_security_rate



def calculate_medicare(gross_pay):

    medicare_rate = 0.0145

    return gross_pay * medicare_rate