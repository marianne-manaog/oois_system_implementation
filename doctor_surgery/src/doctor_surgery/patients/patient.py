# This Python file contains the definition of the class 'Patient', which has two methods that enable to
# request either a repeat prescription or an appointment.

import logging

from doctor_surgery.src.doctor_surgery.constants import (
    DRUG_W_PLACEHOLDER,
    RECEPTIONIST_EMPLOYEE_NUMBER,
    RECEPTIONIST_NAME
)

from doctor_surgery.src.doctor_surgery.staff.healthcare_professionals.doctor import Doctor
from doctor_surgery.src.doctor_surgery.staff.administrative_professionals.receptionist import Receptionist

patient_log = logging.getLogger(__name__)

receptionist = Receptionist(name=RECEPTIONIST_NAME, employee_number=RECEPTIONIST_EMPLOYEE_NUMBER)


class Patient:
    """
      This class defines a patient by their name, address, phone number, doctor with whom they are registered,
      and a list of their prescriptions.
    """

    def __init__(self, name, address, phone, registered_doctor, list_of_prescriptions):  # pragma: no cover
        # type: (str, str, str, Doctor, List[Dict]) -> None
        self.name = name
        self.address = address
        self.phone = phone
        self.registered_doctor = registered_doctor
        self.list_of_prescriptions = list_of_prescriptions

    def __str__(self):  # pragma: no cover
        return "<Patient whose name is '{}', address is '{}', phone number is '{}', registered doctor is '{}', " \
               "and list of prescriptions is '{}'>".format(self.name, self.address, self.phone, self.registered_doctor,
                                                           self.list_of_prescriptions)

    def __repr__(self):  # pragma: no cover
        return "Patient: (name: {}, address: {}, phone: {}, registered_doctor: {}, list_of_prescriptions: {})".format(
            self.name, self.address, self.phone, self.registered_doctor, self.list_of_prescriptions
        )

    def request_repeat_prescription(self, prescription_type):
        # type: (str) -> Tuple[str, Prescription]
        """
        This method enables to request a repeat prescription.

        Args:
            prescription_type: str
                            the name of the drug for which a repeat prescription is requested.

        Returns:
            a tuple with the 'drug_<int>' string (e.g., 'drug_1') and the updated prescription object.
        """

        iter_index = 0
        for prescription in self.list_of_prescriptions:
            iter_index += 1
            drug_string = DRUG_W_PLACEHOLDER.format(iter_index)
            if prescription_type == prescription.get(drug_string).prescription_type:
                if prescription.get(drug_string).quantity > 0:
                    prescription.get(drug_string).quantity -= 1
                    print "The drug '{}' has been ordered successfully.".format(
                        prescription.get(drug_string).prescription_type
                    )
                    patient_log.info(
                        "The repeat prescription '{}' has been requested and its quantity has been "
                        "updated as '{}'.".format(prescription_type, prescription.get(drug_string).quantity))
                    return drug_string, prescription
            else:
                patient_log.error("The following drug has not been prescribed to you; thus, in this case, you "
                                  "cannot request a repeat prescription: ", prescription_type)  # pragma: no cover

    def request_appointment(self, time_chosen):  # pragma: no cover
        # type: (str) -> None
        """
        This method enables to request to schedule an appointment at a chosen time (if available).

        Args:
            time_chosen: str
                the time (format '%H:%M') at which a patient would like to schedule an appointment.
        """

        receptionist.make_appointment(
            time_chosen=time_chosen, patient_full_name=self.name, doctor=self.registered_doctor
        )
