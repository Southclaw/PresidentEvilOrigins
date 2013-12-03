label lab:

    scene room_lab

    "You are in the Lab"

    if task_jenkins == False:
        jump lab_givetask

    else:
        jump lab_continue

label lab_givetask:

    char_jenkins "The president wants to talk to you about something."
    char_jenkins "Also, there's an odd looking sample I noticed in storage earlier\ncan you go grab it for me to analyze?"

    $ task_jenkins = True

    menu:
        "Go to hall":
            jump hall

label lab_continue:

    scene room_lab

    char_jenkins "Haven't you got me that sample yet? Get to it, it's important!"

    menu:
        "Go to hall":
            jump hall

