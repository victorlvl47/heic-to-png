import argparse
import json
import os
from PIL import ExifTags, Image
import pillow_heif


def make_json_safe(value):
    try:
        json.dumps(value)
        return value
    except TypeError:
        return str(value)


def build_metadata(image, source_filename, output_filename):
    metadata = {
        "source_file": source_filename,
        "output_file": output_filename,
        "format": make_json_safe(image.format),
        "mode": make_json_safe(image.mode),
        "width": image.width,
        "height": image.height,
        "info_keys": sorted(str(key) for key in image.info.keys()),
        "exif": {},
    }

    try:
        exif = image.getexif()
        metadata["exif"] = {
            str(ExifTags.TAGS.get(tag_id, tag_id)): make_json_safe(value)
            for tag_id, value in exif.items()
        }
    except Exception as e:
        metadata["metadata_error"] = str(e)

    return metadata


def save_metadata_file(image, source_filename, output_filename, metadata_filepath):
    metadata = build_metadata(image, source_filename, output_filename)

    with open(metadata_filepath, "w", encoding="utf-8") as metadata_file:
        json.dump(metadata, metadata_file, indent=2)


def convert_heic_to_png(input_dir, save_metadata=False):
    pillow_heif.register_heif_opener()

    output_dir = os.path.join(input_dir, "converted-png-files")
    os.makedirs(output_dir, exist_ok=True)

    converted_count = 0

    for filename in os.listdir(input_dir):
        if not filename.lower().endswith(".heic"):
            continue

        input_file = os.path.join(input_dir, filename)
        new_filename = os.path.splitext(filename)[0] + ".png"
        new_filepath = os.path.join(output_dir, new_filename)
        metadata_filename = os.path.splitext(filename)[0] + ".metadata.json"
        metadata_filepath = os.path.join(output_dir, metadata_filename)

        print("Converting:", input_file)

        try:
            with Image.open(input_file) as image:
                image.save(new_filepath, format="PNG")
                print("Saved PNG:", new_filepath)

                if save_metadata:
                    try:
                        save_metadata_file(
                            image,
                            filename,
                            new_filename,
                            metadata_filepath,
                        )
                    except Exception as e:
                        metadata = {
                            "source_file": filename,
                            "output_file": new_filename,
                            "metadata_error": str(e),
                        }

                        with open(
                            metadata_filepath,
                            "w",
                            encoding="utf-8",
                        ) as metadata_file:
                            json.dump(metadata, metadata_file, indent=2)

                    print("Saved metadata:", metadata_filepath)

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

    parser.add_argument(
        "--metadata",
        action="store_true",
        help="Save metadata JSON sidecar files next to the converted PNG files",
    )

    args = parser.parse_args()

    convert_heic_to_png(args.input_dir, args.metadata)


if __name__ == "__main__":
    main()
