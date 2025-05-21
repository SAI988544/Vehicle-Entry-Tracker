
Vehicle Entry Tracker

The Vehicle Entry Tracker is a Python-based web application that uses YOLOv4 and EasyOCR for Automatic Number Plate Recognition (ANPR). It allows admins to manage allowed vehicle plates and security personnel to scan vehicles via images or videos in real time.

Features:

* YOLOv4 + EasyOCR for plate detection and recognition
* Image and video upload support
* Role-based login system (Admin and Security roles)
* Admins can add and manage allowed number plates
* Security personnel can validate vehicles in real time
* Timestamp logging for vehicle entries and exits
* Audio alerts for allowed and not allowed vehicles
* Dashboard to view logs and manage system activity
* Responsive and modern UI with animations
* Toast notifications for quick status updates

Technologies Used:

* Python
* Flask
* YOLOv4 (custom-trained model)
* EasyOCR
* OpenCV
* MySQL
* HTML, CSS, JavaScript (with animations and AJAX)

Project Structure:

* templates/ - HTML templates for all pages
* static/ - Static files including CSS, JS, and uploads
* routes/ - Flask Blueprints for route management
* models.py - SQLAlchemy models
* forms.py - WTForms for user authentication
* utils.py - Utility functions
* anpr\_utils.py - ANPR core logic
* app.py - Main Flask application
* main.py - Entry point for the app

How to Run:

1. Clone the repository
2. Set up the Python environment and install dependencies
3. Configure MySQL connection in app.py
4. Run the app using `python main.py`
5. Access the app at `http://localhost:5000/`

Admin Panel:

Admins can log in to add allowed vehicle number plates and manage user accounts.

Security Panel:

Security users can log in to scan uploaded videos or images and check if the vehicle is allowed or not.

License:

This project is open-source and free to use for educational or personal projects.
