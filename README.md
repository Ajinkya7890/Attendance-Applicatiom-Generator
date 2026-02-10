# Event Attendance Application Generator

This Flask web application generates an attendance request letter for students participating in events. Users enter event details, select participants, preview the letter, and download a Word document (.docx). An optional email notification can be sent via EmailJS.

## Features
- Input event details (name, venue, dates)
- Select student participants from a list
- Live preview of the application letter
- Generate and download a formatted `.docx` file
- Optional email notification using EmailJS
- Vercel-ready deployment

## Installation

### Prerequisites
Ensure you have Python installed. You can check your Python version with:
```sh
python --version
```
Install the required dependencies using:
```sh
pip install -r requirements.txt
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
2. Enter event details and select student names.
3. (Optional) enter a receiver email and enable the email checkbox.
4. Click **Generate Application** to preview.
5. Click **Download as Word** to download the `.docx` file.

### EmailJS Configuration (Optional)
Email sending uses EmailJS in the frontend. If you want to use your own EmailJS account, replace the `emailjs.init`, service ID, and template ID in `templates/index.html`.

## Project Structure
```
/ 
├── app.py                # Flask backend
├── requirements.txt      # Python dependencies
├── templates/
│   └── index.html        # Frontend UI
├── static/
│   └── app.css           # Styling
├── vercel.json           # Vercel deployment config
├── users.json            # Student data (if used/extended)
└── README.md             # Project documentation
```

## Authors
This project was developed by:
- **Ajinkya Mariche**
- **Aryan Thawkar**

## Contributing
Feel free to fork this repository and submit pull requests with improvements.

## License
This project is open-source and available under the [MIT License](LICENSE).
