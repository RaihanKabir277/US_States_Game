
import turtle
import pandas

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

# answer_state = screen.textinput(title="Guess the state", prompt="Whats the another state's name?").title()
# print(answer_state)
# --------if the user cancel the dialog box then it will give the error cause the user does not input anythings------------------

data = pandas.read_csv("50_states.csv")
states = data["state"]
states_list = states.to_list()

guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Whats the another state's name?")
    if answer_state:
        answer_state = answer_state.title()


    # for state_name in states_list:
    #     if state_name == answer_state:
    #         row = data[data.state == state_name]
    #         turtle.goto(int(row.x), int(row.y))
    #         turtle.penup()
    #         turtle.write(f"{state_name}",align="center",font=("Courier", 15, "normal"))

    if answer_state == "Exit":
        missing_states = []
        for state in states_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("learning_states.csv")

        break
    if answer_state in states_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        row = data[data.state == answer_state]
        t.goto(row.x.item(), row.y.item())
        t.write(answer_state)





# turtle.mainloop()   #it is the alternate version of screen.exitonclick()

# screen.exitonclick()
