import turtle
import pandas

FONT = "Calibri"
FONT_SIZE = 10
FONT_TYPE = "normal"
ALIGNMENT = "center"
WIDTH = 725
HEIGHT = 491
DATA_FILE = "50_states.csv"
def main():
    screen = turtle.Screen()
    screen.setup(width = WIDTH + 10, height = HEIGHT + 10)
    turtle.screensize(canvwidth = WIDTH, canvheight = HEIGHT)
    screen.title("U.S. States Game")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)
    turtle.onscreenclick(get_mouse_click_coor)

    # Get data from csv file
    data = pandas.read_csv(DATA_FILE)
    data_states_list = data.state.to_list()

    c = turtle.getcanvas()
    right_guesses = []
    missing_states = []
    score = 0
    while(len(right_guesses) < 50):
        answer = screen.textinput(title=f"{len(right_guesses)}/50 States Correct", prompt="Guess another state's name").title()
        state = answer
        if answer == "Exit" or answer == "E":
            # generate states_to_learn.csv, contains states which haven't been guessed
            for state in data_states_list:
                if state not in right_guesses:
                    missing_states.append(state)
            print(missing_states)
            df = pandas.DataFrame(missing_states)
            print(df)
            df.to_csv("states_to_learn.csv")
            break
        if answer in data_states_list:
            # Write name on the right coordinates on the map
            x = int(data[data.state == state].x)
            # Y is inverted in canvas coordinate system
            y = - int(data[data.state == state].y)
            c.create_text(x, y, text=state, angle=0, font=(FONT, FONT_SIZE, FONT_TYPE))
            right_guesses.append(state)
            score +=1
            print(f"Score: {score}")

def get_mouse_click_coor(x, y):
    print(x, y)
if __name__ == '__main__':
    main()