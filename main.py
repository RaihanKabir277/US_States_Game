
import turtle

screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# ---------retrive x,y coordinate from images ---------
# def get_mouse_click_coor(x,y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# ------------   end      --------------------------

answer_state = screen.textinput(title="Guess the state", prompt="Whats the another state's name?")
# print(answer_state)


turtle.mainloop()   #it is the alternate version of screen.exitonclick()

# screen.exitonclick()
