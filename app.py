from flask import Flask, render_template, request, send_file, jsonify
from docx import Document
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def generate_document():
    data = request.get_json()

    event_name = data.get("eventName", "Unknown Event")
    event_location = data.get("eventLocation", "Unknown Location")
    start_date = data.get("startDate", "Unknown Start Date")
    end_date = data.get("endDate", "Unknown End Date")
    students = data.get("students", [])

    if not students:
        return jsonify({"error": "No students selected"}), 400

    # Extract first student as sender
    sender_name = students[0].split(" (UID")[0]

    # Create Word document
    doc = Document()
    doc.add_paragraph("To\nClass Counsellor\nCSE Data Science\n\n")
    doc.add_paragraph(f"Subject: Request for Attendance Grant – {event_name} Participation\n\n")
    doc.add_paragraph(f"Respected Sir/Madam,\n\nI hope you are doing well. I, {sender_name} from CSE Data Science, am participating in {event_name} to be held at {event_location} from {start_date} to {end_date}. This event is a great opportunity to enhance our technical skills, problem-solving abilities, and teamwork.\n\n")
    doc.add_paragraph("The participating members from our class are:\n")
    
    for student in students:
        doc.add_paragraph(student)

    doc.add_paragraph("\nWe kindly request you to grant us attendance for the mentioned dates.\n\nLooking forward to your kind consideration.\n\n")
    doc.add_paragraph(f"Sincerely,\n{sender_name}\nCSE Data Science")

    # Save file
    filename = "Event_Attendance_Application.docx"
    filepath = os.path.join("static", filename)
    doc.save(filepath)

    return send_file(filepath, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)