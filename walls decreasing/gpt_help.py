import tkinter as tk

class BouncingSquareApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bouncing Square App")

        self.canvas = tk.Canvas(root, width=500, height=500, bg="white")
        self.canvas.pack()

        self.outer_rectangle_width = 300  # Increased the outer rectangle width
        self.outer_rectangle_height = 150  # Increased the outer rectangle height
        self.inner_square_size = 50
        self.bounce_factor = 2  # Increase speed upon collision

        # Create the outer rectangle
        self.outer_rectangle = self.canvas.create_rectangle(50, 50, 50 + self.outer_rectangle_width, 50 + self.outer_rectangle_height, outline="black")
        self.current_outer_width = self.outer_rectangle_width  # Track the current width

        # Initial position and direction of the inner square
        self.inner_square_x = 75
        self.inner_square_y = 75
        self.inner_square_direction = [2, 2]  # [2, 2] means down+right

        # Create the inner square
        self.inner_square = self.canvas.create_rectangle(self.inner_square_x, self.inner_square_y,
                                                         self.inner_square_x + self.inner_square_size,
                                                         self.inner_square_y + self.inner_square_size,
                                                         outline="red", fill="red")

        # Schedule the update method
        self.root.after(10, self.update)

    def update(self):
        # Move the inner square
        self.inner_square_x += self.inner_square_direction[0]
        self.inner_square_y += self.inner_square_direction[1]

        # Check for collisions with the outer rectangle walls
        if (
            self.inner_square_x <= 50
            or self.inner_square_x + self.inner_square_size >= 50 + self.current_outer_width
        ):
            # Change direction and apply a bounce effect on x-axis
            self.inner_square_direction[0] *= -1
            self.current_outer_width -= 2 * self.bounce_factor
            self.canvas.coords(self.outer_rectangle, 50, 50, 50 + self.current_outer_width, 50 + self.outer_rectangle_height)
            self.inner_square_x += self.inner_square_direction[0] * 3  # Move after updating coordinates
        if (
            self.inner_square_y <= 50
            or self.inner_square_y + self.inner_square_size >= 50 + self.outer_rectangle_height
        ):
            # Change direction and apply a bounce effect on y-axis
            self.inner_square_direction[1] *= -1
            self.outer_rectangle_height -= 2 * self.bounce_factor
            self.canvas.coords(self.outer_rectangle, 50, 50, 50 + self.current_outer_width, 50 + self.outer_rectangle_height)
            self.inner_square_y += self.inner_square_direction[1] * 3  # Move after updating coordinates

        # Move the inner square to its new position
        self.canvas.coords(self.inner_square, self.inner_square_x, self.inner_square_y,
                           self.inner_square_x + self.inner_square_size, self.inner_square_y + self.inner_square_size)

        # Check if the inner square has space to move
        if self.current_outer_width > self.inner_square_size and self.outer_rectangle_height > self.inner_square_size:
            # Schedule the next update
            self.root.after(10, self.update)

# Create the Tkinter root window and run the app
root = tk.Tk()
app = BouncingSquareApp(root)
root.mainloop()
