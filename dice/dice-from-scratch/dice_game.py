import dice_game_classes as dgc

d1 = dgc.dice()
d2 = dgc.dice()
d3 = dgc.dice()
d4 = dgc.dice()
d5 = dgc.dice()

dice = [d1, d2, d3, d4, d5]

game = dgc.game()

game.roll_dice(dice)
