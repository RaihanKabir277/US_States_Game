
import turtle

screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

def get_mouse_click_coor(x,y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()   #it is the alternate version of screen.exitonclick()

# screen.exitonclick()
