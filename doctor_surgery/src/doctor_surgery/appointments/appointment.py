# This Python file contains the definition of the class 'Appointment',
# which enables to instantiate an appointment-related object by providing the 'appointment_type' at least.

from doctor_surgery.src.doctor_surgery.staff.healthcare_professionals.healthcare_professional import \
    HealthcareProfessional
from doctor_surgery.src.doctor_surgery.patients.patient import Patient


class Appointment:
    """
    This class defines an appointment by its type (e.g., 'Standard consultation', 'Emergency appointment', etc.), an instance
    of a healthcare professional, and an instance of a patient.
    """

    def __init__(self, appointment_type, staff, patient):  # pragma: no cover
        # type: (str, HealthcareProfessional, Patient) -> None
        self.appointment_type = appointment_type
        self.staff = staff
        self.patient = patient

    def __str__(self):  # pragma: no cover
        return "<Appointment of type '{}' between the healthcare professional '{}' and the patient '{}'>".format(
            self.appointment_type, self.staff, self.patient
        )

    def __repr__(self):  # pragma: no cover
        return "Appointment: (appointment_type: {}, staff: {}, patient: {})".format(
            self.appointment_type, self.staff, self.patient
        )
