areas:
	lab
	hallway
	nighttime hallway
	storage

$ suspect_lexia
$ suspect_jenkins

In lab:
	char_jenkins ""

	task: go to storage room, get sample for jenkins
		lexia becomes suspicious of you working with jenkins to destroy the virus

	task: go talk to lexia in hallway

In hallway
	lexia wants you to bring the sample from storage
		jenkins becomes suspicious that you are working with lexia for evil

	after lexia, talk to Kris the janitor
	he says something is going on, you agree

In storage room:
choice:
	Hide the sample in your mouth and attempt an escape:
		ending: "Felix accidentally infects himself"

	Hide the sample in pocket:
		choice:
			"exit room to hallway"
				jump hallway
			"stay in room until 5PM"
				jump nighttime hallway

In hallway:
choice:
	leave the building
		if suspect_lexia
			ending: "Felix is discovered trying to stop the infection"

		if suspect_jenkins
			ending: "Felix isn’t found, tries to stop the infection but it’s too late"

In nighttime hallway:
choice:
	leave the building
		if suspect_jenkins
			ending: "Felix is discovered trying to stop the infection"

		if suspect_lexia
			ending: "Felix isn’t found, tries to stop the infection but it’s too late"
