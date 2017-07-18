import turtle

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(1)   
    

    n=4
    m=0
    while(m<n):
     
     brad.forward(100)
     brad.right(90)
     m=m+1
    
    #brad.forward(100)
    #brad.right(90)
    #brad.forward(100)
    #brad.right(90)
    #brad.forward(100)
    #brad.right(90)

    angie = turtle.Turtle()
    angie.shape("turtle")
    angie.color("green")
    angie.circle(100)
    
    window.exitonclick()
draw_art()
