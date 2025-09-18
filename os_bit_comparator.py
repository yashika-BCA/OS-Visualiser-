import tkinter as tk
from tkinter import ttk

BIT_SYSTEMS = {
    "16-bit": {
        "Pointer Size": "2 bytes",
        "Max Addressable Memory": "64 KB per segment",
        "Registers": "16-bit wide",
        "OS Example": "MS-DOS",
    },
    "32-bit": {
        "Pointer Size": "4 bytes",
        "Max Addressable Memory": "4 GB",
        "Registers": "32-bit wide",
        "OS Example": "Windows XP",
    },
    "64-bit": {
        "Pointer Size": "8 bytes",
        "Max Addressable Memory": "16 EB (theoretical)",
        "Registers": "64-bit wide",
        "OS Example": "Windows 11, modern Linux",
    },
}

class BitComparator(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("🧮 Bit-Size Comparator")
        self.geometry("900x600")
        self.config(bg="#1e1e1e")

        title = tk.Label(self, text="System Architecture: Bit-Width Comparison",
                         font=("Segoe UI", 18, "bold"), bg="#1e1e1e", fg="#00ff88")
        title.pack(pady=20)

        self.selection = ttk.Combobox(self, values=list(BIT_SYSTEMS.keys()), font=("Segoe UI", 14), state="readonly")
        self.selection.pack()
        self.selection.set("32-bit")
        self.selection.bind("<<ComboboxSelected>>", self.update_display)

        self.frame = tk.Frame(self, bg="#1e1e1e")
        self.frame.pack(pady=30)

        self.output_boxes = {}
        for i, label in enumerate(["Pointer Size", "Max Addressable Memory", "Registers", "OS Example"]):
            tk.Label(self.frame, text=label + ":", font=("Segoe UI", 13, "bold"),
                     bg="#1e1e1e", fg="#00d1b2", anchor="e", width=25).grid(row=i, column=0, padx=5, pady=8)

            val = tk.Label(self.frame, text="", font=("Segoe UI", 13),
                           bg="#1e1e1e", fg="#ffffff", anchor="w", width=40)
            val.grid(row=i, column=1, padx=5, pady=8)
            self.output_boxes[label] = val

        self.update_display()

        note = tk.Label(self, text="📌 Larger bit-systems support more RAM, wider pointers, and enhanced performance.",
                        font=("Segoe UI", 10), bg="#1e1e1e", fg="#aaaaaa")
        note.pack(pady=20)

    def update_display(self, event=None):
        selected = self.selection.get()
        for key, val in BIT_SYSTEMS[selected].items():
            self.output_boxes[key].config(text=val)
