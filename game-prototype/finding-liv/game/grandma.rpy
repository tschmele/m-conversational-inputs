label grandma:

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show grandma neutral at slightleft

    $ active_character = g

    # These display lines of dialogue.

    g """
    Hello darling, you are a detective, aren't you?
    
    I think I might need your [keyword.help].
    """

    $ collect_clue("grandma", "appearance")

    $ keyword_blacklist.discard("grandma")

    $ subkey_blacklist.discard("grandma")

    $ keyword_blacklist.discard("help")

label .help:
label .help_how:

    g "My [keyword.cat] Liv has gone missing and I cannot find her. Please, detective, you must find her! I'm worried sick."
    
    $ collect_clue("cat", "missing")

    $ collect_clue("grandma", "cat")

    $ keyword_blacklist.discard("cat")
    
    $ keyword_blacklist.discard("culprit")

    # this piece of dialogue will explain the basic keyword mechanics . this
    # will include an general explanation of how to detect , where to find 
    # and how to use them
    
    if not key_tutorial:

        jump player_input

    """
    To talk to a character, simply type what you wish to say into the dialogue box when prompted.

    If you ask about topics that the characters know about, they will answer your questions.
    """

    show screen keyword_box()

    """
    The [keyword.menu_on_screen] shows all currently discovered topics. [keyword.Click_on_them] to display the associated keywords.

    You can find a more detailed [keyword.list_of_keywords], including the exact words the game responds to, in the \"[keyword.Dictionary]\" menu. Either at the bottom of the screen or through the pause menu.

    Don't be discouraged if you don't get the answers you want in the first try. Maybe ask your questions again after you learned new information or got to know the characters better.
    """

label .tutorial_keyword:

    "Try it by asking her [keyword.how_long] her [keyword.cat] has been missing."

    $ p_in = renpy.input("You:", length=170)

    $ next_topic, evaluation = process_input(p_in, g)

    if next_topic != "cat_duration":

        "Make sure your spelling of the relevant keywords is correct to avoid misunderstandings."

        jump grandma.tutorial_keyword

    $ key_tutorial = False

    $ collect_clue("grandma", "deaf")

    jump expression active_character.name + '.' + next_topic

label .cat_missing:
label .cat_duration:

    if evaluation < 0:

        g """
        Oh my... You should really not be using such language, Detective.

        With that attitude, I'm afraid you might get in trouble with my [keyword.neighbours].
        """
    
        $ keyword_blacklist.discard("neighbours")
    
    elif evaluation > 0:
        
        g """
        What a polite Detective I have found! You look more reliable already.

        I'm sure you will get along great with my [keyword.neighbours]!
        """
    
        $ keyword_blacklist.discard("neighbours")
    
    g """
    She has been gone for over a day already. The last time I have seen my poor Liv was on friday.

    I still remember feeding her at noon, but when I prepared her food in the evening she wasn't there anymore.
    """

    $ collect_clue("cat", "duration")

    jump player_input

label .cat:
label .cat_about:
label .cat_noise:
label .cat_relationship:

    g """
    My [keyword.cat] is called Liv. She has been with me for over 10 years now. She never left for this long before. You have to believe me, Detective!

    Usually she just walks around the neighbourhood during the day and returns in the evening, when it is time for her food.

    Liv is the only white [keyword.cat] with black spots in our town. All of my [keyword.neighbours] should recognise her. Maybe someone has seen her?
    """

    $ collect_clue("cat", "about")

    $ keyword_blacklist.discard("neighbours")
    
    jump player_input

label .cat_appearance:

    g """
    Her fur used to be bright white with black spots everywhere. But just like me, Liv is growing old.

    By now her spots are almost as grey as my own hair. She is still hard to mistake for another [keyword.cat] in our small town.

    Please, Detective, I hope you can find her.
    """

    $ collect_clue("cat", "description")

    jump player_input

label .cat_behaviour:
label .cat_tips:

    g """
    She must be so lost out there without me...

    You have to know, Detective, Liv only eats the food I get for her. One of my [keyword.neighbours] even got scratched by her after trying to feed her the wrong brand.

    I still have some cans at home that you could take with you. Maybe she will come back on her own when she smells her food.
    """

    $ collect_clue("cat", "tipp1")

    $ collect_clue("grandma", "catfood")

    $ keyword_blacklist.discard("neighbours")
    
    jump player_input

label .cat_location:

    g """
    Oh if I knew where she was, I wouldn't be asking for your help, Detective.

    But she usually never goes far away. I don't think she ever even left our town.
    """

    $ collect_clue("cat", "location")

    jump player_input

label .dialogue_greeting:
label .dialogue_introduction:

    g """
    It is already too late for a \"Good Morning\", so I won't say that, but it's nice to meet you, Detective.
    
    You can just call me \"Grandma\" like everyone else. If I told you my name, people would just be confused by who you're talking about.
    """

    jump player_input

label .neighbours:
label .neighbours_who:

    g """
    Oh our little street is quite cozy. There are only 4 houses in our row and most of the families living in them have stayed the same since I started living there.

    The first house belongs to the Cloversons. After the death of Linda, her husband moved out and wanted to sell the house.

    In the end their son [keyword.Martin] decided to keep the house and is living there on his own.
    """
    
    $ collect_clue("martin", "introduction")

    $ keyword_blacklist.discard("martin")
    
    $ subkey_blacklist.discard("martin")
    
    g "The second house belongs to [keyword.me] and Liv. I was born there, you know? Ever since then I have been living in that street."

    $ collect_clue("grandma", "location")

    g """
    Kyle and Margot van Glean live in the third house. Although I remember Kyle had to go to the hospital last week, nothing too serious, Detective. No need to worry, just a routine check in.

    His knees aren't what they used to be. So now the doctors try to help him every now and then. But until they return, their son [keyword.Robert] is taking care of the house.
    """

    $ collect_clue("robert", "introduction")

    $ keyword_blacklist.discard("robert")
    
    $ subkey_blacklist.discard("robert")
    
    g """
    The last house is where the Brunner family has been living even since before my parents moved here.

    Their eldest son Frank and his wife [keyword.Christine] live their with their two children these days. 
    
    Smart [keyword.kids], I tell you. I'm sure they will get to study in the city when they grow older!
    """

    $ collect_clue("christine", "introduction")

    $ keyword_blacklist.discard("christine")
    
    $ keyword_blacklist.discard("kids")
    
    $ subkey_blacklist.discard("christine")
    
    $ subkey_blacklist.discard("kids")
    
    jump player_input

label .culprit:
label .culprit_who:
label .culprit_grandma:
label .culprit_martin:
label .culprit_robert:
label .culprit_christine:

    g "Do you suspect one of my [keyword.neighbours] took away my Liv? Certainly not, Detective." 
    
    if not "martin" in keyword_blacklist:

        g "[keyword.Martin] might seem a little rough around the edges, but he would never do something so cruel."
    
    $ collect_clue("grandma", "suspicion")

    $ keyword_blacklist.discard("neighbours")

    jump player_input

label .martin:
label .martin_about:
label .martin_name:
label .martin_relationship:

    g """
    Oh [keyword.Martin]... His father must be worried sick about him. But he found a job just recently, so I'm sure he will do just fine.

    He is actually a genius with computers, Detective. He manages to repair mine every time it breaks.

    If only he would put in a bit more effort, he would surely have a bright future ahead of him.
    """

    $ collect_clue("martin", "grandma")
    
    jump player_input

label .robert:
label .robert_about:
label .robert_name:
label .robert_relationship:

    g """
    [keyword.Robert] was always good with numbers even as a kid. I suspect he felt trapped in a small place like our little street.

    The boy took the first chance he got and moved to the big city. His parents were worried for years, but by now I heared he finished university and is working for a large bank.

    He would never admit to it, but I'm sure Robert enjoys it every time he gets a chance to come back here and spend time at his childhood home.
    """

    $ collect_clue("robert", "bigcity")
    
    jump player_input

label .robert_parents:

    g """
    Oh Kyle and Margot are not at home this weekend. They have to be at the clinic because of Kyle's knee.

    I'm sure you would get along great with them if they were here though.
    """

    $ collect_clue("robert", "parents")
    
    jump player_input

label .christine:
label .christine_about:
label .christine_name:
label .christine_relationship:

    g """
    Franks parents moved out really soon after he married [keyword.Christine] and had her move in with him.

    You didn't hear this from me, Detective, but I heard his parents were less than pleased that he would \"Bring an outsider into OUR town?!\" 
    
    After a heated argument they left to live at the retirement home since they couldn't drive out their sons wife.
    """

    $ subkey_blacklist.discard("inlaws")
    
    g """
    Their two [keyword.kids], [keyword.Josie] and [keyword.Sam], are really a handful for their parents. But I'm afraid you might not be able to meet them today.

    I gave the [keyword.kids] tickets to Disneyland for Christmas. Their father took them there this weekend and brought his parents along to let those poor [keyword.kids] meet their own grandparents.

    They are still hung up on the fact that [keyword.Christine] comes from the big city... So instead of stirring up old drama, she decided to stay home alone this time.
    """

    $ collect_clue("christine", "grandma")

    $ keyword_blacklist.discard("josie")
    
    $ keyword_blacklist.discard("sam")
    
    $ subkey_blacklist.discard("family")

    jump player_input

label .christine_inlaws:

    g"""
    Let's not dig too deep into other peoples drama. She will tell you herself if you ask politely, this is not mine to share.
    """

    jump player_input

label .christine_family:
label .kids:
label .kids_about:
label .kids_noise:

    g """
    Those two are probably the ones Liv gets along with the best in our entire street. They look after her when I am not at home.

    [keyword.Sam] used to always run up and down the street, chasing after Liv. It took a lot of convincing from his parents, that he shouldn't be so reckless.

    [keyword.Josie] told me she was going to be a Palo-Paleolo-... She really likes dinosaurs and wants to study them.

    If they get home while you are still there, you should ask her about it. She always gets so excited when she gets a chance to talk about her favourites.
    """

    $ keyword_blacklist.discard("josie")
    
    $ keyword_blacklist.discard("sam")
    
    $ subkey_blacklist.discard("dinosaurs")
    
    jump player_input

label .kids_location:
label .josie_location:
label .sam_location:

    g """
    They should be at Disneyland right now. I gave the [keyword.kids] tickets on Christmas and their father took them there this weekend.

    I hope they make the best out of it. It's just a shame that Christine couldn't come with them...
    """

    jump player_input

label .sam:
label .sam_about:

    g """
    [keyword.Sam] is always active. To my old bones it is a mystery how a kid that age can run around for that long. I could have sworn they spend more time sleeping.

    [keyword.Christine] had him try out for the junior team in a handball club in an effort to power him out enough that he would be calmer at home.

    It didn't quite work out as she had planned, but [keyword.Sam] took a liking to the sport. Last month he told me he would join a big team and become a star player in the future.
    """

    $ collect_clue("christine", "grandma_sam")
    
    $ subkey_blacklist.discard("handball")

    jump player_input

label .sam_handball:

    g"""
    I haven't seen the boy play myself yet. His parents tell me he is quite good at it, but I would like to watch one of his games myself one day.

    I'm sure he would agree if you asked him to play a few rounds.
    """

    jump player_input

label .josie:
label .josie_about:

    g """
    [keyword.Josie] is always busy at home, learning for school. Ever since she made up her mind about what she will study, all she worries about are her grades.

    She hasn't even brought home any friends from school yet. I'm worried that she is all alone at school. 
    
    Maybe that will change when she is surrounded by other people who also study Paeloto- the same as her?
    """

    $ collect_clue("christine", "grandma_josie")
    
    $ subkey_blacklist.discard("dinosaurs")

    jump player_input

label .josie_dinosaurs:

    g"""
    Oh, Josie and her dinosaurs...{w} It really brightens my day to see her so excited, but by now I have heard more different dinosaur names than I have met people.

    Make sure you have nothing urgent planned when you ask her about them, Detective.
    """

    jump player_input

label .culprit_kids:

    g """
    No the [keyword.kids] probably don't even know Liv is missing. They left with their father in the early afternoon, right when [keyword.Josie] came back from school.

    She has a lot of classes on fridays. Back in my days they didn't keep [keyword.kids] in their classrooms until 3 in the afternoon. At least not before highschool.
    """
    
    jump player_input

label .grandma_name:
    
    g """
    Oh, my how rude of me. I shoud've introduced myself before bothering you with my troubles.

    You can just call me \"Grandma\", deary. If I told you my actual name, noone would recognise it anyway. Everyone just calls me Grandma.
    """

    $ collect_clue("grandma", "name")

    jump player_input

label .grandma:
label .grandma_about:

    g """
    Oh there is not much interesting to say about me, Detective. I'm just an old lady that sits at home with my [keyword.cat].

    I just can't move around like I used to do when I was young... These days most of my time is spent reading books, taking care of my [keyword.plants] and preparing the next meal.

    My most exciting days are when I invite my [keyword.neighbours] over for tea. Trying new cake recipes brings me joy, but I couldn't eat a whole cake all on my own, you know?
    """

    $ collect_clue("grandma", "grandma")

    $ subkey_blacklist.discard("plants")

    jump player_input

label .grandma_plants:

    g "Ah yes, my beloved plants. I have..."

    "As Grandma starts talking, you feel your mind slipping.{w=5.0} An indetermined amount of time passes."

    g """
    ...but I shouldn't bore you with all this. We should worry about finding Liv first.
    """
    
    jump player_input

label .help_request:

    g"""
    I really can't do much more than give you a can of Liv's favourite food.

    If I still had the energy to search around my neighbourhood, I would've done so before coming to you, Detective. I'm really sorry.
    """

    jump player_input

label .robert_call:
label .martin_sayshi:
label .martin_alcohol:
label .martin_hungover:
label .christine_coffee:
label .grandma_relationship:
label .default:

    g """
    I'm sorry, darling. I did not quite understand what you want from me.
    """
    
    jump player_input

label .dialogue_leaving:
    
    menu help_her:

        g "Are you going to help me find Liv?"
        
        "Yes":
        
            jump grandma.help_confirmation
        
        "I have some more questions first":
        
            jump player_input
        
label .help_confirmation:

    g """
    Oh thank you so much, Detective! I hope you can find her quickly.

    But it is already so late today, Liv has probably found somewhere to hide for the night. 
    
    Also it is way too dark to be looking around outside and my [keyword.neighbours] should be asleep by now. 

    Here is my address. Why don't you start tomorrow morning and ask around if any of the [keyword.neighbours] have seen her?

    I wish you a good night, Detective. Good luck with your investigation!
    """

    $ collect_clue("grandma", "findcat")

    hide screen keyword_box

    menu finish_tutorial:
        "You are about to move on to the investigation. Do you wish to proceed?"
        "Continue asking questions":

            show screen keyword_box()
            
            jump player_input

        "Move on":
            
            $ keyword_blacklist.discard("neighbours")

            $ keyword_blacklist.discard("martin")
            
            $ keyword_blacklist.discard("robert")
            
            $ keyword_blacklist.discard("christine")
            
            $ subkey_blacklist.discard("martin")
            
            $ subkey_blacklist.discard("robert")
            
            $ subkey_blacklist.discard("christine")

            $ investigation_start = True
            
            hide grandma

            """
            With those words the old lady writes down her address and leaves your office.

            You decide to go to bed and start your investigation early the next morning...
            """

            show bg street

            show screen keyword_box()

            """
            This is where your investigation begins. To document your progress in the case, you brought your trusty notebook.

            [keyword.The_notebook] is accessible through the quickmenu at the bottom of your screen or via the pause menu. Try looking at it when you are unsure about how to continue.

            To start your investigation select the person you want to talk to and knock on their door. If you think you have solved the case, return to Grandma's house and tell her what you found.
            """

            call screen map()

label .insult:

    g "You should really not use this language... Especially while talking to my neighbours."

    jump player_input

label .solved:

    show bg missing

    hide screen keyword_box

    menu solve_case:

        g "Oh have you found her already?"

        "Try to solve the case":
            
            $ p_in = renpy.input("Where is Grandma's cat:")

            $ solved = solve_case(p_in)

            if solved == "almost":

                "You are almost there. Maybe try being more specifc..."

                jump grandma.solved
            
            if solved == "clues":

                "You are missing some information. Speak some more with the neighbours."

                hide screen keyword_box

                call screen map()

            if solved == True:

                jump end

            else:

                "That doesn't seem to be the answer..."

                hide screen keyword_box

                call screen map()

        "Continue looking for clues":

            hide bg missing

            hide screen keyword_box

            call screen map()