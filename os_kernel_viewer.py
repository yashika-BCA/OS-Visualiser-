import tkinter as tk
from tkinter import ttk

KERNEL_TYPES = {
    "Monolithic": {
        "description": "All core services (FS, MM, drivers) run in kernel space. Fast but complex.",
        "kernel_space": ["System Call Interface", "File System", "Memory Manager", "Device Drivers"],
        "user_space": ["User Applications"]
    },
    "Microkernel": {
        "description": "Minimal kernel; services run in user space. More stable, but slower IPC.",
        "kernel_space": ["System Call Interface", "IPC", "Scheduler"],
        "user_space": ["User Applications", "File System", "Memory Manager", "Drivers"]
    },
    "Hybrid": {
        "description": "Core parts in kernel; some moved to modules. Balance of speed and stability.",
        "kernel_space": ["System Call Interface", "File System", "Scheduler", "HAL"],
        "user_space": ["User Applications", "Drivers"]
    },
    "Exokernel": {
        "description": "Bare kernel exposes hardware to apps. Max control, but complex.",
        "kernel_space": ["System Call Interface", "Resource Allocator"],
        "user_space": ["Apps with direct hardware libraries"]
    }
}

class KernelViewer(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("🧠 Kernel Architecture Visualizer")
        self.geometry("1000x700")
        self.config(bg="#1e1e1e")

        ttk.Label(self, text="Select Kernel Type:", font=("Segoe UI", 12)).pack(pady=10)
        self.kernel_option = ttk.Combobox(self, values=list(KERNEL_TYPES.keys()), state="readonly")
        self.kernel_option.set("Monolithic")
        self.kernel_option.pack()
        self.kernel_option.bind("<<ComboboxSelected>>", self.draw_kernel_diagram)

        self.canvas = tk.Canvas(self, width=900, height=500, bg="#1e1e1e", highlightthickness=0)
        self.canvas.pack(pady=20)

        self.desc_label = tk.Label(self, text="", font=("Segoe UI", 11), wraplength=800,
                                   fg="#cccccc", bg="#1e1e1e", justify="center")
        self.desc_label.pack()

        self.draw_kernel_diagram()

    def draw_kernel_diagram(self, event=None):
        self.canvas.delete("all")
        ktype = self.kernel_option.get()
        data = KERNEL_TYPES[ktype]

        # Draw user space
        self.canvas.create_rectangle(50, 50, 850, 230, fill="#2f2f2f", outline="#888")
        self.canvas.create_text(80, 40, anchor="nw", text="User Space", font=("Segoe UI", 12), fill="#00e0ff")
        y_offset = 70
        for item in data["user_space"]:
            self.canvas.create_rectangle(100, y_offset, 400, y_offset + 40, fill="#444", outline="#00ff88", width=2)
            self.canvas.create_text(250, y_offset + 20, text=item, fill="#ffffff", font=("Segoe UI", 11))
            y_offset += 50

        # Draw kernel space
        self.canvas.create_rectangle(50, 260, 850, 460, fill="#222", outline="#888")
        self.canvas.create_text(80, 250, anchor="nw", text="Kernel Space", font=("Segoe UI", 12), fill="#ff6666")
        y_offset = 280
        for item in data["kernel_space"]:
            self.canvas.create_rectangle(100, y_offset, 400, y_offset + 40, fill="#555", outline="#ffaa00", width=2)
            self.canvas.create_text(250, y_offset + 20, text=item, fill="#ffffff", font=("Segoe UI", 11))
            y_offset += 50

        self.desc_label.config(text=f"{ktype} Kernel → {data['description']}")
