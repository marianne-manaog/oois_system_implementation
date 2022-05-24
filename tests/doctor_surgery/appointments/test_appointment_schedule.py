import unittest

from datetime import time

from doctor_surgery.src.doctor_surgery.appointments.appointment_schedule import AppointmentSchedule

appointment_schedule = AppointmentSchedule()

dummy_doctor_name = 'Neil Melendez'
dummy_patient_name = 'Piper Halliwell'

dummy_appointment_assigned = {
        'appointment_type': 'Consultation',
        'time': time(hour=10, minute=0).strftime('%H:%M'),
        'patient_full_name': dummy_patient_name,
        'doctor_full_name': dummy_doctor_name
}

empty_string = ''


class TestAppointmentSchedule(unittest.TestCase):

    def test_add_appointment(self):

        time_selected = '15:00'

        for appointment in appointment_schedule.appointments:
            if appointment.get('time') == time_selected:
                self.assertEqual(empty_string, appointment.get('patient_full_name'))
                break

        appointment_schedule.add_appointment(time_selected, dummy_patient_name)

        self.assertEqual(dummy_patient_name, appointment.get('patient_full_name'))

    def test_cancel_appointment(self):

        appointment_schedule.cancel_appointment(dummy_appointment_assigned)

        self.assertEqual(dummy_appointment_assigned['patient_full_name'], empty_string)
        self.assertEqual(dummy_appointment_assigned['time'], empty_string)

    def test_find_next_available_appointments(self):

        expected_appointments_available = [
            {'appointment_type': '', 'doctor_full_name': '', 'patient_full_name': '', 'time': '10:00'},
            {'appointment_type': '', 'doctor_full_name': '', 'patient_full_name': '', 'time': '12:00'},
            {'appointment_type': '', 'doctor_full_name': '', 'patient_full_name': '', 'time': '14:00'}
        ]

        result_appointments_available = appointment_schedule.find_next_available_appointments()

        self.assertEqual(expected_appointments_available, result_appointments_available)
