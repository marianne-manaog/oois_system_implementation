# This Python file contains the definition of the class 'AppointmentSchedule',
# which enables to add or cancel an appointment, or find the next available ones.

import logging

from datetime import time

from .constants import (
    APPT_TYPE_CONSULT,
    APPT_TYPE_EMERGENCY,
    TIME_STR_FORMAT,
)
from doctor_surgery.src.doctor_surgery.constants import (
    FIRST_DUMMY_DOCTOR,
    SECOND_DUMMY_DOCTOR,
    THIRD_DUMMY_DOCTOR,
    FOURTH_DUMMY_DOCTOR,
    FIRST_DUMMY_PATIENT,
    SECOND_DUMMY_PATIENT,
    THIRD_DUMMY_PATIENT,
    FOURTH_DUMMY_PATIENT
)

appointment_schedule_log = logging.getLogger(__name__)


class AppointmentSchedule:
    """
    This class allows to schedule an appointment with a doctor, cancel it, or find
    the next available one.
    """

    def __init__(self):  # pragma: no cover
        # type: () -> None
        # This attribute contains a list of appointments (list of dictionaries) with a status on their availability.
        self.appointments = [
            {'appointment_type': APPT_TYPE_CONSULT,
             'time': time(hour=9, minute=0).strftime(TIME_STR_FORMAT),
             'patient_full_name': FIRST_DUMMY_PATIENT,
             'doctor_full_name': FIRST_DUMMY_DOCTOR},
            {'appointment_type': '',
             'time': time(hour=10, minute=0).strftime(TIME_STR_FORMAT),
             'patient_full_name': '',
             'doctor_full_name': ''},
            {'appointment_type': APPT_TYPE_EMERGENCY,
             'time': time(hour=11, minute=0).strftime(TIME_STR_FORMAT),
             'patient_full_name': SECOND_DUMMY_PATIENT,
             'doctor_full_name': SECOND_DUMMY_DOCTOR},
            {'appointment_type': '',
             'time': time(hour=12, minute=0).strftime(TIME_STR_FORMAT),
             'patient_full_name': '',
             'doctor_full_name': ''},
            {'appointment_type': APPT_TYPE_EMERGENCY,
             'time': time(hour=13, minute=0).strftime(TIME_STR_FORMAT),
             'patient_full_name': THIRD_DUMMY_PATIENT,
             'doctor_full_name': THIRD_DUMMY_DOCTOR},
            {'appointment_type': '',
             'time': time(hour=14, minute=0).strftime(TIME_STR_FORMAT),
             'patient_full_name': '',
             'doctor_full_name': ''},
            {'appointment_type': '',
             'time': time(hour=15, minute=0).strftime(TIME_STR_FORMAT),
             'patient_full_name': '',
             'doctor_full_name': ''},
            {'appointment_type': APPT_TYPE_CONSULT,
             'time': time(hour=16, minute=0).strftime(TIME_STR_FORMAT),
             'patient_full_name': FOURTH_DUMMY_PATIENT,
             'doctor_full_name': FOURTH_DUMMY_DOCTOR},
        ]

    def __str__(self):  # pragma: no cover
        return "<Appointment schedule containing the list of appointments '{}'>".format(
            self.appointments
        )

    def __repr__(self):  # pragma: no cover
        return "Appointment schedule: (appointments: {})".format(
            self.appointments
        )

    def add_appointment(self, time_chosen, patient_full_name):
        # type: (str, str) -> None
        """
        This method adds an appointment to the list of appointments given a time and a patient.
            Args:
                time_chosen: str
                            the time (format '%H:%M') at which an appointment is sought to be booked.
                patient_full_name: str
                                the full name of the patient for whom an appointment is added.
        """

        for appointment in self.appointments:
            if appointment.get('time') == time_chosen:
                if not appointment.get('patient_full_name'):
                    appointment.update({'patient_full_name': patient_full_name})
                    appointment_schedule_log.info("The following appointment has been added: ", appointment)
                else:
                    appointment_schedule_log.error("The following appointment cannot be added, "
                                                   "as another patient is already booked in: ",
                                                   appointment)  # pragma: no cover
            else:
                appointment_schedule_log.error("The following appointment cannot be added, "
                                               "as the selected time is not available: ",
                                               appointment)  # pragma: no cover

    @staticmethod
    def cancel_appointment(appointment):
        # type: (dict) -> None
        """
        This method cancels an appointment previously scheduled.
            Args:
                appointment: dict
                            the appointment to cancel.
        """

        appointment.update({'patient_full_name': ''})
        appointment.update({'time': ''})

        appointment_schedule_log.info("The following appointment has been cancelled: ", appointment)

    def find_next_available_appointments(self):
        # type: () -> List[Dict]
        """
        This method finds and returns the next available appointments from the list of appointments.

        Returns:
            appointments_available: list
                                    a list of appointments available.
        """

        appointments_available = []
        for appointment in self.appointments:
            if not appointment.get('patient_full_name'):
                appointments_available.append(appointment)
            else:
                appointment_schedule_log.debug("The following appointment is unavailable: ", appointment)

        appointment_schedule_log.info("The available appointments are: ", appointments_available)

        return appointments_available
