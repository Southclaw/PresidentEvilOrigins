# screens
image room_lab = "img/env/lab.png"
image room_hall = "img/env/hall.png"
image room_storage = "img/env/storage.png"
image room_hallnight = "img/env/hallnight.png"

# characters
define char_felix = Character('Felix', color="#ff4700")
define char_jenkins = Character('Jenkins', color="#c8c8c8")
define char_lexia = Character('Lexia', color="#ffff00")
define char_kris = Character('Kris', color="#c8ffc8")

# variables
init:
    $ task_jenkins = False
    $ task_lexia = False
    
    $ suspect_lexia = False
    $ suspect_jenkins = False
    $ has_sample = False

label start:

    scene room_lab

    "Welcome to President Evil Origins!"

    jump lab

label end:

    return
