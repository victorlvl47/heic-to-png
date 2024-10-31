import os
from PIL import Image
import pillow_heif

# set the directory path containing the HEIC files
directory = 'heic_img'

# loop through all files in the directory
for filename in os.listdir(directory):
     # check if the file is in HEIC format
    if filename.lower().endswith(".heic"):
        # create an Image object from the HEIC file
        filepath = os.path.join(directory, filename)
        print("Converting:", filepath)
        heif_file = pillow_heif.read_heif(filepath)
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",
        )

        # create a new filename for the PNG file
        new_filename = os.path.splitext(filename)[0] + ".png"
        new_filepath = os.path.join(directory, new_filename)

        image.save(new_filepath, format("png"))


