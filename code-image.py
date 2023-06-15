import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from io import BytesIO
from PIL import Image, ImageDraw
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import ImageFormatter

# Function to handle button click event
def convert_to_image():
    code = code_text.get("1.0", tk.END).strip()  # Get the code from the text box
    
    if not code:
        messagebox.showerror("Error", "Please paste some code.")
        return

    # Apply syntax highlighting and generate the image
    lexer = get_lexer_by_name("python")  # Adjust the lexer as per your code language
    formatter = ImageFormatter(font_name="Courier New", font_size=14, line_numbers=True)
    image_data = highlight(code, lexer, formatter)

    # Convert image data to PIL Image object
    image = Image.open(BytesIO(image_data))

    # Ask user for save location and image name
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Image", "*.png")])
    
    if file_path:
        # Save the image as PNG
        image.save(file_path)
        messagebox.showinfo("Success", f"Code converted to image and saved as {file_path}.")
    else:
        messagebox.showerror("Error", "No file selected. Code not saved.")

# Create the GUI window
window = tk.Tk()
window.title("Code to Image Converter")

# Create the text box for code input
code_text = tk.Text(window, height=20, width=80)
code_text.pack()

# Create the convert button with styling
convert_button = tk.Button(window, text="Convert to Image", command=convert_to_image, bg="lightblue", fg="black", padx=10, pady=5, font=("Arial", 12, "bold"))
convert_button.pack()

# Start the main GUI loop
window.mainloop()

