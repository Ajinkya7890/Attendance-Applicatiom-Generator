# Event Attendance Request Generator

This Flask web application generates an attendance request document for students participating in events. It allows users to input event details and student names, then generates a Word document (.docx) for submission.

## Features
- Input event details (name, location, dates)
- Add student participants
- Generate a properly formatted attendance request letter in `.docx` format
- Download the document instantly

## Installation

### Prerequisites
Ensure you have Python installed. You can check your Python version with:
```sh
python --version
```
Install the required dependencies using:
```sh
pip install flask python-docx
```

### Clone the Repository
```sh
git clone https://github.com/your-username/event-attendance-request.git
cd event-attendance-request
```

## Usage

### Running the Application
Start the Flask server by running:
```sh
python app.py
```

The application will be accessible at `http://127.0.0.1:5000/`.

### How to Use
1. Open the application in a web browser.
2. Enter event details and add student names.
3. Click the **Generate Document** button.
4. The `.docx` file will be automatically downloaded.

## Project Structure
```
/
├── app.py                 # Flask backend
├── templates/
│   ├── index.html         # Frontend UI
├── static/
│   ├── Event_Attendance_Application.docx  # Generated files (temporary)
├── README.md              # Project documentation
```

## Authors
This project was developed by:
- **Ajinkya Mariche**
- **Manjosh Lilhare**
- **Aryan Thawkar**

## Contributing
Feel free to fork this repository and submit pull requests with improvements.

## License
This project is open-source and available under the [MIT License](LICENSE).
