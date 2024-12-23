import tkinter as tk
from tkinter import filedialog
import gzip
import zipfile
import py7zr
import threading
import os

def compress_file():
    input_file = input_file_entry.get()
    output_file = output_file_entry.get()
    format_choice = format_var.get()
    
    try:
        if not input_file or not output_file:
            raise ValueError("Please provide both input and output file paths.")
        
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file '{input_file}' not found.")
        
        if format_choice == "GZIP":
            with open(input_file, 'rb') as f_in, gzip.open(output_file + ".gz", 'wb', compresslevel=9) as f_out:
                f_out.writelines(f_in)
            result_label.config(text=f"File '{input_file}' compressed to '{output_file}.gz'")
        elif format_choice == "ZIP":
            with zipfile.ZipFile(output_file + ".zip", 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as zipf:
                zipf.write(input_file, arcname=os.path.basename(input_file), compress_type=zipfile.ZIP_DEFLATED)
            result_label.config(text=f"File '{input_file}' compressed to '{output_file}.zip'")
        elif format_choice == "RAR":
            with py7zr.SevenZipFile(output_file + ".rar", 'w') as archive:
                archive.write(input_file, compresslevel=9)  # Adjust compression level as needed
            result_label.config(text=f"File '{input_file}' compressed to '{output_file}.rar'")
        else:
            result_label.config(text="Invalid format selection.")
    except Exception as e:
        result_label.config(text=f"An error occurred: {e}")

def compress_file_async():
    threading.Thread(target=compress_file).start()

def decompress_file():
    input_file = input_file_entry.get()
    output_file = output_file_entry.get()
    format_choice = format_var.get()
    
    try:
        if not input_file or not output_file:
            raise ValueError("Please provide both input and output file paths.")
        
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file '{input_file}' not found.")
        
        if format_choice == "GZIP":
            with gzip.open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
                f_out.writelines(f_in)
            result_label.config(text=f"File '{input_file}' decompressed to '{output_file}'")
        elif format_choice == "ZIP":
            with zipfile.ZipFile(input_file, 'r') as zipf:
                zipf.extractall(output_file)
            result_label.config(text=f"File '{input_file}' decompressed to '{output_file}'")
        elif format_choice == "RAR":
            with py7zr.SevenZipFile(input_file, 'r') as archive:
                archive.extractall(path=output_file)
            result_label.config(text=f"File '{input_file}' decompressed to '{output_file}'")
        else:
            result_label.config(text="Invalid format selection.")
    except Exception as e:
        result_label.config(text=f"An error occurred: {e}")

def decompress_file_async():
    threading.Thread(target=decompress_file).start()

def browse_input_file():
    file_path = filedialog.askopenfilename()
    input_file_entry.delete(0, tk.END)
    input_file_entry.insert(0, file_path)

def browse_output_file():
    file_path = filedialog.asksaveasfilename()
    output_file_entry.delete(0, tk.END)
    output_file_entry.insert(0, file_path)

app = tk.Tk()
app.title("Compressor Elite")

input_file_label = tk.Label(app, text="Input File:")
input_file_label.pack()
input_file_entry = tk.Entry(app)
input_file_entry.pack()
input_file_button = tk.Button(app, text="Browse", command=browse_input_file)
input_file_button.pack()

output_file_label = tk.Label(app, text="Output File:")
output_file_label.pack()
output_file_entry = tk.Entry(app)
output_file_entry.pack()
output_file_button = tk.Button(app, text="Browse", command=browse_output_file)
output_file_button.pack()

compress_button = tk.Button(app, text="Compress", command=compress_file_async)
compress_button.pack()

decompress_button = tk.Button(app, text="Decompress", command=decompress_file_async)
decompress_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

format_var = tk.StringVar()
format_var.set("GZIP")
format_label = tk.Label(app, text="Select Compression/Decompression Format:")
format_label.pack()
format_menu = tk.OptionMenu(app, format_var, "GZIP", "ZIP", "RAR")
format_menu.pack()

app.mainloop()
