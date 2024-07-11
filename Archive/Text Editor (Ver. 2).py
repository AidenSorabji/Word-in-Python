import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
from tkinter.scrolledtext import ScrolledText
import platform

# Set up the root window
root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("800x1100")

# Set up the text area
text_area = ScrolledText(root, width=80, height=25, font=("Arial", 10))
text_area.pack(side="bottom", fill=tk.BOTH, expand=True, pady=2)

# Set up the font size slider 
def change_font_size(size):
    text_area.configure(font=("Arial", size))

font_slider = tk.Scale(root, from_=10, to=33, orient=tk.HORIZONTAL, command=change_font_size)
font_slider.pack(side="right", padx=5, anchor='nw')

# Create the buttons for bold, underline, and italic
button_frame = tk.Frame(root)
button_frame.pack(side="left", fill=tk.X)

bold_button = tk.Button(button_frame, text="Bold", command=lambda: toggle_bold(), font=("Arial", 10, "normal"), bd=0)
bold_button.pack(side="left", padx=5, anchor='nw')


underline_button = tk.Button(button_frame, text="Underline", command=lambda: toggle_underline(), font=("Arial", 10, "normal"), bd=0)
underline_button.pack(side="left", padx=5, anchor='nw')

italic_button = tk.Button(button_frame, text="Italics", command=lambda: toggle_italic(), font=("Arial", 10, "normal"), bd=0)
italic_button.pack(side="left", padx=5, anchor='nw')

# Define functions for toggling bold, underline, and italic styles
def toggle_bold():
    if "bold" in text_area.tag_names("sel.first"):
        text_area.tag_remove("bold", "sel.first", "sel.last")
        text_area.tag_configure("bold", font=("Arial", size, "normal"))
    else:
        wat = text_area.cget('size')
        text_area.tag_add("bold", "sel.first", "sel.last")
        text_area.tag_configure("bold", font=("Arial", size, "bold"))

def toggle_underline():
    if "underline" in text_area.tag_names("sel.first"):
        text_area.tag_remove("underline", "sel.first", "sel.last")
        text_area.tag_configure("underline", font=("Arial", size, "normal"))
    else:
        text_area.tag_add("underline", "sel.first", "sel.last")
        text_area.tag_configure("underline", font=("Arial", size, "underline"))

def toggle_italic():
    if "italic" in text_area.tag_names("sel.first"):
        text_area.tag_remove("italic", "sel.first", "sel.last")
        text_area.tag_configure("italic", font=("Arial", size, "normal"))
    else:
        text_area.tag_add("italic", "sel.first", "sel.last")
        text_area.tag_configure("italic", font=("Arial", size, "italic"))

# Set up the key bindings for bold, underline, and italic
root.bind("<Command-b>", lambda event: text_area.tag_add("bold", "sel.first", "sel.last"))
root.bind("<Command-u>", lambda event: text_area.tag_add("underline", "sel.first", "sel.last"))
root.bind("<Command-i>", lambda event: text_area.tag_add("italic", "sel.first", "sel.last"))

# Set up the key binding for deleting the current line
def delete_line(event):

    # Get the line number of the cursor and delete the entire line
    current_line = text_area.index(tk.INSERT).split('.')[0]
    text_area.delete(current_line + ".0", current_line + ".end")

# Bind Command-Delete to the delete_line function
root.bind("<Command-Delete>", delete_line)

# Set up the save button
def save_file():
    filename = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("fortnite Documents", "*.docx")])
    if filename:
        try:
            with open(filename, "w") as f:
                f.write(text_area.get("1.0", tk.END))
            messagebox.showinfo("File Saved", "File saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error saving file: {e}")

save_button = tk.Button(root, text="Save", command=save_file)
save_button.pack(side="right", padx=5,anchor='w')

# Set up the about button
def show_about():
    messagebox.showinfo("About", f"""Version 1.0.0

Copyright © 2019-2023 Aiden Sorabji
All Rights Reserved.""")

about_button = tk.Button(root, text="About", command=show_about)
about_button.pack(side="right", padx=5,anchor='w')


# Set up the tag configurations for bold, underline, and italic
text_area.tag_configure("bold", font=("Arial", 12, "bold"))
text_area.tag_configure("underline", font=("Arial", 12, "underline"))
text_area.tag_configure("italic", font=("Arial", 12, "italic"))

root.mainloop()
