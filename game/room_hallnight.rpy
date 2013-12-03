label hallnight:

    scene room_hallnight

    "You are in the Hall at night"

    if suspect_jenkins == True:
        jump ending_bad

    if suspect_lexia == True:
        jump ending_good
