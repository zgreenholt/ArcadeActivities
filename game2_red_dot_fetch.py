import arcade
import random


# Define constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.BLACK
GAME_TITLE = "Red_Dot_Fetch"
GAME_SPEED = 1/60

class dot(arcade.Sprite):
    def __init__(self):
        super().__init__("images/dot.png")
        self.center_x = random.randint(1,500)
        self.center_y = random.randint(1,500)

class red_dot_fetch(arcade.Window):
    def __init__(self):
        """ Initialize variables """
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)

    def setup(self):
        """ Setup the game (or reset the game) """
        arcade.set_background_color(BACKGROUND_COLOR)

    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()

    def on_update(self, delta_time):
        """ Called every frame of the game (1/GAME_SPEED times per second)"""



def main():
    window = red_dot_fetch()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
