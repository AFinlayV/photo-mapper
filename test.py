import exifread
import piexif
from PIL import Image

with open("test_photos/PXL_20250121_213752690.jpg", "rb") as f:
    exif_data_exifread = exifread.process_file(f)

exif_data_piexif = piexif.load(Image.open("test_photos/PXL_20250121_213752690.jpg").info["exif"])

print("EXIF Read by exifread:", exif_data_exifread.keys())
print("EXIF Read by piexif:", exif_data_piexif.keys())
