import stage
import ugame


def game_scene():
    # this function is for the main game game_scene

    # image banks for circuitpython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_background, 10, 8)

    # create a sprite
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)

    # create a stage for the game
    game = stage.Stage(ugame.display, 60)
    # set the layers of all sprites
    game.layers = [ship] + [background]
    # renders the sprites
    game.render_block()

    # repeats game forever
    while True:

        game.render_sprites([ship])
        game.tick()

        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_RIGHT:
            ship.move(ship.x + 1, ship.y)
        if keys & ugame.K_LEFT:
            ship.move(ship.x - 1, ship.y)
        if keys & ugame.K_UP:
            ship.move(ship.x, ship.y - 1)
        if keys & ugame.K_DOWN:
            ship.move(ship.x, ship.y + 1)


if __name__ == "__main__":
    game_scene()
