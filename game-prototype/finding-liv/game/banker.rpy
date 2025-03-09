default banker_visit = 0
default banker_greeted = False
default banker_introduced = False
default banker_knowsmissing = False
default banker_knowsduration = False
default banker_call = False
default banker_callcount = None
default banker_grandmacount = 0
default cat_trapped = False
default banker_goodbye = None

label banker:

    $ active_character = b

    scene bg robert

    hide screen keyword_box

    menu ring_banker:
        
        "The doorbell reads \"van Glean\""
        
        "Ring the doorbell":

            if banker_goodbye == None:

                $ banker_goodbye = False

            show screen keyword_box()

            show banker neutral at slightleft

            if banker_visit == 0:
                    
                "A man in a suit opens the door a short time after you've run the doorbell."

                "You fail to spot a single blemish on his suit and his hair is neatly gelled back even this early in the morning."
            
                $ collect_clue("martin", "introduction")

                b "Yes? How can I help you?"

            else:

                if b.attitude < 0:

                    b "The Star-Detective has returned..."

                    if not banker_goodbye:

                        b "...or maybe he just never left?"

                else:

                    if not banker_goodbye:

                        b neutral "I almost didn't notice you left after you just went on without a word. Oh well..."

                    b happy "Welcome back, Detective. Have you made progress?"

                    show banker neutral at slightleft

            $ banker_visit += 1

            $ collect_clue("robert", "appearance")

            $ banker_goodbye = False

            jump player_input
                    
        "Leave":

            show screen keyword_box()

            call screen map()

label .dialogue_greeting:

    if banker_greeted:

        if b.attitude < 0:

            b "I don't have unlimited time. Get to the point."

        else:

            b "Yes yes. Good morning."
    
    else:
 
        $ b.update_attitude(1)
       
        if b.attitude < 0:

            b "Morning. Do you have a good reason to disturb me on a Sunday morning?"

        else:

            b "Good morning. To what do I owe a visit this early on a Sunday?"

        $ banker_greeted = True

    jump player_input
    
label .dialogue_introduction:

    if banker_introduced:
        
        b "Yes, I already know who you are."

    else:

        $ b.update_attitude(1)

        if banker_greeted:

            if b.attitude < 0:

                b "A Detective? Probably not a very good one if you need to take on jobs that bring you here..."

            else:

                b"""
                So you're a Detective? Can't say I have an idea what you might want in this corner of the world.

                My name is Robert van Glean, just call me Robert as anyone else here. 
                """

        else:

            b "Good morning, Detective. I am Robert van Glean, but I probably won't be of much help in your investigation."

            if b.attitude < 0:

                b "So what brings someone like you to knock on my door on a Sunday morning?"

            else:

                b "What is there even to investigate in a quiet place like this street?"

        $ banker_introduced = True

    jump player_input
    
label .cat:

    b "The cat? I believe she was called Liv. What about her?"

    jump player_input

label .cat_missing:

    if b.attitude < 0:

        b "Why would you bring that to me? I wouldn't want anything to do with that cat if it were gifted to me"

    else:
        
        b "I'm sorry, I don't really live here anymore. This is my parents house and I am only looking after it while they are out."
        
        $ subkey_blacklist.discard("parents")

    b """
    I have only seen the cat myself a handful of times. Usually I only hear her through the walls when I'm trying to sleep at night.

    Speaking of noise, are you sure she is missing? I've heard her as usual while trying to sleep last night and she's not in {i}my{/i} house.

    But if she isn't at Grandma's house, then it was probably from the kids' room next door...
    """

    $ collect_clue("cat", "noise1")

    $ cat_trapped = True
    
    $ keyword_blacklist.discard("kids")

    $ subkey_blacklist.discard("kids")

    $ subkey_blacklist.discard("noise")

    if b.attitude > 0:

        b "You should probably check in with the family next door. If they have the cat trapped in their room, noone would realise until the kids come home from their trip."

    if not banker_knowsduration:
    
        b "How long did you say she was missing?"

    $ banker_knowsmissing = True

    jump player_input

label .cat_duration:

    if banker_knowsduration:

        b "I have already told you I haven't been around on Friday. You should really ask someone else."

    else:

        if b.attitude > 0:

            b"""
            I wasn't here on Friday, but I can give my parents a call. Maybe they have an Idea. I'll let you know if they said anything helpful.

            Until then, you should check in with the family next door. I've heard cat noises all night yesterday, I even checked my own house to be sure she isn't here somehow.

            Unless they have their own cat by now, it is more likely that Liv got trapped by those kids. Although it would be a miracle if their mother hasn't heard anything yet.
            """
            
            $ subkey_blacklist.discard("call")

            $ banker_call = True

            $ banker_callcount = banker_visit

        else:

            b "Well I wasn't here on Friday. Maybe the family next door got their own cat and that is what I have been hearing all night yesterday?"
            
        $ collect_clue("cat", "noise1")

        $ cat_trapped = True

        $ subkey_blacklist.discard("parents")

        $ subkey_blacklist.discard("noise")

        $ banker_knowsduration = True

        $ banker_knowsmissing = True

    jump player_input

label .cat_about:
label .cat_behaviour:
label .cat_appearance:
label .cat_location:
label .cat_tips:

    if b.attitude < 0:

        b "Look, Detective, I can't help you. I'm barely even around here these days."

    else:

        b """
        Since this is normally my parents house and I'm only here for a couple of days every year, I am not too familiar with this cat.

        She has white fur and black spots, but everyone in this street could tell you that. 
        
        Beyond that I only know that she is a picky eater.
        """

        $ collect_clue("cat", "description")

        $ subkey_blacklist.discard("parents")

        if b.attitude > 3:

            b happy "If you really need help, you should go see if Martin is awake already. He is the local cat expert if you aren't counting Grandma."

            show banker neutral at slightleft

    jump player_input

label .cat_noise:

    if b.attitude < 0:

        b "This cat is making noise all day every day. Just make sure that it makes noise somewhere else."

    else:

        if banker_knowsmissing:

            b """
            I've heard her all night yesterday, so I never expected it to be missing. It would make sense if those kids trapped it in their room before leaving.       
            
            You would do me a favour if you find her actually. I'm sure she was louder than usual last night. Probably because she is trapped.
            """

            $ collect_clue("cat", "trapped")

            $ keyword_blacklist.discard("kids")

            $ subkey_blacklist.discard("kids")

            $ cat_trapped = True

        else:

            b """
            I've heard her all night yesterday. And I already got home later than usual. 

            People always tell me cats spend most of their day sleeping, but this one spends most of it's time making noise when I want to sleep.
            """

    jump player_input

label .cat_relationship:

    if b.attitude > 0:

        b """
        I'm allergic, so I try my best to keep my distance from her. But that is probably a mututal sentiment.

        She is already a picky eater, but if I try to feed her, she won't even eat her favourites.
        """

        $ collect_clue("robert", "allergy")

    else:

        b "I don't like cats. Any more questions?"

    jump player_input

label .grandma:
label .grandma_about:
label .grandma_name:
label .grandma_plants:

    if banker_grandmacount == 0:

        b """
        She has been living in that house already while I was still a child growing up in this street. 
        
        The cat is relatively new, but has also been around for a few years already.
        """

        if b.attitude < 0:

            b"""
            I can't tell you much about her. It has been a while since I moved out and haven't talked to her in years.
            """

        else:

            b"""
            I remember her taking care of me and the other kids on this street when our parents were busy.

            We took to calling her Grandma, because she mostly was one for all of us. I don't even remember her real name.
            """

            $ collect_clue("grandma", "robert_fact1")
    
            $ banker_grandmacount += 1

    elif banker_grandmacount == 1:

        b"""
        One very important thing to know is to never ask Grandma about her cheesecake.

        She keeps claiming that it's her best work, but that is the only unedible cake she has ever baked to my knowledge.

        Every else she bakes or cooks is of really high quality, but if she offers cheesecake, tell her you are allergic and leave.
        """

        $ collect_clue("grandma", "robert_fact2")

        $ banker_grandmacount += 1

    elif banker_grandmacount >= 2:

        b """
        You should really talk to her yourself if you are interested.
        
        But just as a heads up, I don't think she ever had a partner and I doubt she is willing to change that now.
        """
        
        $ banker_grandmacount += 1

    jump player_input

label .neighbours:
label .neighbours_who:

    if b.attitude > 0:

        b"""
        Two houses down the road lives an old childhood friend of mine: Martin. My direct neighbours are the old lady whos cat you are looking for and a family of four.

        I don't know much about that family. Their kids make enough noise for the whole town, but that is pretty much all I know.
        """

        $ collect_clue("robert", "childhood")

    else:

        b"""
        I don't really live here, Detective. I don't even know most of the neighbours names. If my parents were here, they could probably tell you a lot more.
        """

    jump player_input

label .grandma_relationship:

    if b.attitude > 0:

        b"""
        She took care of all the kids growing up in this street. I haven't contacted her as often as I probably should these last years.

        Grandma is a really sweet old lady, but the amount of cat hairs in her house make it impossible for me to visit.
        """
    
    else:

        b "She is a Grandma for everyone on this street. Including me."

    $ collect_clue("grandma", "robert_fact1")

    jump player_input

label .martin_relationship:

    if b.attitude < 0:

        b"""
        We grew up together. We've drifted apart after I moved away, but thats all there is to it.
        """

    else:

        b"""
        I just went to meet him yesterday. It was good to see an old friend again.

        We sat in his house and had a few drinks. Probably made the noises at night even worse than they usually are.

        He didn't mention a cat even while drunk, so I'm sure he really doesn't know where it went.
        """

        $ collect_clue("robert", "alibi")

        $ subkey_blacklist.discard("alcohol")

        if b.attitude > 3:

            b happy "Just don't listen to anything he says about me, when you talk to him. He has a habit of making things up just to be funny and cause problems for me personally."

            show banker neutral at slightleft

    jump player_input

label .martin:
label .martin_about:
label .martin_name:

    if b.attitude < 0:

        b"""
        We both grew up in this street. I went to greet him yesterday, but aside from that we don't have much contact anymore these days.

        He would never do anything to harm the old lady next door, so if you suspect he did anything to the cat, you are probably on the wrong track.
        """

        $ collect_clue("martin", "robert_neutral")

    else:

        b"""
        Martin was one of my closest friends growing up. We don't see each other as often since I moved away, but we still talk often.

        He really likes the old lady next door and even takes care of her cleaning every other week. So I'm sure he has nothing to do with the missing cat.

        But then again, you should probably ask Martin for help with the search. He is the local cat expert. Just don't trust anything he tells you about me. 
        """

        $ collect_clue("martin", "robert_fren")

    jump player_input

label .martin_alcohol:

    if b.attitude < 0:

        b "Maybe you should look into your missing cat before you start gossiping."

    else:

        b"""
        I'm convinced the mother next door thinks Martin is an alcoholic, but that's not it.

        He only drinks on weekends and even then his biggest issue is being a lightweight. We barely had two beers yesterday and he was out cold by the time I left.
        """

        $ collect_clue("martin", "robert_algul")

    jump player_input

label .martin_hungover:

    if b.attitude > 0:

        b"""
        We had a couple drinks yesterday...{w} I guess he didn't quite recover from that yet.

        Martin really can't hold his alcohol, we barely had two beer each. He'll get over it in time, no need for concern.
        """

        $ collect_clue("martin", "robert_algul")

    else:

        b "Maybe you should look into your missing cat before you start gossiping."

    jump player_input

label .robert:
label .robert_about:

    if b.attitude > 3:

        b happy """
        I'm working at a bank in the city. Most likely not something you would find interesting. 

        I've always had an easier time working with numbers than my peers and in the end that is where it took me.

        I moved out quite a while ago, normally you would've been greeted by my parents. They asked me to look after the house while they are gone.

        There isn't even really anything for me to look after here, but it soothes their mind that I am here taking care of things.
        """

        $ collect_clue("robert", "bigcity")

        show banker neutral at slightleft
    
    else:

        if banker_knowsmissing:
            
            b "My story is nothing I would share with a stranger and it isn't related to that missing cat of yours."
        
        else:

            b "Who are you? Why would you just ask about my life when we have never met before?"

    jump player_input

label .robert_name:

    if banker_introduced:

        b "My name is Robert van Glean, but you should know this already."

    else:

        b "I am called Robert van Glean. Who am I speaking to and how can I help you?"

    jump player_input

label .robert_parents:

    if b.attitude > 0:

        b"""
        They are currently at the hospital. It's nothing serious, so no need to worry.

        My father has some issues with his knee. This is just a routine check-up to see if there are any issues remaining from the most recent surgery.

        They will be back tomorrow, so you probably won't meet them.
        """

        $ collect_clue("robert", "parents")

    else:

        b "My parents aren't home this weekend. If you are still around by monday you might get a chance to speak to them."

    jump player_input

label .robert_call:

    if not banker_call:

        jump banker.default

    if banker_visit > banker_callcount:

        if b.attitude < 0:

            b "I have not reached them yet. They will call back eventually."

        else:

            b """
            Yes, I called them. As expected they were mostly worried about 'Poor old Liv' and hope you can find her soon.
            
            But I must disappoint you, Detective. They have no idea where she could be.
            """
    
    else:

        b "I will call them, don't worry. But I don't expect them to know anything either."

    jump player_input

label .martin_sayshi:

    if not robert_sayhi:

        jump banker.default

    if b.attitude > 3:

        b blush "Eh, thanks? But I went to see him just yesterday..."

        $ collect_clue("robert", "haiii")

        show banker neutral at slightleft
    
    else:

        b "I just met him yesterday."

    jump player_input

label .christine_relationship:
label .christine:
label .christine_about:
label .christine_name:
label .christine_family:

    b"""
    I'm not sure what you expect from me. They moved in after I moved out, so I have never really spoken to them at length.

    Their kids are the bane of my existence when I visit my parents, but that is pretty much all I know.
    """

    $ collect_clue("robert", "hater")

    jump player_input

label .kids:
label .kids_about:

    if b.attitude < 0:

        b "What is there to say other than 'Children are noisy'?"

    else:
            
        b"""
        All I know is that they are terribly noisy. Every time I visit my parents or look after their house like right now, these kids is all I hear.

        How can they even be this loud with such tiny bodies? And for that long too. Starting bright and early in the morning and then going until late at night.
        """

        $ collect_clue("robert", "hater")

        if b.attitude > 3:

            b happy "It really is a blessing that they are on a trip this weekend. If it weren't for the cat they probably trapped I would've gotten a whole night of proper rest."

            show banker neutral at slightleft

    jump player_input

label .kids_noise:

    if b.attitude < 0:

        b "They are active at all times of the day, screaming at everyone and everything. It got worse when they learned to speak because now they include actual words in their yelling."

        $ collect_clue("robert", "hater")

    else:

        b"""
        Honestly the walls between these buildings are thinner than they have any right to be. And the kids bedrooms are on the same floor as mine.

        So I have to hear them every time they play around in there. It is honestly a blessing that they play outside for most of the day.
        """

        $ collect_clue("robert", "thinwalls")

    jump player_input

label .josie:
label .josie_about:
label .sam:
label .sam_about:

    b"""
    Urgh, you're talking about those kids, right? Nothing to say here. They are too loud.
    """

    $ collect_clue("robert", "hater")

    jump player_input

label .culprit_robert:
    
    b"""
    I arrived here yesterday afternoon and only met up with someone I've known from when I still lived here.

    When did you say the cat went missing? Can't be that long since I haven't had a panicked old lady breaking down my door to look for her...
    """

    jump player_input

label .culprit:
label .culprit_who:
label .culprit_grandma:
label .culprit_martin:
label .culprit_christine:
label .culprit_kids:

    if b.attitude < 0:

        b "Go find the 'culprit' yourself, {i}Detective{/i}."

    else:

        b"""
        Noone in this street would maliciously take away that cat. Not even me, no matter how much it annoys me.

        If anything those kids probably lured it into their room and then it got trapped in there when they left for their trip on Friday.

        You should ask their mother about this. They live right next door, can't miss it.
        """

        $ collect_clue("robert", "culprit")

        $ cat_trapped = True

    jump player_input

label .dialogue_leaving:

    if b.attitude < 0:

        b "Don't be back too soon."
    
    else:

        b happy "Good luck with finding the cat and see you later."

    if banker_call and (banker_visit <= banker_callcount):

        b "I'll let you know what my parents had to say when you come back."

    hide banker

    $ banker_goodbye = True

    call screen map()

label .help:
label .help_request:

    if b.attitude > 3:

        if not banker_call:

            b "I'll call my parents to see if they have anything to contribute."

            $ subkey_blacklist.discard("call")
        
        b happy "I myself won't really be of help to you, but Martin is an expert on cat behavious. If anyone can help, it would be him."

        show banker neutral at slightleft

    else:

        b "I can't help you, Detective. Maybe ask around the neighbourhood."

    jump player_input

label .josie_dinosaurs:
label .sam_handball:
label .josie_location:
label .sam_location:
label .kids_location:
label .robert_relationship:
label .christine_inlaws:
label .christine_coffee:
label .help_how:
label .help_confirmation:
label .default:

    if b.attitude < 0:

        b "What are you trying to say..."

    else:

        b "I'm sorry. I don't think I understand what you're trying to say."

    jump player_input

label .insult():

    b angry "Do you really think this is appropriate language?"

    show banker neutral at slightleft

    jump player_input
    