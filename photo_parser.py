from PIL import Image
import exifread
import os
import json
import base64
from io import BytesIO

def parse_photo_metadata(image_path):
    """Extract relevant metadata from a photo, including GPS data and thumbnail."""
    try:
        with open(image_path, "rb") as f:
            tags = exifread.process_file(f, details=False)

        metadata = {
            "filename": os.path.basename(image_path),
            "gps_data": get_gps_data(tags),
            "camera_model": str(tags.get("Image Model", "Unknown")),
            "datetime_taken": str(tags.get("EXIF DateTimeOriginal", "Unknown")),
            "thumbnail": get_exif_thumbnail(tags),
        }

        return metadata

    except Exception as e:
        return {"filename": os.path.basename(image_path), "error": str(e)}

def get_gps_data(tags):
    """Extract and convert GPS data from EXIF metadata."""
    def convert_to_degrees(value):
        try:
            d, m, s = value
            return float(d.num) / float(d.den) + \
                   (float(m.num) / float(m.den)) / 60 + \
                   (float(s.num) / float(s.den)) / 3600
        except Exception as e:
            return {"error": f"Error converting GPS data: {str(e)}"}

    try:
        if 'GPS GPSLatitude' in tags and 'GPS GPSLongitude' in tags:
            lat = convert_to_degrees(tags['GPS GPSLatitude'].values)
            lon = convert_to_degrees(tags['GPS GPSLongitude'].values)

            # Ensure references are properly read
            lat_ref = tags.get('GPS GPSLatitudeRef', None)
            lon_ref = tags.get('GPS GPSLongitudeRef', None)

            if lat_ref and lat_ref.values[0] != 'N':
                lat = -lat
            if lon_ref and lon_ref.values[0] != 'E':
                lon = -lon

            return {"latitude": lat, "longitude": lon}
        return {"error": "No GPS Data"}

    except Exception as e:
        return {"error": f"Error reading EXIF: {str(e)}"}

def get_exif_thumbnail(tags):
    """Extract and encode the EXIF thumbnail as a Base64 string."""
    try:
        if "JPEGThumbnail" in tags:
            thumbnail_data = tags["JPEGThumbnail"]
            if isinstance(thumbnail_data, bytes):
                return base64.b64encode(thumbnail_data).decode('utf-8')
        return None
    except Exception as e:
        return {"error": f"Error extracting thumbnail: {str(e)}"}
