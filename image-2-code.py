import os



import pytesseract



from PIL import Image



import tkinter as tk



from tkinter import filedialog



from PIL import ImageTk







# Function to extract text from an image



def extract_text_from_image(image_path):



    image = Image.open(image_path)



    text = pytesseract.image_to_string(image)



    return text







# Function to save text to a file



def save_text(text, file_path):



    with open(file_path, 'w') as file:



        file.write(text)







# Function to handle the button click event



def select_image():



    # Open a file dialog to select an image



    image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])







    # Display the selected image



    if image_path:



        # Save the selected image path



        global selected_image_path



        selected_image_path = image_path







        # Open and display the selected image



        image = Image.open(image_path)



        image.thumbnail((400, 400))  # Resize the image for display



        image_tk = ImageTk.PhotoImage(image)



        image_label.configure(image=image_tk)



        image_label.image = image_tk







# Function to process the selected image



def process_image():



    if selected_image_path:



        # Take a snapshot of the image



        snapshot_path = "snapshot.jpg"  # Provide a name for the snapshot image



        snapshot = Image.open(selected_image_path)



        snapshot.save(snapshot_path)







        # Extract text from the snapshot image



        extracted_text = extract_text_from_image(snapshot_path)







        # Display the extracted text



        print("Extracted Text:")



        print(extracted_text)







        # Ask the user where to store the text



        save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])







        # Save the extracted text to the specified location



        if save_path:



            save_text(extracted_text, save_path)







        # Remove the snapshot image



        os.remove(snapshot_path)







# Create the main window



window = tk.Tk()







# Create an "Upload" button



upload_button = tk.Button(window, text="Upload Image", command=select_image)



upload_button.pack(pady=10)







# Create a label to display the selected image



image_label = tk.Label(window)



image_label.pack()







# Create a "Process" button



process_button = tk.Button(window, text="Process Image", command=process_image)



process_button.pack(pady=10)







# Initialize the selected_image_path variable



selected_image_path = None







# Start the main loop



window.mainloop()

