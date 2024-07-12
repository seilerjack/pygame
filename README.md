# pygame

Follows generally the program flow below:

while True:
    events()    - proceeds events like pressed keys, mouse motion etc.
    loop()      - compute changes in the game world like NPC's moves, player moves, AI, game score.
    render()    - print out on the screen graphic.