# Watermarkify

This Python program allows users to add watermarks to images. By creating a watermark on your image, you can protect your professional artwork and provide copyright protection in a digital format.

## Overview

The program utilizes the Pillow library (`PIL`) for image processing. It provides a `Watermark` class that enables users to add a custom watermark to their images.

## Requirements

1. Install the Pillow library using the following command:

    ```bash
    pip install pillow
    ```

## Usage

1. Clone the repository or download the script:

    ```bash
    git clone https://github.com/shrutiwd/Watermarkify.git
    cd Watermarkify
    ```

2. Ensure you have Python installed on your system.

3. Run the program:

    ```bash
    python watermarkify.py
    ```

4. Enter the required information such as image path, watermark text, text color, position, size, and output path.

## File Structure

- `watermarkify.py`: The main Python script for adding watermarks to images.
- `Requirements.txt`: File specifying the dependencies for the program.

## Important Notes

1. `Image.open`: Opens the image specified by the user.
2. `ImageDraw`: Adds functionalities to draw 2D graphics onto new or existing images.
3. `ImageFont.truetype`: Provides font and font size parameters for the watermark.
4. `draw.text`: Used to store functionalities like position, text color, text, font, etc.
5. `img.show`: Displays the image with the added watermark.
6. `img.save`: Saves the watermarked image in the specified output path.

Feel free to customize the program or add your watermarking preferences according to your specific needs.

Happy watermarking!
