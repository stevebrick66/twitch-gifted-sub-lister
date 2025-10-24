import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

def parse_line(filename, GIFTED_SUBS_PER_ENTRY):
    try:
        with open(filename, 'r') as file:
            output_box.delete('1.0', tk.END)
            for line in file:
                words = line.split()
                if len(words) < 4:
                    continue
                username = words[0]
                try:
                    gifted_subs = int(words[3])
                except ValueError:
                    continue
                print_amount = gifted_subs // GIFTED_SUBS_PER_ENTRY
                for _ in range(print_amount):
                    output_box.insert(tk.END, f"{username}\n")
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def choose_file():
    filename = filedialog.askopenfilename(
        title="Select Subs File",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )
    if filename:
        file_path_var.set(filename)

def run_parser():
    filename = file_path_var.get()
    if not filename:
        messagebox.showwarning("Missing File", "Please select a file.")
        return
    try:
        GIFTED_SUBS_PER_ENTRY = int(entry_per_var.get())
        if GIFTED_SUBS_PER_ENTRY <= 0:
            raise ValueError
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a positive integer for how many gifted subs an entry will equal.")
        return

    parse_line(filename, GIFTED_SUBS_PER_ENTRY)

root = tk.Tk()
root.title("Twitch Gifted Sub Lister")
root.geometry("500x400")

file_path_var = tk.StringVar()
entry_per_var = tk.StringVar(value="5")

tk.Label(root, text="Select The File With Sub Info:").pack(pady=5)
tk.Entry(root, textvariable=file_path_var, width=40).pack()
tk.Button(root, text="Browse", command=choose_file).pack(pady=5)

tk.Label(root, text="Gifted Subs per Entry:").pack(pady=5)
tk.Entry(root, textvariable=entry_per_var, width=10).pack()

tk.Button(root, text="Run Parser", command=run_parser).pack(pady=10)

output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=10)
output_box.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

root.mainloop()
