import random
import bisect
import json
from enum import Enum, auto
import datetime

class Doctor():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.u_id = random.randint(1, 2**32-1)
        self.appointments = {}
    
    def add_appointment(self, appointment):
        if appointment.date in self.appointments:
            daily_appointments = self.appointments[appointment.date]
            daily_appointments.add(appointment)
        else:
            self.appointments[appointment.date] = {appointment}

    def delete_appointment(self, u_id):
        for date in self.appointments:
            for appointment in self.appointments[date]:
                if appointment.u_id == u_id:
                    self.appointments[date].remove(appointment)
                    return True
        return False

    def json(self):
        values = {
            'first_name' : self.first_name,
            'last_name' :  self.last_name,
            'u_id' : self.u_id
        }
        return values

    def __str__(self):
        return json.dumps(self.json())

class Appointment():
    class AppointmentType(Enum):
        FOLLOW_UP = auto()
        NEW_PATIENT = auto()

    def __init__(self, first_name, last_name, date, time, kind):
    
        time_splits = time.split(':')
        hour, minute = int(time_splits[0]), int(time_splits[1])

        date_splits  = date.split('/')
        month, day, year = int(date_splits[0]), int(date_splits[1]), int(date_splits[2])

        time = datetime.time(hour=hour, minute=minute)
        print(date_splits)
        date = datetime.date(day=day, month=month, year=year)

        kind = Appointment.AppointmentType[kind]

        self.first_name = first_name
        self.last_name = last_name
        self.u_id = random.randint(1, 2**32-1)
        self.date = date
        self.time = time
        self.kind = kind

    def json(self):
        values = {
            'first_name' : self.first_name,
            'last_name' :  self.last_name,
            'u_id' : self.u_id,
            'date' : str(self.date),
            'time' : str(self.time),
            'kind' : self.kind.name
        }
        return values

    def __str__(self):
        return json.dumps(self.json())

