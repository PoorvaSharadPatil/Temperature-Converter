import turtle

def draw_petal(t):
    t.circle(100, 60)  # Draw a semicircle
    t.left(120)        # Turn left
    t.circle(100, 60)  # Draw another semicircle
    t.left(120)        # Turn left to original position

def draw_flower(t, petals):
    for _ in range(petals):
        draw_petal(t)
        t.left(360 / petals)  # Rotate to position for the next petal

def draw_stem(t):
    t.right(90)  # Point downwards
    t.forward(200)  # Draw the stem

def main():
    screen = turtle.Screen()
    screen.bgcolor("black")  # Set background color to black

    t = turtle.Turtle()
    t.color("blue")  # Petal color
    t.fillcolor("blue")  # Fill color for petals
    t.speed(10)  # Set the speed of drawing

    t.begin_fill()
    draw_flower(t, 6)  # Draw a flower with 6 petals
    t.end_fill()

    t.color("green")  # Change color for the stem
    t.pensize(5)  # Set the pen size for the stem
    draw_stem(t)

    # Write "FLOWER" at the bottom
    t.penup()
    t.goto(0, -250)  # Position for the text
    t.pendown()
    t.color("white")  # Text color
    t.write("FLOWER", align="center", font=("Arial", 24, "bold"))

    t.hideturtle()  # Hide the turtle after drawing
    screen.mainloop()  # Keep the window open

if __name__ == "__main__":
    main()