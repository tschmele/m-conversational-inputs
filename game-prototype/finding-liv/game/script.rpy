# The script of the game goes in this file.

init python:
    from game.scripts.app_client import Client
    from game.scripts.profile import Profile
    from game.scripts.notebook import Notebook

    import json

    import string

    # open the keyword document from file

    all_keys = json.load(renpy.file('./data/keywords.json'))
    subkey_list = {}

    for mk in all_keys:
        sk = []
        for t in all_keys[mk]:
            sk.extend(all_keys[mk][t])
        subkey_list[mk] = sk

    client_socket = Client('9.tcp.eu.ngrok.io', 23051)      # host address should be stable 

    class textParser(object):
        def __init__(self, open_tag, close_tag):
            self._open = open_tag
            self._close = close_tag

        def __getattr__(self, text):
            words = text.split('_')
            
            return self._open + ' '.join(words) + self._close


    def add_history_entry(who, what, pop_last_entry=False):
        """
        A function to easily add an entry to the history log
        without displaying it to the player.
        by Feniks (renpy discord)

        Parameters:
        -----------
        who : Character
            The person who's saying this entry (or None if it's the narrator).
        what : string
            The text of the history entry.
        pop_last_entry : bool
            True if we should also remove the most recent entry to
            the history log (e.g. if you want to modify the last entry).
        """
        if pop_last_entry and store._history_list:
            store._history_list.pop()

        if who is None:
            who = store.narrator

        if isinstance(who, NVLCharacter):
            kind = "nvl"
        else:
            kind = "adv"
        who.add_history(kind, who.name, what)
    

    def find_keywords(utt, name):
        stripped = utt.lower().strip()
        stripped = stripped.translate(str.maketrans('', '', string.punctuation))

        print(stripped)

        main_key = set(stripped.split()) & (set(all_keys.keys()) | {"liv", "frank", "family", "sammy", "kyle", "margot", "assist", "children", "yourself", "yours", "plants", "culprits", "your", "you", "grandmas", "christines", "franks", "roberts", "martins", "livs"} )
        main_key.discard('dialogue')

        if "grandmas" in main_key:
            main_key.discard("grandmas")
            main_key.add("grandma")

        if "livs" in main_key:
            main_key.discard("livs")
            main_key.add("cat")

        if "christines" in main_key:
            main_key.discard("christines")
            main_key.add("christine")

        if "franks" in main_key:
            main_key.discard("franks")
            main_key.add("frank")

        if "roberts" in main_key:
            main_key.discard("roberts")
            main_key.add("robert")

        if "martins" in main_key:
            main_key.discard("martins")
            main_key.add("martin")

        sub_keys = {}
        topics = set()

        jumps = []

        if "coffee" in stripped and name == "mother":
            jumps.append('christine_coffee')
        if robert_sayhi and name == "banker":
            for k in all_keys["martin"]["sayshi"]:
                if k in stripped:
                    jumps.append('martin_sayshi')

        if len(main_key) > 0:

            if len({"kyle", "margot"} & main_key) > 0:
                main_key.discard("kyle")
                main_key.discard("margot")
                main_key.add("robert")
            if "liv" in main_key:
                main_key.discard("liv")
                main_key.add("cat")
            if "assist" in main_key:
                main_key.discard("assist")
                main_key.add("help")
            if "children" in main_key:
                main_key.discard("children")
                main_key.add("kids")
            if "sammy" in main_key:
                main_key.discard("sammy")
                main_key.add("sam")
            if "culprits" in main_key:
                main_key.discard("culprits")
                main_key.add("culprit")
            if len({"frank", "family"} & main_key) > 0:
                main_key.discard("frank")
                main_key.discard("family")
                main_key.add("christine")
            if (len({"yourself", "yours", "your"} & main_key) > 0) or ("you" in main_key and "called" in stripped) or ("you" in main_key and "culprit" in stripped):
                main_key.discard("yourself")
                main_key.discard("yours")
                if name == "drunk":
                    main_key.add("martin")
                if name == "banker":
                    main_key.add("robert")
                if name == "mother":
                    main_key.add("christine")
                if name == "grandma":
                    main_key.add("grandma")
            if "plants" in main_key:
                main_key.discard("plants")
                main_key.discard("grandma")
                main_key.add("grandma")
            main_key.discard("your")
            main_key.discard("you")

            for mk in main_key:

                sub_keys[mk] = [s for s in subkey_list[mk] if s in stripped]
                
                if len(sub_keys[mk]) > 0:
                    for k in sub_keys[mk]:
                        for t in all_keys[mk]:
                            if k in all_keys[mk][t]:
                                topics.add(t)

            if len(topics) > 0:
                for t in topics:
                    for mk in main_key:
                        if t in all_keys[mk]:
                            jumps.append('_'.join([mk, t]))
            else:
                for mk in main_key:
                    jumps.append(mk)

        sub_keys["dialogue"] = [s for s in subkey_list["dialogue"] if s in stripped]
        if len(sub_keys["dialogue"]) > 0:
            for sk in sub_keys["dialogue"]:
                if sk in all_keys["dialogue"]["leaving"]:
                    jumps.append('dialogue_leaving')
                    
                if sk in all_keys["dialogue"]["introduction"]:
                    jumps.append('dialogue_introduction')
                    
                if sk in all_keys["dialogue"]["greeting"]:
                    if "martin_sayshi" in jumps:
                        pass
                    else:
                        jumps.append('dialogue_greeting')
        else:
            jumps.append('default')
        
        print(jumps)

        if len(jumps) == 1:
            return jumps[0]
        elif len(jumps) > 1:
            for mk in all_keys:
                for sk in all_keys[mk]:
                    if sk == "greeting":
                        if name == "drunk":
                            drunk_greeted = True
                        if name == "banker":
                            banker_greeted = True
                        if name == "mother":
                            mother_greeted = True
                        continue
                    if sk == "introduction":
                        if name == "drunk":
                            drunk_introduced = True
                        if name == "banker":
                            banker_introduced = True
                        if name == "mother":
                            mother_introduced = True
                        continue
                    for j in jumps:
                        if mk in j and sk in j:
                            return j
            for j in jumps:
                if "dialogue" in j and "introduction" in j:
                    return j
                if "dialogue" in j and "greeting" in j:
                    return j

        return 'default'


    def process_input(utt, character):
        name = character.name

        add_history_entry(you, utt)

        # send the input to the server which analyses it and sends a response
        # detailing how polite the request was evaluated to be .

        try:
            evaluation = client_socket.loop(utt)
        except Exception:
            print(
                f"Main: Error: Exception for {message.addr}:\n"
                f"{traceback.format_exc()}"
            )
            evaluation = 0

        # TODO: general error handling

        if evaluation == None:
            evaluation = 0
        elif evaluation not in [-3, 0, 1, 2]:
            evaluation = 0

        # update the attitude based on the politeness-evaluation from the
        # server by adding the numerical reply to their attitude score .

        character.update_attitude(int(evaluation))

        key = find_keywords(utt, character.name)

        return (key, evaluation)
    
    
    def collect_clue(topic, clue):
        for c in all_clues[topic]:
            if c["clue"] == clue and not c["collected"]:
                c["collected"] = True
                if not player_notes[topic]:
                    player_notes[topic] = []
                player_notes[topic].append(c["note_text"])
                break


    def ask_confirmation(utt):
        stripped = utt.lower().strip()
        stripped = stripped.translate(str.maketrans('', '', string.punctuation))

        if "yes" in stripped:
            return True
        else:
            return False
        


    def solve_case(utt):
        # check if necessary clues were collected
        clues = [c["collected"] for c in all_clues["cat"] if c["clue"] in ["noise1", "noise2"]]

        if not False in clues:
            # now see what the player said
            answer = utt.lower().strip().translate(str.maketrans('', '', string.punctuation))

            house = set(answer.split()) & set(solutions["house"])
            location = set(answer.split()) & set(solutions["location"])

            if len(house) > 0 and len(location) > 0:
                return True
            elif len(house) > 0 or len(location) > 0:
                return "almost"

            return False

        else:
            return "clues"


# ---------------------------------------------------------------------------

# declare any new tranforms used in the game

transform slightleft:
    yalign 1.0
    xcenter 0.25

transform slightright:
    yalign 1.0
    xcenter 0.75

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define keyword = textParser("{color="+gui.accent_color+"}", "{/color}")

define you = Character("You", color="#3cb371")

define character.g = Character("Grandma", color="#9552f2", image="grandma", what_prefix='"', what_suffix='"')
default g = Profile("grandma", 1)

define character.b = Character("Robert", color="#9552f2", image="banker", what_prefix='"', what_suffix='"')
default b = Profile("banker", -1, [.5, 0, 0])

define character.d = Character("Martin", color="#9552f2", image="drunk", what_prefix='"', what_suffix='"')
default d = Profile("drunk", 0, [0, 0, 1])

define character.m = Character("Christine", color="#9552f2", image="mother", what_prefix='"', what_suffix='"')
default m = Profile("mother", 0, [0, 0, -1])

define note_button_names = {
    "cat":"Cat",
    "grandma":"Grandma",
    "martin":"Martin",
    "robert":"Robert",
    "christine":"Christine"
}

define solutions = {
    "house":["2","two","2nd","second","grandmas","your"],
    "location":["upstairs","attic","upper floor","trapped","locked"]
}

# declare any other remaining variables that should be kept per save-file
# through the default operator

default player_keywords = {
    "top_level":[]
}

default all_clues = json.load(renpy.file("./data/clues.json"))

default player_notes = {"cat":[], "grandma":[], "martin":[], "robert":[], "christine":[]}

default active_topic = 'grandma'

default keyword_buttons = dict()

default subkey_buttons = dict()

default active_character = g

default invited = None

default key_tutorial = True

default investigation_start = False

default keyword_blacklist = {"help", "cat", "culprit", "grandma", "martin", "robert", "christine", "kids", "josie", "sam", "neighbours"}

default subkey_blacklist = {"noise", "grandma", "martin", "robert", "christine", "kids", "plants", "alcohol", "hungover", "parents", "call", "sayshi", "family", "inlaws", "dinosaurs", "handball", "coffee"}

# default keyword_blacklist = {}

# default subkey_blacklist = {}

default menu_survey_link = "{a=https://www.umfrageonline.com/c/veifhdff}https://www.umfrageonline.com/c/veifhdff{/a}\n"

# ---------------------------------------------------------------------------

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # call screen map()

    scene bg office

    # show screen keyword_box(all_keys)

    # call screen map()

    # jump banker

    # $ collect_clue("cat", "missing")

    # $ collect_clue("cat", "description")

    # $ collect_clue("cat", "name")

    # call screen test_screen()

    """
    It was a late Saturday evening. The sun had almost set completely.

    The office to your private detective office had been as quiet today as it had been all week so far.

    You were just about to pack up and go home, when you heard a knock on the door and an old lady entered your office.
    """

    jump grandma

label player_input:

    $ p_in = renpy.input("You:", length=170)

    $ next_topic, evaluation = process_input(p_in, active_character)

    if evaluation < 0:

        jump expression active_character.name + '.insult'

    jump expression active_character.name + '.' + next_topic

label open_map():
    
    if investigation_start:

        call screen map()

    else:

        return

label end:

    hide screen keyword_box

    show bg found

    show grandma neutral at slightleft

    g "My poor Liv! I am so sorry for locking you in here."

    g "Thank you, Detective."

    if d.attitude < 0 or b.attitude < 0 or m.attitude < 0:

        g "I've heard some bad things about you from my neighbours, but at least you found my Liv."

    else:

        g "My neighbours seem to like you. Good thing I found such a fine Detective."

    hide grandma

    """
    Thank you for playing \"Finding Liv\". I hope you had a good time playing.
    
    This game was delevoped as part of {b}Masters Thesis{/b}. If you are willing to support me with this, it would help a lot if you could fill out my questionnaire.

    The questions revolve around your experience with this game. So sending in your answers would help a lot even if you did not enjoy your time here.
    """

    menu questionnaire:
        "Do you have 5-10 minutes to fill out the questionnaire?"
        "Yes, I want to support you":

            "Thank you! You can find it here: \n{a=https://www.umfrageonline.com/c/v39ggecz}https://www.umfrageonline.com/c/v39ggecz{/a}"

            $ menu_survey_link = "{a=https://www.umfrageonline.com/c/v39ggecz}https://www.umfrageonline.com/c/v39ggecz{/a}\n"

        "No, I'm sorry":

            "No problem. If you change your mind, you can still find the link from the Main Menu."

    "Have a nice day!"

    $ MainMenu(confirm=False)()
