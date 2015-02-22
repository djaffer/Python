import turtle

def draw_square(color,length):
    tony = turtle.Turtle()
    tony.shape("turtle")
    tony.color(color)
    tony.hideturtle()
    tony.speed(2)
    i = 0
    while i<4:
        tony.forward(length)
        tony.right(90)
        i += 1
def draw_circle(color,radius):        
    anji = turtle.Turtle()
    anji.shape("arrow")
    anji.color(color)
    anji.circle(radius)

def draw_triangle(color,length):
    tri = turtle.Turtle()
    tri.shape("arrow")
    tri.color(color)
    i = 0
    
    while i<3:
        tri.forward(length)
        tri.right(120)
        i+=1

# Main
window = turtle.Screen()
window.bgcolor("red")
draw_square("blue",100)
draw_circle("blue",100)
draw_triangle("blue",100)
window.exitonclick()
