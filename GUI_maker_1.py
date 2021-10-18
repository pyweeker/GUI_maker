import arcade
import ast

"""
https://github.com/pythonarcade/arcade/issues/1017
"""


# Set how many rows and columns we will have
ROW_COUNT = 100

COLUMN_COUNT = 200

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 10
HEIGHT = 10

# This sets the margin between each cell
# and on the edges of the screen.
#MARGIN = 5
MARGIN = 0

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN
SCREEN_TITLE = "Array Backed Grid Buffered Example"

white = arcade.color.WHITE

green = arcade.color.GREEN
red = arcade.color.RED
blue = arcade.color.BLUE
amber = arcade.color.AMBER
ao = arcade.color.AO
champagne = arcade.color.CHAMPAGNE
yellow = arcade.color.YELLOW
violet = arcade.color.VIOLET
#grey = arcade.color.GREY


colors_list = [green,red,blue,amber,ao,champagne,yellow,violet]


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """
        Set up the application.
        """
        super().__init__(width, height, title, fullscreen = True)

        arcade.set_background_color(arcade.color.BLACK)

        # One dimensional list of all sprites in the two-dimensional sprite list
        self.grid_sprite_list = arcade.SpriteList()

        # This will be a two-dimensional grid of sprites to mirror the two
        # dimensional grid of numbers. This points to the SAME sprites that are
        # in grid_sprite_list, just in a 2d manner.
        self.grid_sprites = []

        self.clickeds = arcade.SpriteList()

        self.registereds = arcade.SpriteList()

        #self.shape_list = arcade.SpriteList()
        self.shape_list = arcade.ShapeElementList()

        self.data_export = list()

        self.copy_mode = False

        self.loaded_datas = list()

        




        # Create a list of solid-color sprites to represent each grid location
        for row in range(ROW_COUNT):
            self.grid_sprites.append([])
            for column in range(COLUMN_COUNT):
                x = column * (WIDTH + MARGIN) + (WIDTH / 2 + MARGIN)
                y = row * (HEIGHT + MARGIN) + (HEIGHT / 2 + MARGIN)
                sprite = arcade.SpriteSolidColor(WIDTH, HEIGHT, arcade.color.WHITE)
                sprite.center_x = x
                sprite.center_y = y
                self.grid_sprite_list.append(sprite)
                self.grid_sprites[row].append(sprite)



        self.copy_sprite = None
        self.copylist = arcade.ShapeElementList()



    @property
    def last_p(self):
        last_point = tuple((self.clickeds[-1].center_x, self.clickeds[-1].center_y))
        return last_point


    @property
    def last_c(self):
        last_point = tuple((self.clickeds[-1].center_x, self.clickeds[-1].center_y))

        column = int(self.last_p[0] // (WIDTH + MARGIN))
        row = int(self.last_p[1] // (HEIGHT + MARGIN))

        return tuple((column, row))


    @property
    def current_color(self):

        len_shape_list = len(self.shape_list)

        #if len_shape_list == 0:
        #    return arcade.color.GREEN
        #else:
        #    return colors_list[len(self.shape_list) -1]

        return colors_list[len(self.shape_list) -1]


    def setup(self):

       pass
    

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        self.grid_sprite_list.draw()

        if len(self.clickeds) > 0:
            arcade.draw_text(f" {self.last_p} {self.last_c}  ", 1700, 500,arcade.color.YELLOW, 17, width=25, align="center")



        if len(self.shape_list) > 0:
            self.shape_list.draw()

        if self.copy_mode is True:
            
            if len(self.copylist) > 0:
                

                self.copylist.draw()


        



    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """

        # Change the x/y screen coordinates to grid coordinates
        column = int(x // (WIDTH + MARGIN))
        row = int(y // (HEIGHT + MARGIN))

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        if row < ROW_COUNT and column < COLUMN_COUNT:

            # Flip the location between 1 and 0.
            if self.grid_sprites[row][column].color == arcade.color.WHITE:
                #self.grid_sprites[row][column].color = arcade.color.GREEN
                self.grid_sprites[row][column].color = self.current_color




                self.clickeds.append(self.grid_sprites[row][column])
            else:
                self.grid_sprites[row][column].color = arcade.color.WHITE

                for clicked in self.clickeds:
                    if clicked is self.grid_sprites[row][column]:
                        self.clickeds.remove(clicked)


                        print(f" self.clickeds.remove(clicked)  {clicked} ")

                        self.grid_sprites.remove([row][column])

                        print(f" self.grid_sprites.remove([row][column])   ")


                        idx_2_kill = row * column

                        self.grid_sprite_list.remove(idx_2_kill)



    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            #self.grid_sprite_list.pop()

            last_clicked = self.clickeds[-1]

            for grigri in self.grid_sprite_list:
                if grigri == last_clicked:
                    grigri.color = arcade.color.WHITE



            self.clickeds.pop()

            

        


        if key == arcade.key.SPACE:

            print(f"  self.registereds {self.registereds}   len {len(self.registereds)}  ")

            for registar in self.registereds:
                print(f" -registar  {registar} ")


            self.registereds.append(self.clickeds[-2])
            self.registereds.append(self.clickeds[-1])

            reg0 = self.registereds[0]
            reg1 = self.registereds[1]

            print(f" ____reg0  {reg0} ")
            print(f" reg1  {reg1} ")

            

            print(f"  self.clickeds[-2] {self.clickeds[-2]}     ")
            print(f"  self.clickeds[-1] {self.clickeds[-1]}     ")

            print(f"  self.registereds {self.registereds}     len {len(self.registereds)}  ")

            for registar in self.registereds:
                print(f" -registar  {registar} ")

            print(f"  reg0 {reg0}    reg1 {reg1} ")

            #current_rect = arcade.create_rectangle_filled(reg0.center_x, reg0.center_y, reg1.center_x - reg0.center_x, reg0.center_y - reg1.center_y, color=arcade.color.GREEN)
            

            #current_rect = arcade.create_rectangle_filled(reg0.center_x, reg0.center_y, abs(reg1.center_x - reg0.center_x), abs(reg0.center_y - reg1.center_y), color=arcade.color.GREEN)
            
            #current_rect = arcade.create_rectangle_filled(reg0.center_x +0.5*abs(reg1.center_x - reg0.center_x), reg0.center_y -0.5*abs(reg0.center_y - reg1.center_y), abs(reg1.center_x - reg0.center_x), abs(reg0.center_y - reg1.center_y), color=arcade.color.GREEN)
            current_rect = arcade.create_rectangle_filled(reg0.center_x +0.5*abs(reg1.center_x - reg0.center_x), reg0.center_y -0.5*abs(reg0.center_y - reg1.center_y), abs(reg1.center_x - reg0.center_x), abs(reg0.center_y - reg1.center_y), color=self.current_color)



            #current_rect = arcade.draw_xywh_rectangle_filled(reg0.center_x, reg0.center_y, abs(reg1.center_x - reg0.center_x), abs(reg0.center_y - reg1.center_y), color=arcade.color.GREEN)

            self.shape_list.append(current_rect)

            print(f"  self.shape_list  {self.shape_list}    {len(self.shape_list)}    ")

            self.clickeds = self.clickeds[2:]

            self.registereds = self.registereds[2:]


            print(f"current_rect  {current_rect} ")

            print(f"current_rect.__dict__  {current_rect.__dict__} ")


            #del reg0
            #del reg1


            #self.grid_sprite_list.pop()

            print("\n\n\n")
            print("------------------------------------------")

            print(f" reg0.center_x  {reg0.center_x}  reg0.center_y  {reg0.center_y} ")
            print(f"                                                                                    reg1.center_x  {reg1.center_x}  reg1.center_y  {reg1.center_y} ")
            print(f" width  {abs(reg1.center_x - reg0.center_x)}  height  {abs(reg0.center_y - reg1.center_y)} ")
            print(f" self.current_color  {self.current_color} ")
            print("\n\n\n")

            rectx = reg0.center_x
            recty = reg0.center_y

            width = abs(reg1.center_x - reg0.center_x)
            height = abs(reg0.center_y - reg1.center_y)

            #rect_export = tuple((rectx, recty, width, height))
            rect_export = tuple((rectx, recty, width, height, self.current_color))

            print("------->>>>>>>>>>>>>>>>>>>>")

            print("rect_export = ", rect_export)

            self.data_export.append(rect_export)

            print("self.data_export = ", self.data_export)




    def on_key_release(self, key, modifiers):


        if key == arcade.key.C:

            print(f"  self.copy_mode = {self.copy_mode}   ")

            self.copy_mode = True

            self.copylist.append(self.shape_list[-1])


        if key == arcade.key.ENTER:

            #print(f"  self.copy_mode = {self.copy_mode}   ")

            newfile = "./exportfiles/rects.txt"

            with open(newfile, 'w') as outfile:
                outfile.write(str(self.data_export))
                
                #for rect in self.data_export:
                    #outfile.write(rect)         # TypeError: write() argument must be str, not tuple
                    #outfile.write(str(rect))

        if key == arcade.key.L:

            #print(f"  self.copy_mode = {self.copy_mode}   ")

            savfile = "./exportfiles/rects.txt"

            with open(savfile, 'r') as infile:
                infile_content = infile.read().split('\n')
                print(f" infile_content = {infile_content}    type {type(infile_content)}")

                #self.loaded_datas = ast.literal_eval(infile_content)    # ['(305.0, 895.0, 280.0, 300.0, (255, 0, 0))(605.0, 885.0, 410.0, 110.0, (0, 0, 255))(605.0, 765.0, 400.0, 170.0, (255, 191, 0))(315.0, 585.0, 710.0, 370.0, (0, 128, 0))(1045.0, 875.0, 520.0, 670.0, (247, 231, 206))']
                self.loaded_datas = ast.literal_eval(infile_content[0])

                for rect in self.loaded_datas:
                    current_rect = arcade.create_rectangle_filled(*rect)
                    self.shape_list.append(current_rect)



            






    def on_mouse_motion(self, x, y, dx, dy):





        if len(self.copylist) >0:
            self.copylist[-1].center_x = x
            self.copylist[-1].center_y = y



def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()