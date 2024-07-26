    # while something_is_tru:
    #do something repeatedly


    # while not something_is_true: # while using negation
    #do some 





def jump():
    turn_left()
    while wall_on_right():
        move()
        turn_right()
        move() 
        turn_right()

    while front_is_clear():
        move()
    turn__left()



while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
