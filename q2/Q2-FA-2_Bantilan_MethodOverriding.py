class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    # Getter methods
    def get_name(self):
        return self.__name

    def get_bill_amount(self):
        return self.__bill_amount

    # Setter methods
    def set_name(self, name):
        self.__name = name

    def set_bill_amount(self, bill_amount):
        if bill_amount >= 0:
            self.__bill_amount = bill_amount
        else:
            raise ValueError("Bill amount cannot be negative.")

    # Calculate full bill
    def calculate_bill(self):
        return self.__bill_amount


# Child class for senior citizens
class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80


# Child class for PhilHealth members
class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85


# Create patient objects
regular_patient = Patient("Katleen Amistoso", 15000)
senior_patient = SeniorPatient("Sammy Velasco", 15000)
philhealth_patient = PhilHealthPatient("Twyla Javier", 15000)

# Store patients in a list
patients = [
    regular_patient,
    senior_patient,
    philhealth_patient
]

# Display the original and final bills
for patient in patients:
    print("\nPatient Name:", patient.get_name())
    print("Original Bill: ₱{:,.2f}".format(
        patient.get_bill_amount()
    ))
    print("Final Bill: ₱{:,.2f}".format(
        patient.calculate_bill()
    ))
