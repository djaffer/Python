import turtle

#draws initial of my name 
def initials():
    anji = turtle.Turtle()  #instance of turtle defined as anji
    anji.shape("arrow") 
    anji.color("red")
    anji.pensize(3)

    #draws letter 'D' 
    anji.left(90)
    anji.backward(120)
    anji.right(90)
    anji.circle(60,180)

    #moves turtle backward with transparent color
    anji.color("")
    anji.backward(100)

    #draws letter 'J'
    anji.color("red")
    anji.backward(100)
    anji.forward(50)
    anji.left(90)
    anji.forward(90)
    anji.right(180)
    anji.circle(35,-170)
    anji.hideturtle()

#Main    
window = turtle.Screen()    #creates window for turtle
window.bgcolor("black")     #sets background color
initials()
window.exitonclick()        #exits window if clicked anywhere on screen
