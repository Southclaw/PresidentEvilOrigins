label hallnight:

    scene room_hallnight

    "You are in the Hall at night"

    if suspect_jenkins == True:
        "Jenkins is there waiting for you and knows you are up to something!"
        jump ending_bad

    else:
        "Jenkins has gone home for the night, the coast is clear and you can escape!"
        jump ending_good
