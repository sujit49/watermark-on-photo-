# IMAGE WATERMARKING DESKTOP APPLICATION
# Developed by [Sujit]

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont


class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Watermarking Tool")
        self.root.geometry("900x800")  # Increased window size
        self.root.resizable(False, False)

        # Initialize variables
        self.image_path = None
        self.watermarked_image = None

        # Create UI Components
        self.create_widgets()

    def create_widgets(self):
        """
        Create and arrange widgets for the application.
        """
        # Title Label
        title_label = tk.Label(self.root, text="Image Watermarking Tool", font=("Arial", 24, "bold"))
        title_label.pack(pady=20)

        # Upload Button
        upload_button = tk.Button(self.root, text="Upload Image", font=("Arial", 14), command=self.upload_image)
        upload_button.pack(pady=10)

        # Canvas to display image
        self.image_canvas = tk.Canvas(self.root, width=700, height=400, bg="lightgray", relief="ridge", bd=2)
        self.image_canvas.pack(pady=10)

        # Entry for watermark text
        self.watermark_entry = tk.Entry(self.root, font=("Arial", 14), width=40)
        self.watermark_entry.pack(pady=10)
        self.watermark_entry.insert(0, "Enter watermark text here")

        # Add Watermark Button
        add_watermark_button = tk.Button(self.root, text="Add Watermark", font=("Arial", 14), command=self.add_watermark)
        add_watermark_button.pack(pady=10)

        # Save Button
        save_button = tk.Button(self.root, text="Save Watermarked Image", font=("Arial", 14), command=self.save_image)
        save_button.pack(pady=10)

    def upload_image(self):
        """
        Open a file dialog to select an image and display it on the canvas.
        """
        self.image_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")]
        )
        if self.image_path:
            try:
                image = Image.open(self.image_path)
                image.thumbnail((800, 600))  # Resize for display
                self.image_tk = ImageTk.PhotoImage(image)
                self.image_canvas.create_image(400, 300, image=self.image_tk)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load image: {e}")

    def add_watermark(self):
        """
        Add the watermark text to the uploaded image.
        """
        if not self.image_path:
            messagebox.showwarning("Warning", "Please upload an image first!")
            return

        watermark_text = self.watermark_entry.get().strip()
        if not watermark_text:
            messagebox.showwarning("Warning", "Please enter a watermark text!")
            return

        try:
            image = Image.open(self.image_path)
            drawable = ImageDraw.Draw(image)
            font = ImageFont.truetype("arial.ttf", 36)  # Use Arial font, size 36

            # Calculate text size using textbbox
            text_bbox = drawable.textbbox((0, 0), watermark_text, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]

            # Add text at bottom-right corner
            position = (image.width - text_width - 10, image.height - text_height - 10)
            drawable.text(position, watermark_text, font=font, fill=(255, 255, 255, 128))  # Semi-transparent white

            self.watermarked_image = image
            image.thumbnail((700, 600))  # Resize for display
            self.image_tk = ImageTk.PhotoImage(image)
            self.image_canvas.create_image(400, 300, image=self.image_tk)

            messagebox.showinfo("Success", "Watermark added successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add watermark: {e}")

    def save_image(self):
        """
        Save the watermarked image to the user's selected location.
        """
        if not self.watermarked_image:
            messagebox.showwarning("Warning", "No watermarked image to save!")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Files", "*.png"), ("JPEG Files", "*.jpg"), ("All Files", "*.*")]
        )
        if file_path:
            try:
                self.watermarked_image.save(file_path)
                messagebox.showinfo("Success", "Image saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save image: {e}")


if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()
