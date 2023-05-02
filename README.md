# HEIC to PNG Converter

This is a simple Python script that converts all HEIC files in a directory to PNG format. It uses the `pillow-heif` library to read the HEIC files and the `Pillow` library to save them as PNG files.

![heic to png](heic-to-png.png)

## Requirements

This script requires the following libraries to be installed:

- `Pillow`
- `pillow-heif`

You can install them by running:

```
pip install pillow
```

```
 pip install pillow-heif
```

## Usage

1. Place all the HEIC files you want to convert in the `heic_img` directory.

2. Run the script `main.py` using the following command:

   ```
   python main.py
   ```

3. All HEIC files in the `heic_img` directory will be converted to PNG format and saved in the same directory with the same name but with the `.png` extension.

## Notes

- If you want to convert HEIC files in a different directory, modify the `directory` variable in the script to the appropriate directory path.
```python
# set the directory path containing the HEIC files
directory = 'heic_img'
```

- This script was developed and used only on Windows 10.