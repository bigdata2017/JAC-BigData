import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("pink")
 
    sqr = turtle.Turtle()
    sqr.shape("triangle")
    sqr.color("yellow")
    sqr.speed (2)
              
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
