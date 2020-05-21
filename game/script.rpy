# The story of the game is in this file.

# ESN Cyan #00aeef
# ESN Magenta #ec008c
# ESN Green #7ac143
# ESN Orange #f47b20
# ESN Dark Blue #2e3192

# Main character assets
define b = Character("[name]")

# President assets
define prez = Character("President", color="#f47b20")
image prez_catsmile = im.FactorScale("prez_catsmile.png", 0.3, 0.3)
image prez_neutral = im.FactorScale("prez_neutral.png", 0.3, 0.3)
image prez_pout = im.FactorScale("prez_pout.png", 0.3, 0.3)
image prez_sad = im.FactorScale("prez_sad.png", 0.3, 0.3)
image prez_surprised = im.FactorScale("prez_surprised.png", 0.3, 0.3)

# Vicepresident assets
define vice = Character("Vicepresident", color="#7ac143")
image vice_angry = im.FactorScale("vice_angry.png", 0.3, 0.3)
image vice_curious = im.FactorScale("vice_curious.png", 0.3, 0.3)
image vice_happy = im.FactorScale("vice_happy.png", 0.3, 0.3)
image vice_normal = im.FactorScale("vice_normal.png", 0.3, 0.3)
image vice_surprised = im.FactorScale("vice_surprised.png", 0.3, 0.3)
image vice_worried = im.FactorScale("vice_worried.png", 0.3, 0.3)

# Backgrounds
image bg_door = im.FactorScale("bg_door.jpeg", 1, 1)
image bg_corridor = im.FactorScale("bg_corridor.jpeg", 0.3, 0.3)
image bg_meeting = im.FactorScale("bg_meeting.jpeg", 0.4, 0.4)
image bg_office = im.FactorScale("bg_office.jpeg", 0.4, 0.4)

# The game starts here.

label start:

    python:
        name = renpy.input(_("What's your name?"))

        name = name.strip() or __("Guy Shy")

    b "So this is office of ESN club. I just wonder why is it underground of probably the oldest university building..."

    scene bg_door with Dissolve(.5)
    "Knock-knock."
    vice "I'm coming, I'coming!"

    scene bg_corridor with Dissolve(.5)
    show vice_curious
    vice "Who could that..."
    show vice_happy
    vice "Oh! A new member!"
    prez "Vicepresident? Who are you talking to?"
    show prez_pout at right
    prez "I told you to finish that poster before we..."
    show prez_surprised at right
    prez "Newbie, huh? Ara, ara... let's talk in the meeting room..."
    show vice_worried
    vice "But President! I just wanted to take him to the office and register!"
    menu:
        "Go with the President.":
            jump meeting_with_prez

        "Go with the Vicepresident.":
            jump office_with_vice

label meeting_with_prez:
    $ went_with_prez = True
    b "Eeeh... yes, let's talk in the meeting room."
    show prez_catsmile at right

    scene bg_meeting with Dissolve(.5)
    show prez_neutral
    prez "Welcome [name]."

    jump chapter_1

label office_with_vice:
    $ went_with_prez = False
    b "Yes, I think I should register first."
    show vice_happy

    scene bg_office with Dissolve(.5)
    show vice_happy
    vice "Welcome [name]."

    jump chapter_1

label chapter_1:
    scene black
    "To be continued..."

    # This ends the game.

return
