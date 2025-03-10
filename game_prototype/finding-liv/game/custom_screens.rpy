
## Keyword screen ##############################################################
##
## the keyword list the player currently knows

screen keyword_box(keys=all_keys):
    frame:
        # background "./gui/game_menu.png"
        area(1000, 0, 280, 535)
        viewport id "key_scroller":
            mousewheel True
            draggable True
            vbox:
                for key in keys:
                    if not key in keyword_blacklist:
                        python:
                            if key not in keyword_buttons:
                                keyword_buttons[key] = False

                            if key == "sayshi":
                                content = "says hi"
                            else:
                                content = key
                        vbox:
                            spacing 5
                            textbutton content:
                                action ToggleDict(keyword_buttons, key, true_value=True, false_value=False)
                                text_color gui.accent_color
                            if keyword_buttons[key]:
                                for k in keys[key]:
                                    if not k in subkey_blacklist:
                                        python:
                                            if k == "sayshi":
                                                content = "says hi"
                                            else:
                                                content = k
                                        textbutton "    " + content:
                                            text_color gui.text_color
        vbar value YScrollValue("key_scroller"):
            xalign 1.


## Notebook screen #############################################################
##
## the notebook collecting all the clues the player collected
## has several tabs sorted by clue topic on the left
## the right is a chronological list of all collected clues

# screen notebook_screen(notes=player_notes):
#     frame:
#         background "gui/overlay/main_menu.png"
#         padding (10, 30, 10, 0)
#         ysize 1.
#         has hbox
#         xfill True
#         vbox:
#             xsize 250
#             for topic in notes:
#                 if len(notes[topic]) < 1:
#                     continue
#                 textbutton topic:
#                     xpos .1
#                     action SetVariable("active_topic", topic)
#                     size_group "note_button"
#             textbutton "close":
#                 xpos .1
#                 ypos 1.
#                 action Return()

#         viewport id "key_scroller":
#             mousewheel True
#             draggable True
#             xsize .75
#             xalign 1.
#             vbox:
#                 for entry in notes[active_topic]:
#                     text entry xalign 0. color gui.text_color
#                     text "-----------" xalign 0. color gui.text_color
#         vbar value YScrollValue("key_scroller"):
#             xalign 1.   


screen notebook(notes=player_notes):
    tag menu
    use game_menu(_("Notebook"), scroll="viewport"):
        style_prefix "notebook"
        vbox:
            spacing 20
            hbox:
                spacing 15
                for topic in notes:
                    if len(notes[topic]) < 1:
                        continue
                    textbutton note_button_names[topic]:
                        action SetVariable("active_topic", topic)
                        text_selected_color gui.accent_color
            vbox:
                for entry in notes[active_topic]:
                    text entry xalign 0. color gui.text_color
                    text "-----------" xalign 0. color gui.text_color


## Map screen ##################################################################
##
## a screen showing the entire street this case plays out on
## clicking any house will navigate to their door and lets the player
## talk to the inhabitants
## clicking the grandma's house will trigger the "solve case" prompt

screen map():
    frame:
        background "bg street"
        padding(10, 30, 10, 0)
        ysize 1.
        xsize 1.
        textbutton "Talk to Martin" action Jump("drunk"):
            text_color gui.text_color
            text_hover_color gui.accent_color
            yalign .5
            xpos 200
        textbutton "Solve the case" action Jump("grandma.solved"):
            text_color gui.text_color
            text_hover_color gui.accent_color
            yalign .5
            xpos 450
        textbutton "Talk to Robert" action Jump("banker"):
            text_color gui.text_color
            text_hover_color gui.accent_color
            yalign .5
            xpos 750
        textbutton "Talk to Christine" action Jump("mother"):
            text_color gui.text_color
            text_hover_color gui.accent_color
            yalign .5
            xpos 1000


## Dictionary ##################################################################
##
## contains a dictionary for all currently unlocked keywords

screen dictionary(keys=all_keys):
    tag menu
    use game_menu(_("Dictionary"), scroll="viewport"):
        style_prefix "dictionary"
        label "Keywords"
        text _("Here you can find a list of all found keywords and the precise terms the game checks for. Refer to this if you have trouble getting the game to understand what you want to say.\n")
        vbox:
            for key in keys:
                if key in keyword_blacklist:
                    continue
                python:
                    if key not in keyword_buttons:
                        keyword_buttons[key] = False
                vbox:
                    spacing 0
                    textbutton key:
                        action ToggleDict(keyword_buttons, key, True, False)
                        text_color gui.accent_color

                    if keyword_buttons[key]:
                        for k in keys[key]:
                            if k in subkey_blacklist:
                                continue
                            python:
                                if k not in subkey_buttons:
                                    subkey_buttons[k] = False
                                if k == "sayshi":
                                    content = "says hi"
                                else:
                                    content = k
                            textbutton "    " + content:
                                action ToggleDict(subkey_buttons, k, True, False)
                                text_color gui.text_color
                                
                            if subkey_buttons[k]:
                                for w in keys[key][k]:
                                    text "        \"" + w + "\"":
                                        color gui.text_color


## Questionnaire ###############################################################
##
## add to the main menu 
## contians a link to the questionnaire and some lore ?

screen questionnaire():
    tag menu
    use game_menu(_("Thesis Feedback"), scroll="viewport"):
        style_prefix "questionnaire"
        vbox:
            label "Created by"
            text _("@the_first_lilly (on Discord)\n")
            label "Art by"
            text _("@annotherdemon (on Discord and Instagram)\n\n")
            label "Support the project:"
            text _("This game was created as part of my Masters Thesis. If you want to help me out, you could fill out the following questionnaire after trying the game (5-10 minutes):")
            text _(menu_survey_link)
            label "About my thesis"
            text _("The thesis is titled {b}\"Being Polite is a Choice: Trying to Create Immersion through Conversational Inputs and adequate Reactions to the Player's Manners in Role-Playing Games\"{/b}")
            text _("With this game and your responses from the questionnaire, I am trying to find out whether having the freedom to write your own side of the dialogue immerses the player into the story.")
            text _("The hypothesis is that this will motivate the player to treat the characters more like people, which will lead to a feeling of having actual conversations opposed to just clicking through a menu with regular dialogue trees.")

