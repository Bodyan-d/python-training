def lose(power_pellet_active, touching_ghost):
    """Trigger the game loop to end (GAME OVER) when Pac-Man touches a ghost without his power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player lost the game?
    """

    match power_pellet_active, touching_ghost:
        case True, True:
            return False
        case True, False:
            return False
        case False, True:
            return True
        case False, False:
            return False
    


print(lose(True, True))