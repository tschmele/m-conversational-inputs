default mother_visit = 0
default mother_greeted = False
default mother_introduced = False
default mother_knowsmissing = False
default mother_knowsduration = False
default mother_aboutkids = False
default mother_coffee = False
default mother_goodbye = None

label mother:

    $ active_character = m

    scene bg christine

    hide screen keyword_box

    menu ring_mother:
        
        "\"Brunner\" is written on the Doorbell"

        "Ring the Doorbell":

            if mother_goodbye == None:

                $ mother_goodbye = False

            show screen keyword_box()

            show mother neutral at slightleft

            if mother_visit == 0:

                "A young woman in simple but comfortable clothes stands in the door."

                "She is giving you an exhausted look."
            
                m "Yes? Hello? How can I help you?"

                $ collect_clue("martin", "introduction")

            else:

                if m.attitude < 0:

                    m angry "Got any more intrusive questions?"

                else:

                    if not mother_goodbye:

                        m neutral "You surprised me last time, when you just left without a word."

                    m happy "Welcome back, Detective. Have you found Liv yet?"

                show mother neutral at slightleft

            $ mother_visit += 1

            $ collect_clue("christine", "appearance")

            $ mother_goodbye = False

            jump player_input
 
        "Leave":

            show screen keyword_box()

            call screen map()

label .dialogue_greeting:

    if not mother_greeted:

        $ m.update_attitude(1)

        if not mother_introduced:

            if m.attitude < 0:

                m "At least introduce yourself first."

            else:

                m "Hello there. I'm Christine, who are you?"

        else:

            if m.attitude < 0:

                m "I have things to attend to in the house. Make it quick."

            else:

                m "Good morning, Detective. What can I do for you?"

    else:

        if m.attitude < 0:

            m "Yes. Hello."

        else:

            m "Hello again, Detective. Is there something I can help you with?"

    $ mother_greeted = True

    jump player_input

label .dialogue_introduction:

    if not mother_introduced:

        $ m.update_attitude(1)

        if m.attitude < 0:

            m "Interesting. I'm Christine."

        else:

            if not mother_greeted:

                m "Good morning, Detective. My name is Christine, what can I do for you?"

            else:

                m "Nice to meet you, Detective. I am Christine."

    else:

        if m.attitude < 0:

            m "That's what you said before. Don't think I believe you."

        else:

            m "I believe you mentioned that already, Detective. What can I help you with?"

    $ mother_introduced = True

    jump player_input

label .help:
label .help_request:

    if m.attitude < 0:

        m "I can't do anything to help you."

    else:
        
        if mother_knowsmissing:
        
            m """
            Finding Liv is definitely important, but I don't think I can do much to help you.
            
            I'll do my best to provide you with what you want to know, but I have no idea what else I could do.
            """

        else:

            m "I will do my best, but what do you need help with?"

    jump player_input

label .cat_missing:

    m """
    Oh poor little Liv is missing? That explains why she hasn't stopped by the past few days.
    
    Oh I hope she's alright...
    """

    $ collect_clue("christine", "cat")

    $ mother_knowsmissing = True

    jump player_input

label .cat_duration:

    m "Oh this is terrible... I hope she turns up soon. That is a really long time for her to be gone..."

    $ collect_clue("christine", "cat")

    $ mother_knowsduration = True

    jump player_input

label .cat:
label .cat_about:
label .cat_behaviour:
label .cat_appearance:

    if m.attitude < 0:

        m """
        Shouldn't Grandma have told you about Liv already?
        
        A white cat with black spots. Sticks close to the neighbourhood.
        """

    else:

        m "Well her name is Liv and she's white with dark spots. But you should know that. Granny probably told you all about her, didn't she."
        
        if mother_knowsmissing:

            m "Now that I think about it, it is weird that I haven't seen her around. She usually sticks very close to the neighbourhood when she is outside."

    $ collect_clue("cat", "description")

    $ collect_clue("cat", "wellknown")

    jump player_input

label .cat_location:

    if m.attitude < 0:

        m "No, I do not know where she is. I didn't hear her. Go ask the other neighbours."

    else:

        if mother_knowsmissing:

            m """
            I wish I knew. Oh god, I just hope she didn't run in front of a car. Or got locked in somewhere.

            But I haven't heard her at all. That cat is a good kitty, but she's not the most quiet one, you know.

            But I've been in the basement doing laundry all day. Maybe one of our other neighbours has heard something.
            """

            $ collect_clue("christine", "alibi")

        else:

            m """
            Liv? She's usually somewhere around this street. She doesn't wander far.
            
            If she is not outside, then you should ask the old lady in the second house.
            """

    jump player_input

label .cat_noise:

    m "There were loud cat noises? Can't say I have heard anything."

    if m.attitude > 0:

        m "But that could be because I've been doing laundry in the basement all day..."

        $ collect_clue("christine", "alibi")

    jump mother.culprit_kids

label .cat_relationship:

    m """
    Well I sometimes look after the cat for Grandma. She's a nice little Lady... {w}the cat, I mean.

    Well Grandma too, but we were talking about Liv, right. Well, Liv is nice. And good with the kids.

    I mean the kids love her.
    """

    if m.attitude > 0:

        m "She's a picky eater though, won't eat out of a black bowl. I have no idea why."

    $ collect_clue("christine", "cat")

    jump player_input

label .grandma:
label .grandma_about:
label .grandma_name:

    m """
    Oh Grandma? She's the best. She insists on everyone calling her Grandma.
    
    She takes care of the kids from time to time. That's a real help.

    Uhm, I don't know if she has any family outside of her cat? {w}Well I guess she found her own set of grandkids in this street.
    """

    $ collect_clue("grandma", "name")

    $ collect_clue("christine", "oldlady")

    jump player_input

label .neighbours:
label .neighbours_who:

    if m.attitude < 0:

        m "There are only four houses, check them out if you're curious."

    else:

        m """
        Our direct neighbours are the van Gleans, but right now you would only meet their son Robert.
        
        The next house over is Grandma. If I understood you correctly you should already know about her.

        In the last house lives Martin, he is nice when he isn't currently hungover. Very helpful if any of use have trouble with technology.
        """

        $ subkey_blacklist.discard("alcohol")

        $ subkey_blacklist.discard("hungover")

    jump player_input

label .grandma_relationship:

    m "I love her. She was the first one to welcome me in, she brought over a cheesecake."

    if m.attitude > 3:

        m happy "I thought she was trying to kill me right then and there...{w} Ever since that day we insist on apple pie whenever she offers to bake for us."

    m neutral "By now she is probably more Grandma to my kids than their actual grandparents."
    
    if m.attitude > 3:

        m happy "Did you know she got them tickets to Disneyland?{w} My in-laws are leeching off of those right now."

    m neutral "Honestly, I wouldn't know what to do without her."

    if m.attitude > 3:

        $ collect_clue("christine", "suspect")
    
    jump player_input

label .martin_relationship:

    if m.attitude < 0:

        m "We are neighbours, that covers all you need to know."

    else:

        m "Martin helps us with issues around the house sometimes. Aside from that we don't really have any connections."

    jump player_input

label .robert_relationship:

    if m.attitude < 0:

        m "Robert? He doesn't even really live here."

    else:

        m """
        I haven't had many opportunities to talk to him if I'm being honest.
        
        He moved out before I met my husband and moved here. Ever since then Robert only comes by occasionally to visit his parents.
        """

    jump player_input

label .martin:
label .martin_about:
label .martin_name:

    if m.attitude < 0:

        m "Ask him yourself, he lives right down the street. I'm not your maid."

    else:

        m """
        I don't know much about him. I think he works in IT? I don't know...
        
        He's nice though. Helped out once when our sink broke and Frank couldn't fix it.
        """

        if m.attitude > 3:

            m happy """
            Frank is still embarassed about that one. And Josie still sometimes calls him Swamp Monster, because he had water and spinach all over him hahahaha

            Martin was a great help though. Had all the right tools and everything.
            """

        m neutral """
        He is kind of a drunk though... although that doesn't do him justice. He just usually goes out on weekends and is then hungover.

        I just try to keep my kids away from that house then, if i can. Otherwise he's a good neighbour.
        """

        $ collect_clue("martin", "christine")

        $ subkey_blacklist.discard("alcohol")

    jump player_input

label .martin_alcohol:
label .martin_hungover:

    if m.attitude < 0:

        m "That's something you should discuss with him instead."

    else:

        m """
        He isn't an alcoholic if that's what you think. But he gets drunk very quickly, so he spends most of his weekends hungover.
        
        If you catch him any other time, Martin is a really open and friendly guy.
        """

    jump player_input

label .robert:
label .robert_about:
label .robert_name:

    if m.attitude < 0:

        m "Why don't you ask him yourself? I don't really know him anyway."

    else:

        m """
        Eeehm... His mom is nice.
        
        He is only here to take care of the house while she's in the hospital with his father. I think he works at the Bank.
        """

        if m.attitude > 3:

            m happy """
            His suit would suggest so. I have literally never seen him without one. Even when he visits his mom on sundays.

            I mean, maybe he is one of those weirdos who wear a suit to church, but frankly that's not his vibe.

            His vibe is more \"Knows way too much about trust funds\" and not \"Knows what's written in Leviticus 12:2\", you know?
            """

            $ collect_clue("robert", "christine")
        
        m neutral "But that's all I know. If you want to more ask Martin... or Frank. Or just ask him directly. He should be home, I think?"

    jump player_input

label .robert_parents:

    if m.attitude < 0:

        m "They aren't here anyway..."

    else:

        m """
        They are good neighbours. Always nice and don't make problems for us and the kids.

        Roberts father has had troubles with his knee for quite a while. From what I know he is currently at a check-up because of his last surgery?
        """

        $ collect_clue("robert", "parents")

    jump player_input

label .christine:
label .christine_about:
label .christine_family:

    m """
    Well I live here with Frank, my husband, and our two kids.
    
    I'm not technically from here, but from the next town over.
    """
    
    if m.attitude > 0:

        m "That won't stop my mother in law from being rude because \"I'm not from this town\" even though her damn retirement home is in that exact town anyway."

        $ collect_clue("christine", "inlaws")

    m "I work in marketing. I guess that's all there is."

    jump player_input

label .christine_name:

    m "Oh... uhm... my name is Christine"

    jump player_input

label .christine_inlaws:

    m "Let's leave it at \"We are not each other's favourite person\"."

    if m.attitude > 3:

        m happy """
        But if you must know more, my mother in law is not excited about the fact that I am not \"from around here\".
        
        She takes every opportunity to make that very clear when we meet.
        """

        $ collect_clue("christine", "inlaws")

        show mother neutral at slightleft

    jump player_input

label .kids:
label .kids_about:  

    if m.attitude < 0:

        m "Wouldn't you like to know, Weirdo?"

    else:

        m """
        Well my little Josie is 7 and my Sammy is 4. Josie's in second grade. 
        
        Josie's a smart little cookie. She's really into dinosaurs.
        """

        if m.attitude > 3:

            m happy """
            Do you know how hard it is to make up bedtime stories about dinosaurs? Especially with a little fact checker next to you.
            
            Don't get me wrong, it's fun. But it's a challenge haha.
            """
        
        m neutral "My little Sammy still goes to kindergarten. He is my little rascal."

        if m.attitude > 3:

            m happy """
            Last month he ran against the little cement trash house at full speed. Thank god he only lost a tooth and the scrape wasn't too big, but we still went to the hospital to be safe.

            And you know what, the kids started handing out little chestnut animals to the staff. Why?
            """
        
        $ collect_clue("christine", "kids")

        $ keyword_blacklist.discard("josie")
        
        $ keyword_blacklist.discard("sam")
        
        show mother neutral at slightleft

        $ mother_aboutkids = True

    jump player_input

label .kids_noise:

    if m.attitude < 0:

        m "Those noises sound very much like none of your business."

    else:

        m "Those two really can get quite loud. But Josie is in school during the morning and Sam mostly plays outside, so it isn't too distracting when I'm at home."

    jump player_input

label .kids_location:
label .josie_location:
label .sam_location:

    if m.attitude < 0 or not mother_aboutkids:

        m "That is really none of your business. They are not here."

    else:

        m """
        They are at Disneyland with my husband and his parents. They drove down Friday, after Josie came home from her piano lesson.

        I had some laundry to catch up on, so I stayed behind.
        """

        if m.attitude > 3:

            m happy """
            It's not like I would've wanted to go anyway, with my mother in law trotting along.

            That woman can go to hell for all I care. I hope the kids get a sugar rush while they are still with her.
            """

            show mother neutral at slightleft

        $ collect_clue("christine", "disneyland")

    jump player_input

label .josie:
label .josie_about:
label .josie_dinosaurs:

    if m.attitude < 0:

        m "My children are none of your business."

    else:

        if not mother_aboutkids:

            m "Oh you talked to Grandma about her, I assume?"

            $ mother_aboutkids = True

        m happy """
        Well Josie is my eldest. I'm so proud of her. She's so smart.

        She really loves dinosaurs, wants to be a paleontologist when she grows up. Trust me, she will be. She will chew your ear off if you talk to her about them.
        
        Josie can tell you all about your favourite dinosaur and will get offended if you don't have one, because in her words \"Every normal adult has a favourite dinosaur, otherwise they are doing it wrong.\"

        Her favourite is the Troodon. Of course it couldn't be one of the mainstream ones. That would have been too easy haha.

        Oh well, it is kinda cute though.
        """

        $ collect_clue("christine", "josie")

        show mother neutral at slightleft

    jump player_input

label .sam:
label .sam_about:
label .sam_handball:

    if m.attitude < 0:

        m "My children are none of your business."

    else:

        if not mother_aboutkids:

            m "Oh Grandma told you about him already then?"

            $ mother_aboutkids = True

        m """
        So Sam is my young one. He's already 4... {w}My how the time flies. He is my little rascal.

        We didn't know what to do with all his energy, so we put him in handball. The local handball club has a mini league.

        Of course he protested, because \"He is not mini, he can get dressed all on his own\", but he is very happy there.

        Do you know how adorable mini handball is? They all have a concept of throwing and ideas of catching a ball, but the connection is not really made. It's just utter chaos.

        But Sam is having the time of his life and that's all that matters, right?
        """

    jump player_input

label .culprit:
label .culprit_who:
label .culprit_grandma:
label .culprit_martin:
label .culprit_robert:
label .culprit_christine:

    if m.attitude < 0:

        m "I highly doubt there is a 'culprit' to find for you, Detective."

    else:

        m """
        We aren't exactly all one big family, but if nothing else everyone loves Grandma. None of us would take her Liv away on purpose.
        
        If you are searching for some 'culprit' that stole Grandmas cat, I would suggest taking a different approach.
        """

    $ collect_clue("christine", "culprit")

    jump player_input

label .culprit_kids:

    if not cat_trapped:

        jump mother.culprit

    m "If you want I can check the kids rooms..."

    hide mother

    "She walks back into the building, you hear her walking up the stairs...{w=5.0}"

    show mother neutral at slightleft

    "When she returns she shakes her head"

    m "No, I'm sorry. She's not up there."

    if m.attitude > 0:

        m """
        I wouldn't have put it past my kids to put a cat up there.
        
        They are a handful you know. But they are not bad kids, they just love Liv, you know?
        """

    $ collect_clue("cat", "nottrapped")

    jump player_input

label .christine_coffee:

    if mother_coffee:

        you "{i}Nothing beats a nice refreshing coffee break, don't you think...{/i}"

        "..."
    
    else:

        jump mother.default

    jump player_input

label .dialogue_leaving:

    if m.attitude < 0:

        m "Finally."

    elif m.attitude > 3:

        m happy "Bye then. Come by if you need a coffee break."

        $ mother_coffee = True

        $ keyword_blacklist.discard("coffee")

    else:

        m "Good bye, Detective."

    hide mother

    $ mother_goodbye = True

    call screen map()

label .help_how:
label .help_confirmation:
label .cat_tips:
label .grandma_plants:
label .christine_relationship:
label .robert_call:
label .martin_sayshi:
label .default:

    if m.attitude < 0:

        m "Excuse me, what?"

    else:

        m "I'm not sure what you are talking about."

    jump player_input

label .insult():

    m angry "You are lucky my kids aren't around to hear such language..."

    show mother neutral at slightleft

    jump player_input
    