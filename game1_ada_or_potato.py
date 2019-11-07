import arcade

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.BLACK
GAME_TITLE = "Introduction"
GAME_SPEED = 1/60

class ada(arcade.Sprite):
    timer: int

    def __init__(self):
        super().__init__("images/ada.png")
        self.timer = 0
        self.center_y = (WINDOW_HEIGHT/2)
        self.center_x = (WINDOW_WIDTH/2)

    def update(self):
        self.timer += (1/60)
        if (self.timer % 2) >= 0 and (self.timer % 2) < .9:
            self.alpha = 255
        else:
            self.alpha = 0




class potato(arcade.Sprite):
    timer: int

    def __init__(self):
        super().__init__("images/potato.png", scale=.15)
        self.timer = 0
        self.center_y = (WINDOW_HEIGHT/2)
        self.center_x = (WINDOW_WIDTH/2)

    def update(self):
        self.timer += (1/60)
        if (self.timer % 2) >= 1 and (self.timer % 2) < 1.9:
            self.alpha = 255
        else:
            self.alpha = 0





class ada_or_potato(arcade.Window):
    score: int
    timer: int
    def __init__(self):
        """ Initialize variables """
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
        self.logo_list = None
        self.score = 0
        self.timer = 0

    def setup(self):
        """ Setup the game (or reset the game) """
        arcade.set_background_color(BACKGROUND_COLOR)
        self.logo_list = arcade.SpriteList()
        self.logo_list.append(ada())
        self.logo_list.append(potato())
        self.score = 0
        self.timer = 0

    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()
        self.logo_list.draw()
        output = "Score:" + str(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_update(self, delta_time):
        """ Called every frame of the game (1/GAME_SPEED times per second)"""
        self.logo_list.update()
        self.timer += (1/60)

    def on_mouse_press(self, x, y, button, modifiers):
        if 0 <= (self.timer % 2) < .9:
            if (109.5 <= x <= 390.5) and (28 <= y <= 472):
                self.score += 1
        elif 1 <= (self.timer % 2) < 1.9:
            if (73 <= x <= 427) and (119.125 <= y <= 380.875):
                self.score -= 1



def main():
    window = ada_or_potato()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()