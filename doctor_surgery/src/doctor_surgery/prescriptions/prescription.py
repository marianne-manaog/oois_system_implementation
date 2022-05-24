# This Python file contains the definition of the class 'Prescription'.

class Prescription:
    """
    This class defines a prescription by its type (the name of the drug being prescribed), an instance of a patient,
    an instance of a doctor, a quantity, and a dosage.
    """

    def __init__(self, prescription_type, patient, doctor, quantity, dosage):  # pragma: no cover
        # type: (str, Patient, Doctor, int, float) -> None
        self.prescription_type = prescription_type
        self.patient = patient
        self.doctor = doctor
        self.quantity = quantity
        self.dosage = dosage

    def __str__(self):  # pragma: no cover
        return "<Prescription of the drug '{}' (quantity: '{}'; dosage: '{}') given by the doctor '{}' to the " \
               "patient '{}'>".format(self.prescription_type, self.quantity, self.dosage, self.doctor, self.patient)

    def __repr__(self):  # pragma: no cover
        return "Prescription: (prescription_type: {}, patient: {}, doctor: {}, quantity: {}, dosage: {})".format(
            self.prescription_type, self.patient, self.doctor, self.quantity, self.dosage
        )
