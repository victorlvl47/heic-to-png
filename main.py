import argparse
import os
from PIL import Image
import pillow_heif


def convert_heic_to_png(input_dir):
    output_dir = os.path.join(input_dir, "output")
    os.makedirs(output_dir, exist_ok=True)

    converted_count = 0

    for filename in os.listdir(input_dir):
        if not filename.lower().endswith(".heic"):
            continue

        input_file = os.path.join(input_dir, filename)
        new_filename = os.path.splitext(filename)[0] + ".png"
        new_filepath = os.path.join(output_dir, new_filename)

        print("Converting:", input_file)

        try:
            heif_file = pillow_heif.read_heif(input_file)

            image = Image.frombytes(
                heif_file.mode,
                heif_file.size,
                heif_file.data,
                "raw",
            )

            image.save(new_filepath, format="PNG")
            print("Saved:", new_filepath)

            converted_count += 1

        except Exception as e:
            print(f"Error converting {input_file}: {e}")

    print(f"\nDone. Converted {converted_count} file(s).")
    print(f"PNG files saved in: {output_dir}")


def main():
    parser = argparse.ArgumentParser(
        description="Convert HEIC images in a folder to PNG."
    )

    parser.add_argument(
        "input_dir",
        help="Folder containing HEIC files",
    )

    args = parser.parse_args()

    convert_heic_to_png(args.input_dir)


if __name__ == "__main__":
    main()