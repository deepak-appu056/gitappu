def flask
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data for demonstration
staff_information = {}
training_requests = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/staff', methods=['GET', 'POST'])
def manage_staff():
    if request.method == 'POST':
        # Handle staff information submission
        # Update staff_information dictionary
        staff_id = request.form['staff_id']
        staff_info = {
            'name': request.form['name'],
            'qualifications': request.form['qualifications'],
            'roles': request.form['roles'],
            'contact_info': request.form['contact_info']
        }
        staff_information[staff_id] = staff_info
    return render_template('manage_staff.html', staff_information=staff_information)

@app.route('/training', methods=['GET', 'POST'])
def track_training():
    if request.method == 'POST':
        # Handle training request submission
        # Update training_requests list
        request_info = {
            'staff_id': request.form['staff_id'],
            'training_type': request.form['training_type'],
            'status': 'Pending'
        }
        training_requests.append(request_info)
    return render_template('track_training.html', training_requests=training_requests)

@app.route('/approve_deny/<int:request_id>/<string:decision>')
def approve_deny(request_id, decision):
    # Update the status of the training request
    if decision == 'approve':
        training_requests[request_id]['status'] = 'Approved'
    else:
        training_requests[request_id]['status'] = 'Denied'
    return redirect(url_for('track_training'))

if __name__ == '__main__':
    app.run(debug=True)