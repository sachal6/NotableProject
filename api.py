from database_objects import Doctor, Appointment
import flask
from flask import request, jsonify
import sqlite3
import datetime
from datetime import date, time

app = flask.Flask(__name__)
app.config["DEBUG"] = True

'''INITIALIZING DATABASE'''
appointment = Appointment('a','b', '1/2/2011', '11:21', 'FOLLOW_UP')
doc = Doctor('d','a')
doc2 = Doctor('a','b')
doc.u_id= 4034240455
appointment.u_id = 14240411
doc.add_appointment(appointment)

doctors = [doc,doc2]
print("STARTED")
print([doc.u_id for doc in doctors])
'''END INITIALIZING DATASE'''



@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The requested resource could not be found.</p>", 404

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Notable Backend Project</h1>'''

@app.route('/api/v1/resources/doctors/all', methods=['GET'])
def fetch_doctors():
    return jsonify([doc.json() for doc in doctors])

@app.route('/api/v1/resources/doctors/appointments', methods=['GET'])
def fetch_appointments():
    query_parameters = request.args
    u_id = query_parameters.get('u_id')
    date = query_parameters.get('date')
    if not date or not u_id:
        return page_not_found(404)

    date_splits  = date.split('/')
    month, day, year = int(date_splits[0]), int(date_splits[1]), int(date_splits[2])
    date = datetime.date(day=day, month=month, year=year)

    u_id = int(u_id)
    for doc in doctors:
        if doc.u_id == u_id:
            if date in doc.appointments:
                appointments = list(doc.appointments[date])
                return jsonify([appointment.json() for appointment in appointments])

            else:
                return jsonify([])
    return page_not_found(404)

@app.route('/api/v1/resources/doctors/appointments', methods=['DELETE'])
def delete_appointments():
    query_parameters = request.args
    u_id = query_parameters.get('u_id')
    if not u_id:
        return page_not_found(404)
    u_id = int(u_id)
    for doc in doctors:
        success = doc.delete_appointment(u_id)
        if success:
            return jsonify('Successfully Deleted'), 200
    return page_not_found(404)

@app.route('/api/v1/resources/doctors/appointments/new', methods=['GET'])
def add_appointment():
    query_parameters = request.args
    doc_id = query_parameters.get('u_id')

    print('GOT HERE')
    first_name = query_parameters.get('first_name')
    last_name = query_parameters.get('first_name')
    date = query_parameters.get('date')
    time = query_parameters.get('time')
    kind = query_parameters.get('kind')

    if not (doc_id and first_name and last_name and time and date and kind):
        return page_not_found(404)

    doc_id = int(doc_id)

    appointment = Appointment(
        first_name=first_name,
        last_name=last_name,
        time=time,
        date=date,
        kind=kind
    )

    for doc in doctors:
        if doc.u_id == doc_id:
            doc.add_appointment(appointment)
            return jsonify('Successfully added'), 200
    return page_not_found(404)

app.run()


# print(app)

# doc.add_appointment(app)

# print(doc.appointments)

# doc.delete_appointment(app.u_id)

# print(doc.appointments)
