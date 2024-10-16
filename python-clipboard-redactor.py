import tkinter as tk
import pyperclip
import re

# Function to search and replace sensitive info
def replace_sensitive_info(text):
    search_string = search_entry.get()
    replace_string = replace_entry.get()
    
    # Replace text based on input fields
    if search_entry:
        text = re.sub(re.escape(search_string), replace_string, text)
    return text

# Function to paste from clipboard into text box
def paste_from_clipboard():
    clipboard_content = pyperclip.paste()
    # Display the original clipboard content
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, clipboard_content)

# Function to process and replace sensitive info
def replace_and_copy_to_clipboard():
    content = text_box.get(1.0, tk.END)
    updated_content = replace_sensitive_info(content)
    # Replace content in the text box
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, updated_content)
    # Copy the updated content back to the clipboard
    pyperclip.copy(updated_content)

def clear_text_box():
    text_box.delete(1.0, tk.END)

# Create the GUI window
root = tk.Tk()
root.title("Clipboard Redactor")

# Text box for displaying and editing clipboard content
text_box = tk.Text(root, wrap='word', height=10, width=50)
text_box.pack(padx=10, pady=10)

# Clear button placed underneath textbox for contextual UI association
clear_button = tk.Button(root, text="Clear Text", command=clear_text_box)
clear_button.pack(pady=5)

# Manually adding input fields for search and replace strings:
search_label = tk.Label(root, text="Search for:")
search_label.pack()

search_entry = tk.Entry(root, width=35)
search_entry.pack()

replace_label = tk.Label(root, text="Replace with:")
replace_label.pack()

replace_entry = tk.Entry(root, width=30)
replace_entry.pack()

# Buttons to trigger actions
paste_button = tk.Button(root, text="Paste from Clipboard", command=paste_from_clipboard)
paste_button.pack(pady=5)

replace_button = tk.Button(root, text="Replace & Copy to Clipboard", command=replace_and_copy_to_clipboard)
replace_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear Text", command=clear_text_box)
clear_button.pack(pady=5)

# Run the GUI event loop
root.mainloop()
