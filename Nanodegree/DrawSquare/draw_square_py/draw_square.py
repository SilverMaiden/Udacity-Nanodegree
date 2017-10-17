import turtle

def draw_square_circle():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.speed(100)
    i = 0

    for j in range (1, 37):
        while i < 4:
            brad.forward(100)
            brad.right(90)
            i += 1
        i = 0
        brad.right(10)


def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)


window = turtle.Screen()
window.bgcolor("red")
draw_square_circle()
draw_circle()
window.exitonclick()
