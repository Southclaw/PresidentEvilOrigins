label storage:

    scene room_storage

    "You are in the Storage Room"

    "The sample is on the shelf in front of you"

    if suspect_lexia == True:
        "But why did Jenkins tell you to hide it from Lexia?"

    else:
        "This sample that Lexia wanted looks like a bio-weapon! I should escape and dispose of it."

    menu:
        "Hide the sample in your mouth and attempt an escape":
            jump storage_death

        "Hide the sample in pocket":
            jump storage_survive

label storage_death:
    
    jump ending_dead


label storage_survive:

    $ has_sample = True

    "You have the sample hidden in your pocket now."

    if suspect_lexia == True:
        char_felix "I don't want to get caught with this... and Lexia was right outside a second ago!"

    else:
        char_felix "Lexia left after our talk, but Jenkins is probably getting suspicious... I should escape!"

    char_felix "Shall I risk leaving now or wait until later?"

    menu:
        "Exit the storage room":
            jump hall

        "Hide until 5PM":
            jump hallnight
