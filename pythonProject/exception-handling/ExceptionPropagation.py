def son():
    # yaha exception throw ho raha hai
    raise RuntimeError("Lost My money")


def mom():

    try:
        son()  # call ho raha hai
    except RuntimeError as e:
        print(e)
        # yaha handle nahi ho raha → propagate hoga



def dad():
    mom()
      # yaha handle ho gaya


# main function jaisa
dad()