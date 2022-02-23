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
    data_dict = data.to_dict()
    # print(data_dict)
    data_states_list = data.state.to_list()
    print(data_states_list[0])

    game_is_on = True
    c = turtle.getcanvas()
    right_guesses = []
    score = 0
    while(game_is_on):
        answer = screen.textinput(title="Guess the state", prompt="Guess another state's name")
        screen.listen()
        state = answer.lower()
        for i, state in enumerate(data_states_list):
            if answer.lower() == state.lower() :
                # Write name on the right coordinates on the map
                x = int(data[data.state == state].x)
                # Y is inverted in canvas coordinate system
                y = - int(data[data.state == state].y)
                c.create_text(x, y, text=state, angle=0, font=(FONT, FONT_SIZE, FONT_TYPE))
                right_guesses.append(state)
                score +=1
                print(f"Score: {score}")
    turtle.mainloop()

def get_mouse_click_coor(x, y):
    print(x, y)
if __name__ == '__main__':
    main()