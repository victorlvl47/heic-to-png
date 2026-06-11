# HEIC to PNG Converter

This is a simple Python script that converts all HEIC files in a directory to PNG format. It uses the `pillow-heif` library to read the HEIC files and the `Pillow` library to save them as PNG files.

![heic to png](heic-to-png.png)

## Requirements

This script was tested with:

* Python `3.12.10`
* Windows 11
* `Pillow`
* `pillow-heif`

Install the Python dependencies by running:

```bash
pip install -r requirements.txt
```

You can check your Python version with:

```bash
python --version
```

Expected working version:

```bash
Python 3.12.10
```


## Usage

Run the script and pass the folder that contains your HEIC photos:

```bash
python main.py "C:\path\to\your\photos"
```

Example:

```bash
python main.py "C:\Users\viclv\Pictures\iPhone Photos"
```

The script will automatically create an `output` folder inside the selected folder and save the converted PNG files there.

Example result:

```text
iPhone Photos/
  IMG_001.HEIC
  IMG_002.HEIC
  output/
    IMG_001.png
    IMG_002.png
```

No manual output folder creation is needed.


## Notes

* The folder path is passed from the command line when running the script.
* The script automatically creates an `output` folder inside the selected folder.
* Converted PNG files are saved in the `output` folder.
* Original HEIC files are not modified or deleted.
* Folder paths with spaces should be wrapped in quotes.

Example:

```bash
python main.py "C:\Users\viclv\Pictures\iPhone Photos"
```

> [!NOTE]
> This script was developed and tested on Windows 11 using Python `3.12.10`.
