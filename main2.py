import random
import string
import tkinter as tk
from tkinter import ttk, messagebox

def update_unused_chars(*args):
    try:
        kop = int(total_length_var.get() or 0)
        sim = int(symbols_var.get() or 0)
        cip = int(digits_var.get() or 0)
        liel = int(uppercase_var.get() or 0)
        maz = int(lowercase_var.get() or 0)
        lv_liel = int(latvian_uppercase_var.get() or 0)
        lv_maz = int(latvian_lowercase_var.get() or 0)
    except ValueError:
        unused_chars_var.set("Invalid input")
        return

    used_chars = sim + cip + liel + maz + lv_liel + lv_maz
    if used_chars > kop:
        unused_chars_var.set("Too many characters!")
    else:
        unused_chars_var.set(f"Unused characters: {kop - used_chars}")

# Function to generate passwords
def generate_passwords():
    try:
        kop = int(total_length_var.get())
        sim = int(symbols_var.get())
        cip = int(digits_var.get())
        liel = int(uppercase_var.get())
        maz = int(lowercase_var.get())
        lv_liel = int(latvian_uppercase_var.get())
        lv_maz = int(latvian_lowercase_var.get())
        b = int(num_passwords_var.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integer values.")
        return

    if sim > kop or cip > kop or liel > kop or maz > kop or lv_liel > kop or lv_maz > kop or kop < sim + cip + liel + maz + lv_liel + lv_maz:
        messagebox.showerror("Input Error", "Invalid input values. Please check your inputs.")
        return

    symbols = ['!', '@', '#', '$', '%', '^', '&', '*']
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    latvian_lowercase = ['ā', 'č', 'ē', 'ģ', 'ī', 'ķ', 'ļ', 'ņ', 'š', 'ū', 'ž']
    latvian_uppercase = ['Ā', 'Č', 'Ē', 'Ģ', 'Ī', 'Ķ', 'Ļ', 'Ņ', 'Š', 'Ū', 'Ž']

    output_text.delete(1.0, tk.END)
    for _ in range(b):
        parole = []

        for _ in range(maz):
            parole.append(random.choice(lowercase_letters))

        for _ in range(liel):
            parole.append(random.choice(uppercase_letters))

        for _ in range(cip):
            parole.append(str(random.randint(0, 9)))

        for _ in range(sim):
            parole.append(random.choice(symbols))

        for _ in range(lv_liel):
            parole.append(random.choice(latvian_uppercase))

        for _ in range(lv_maz):
            parole.append(random.choice(latvian_lowercase))

        random.shuffle(parole)
        parole = "".join(parole)
        output_text.insert(tk.END, parole + "\n")

# Set up the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x550")
root.resizable(False, False)

# Style configuration
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 10))
style.configure("TEntry", font=("Helvetica", 10))
style.configure("TButton", font=("Helvetica", 10, "bold"))

# Create the main frame
main_frame = ttk.Frame(root, padding="10 10 10 10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Labels and Entry fields
labels = [
    "Total Password Length:",
    "Number of Uppercase Letters:",
    "Number of Lowercase Letters:",
    "Number of Digits:",
    "Number of Symbols:",
    "Number of Latvian Uppercase Letters:",
    "Number of Latvian Lowercase Letters:",
    "Number of Different Passwords:"
]

variables = [
    total_length_var := tk.StringVar(),
    uppercase_var := tk.StringVar(),
    lowercase_var := tk.StringVar(),
    digits_var := tk.StringVar(),
    symbols_var := tk.StringVar(),
    latvian_uppercase_var := tk.StringVar(),
    latvian_lowercase_var := tk.StringVar(),
    num_passwords_var := tk.StringVar()
]

for i, (label_text, var) in enumerate(zip(labels, variables)):
    ttk.Label(main_frame, text=label_text).grid(row=i, column=0, sticky=tk.W, pady=2)
    entry = ttk.Entry(main_frame, textvariable=var, width=25)
    entry.grid(row=i, column=1, pady=2)
    var.trace_add('write', update_unused_chars)  # Update unused characters on input change

# Unused characters label
unused_chars_var = tk.StringVar()
ttk.Label(main_frame, textvariable=unused_chars_var, font=("Helvetica", 10, "bold")).grid(row=len(labels), column=0, columnspan=2, pady=5)

# Generate Button
ttk.Button(main_frame, text="Generate Passwords", command=generate_passwords).grid(row=len(labels)+1, column=0, columnspan=2, pady=10)

# Output Text Box
output_frame = ttk.Frame(root, padding="10 10 10 10")
output_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

output_text = tk.Text(output_frame, height=10, width=50, wrap=tk.WORD, font=("Helvetica", 10))
output_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Add a scrollbar to the output text box
scrollbar = ttk.Scrollbar(output_frame, orient=tk.VERTICAL, command=output_text.yview)
scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
output_text['yscrollcommand'] = scrollbar.set

root.mainloop()
