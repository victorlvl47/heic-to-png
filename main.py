import os
from PIL import Image
import pillow_heif

# set the directory path containing the HEIC files
input_dir = 'heic-dir'
output_dir = os.path.join(input_dir, "output")

# loop through all files in the directory
for filename in os.listdir(input_dir):
     # check if the file is in HEIC format
    if filename.lower().endswith(".heic"):
        # create an Image object from the HEIC file
        input_file = os.path.join(input_dir, filename)
        print("Converting:", input_file)
        try:
            heif_file = pillow_heif.read_heif(input_file)
            image = Image.frombytes(
                heif_file.mode,
                heif_file.size,
                heif_file.data,
                "raw",
            )
            # create a new filename for the PNG file
            new_filename = os.path.splitext(filename)[0] + ".png"
            new_filepath = os.path.join(output_dir, new_filename)

            image.save(new_filepath, format("png"))
        except Exception as e:
            print(f"Error converting {input_file}: {e}")
