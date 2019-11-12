import arcade
import random

# Define constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.BLACK
GAME_TITLE = "Red_Dot_Fetch"
DOT_SIZE = 30
DOT_IMAGE = arcade.make_soft_circle_texture(DOT_SIZE, arcade.color.RED, 255, 120)


class dot(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = DOT_IMAGE
        self.center_x = random.randint(0, WINDOW_WIDTH)
        self.center_y = random.randint(0, WINDOW_HEIGHT)
        self.velocity = [random.randint(-4, 4), random.randint(-4, 4)]

    def on_update(self):
        if self.right > WINDOW_WIDTH:
            self.change_x *= -1
        if self.left < 0:
            self.change_x *= -1
        if self.top > WINDOW_HEIGHT:
            self.change_y *= -1
        if self.bottom < 0:
            self.change_y *= -1


red_dot = dot()


class red_dot_fetch(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
        self.red_dots = None

    def setup(self):
        """ Setup the game (or reset the game) """
        arcade.set_background_color(BACKGROUND_COLOR)
        self.red_dots = arcade.SpriteList()
        self.red_dots.append(red_dot)

    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()
        self.red_dots.draw()

    def on_update(self, delta_time):
        """ Called every frame of the game (1/GAME_SPEED times per second)"""

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        if dot.collides_with_point(x, y):
            self.red_dots.append(red_dot)
            self.red_dots.draw


def main():
    window = red_dot_fetch()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
