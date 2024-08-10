

# JPG to PNG Converter

This script converts all JPG images in a specified directory to PNG format and saves them to a new directory.

## Requirements

- Python 3.x
- Pillow library

You can install Pillow using pip if you don't already have it:

```bash
pip install Pillow
```

## Usage

1. **Prepare your directories:**
   - `old_file`: Directory containing the JPG images you want to convert.
   - `new_file`: Directory where you want to save the converted PNG images.

2. **Run the script:**

   ```bash
   python convert_jpg_to_png.py old_file new_file
   ```

   - Replace `convert_jpg_to_png.py` with the name of your script file.
   - Replace `old_file` with the path to the directory containing the JPG images.
   - Replace `new_file` with the path to the directory where you want to save the PNG images.

## Example

Suppose you have a directory named `jpg_images` containing your JPG files and you want to save the converted PNG files to a directory named `png_images`. You would run:

```bash
python convert_jpg_to_png.py jpg_images png_images
```

If `png_images` does not already exist, it will be created.

## Script Details

- **Imports:**
  - `sys`: For command-line arguments.
  - `os`: For file and directory operations.
  - `PIL.Image`: For image processing.

- **Functionality:**
  - The script reads all files from the `old_file` directory.
  - It converts each JPG image to PNG format.
  - The converted images are saved in the `new_file` directory with the same base name but with a `.png` extension.

## License

This script is provided as-is. Feel free to use and modify it according to your needs.


