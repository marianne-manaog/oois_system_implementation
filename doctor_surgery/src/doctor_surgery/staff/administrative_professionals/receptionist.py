# This Python file contains the definition of the class 'Receptionist', which enables to make or cancel an
# appointment on behalf of a doctor.

class Receptionist:
    """
    This class defines a receptionist by their name and employee number.
    """

    def __init__(self, name, employee_number):
        # type: (str, str) -> None
        self.name = name
        self.employee_number = employee_number

    def __str__(self):  # pragma: no cover
        return "<Receptionist whose name is '{}' and employee number is '{}'>".format(
            self.name, self.employee_number
        )

    def __repr__(self):  # pragma: no cover
        return "Receptionist: (name: {}, employee number: {})".format(
            self.name, self.employee_number
        )

    @staticmethod
    def make_appointment(time_chosen, patient_full_name, doctor):  # pragma: no cover
        # type: (str, str, Doctor) -> None
        """
        This method enables to make an appointment between a doctor and a patient at a chosen time.

        Args:
            time_chosen: str
                    the time at which an appointment is made.
            patient_full_name: str
                            the full name of the patient for whom an appointment is made.
            doctor: Doctor
                    the doctor with whom an appointment is made.
        """

        doctor.appointments_list.add_appointment(
            time_chosen=time_chosen,
            patient_full_name=patient_full_name
        )

    @staticmethod
    def cancel_appointment(doctor, appointment):  # pragma: no cover
        # type: (Doctor, dict) -> None
        """
        This method enables to cancel an appointment previously scheduled.

        Args:
            doctor: Doctor
                the doctor with whom an appointment has to be cancelled.
            appointment: dict
                    the appointment to cancel.
        """

        doctor.appointments_list.cancel_appointment(appointment)
