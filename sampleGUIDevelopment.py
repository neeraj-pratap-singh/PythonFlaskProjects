import tkinter as tk

def on_button_click():
    label.config(text="Hello, Tkinter!")

# Create the main window
root = tk.Tk()
root.title("Simple Tkinter Window")

# Add a Label
label = tk.Label(root, text="Click the button to change this text.")
label.pack(pady=20)

# Add a Button
button = tk.Button(root, text="Click Me!", command=on_button_click)
button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
