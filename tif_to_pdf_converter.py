import os
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tkinter as tk
from tkinter import filedialog

# Function to convert a TIF image to a PDF file
def tif_to_pdf(tif_path, pdf_path):
    print(f"Converting {tif_path} to {pdf_path}")
    img = Image.open(tif_path)
    width, height = img.size
    
    # Create a PDF canvas with the same dimensions
    c = canvas.Canvas(pdf_path, pagesize=(width, height))
    
    # Draw the TIF image onto the PDF canvas
    c.drawImage(tif_path, 0, 0, width, height)
    
    # Save the PDF file
    c.save()
    print(f"Conversion completed: {tif_path} -> {pdf_path}")

# Function to convert all TIF files in a directory to PDF
def convert_directory(input_dir, output_dir):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # List all TIF files in the input directory
    tif_files = [f for f in os.listdir(input_dir) if f.lower().endswith(".tif")]

    # Loop through each TIF file and convert it to PDF
    for tif_file in tif_files:
        tif_path = os.path.join(input_dir, tif_file)
        
        # Create the PDF file path by changing the extension
        pdf_file = os.path.splitext(tif_file)[0] + ".pdf"
        pdf_path = os.path.join(output_dir, pdf_file)
        
        # Call the tif_to_pdf function to perform the conversion
        tif_to_pdf(tif_path, pdf_path)

# Function to open a file dialog for selecting the input directory
def browse_input_directory():
    input_dir = filedialog.askdirectory(title="Select Input Directory")
    input_directory_entry.delete(0, tk.END)
    input_directory_entry.insert(0, input_dir)

# Function to open a file dialog for selecting the output directory
def browse_output_directory():
    output_dir = filedialog.askdirectory(title="Select Output Directory")
    output_directory_entry.delete(0, tk.END)
    output_directory_entry.insert(0, output_dir)

# Function to start the conversion process
def start_conversion():
    input_dir = input_directory_entry.get()
    output_dir = output_directory_entry.get()
    
    # Call the convert_directory function to perform the conversion
    convert_directory(input_dir, output_dir)
    
    # Update the result label to indicate completion
    result_label.config(text="Conversion completed!")

# Create the main GUI window
root = tk.Tk()
root.title("TIF to PDF Converter")

# Input Directory Label and Entry
input_directory_label = tk.Label(root, text="Input Directory:")
input_directory_label.pack()
input_directory_entry = tk.Entry(root, width=50)
input_directory_entry.pack()
input_browse_button = tk.Button(root, text="Browse", command=browse_input_directory)
input_browse_button.pack()

# Output Directory Label and Entry
output_directory_label = tk.Label(root, text="Output Directory:")
output_directory_label.pack()
output_directory_entry = tk.Entry(root, width=50)
output_directory_entry.pack()
output_browse_button = tk.Button(root, text="Browse", command=browse_output_directory)
output_browse_button.pack()

# Conversion Button
convert_button = tk.Button(root, text="Convert", command=start_conversion)
convert_button.pack()

# Result Label
result_label = tk.Label(root, text="")
result_label.pack()

# Start the GUI event loop
root.mainloop()
