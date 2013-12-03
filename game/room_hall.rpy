label hall:

    scene room_hall

    if task_lexia == False:
        jump hall_lexia

    if has_sample == True
        jump hall_escape
    
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
        "Felix is discovered trying to stop the infection"

    else if suspect_jenkins == True:
        "Felix isn’t found, tries to stop the infection but it’s too late"

    return
