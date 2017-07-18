import turtle

def draw_square(some_turtle):
     for i in range(1,5):
         some_turtle.forward(100)
         some_turtle.right(90)
         
def turn_10(some_turtle):
     some_turtle.right(10)



def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(10)
    #draw_square(brad)
    for i in range(1,37):
       draw_square(brad)
       turn_10(brad)
    
    #angie = turtle.Turtle()
    #angie.shape("turtle")
    #angie.color("green")
    #draw_circle(angie)
    #angie.circle(100)
    
    window.exitonclick
draw_art()


    
