import turtle

var_straigh = 100
var_turn = 90
var_counter = 0

window = turtle.Screen()
window.bgcolor("black")
    
def draw_square():
    sqr = turtle.Turtle()
    sqr.shape("square")
    sqr.color("white")
    sqr.speed(3)

    for var_counter in range (0,4):
        sqr.forward(100)
        sqr.right(var_turn)
        var_counter = var_counter + 1
 
draw_square()  

def draw_circle():
    
    circle = turtle.Turtle()
    circle.shape("circle")
    circle.color("white")
    circle.circle(100)  
   
draw_circle()

def draw_triangle():
    triangle = turtle.Turtle()
    triangle.shape("triangle")
    triangle.color("white")

    var_counter = 0
    for var_counter in range (0,3):
        triangle.forward(100)
        triangle.left(120)

        var_counter = var_counter + 1
        
draw_triangle()
window.exitonclick()  

