import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
 
    sqr = turtle.Turtle()
    sqr.forward(100)
    sqr.right(90)
    sqr.forward(100)
    sqr.right(90)
    sqr.forward(100)
    sqr.right(90)
    sqr.forward(100)
    sqr.right(90)

    window.exitonclick()

draw_square()
