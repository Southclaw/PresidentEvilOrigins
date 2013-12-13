label hall:

    scene room_hall

    if has_sample == True:
        jump hall_escape

    if task_lexia == False:
        jump hall_lexia

    jump hall_empty


label hall_lexia:

    "You are in the Hall"
    "Lexia is waiting for you"

    menu:
        "Talk to Lexia":
            jump hall_lexia_talk

        "Go get the sample from storage for Jenkins instead":
            jump hall_gotostorage


label hall_lexia_talk:

    char_lexia "Ah Felix! Just the person I need. I think that Jenkins is a\nterrorist trying to bring down our research from the inside!"

    char_lexia "I need you to go down to the storage room and grab the sample\nlabeled 'Z' in case Jenkins tried to alter it. Don't let him see you!"

    "Lexia leaves abruptly before you can respond."

    $ task_lexia = True
    $ suspect_jenkins = True

    menu:
        "Go to the storage room":
            jump storage

        "Go back into the lab":
            jump lab


label hall_gotostorage:

    "Lexia gives you a strange look as you rush past and head down to the storage room"
    $ suspect_lexia = True
    jump storage


label hall_empty:

    menu:
        "Go to the storage room":
            jump storage

        "Go back into the lab":
            jump lab


label hall_escape:

    if suspect_lexia == True:
        "Just as you thought, Lexia is waiting outside and sees you!"
        jump ending_bad

    else:
        "Lexia left the area earlier so the coast is clear to escape!"
        jump ending_good
