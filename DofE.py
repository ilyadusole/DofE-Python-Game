import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"


CHARACTER_SCALING = 1
TILE_SCALING = 0.5


class MyGame(arcade.Window):


    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)


        self.wall_list = None
        self.player_list = None


        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)

        #Set up the player placing it at coordinates.
        image_source = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.player_list.append(self.player_sprite)

        #Create the ground
        #This shows using a loop to place multiple sprites horizontally
        for x in range(0, 1250, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)

        #Put some crates on the ground
        # using a coordinate list to place
        coordinate_list = [[512, 96], [256, 96], [768, 96]]

        for coordinate in coordinate_list:
            #Add a crate on ground
            wall = arcade.Sprite(
                ":resources:images/tiles/boxCrate_double.png", TILE_SCALING
            )
            wall.position = coordinate
            self.wall_list.append(wall)
        
        pass

    def on_draw(self):

        self.clear()
        #draw sprites
        self.wall_list.draw()
        self.player_list.draw()

def main():

    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

