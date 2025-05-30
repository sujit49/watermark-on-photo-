# Image Watermarking Desktop Application

## Developed by Sujit

This is a simple desktop application built using Python and Tkinter to add watermarks to your images.

## Features

* **Upload Image:** Easily select and upload images from your local file system.
* **Display Image:** Preview the uploaded image within the application.
* **Enter Watermark Text:** Input the text you want to use as a watermark.
* **Add Watermark:** Apply the entered text as a watermark to the image, positioned at the bottom-right corner with a semi-transparent white color and Arial font.
* **Save Watermarked Image:** Save the watermarked image to your desired location in PNG, JPEG, or any other supported format.

## Prerequisites

* Python 3.x installed on your system.
* Pillow (PIL) library installed. You can install it using pip:
    ```bash
    pip install Pillow
    ```

## How to Run the Application

1.  Save the provided Python code as a `.py` file (e.g., `watermark_app.py`).
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you saved the file.
4.  Run the application using the command:
    ```bash
    python watermark_app.py
    ```

This will open the Image Watermarking Tool window.

## Usage

1.  Click the "Upload Image" button to select an image file from your computer. The image will be displayed in the application window.
2.  In the text entry field, type the watermark text you want to add.
3.  Click the "Add Watermark" button. The watermark will be applied to the displayed image.
4.  To save the watermarked image, click the "Save Watermarked Image" button. A file dialog will appear, allowing you to choose the save location and file name.

## Libraries Used

* **tkinter:** For creating the graphical user interface.
* **Pillow (PIL):** For image manipulation, drawing text on images, and handling different image formats.

## Author

Sujit

## License

[Optional: Add a license if you have one, e.g., MIT License]
