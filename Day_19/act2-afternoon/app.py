from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="eptals"
)
cursor = conn.cursor(dictionary=True)

@app.route("/patients-inner-join")
def inner_join():
    cursor.execute("""
        SELECT p.patient_id, p.name AS patient_name, d.name AS doctor_name,
               a.appointment_date, a.appointment_time
        FROM appointment a
        INNER JOIN patient p ON a.patient_id = p.patient_id
        INNER JOIN doctor d ON a.doctor_id = d.doctor_id
        WHERE d.specialty = 'Cardiology' AND a.appointment_date = CURDATE()
    """)
    result = cursor.fetchall()
    for row in result:
        if row["appointment_time"]:
            row["appointment_time"] = str(row["appointment_time"])
    return jsonify(result)

@app.route("/patients-left-join")
def left_join():
    cursor.execute("""
        SELECT p.patient_id, p.name AS patient_name, d.name AS doctor_name,
               a.appointment_date, a.appointment_time
        FROM patient p
        LEFT JOIN appointment a ON p.patient_id = a.patient_id
        LEFT JOIN doctor d ON a.doctor_id = d.doctor_id
        WHERE d.name IS NULL OR a.appointment_id IS NULL
    """)
    result = cursor.fetchall()
    for row in result:
        if row["appointment_time"]:
            row["appointment_time"] = str(row["appointment_time"])
    return jsonify(result)

@app.route("/patients-right-join")
def right_join():
    cursor.execute("""
        SELECT p.patient_id, p.name AS patient_name, d.name AS doctor_name,
               a.appointment_date, a.appointment_time
        FROM doctor d
        RIGHT JOIN appointment a ON d.doctor_id = a.doctor_id
        RIGHT JOIN patient p ON a.patient_id = p.patient_id
        WHERE d.specialty = 'Pediatrics' OR p.name LIKE 'A%'
    """)
    result = cursor.fetchall()
    for row in result:
        if row["appointment_time"]:
            row["appointment_time"] = str(row["appointment_time"])
    return jsonify(result)
