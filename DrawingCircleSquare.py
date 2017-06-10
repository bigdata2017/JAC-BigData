import turtle


def draw_square(some_turtle):
    for i in range(0,4):
        some_turtle.forward(100)
        some_turtle.right(90)           

def draw_art():        
    # Create window screen
    window = turtle.Screen()
    window.bgcolor("red")

    # Create turtle "brad"
    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("yellow")
    brad.speed(10)

    # Draw 50 squares
    for i in range (0, 24):
        draw_square(brad)
        brad.right(20)

    window.exitonclick()

draw_art()
