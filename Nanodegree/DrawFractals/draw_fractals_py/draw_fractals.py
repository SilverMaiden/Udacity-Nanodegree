import turtle

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()

    brad.shape("turtle")
    brad.speed(700)
    brad.color("blue")
    i = 0
    for j in range (1, 37):
        while i < 3:
            brad.forward(100)
            brad.right(120)
            i += 1
        brad.right(10)
        i = 0

    for j in range(1, 37):
        while i < 4:
            brad.forward(120)
            brad.right(90)
            i += 1
        brad.right(10)
        i = 0

    for j in range(1, 37):
        while i < 4:
            brad.forward(130)
            brad.right(90)
            i += 1
        brad.right(20)
        i = 0


    window.exitonclick()



draw_flower()