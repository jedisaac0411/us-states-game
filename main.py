import turtle
import pandas

state = turtle.Turtle()
screen = turtle.Screen()

bg_img = "blank_states_img.gif"
screen.addshape(bg_img)
turtle.shape(bg_img)
data_states = pandas.read_csv("50_states.csv")
state.penup()
state.hideturtle()
score = 0
total_states = len(data_states.state)
print(total_states)
is_true = True
guessed_answers = []
while is_true:
    answer_state = screen.textinput(title=f"{score}/{total_states}", prompt="What's another state?")
    screen.tracer(0)
    for i in data_states.state:
        if i.lower() == answer_state.lower():
            if answer_state.lower() not in guessed_answers:
                state_details = data_states[data_states.state == i]
                xcor = state_details.x
                ycor = state_details.y
                new_cor = (xcor.values[0], ycor.values[0])
                state.goto(new_cor)
                state.write(i)
                score += 1
                guessed_answers.append(answer_state)
                if score == total_states:
                    is_true = False
    screen.update()
    print(guessed_answers)
screen.exitonclick()
