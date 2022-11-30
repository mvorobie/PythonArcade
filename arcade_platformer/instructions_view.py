import arcade
from constants import *
from platformer_view import PlatformerView

class InstructionsView(arcade.View):
    """Show instructions to the player"""

    def __init__(self, title_view: arcade.View) -> None:
        """Create instructions screen"""
        super().__init__()
        self.title_view = title_view
        # Find the instructions image in the image folder
        instructions_image_path = (
            ASSETS_PATH / "images" / "instructions_image.png"
        )

        # Load our title image
        self.instructions_image = arcade.load_texture(instructions_image_path)

    def on_draw(self) -> None:
        # Start the rendering loop
        arcade.start_render()

        # Draw a rectangle filled with the instructions image
        arcade.draw_texture_rectangle(
            center_x=SCREEN_WIDTH / 2,
            center_y=SCREEN_HEIGHT / 2,
            width=SCREEN_WIDTH,
            height=SCREEN_HEIGHT,
            texture=self.instructions_image,
        )

    def on_key_press(self, key: int, modifiers: int) -> None:
        """Start the game when the user presses Enter

        Arguments:
            key -- Which key was pressed
            modifiers -- What modifiers were active
        """
        if key == arcade.key.RETURN:
            game_view = PlatformerView(self.title_view)
            game_view.setup()
            self.window.show_view(game_view)

        elif key == arcade.key.ESCAPE:
            self.window.show_view(self.title_view)
