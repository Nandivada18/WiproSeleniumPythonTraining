from flask import Flask, jsonify, request

app = Flask(__name__)
# In-memory "database"

doctors = {}
patients = {}
appointments = {}

current_doctor_id = 1
current_patient_id = 1
current_appointment_id = 1
# Step 1: Create Doctor (POST)
@app.route("/v1/doctors", methods=["POST"])
def create_doctor():
    global current_doctor_id
    data = request.get_json()
    data["doctor_id"] = current_doctor_id
    doctors[current_doctor_id] = data
    current_doctor_id += 1
    return jsonify(data), 201
# Step 2: Patient Registration (POST)

@app.route("/v1/patients", methods=["POST"])
def register_patient():
    global current_patient_id
    data = request.get_json()

    # Edge cases
    if "age" in data and data["age"] < 0:
        return jsonify({"error": "Invalid age"}), 400
    if not data.get("email"):
        return jsonify({"error": "Email required"}), 400
    if any(p["phone"] == data.get("phone") for p in patients.values()):
        return jsonify({"error": "Duplicate phone"}), 409

    data["patient_id"] = current_patient_id
    patients[current_patient_id] = data
    current_patient_id += 1
    return jsonify(data), 201



# Step 3: Book Appointment (POST)
@app.route("/v1/appointments", methods=["POST"])
def book_appointment():
    global current_appointment_id
    data = request.get_json()

    # Check if doctor and patient exist
    if data["doctor_id"] not in doctors or data["patient_id"] not in patients:
        return jsonify({"error": "Doctor or Patient not found"}), 404

    # Check if slot is already booked
    for a in appointments.values():
        if a["doctor_id"] == data["doctor_id"] and a["date"] == data["date"] and a["time"] == data["time"]:
            return jsonify({"error": "Slot already booked"}), 409

    data["appointment_id"] = current_appointment_id
    appointments[current_appointment_id] = data
    current_appointment_id += 1
    return jsonify(data), 201
# Step 4: View Appointment (GET)
@app.route("/v1/appointments/<int:id>", methods=["GET"])
def view_appointment(id):
    appointment = appointments.get(id)
    if appointment:
        return jsonify(appointment), 200
    return jsonify({"error": "Appointment not found"}), 404
# Step 5: Reschedule Appointment (PUT)
@app.route("/v1/appointments/<int:id>", methods=["PUT"])
def reschedule_appointment(id):
    appointment = appointments.get(id)
    if not appointment:
        return jsonify({"error": "Appointment not found"}), 404

    data = request.get_json()
    # Check if new slot is available
    for a_id, a in appointments.items():
        if a_id != id and a["doctor_id"] == appointment["doctor_id"] and a["date"] == data["date"] and a["time"] == \
                data["time"]:
            return jsonify({"error": "Slot already booked"}), 409

    appointment.update(data)
    return jsonify(appointment), 200


# Step 6: Cancel Appointment (DELETE)
@app.route("/v1/appointments/<int:id>", methods=["DELETE"])
def cancel_appointment(id):
    if id in appointments:
        del appointments[id]
        return "", 204
    return jsonify({"error": "Appointment not found"}), 404

# Run the server
if __name__ == "__main__":
    app.run(debug=True)
