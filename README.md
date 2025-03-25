Photo Location Mapping Tool

A Flask-based application that extracts EXIF metadata from photos, including GPS coordinates and thumbnails, and displays them on a web interface.

Features
    •    EXIF Metadata Extraction:
Parse image EXIF data (camera model, datetime, GPS coordinates) using exifread.
    •    Image Display:
Show photos (from the static directory) along with their GPS data on a simple HTML page.
    •    Dockerized Environment:
Easily build and run the application inside a Docker container.
    •    Modular Design:
GPS and thumbnail extraction are handled in the separate photo_parser.py module.

Prerequisites
    •    Docker Desktop installed.
    •    A GitHub account (for version control, optional).

Getting Started

1. Clone the Repository

git clone https://github.com/your-username/photo-mapper.git
cd photo-mapper

2. Place Your Photos
    •    Place your JPEG/PNG images into the static/ directory.
For example:

cp /path/to/your/photos/* static/



3. Build and Run with Docker

Build and start the Docker container:

docker compose up --build

This command will:
    •    Build the Docker image using the provided Dockerfile
    •    Start the Flask server on port 5001

4. Access the Application
    •    API Endpoint:
Visit http://localhost:5001/photos to see the JSON data containing image metadata.
    •    Display Page:
Visit http://localhost:5001/display to view the photos with their GPS coordinates.

Project Structure

photo-mapper/
├── Dockerfile
├── docker-compose.yml
├── app.py                  # Main Flask application
├── photo_parser.py         # Module for extracting EXIF metadata (GPS, thumbnails)
├── requirements.txt        # Python dependencies
├── static/                 # Static assets folder; place images here
│   └── (your image files)
└── templates/
    └── display.html        # HTML template for displaying photos and GPS data

Troubleshooting
    •    Empty Photo List:
Ensure that your images are placed inside the static/ folder and that the filenames end with .jpg, .jpeg, or .png.
    •    GPS Data Issues:
If GPS data isn’t showing, verify that your images contain EXIF GPS tags. You can use tools like exiftool to inspect your images.
    •    Docker Issues:
If you run into Docker build issues, try running:

docker-compose down
docker-compose up --build



License

This project is licensed under the MIT License – see the LICENSE file for details.

⸻

Feel free to modify the content as necessary. Let me know if you need further adjustments!
