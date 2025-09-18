import tkinter as tk
from tkinter import ttk
import mysql.connector
import time

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root@2024",
    "database": "os_timeline"
}

def get_os_flow():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("SELECT layer_name, description FROM os_flow_components ORDER BY layer_order ASC")
        rows = cursor.fetchall()
        conn.close()
        return rows
    except mysql.connector.Error as err:
        print("DB error:", err)
        return []

class OSFlowSimulator(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("🔄 OS Flow Visualizer")
        self.geometry("1500x1000")
        self.resizable(True, True)

        self.canvas = tk.Canvas(self, bg="#1e1e1e", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.layers = get_os_flow()
        self.node_positions = []
        self.draw_os_layers()
        self.after(1000, self.animate_flow)

    def draw_os_layers(self):
        x, y = 100, 100
        for layer, desc in self.layers:
            box = self.canvas.create_rectangle(x, y, x+800, y+80, fill="#333", outline="#00d1b2", width=2)
            label = self.canvas.create_text(x+400, y+40, text=layer, fill="white", font=("Segoe UI", 16, "bold"))
            tooltip = self.canvas.create_text(x+400, y+105, text=desc, fill="#aaa", font=("Segoe UI", 10), width=760)
            self.node_positions.append((x+400, y+40))
            y += 130

    def animate_flow(self):
        circle = self.canvas.create_oval(90, 90, 110, 110, fill="#00ff88", outline="white")
        for cx, cy in self.node_positions:
            self.canvas.coords(circle, cx-10, cy-10, cx+10, cy+10)
            self.canvas.update()
            time.sleep(1)

        # Animate back up
        for cx, cy in reversed(self.node_positions):
            self.canvas.coords(circle, cx-10, cy-10, cx+10, cy+10)
            self.canvas.update()
            time.sleep(0.6)

        # Restart animation
        self.after(2000, self.animate_flow)
