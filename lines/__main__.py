import tkinter as tk
import random


# Function to draw a snowflake with 6 axes of symmetry
def draw_snowflake(canvas, center_x, center_y, size):
    colors = ["white", "blue", "purple", "grey", "magenta"]

    # Set the angle between each branch for 6 axes of symmetry
    angle_between_branches = 60

    # Draw 6 branches, each at a 60-degree separation
    for i in range(6):
        angle = i * angle_between_branches
        draw_branch(canvas, center_x, center_y, size, angle, random.choice(colors))


# Function to draw a single branch
def draw_branch(canvas, start_x, start_y, size, angle, color):
    branch_length = 10 * size
    for _ in range(3):
        for _ in range(3):
            end_x = start_x + branch_length * 0.1 * size * random.uniform(0.9, 1.1) * random.choice([1, -1])
            end_y = start_y + branch_length * 0.1 * size * random.uniform(0.9, 1.1) * random.choice([1, -1])
            canvas.create_line(start_x, start_y, end_x, end_y, fill=color, width=2)
            start_x, start_y = end_x, end_y
            angle += random.uniform(-45, 45)  # small variation to give it a natural fractal look


# Set up the Tkinter window and canvas
def main():
    # Create the main window
    root = tk.Tk()
    root.title("Snowflake")

    # Create a canvas to draw on
    canvas = tk.Canvas(root, width=600, height=600, bg="black")
    canvas.pack()

    # Draw multiple snowflakes
    for _ in range(20):
        x = random.randint(100, 500)
        y = random.randint(100, 500)
        size = random.randint(1, 4)
        draw_snowflake(canvas, x, y, size)

    # Start the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    main()
