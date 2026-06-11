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

1. Place all the HEIC files you want to convert in the `heic_img` directory.

2. Create an `output` directory

3. Run the script `main.py` using the following command:

   ```
   python main.py
   ```

4. All HEIC files in the `heic_img` directory will be converted to PNG format and saved in the same directory with the same name but with the `.png` extension.

## Notes

- If you want to convert HEIC files in a different directory, modify the `input_dir` variable in the script to the appropriate directory path.
```python
# set the directory path containing the HEIC files
directory = 'heic_img'
```

> [!NOTE]
> This script was developed and tested on Windows 11 using Python `3.12.10`.
