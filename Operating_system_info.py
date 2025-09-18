import tkinter as tk
from tkinter import ttk
import mysql.connector
import ttkbootstrap as tb
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from os_layer import OSFlowSimulator  
from os_simulation import CommandSimulator
from os_bit_comparator import BitComparator
from os_kernel_viewer import KernelViewer
from os_memory_simulator import MemorySimulator




# ⚙️ MySQL Connection Config — update your user/pass here!
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root@2024",
    "database": "os_timeline"
}

def fetch_os_data():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("SELECT name, year, developer, company, about FROM operating_systems ORDER BY year ASC")
        data = cursor.fetchall()
        conn.close()
        return data
    except mysql.connector.Error as err:
        print("Database error:", err)
        return []

class OSTimelineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 OS Timeline Explorer Pro — MySQL Edition")
        self.root.geometry("1100x700")

        self.style = tb.Style("darkly")
        self.tab_control = ttk.Notebook(self.root)

        self.create_timeline_tab()
        self.create_graphs_tab()

        self.tab_control.pack(expand=True, fill="both")

    def create_timeline_tab(self):
        timeline_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(timeline_tab, text="📜 Timeline View")

        columns = ("Name", "Year", "Developer", "Company", "About")
        tree = ttk.Treeview(timeline_tab, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=160 if col != "About" else 400)

        data = fetch_os_data()
        for row in data:
            tree.insert("", "end", values=row)

        tree.pack(expand=True, fill="both", padx=10, pady=10)

    def create_graphs_tab(self):
        graph_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(graph_tab, text="📊 Chart View")

        os_data = fetch_os_data()
        year_counts = {}

        for _, year, *_ in os_data:
            # Handle year ranges like '1965–69' and '1960s'
            try:
                clean_year = int(str(year)[:4])
                year_counts[clean_year] = year_counts.get(clean_year, 0) + 1
            except:
                pass

        fig, ax = plt.subplots(figsize=(9.5, 8.8))
        ax.bar(year_counts.keys(), year_counts.values(), color="#00d1b2")
        ax.set_title("OS Releases per Year", fontsize=14)
        ax.set_xlabel("Year")
        ax.set_ylabel("Number of Releases")
        ax.grid(True, linestyle="--", alpha=0.6 )

        canvas = FigureCanvasTkAgg(fig, master=graph_tab)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=False, fill="both", padx=10, pady=10)

    
        # Optionally, add the button here:
        viz_btn = ttk.Button(self.root, text="🎬 Launch OS Flow Visualizer", command=self.open_visualizer)
        viz_btn.pack(pady=10)

        sim_btn = ttk.Button(self.root, text="🧠 Simulate Command Flow", command=self.open_sim)
        sim_btn.pack(pady=10)

        bit_btn = ttk.Button(self.root, text="📏 Compare Bit Systems", command=self.open_bit_viewer)
        bit_btn.pack(pady=10)

        btn_kernel = ttk.Button(self.root, text="🧬 Explore Kernel Types", command=self.open_kernel_viewer)
        btn_kernel.pack(pady=10)

        mem_btn = ttk.Button(self.root, text="🧮 Memory Simulator", command=self.open_memory)
        mem_btn.pack(pady=10)


    # 👇 Add this new method:
    def open_visualizer(self):
        OSFlowSimulator(self.root)

    def open_sim(self):
        CommandSimulator(self.root)

    def open_bit_viewer(self):
        BitComparator(self.root)

    def open_kernel_viewer(self):
        KernelViewer(self.root)

    def open_memory(self):
        MemorySimulator(self.root)


# 🌟 Run the App
if __name__ == "__main__":
    root = tb.Window(themename="darkly")
    app = OSTimelineApp(root)
    root.mainloop()
