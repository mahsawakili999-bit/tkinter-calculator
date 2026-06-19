import tkinter as tk
root = tk.Tk()
root.title("ماشین حساب")
root.geometry("350x500")
root.resizable(False, False)
dark_mode = True
def click(value):
    entry.insert(tk.END, value)
def clear():
    entry.delete(0, tk.END)
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
def toggle_theme():
    global dark_mode
    if dark_mode:
        root.configure(bg="white")
        entry.configure(bg="white", fg="black", insertbackground="black")
        for btn in buttons:
            btn.configure(bg="#E0E0E0", fg="black")
        theme_btn.configure(bg="#CCCCCC", fg="black")
        dark_mode = False
    else:
        root.configure(bg="#1E1E1E")
        entry.configure(bg="#2D2D2D", fg="white", insertbackground="white")
        for btn in buttons:
            btn.configure(bg="#3C3F41", fg="white")
        theme_btn.configure(bg="#555555", fg="white")
        dark_mode = True
root.configure(bg="#1E1E1E")
entry = tk.Entry(
    root,
    font=("Arial", 24),
    justify="right",
    bg="#2D2D2D",
    fg="white",
    insertbackground="white"
)
entry.pack(fill="x", padx=10, pady=15, ipady=15)
theme_btn = tk.Button(
    root,
    text="🌙 / ☀",
    font=("Arial", 12),
    command=toggle_theme,
    bg="#555555",
    fg="white"
)
theme_btn.pack(pady=5)
frame = tk.Frame(root, bg=root["bg"])
frame.pack(expand=True, fill="both", padx=10, pady=10)
btn_texts = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]
buttons = []
row = 0
col = 0
for text in btn_texts:
    if text == "=":
        cmd = calculate
    elif text == "C":
        cmd = clear
    else:
        cmd = lambda t=text: click(t)
    btn = tk.Button(
        frame,
        text=text,
        font=("Arial", 18),
        bg="#3C3F41",
        fg="white",
        command=cmd
    )
    btn.grid(row=row, column=col, sticky="nsew", padx=3, pady=3)
    buttons.append(btn)
    col += 1
    if col > 3:
        col = 0
        row += 1
for i in range(4):
    frame.columnconfigure(i, weight=1)
for i in range(4):
    frame.rowconfigure(i, weight=1)
root.mainloop()