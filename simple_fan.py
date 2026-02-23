import tkinter as tk
import math

class FanSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("2D Fan Simulation")

        self.angle = 0
        self.speed = 0

        self.canvas = tk.Canvas(root, width=400, height=400, bg="White")
        self.canvas.pack()

        self.speed_slider = tk.Scale(root, from_=0, to=100, orient="horizontal",label="(10-100)", length=300, command=self.update_speed)
        self.speed_slider.pack(pady=20)
        self.animate()
    def update_speed(self, val):
        self.speed = int(val)

    def draw_fan(self):
        self.canvas.delete("fan")
        center_x, center_y = 200, 200
        radius = 100

        for i in range(3):
            blade_angle = math.radians(self.angle + (i * 120))
            end_x = center_x + radius * math.cos(blade_angle)
            end_y = center_y + radius * math.sin(blade_angle)
            self.canvas.create_line(center_x, center_y, end_x, end_y, width=10,fill="blue", tags="fan")
        self.canvas.create_oval(190, 190, 210, 210, fill="black", tags="fan")
    def animate(self):
        if self.speed >= 10:
            self.angle += (self.speed / 10)
        self.draw_fan()

        self.root.after(20, self.animate)
if __name__ == ("__main__"):
    root = tk.Tk()
    app = FanSimulator(root)
    root.mainloop()
import tkinter as tk
import math

class FanSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("2D Fan Simulation")

        self.angle = 0
        self.speed = 0

        self.canvas = tk.Canvas(root, width=400, height=400, bg="White")
        self.canvas.pack()

        self.speed_slider = tk.Scale(root, from_=0, to=100, orient="horizontal",label="(10-100)", length=300, command=self.update_speed)
        self.speed_slider.pack(pady=20)
        self.animate()
    def update_speed(self, val):
        self.speed = int(val)

    def draw_fan(self):
        self.canvas.delete("fan")
        center_x, center_y = 200, 200
        radius = 100

        for i in range(3):
            blade_angle = math.radians(self.angle + (i * 120))
            end_x = center_x + radius * math.cos(blade_angle)
            end_y = center_y + radius * math.sin(blade_angle)
            self.canvas.create_line(center_x, center_y, end_x, end_y, width=10,fill="blue", tags="fan")
        self.canvas.create_oval(190, 190, 210, 210, fill="black", tags="fan")
    def animate(self):
        if self.speed >= 10:
            self.angle += (self.speed / 10)
        self.draw_fan()

        self.root.after(20, self.animate)
if __name__ == ("__main__"):
    root = tk.Tk()
    app = FanSimulator(root)
    root.mainloop()
