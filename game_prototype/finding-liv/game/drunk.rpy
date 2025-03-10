default drunk_visit = 0
default drunk_greeted = False
default drunk_introduced = False
default drunk_knowsmissing = False
default drunk_knowsduration = False
default drunk_mentionrob = False
default drunk_robdetails = False
default robert_sayhi = False
default drunk_goodbye = None

default drunk_funfacts = {
    "He will tell you he doesn't even like cats. But he's lying. He loves cats more than anyone I know. That includes Grandma.",
    "Last time I checked he owns one Superhero shirt in between his suits and it's a Spiderman shirt.",
    "He's such a pedant... He even has his initials stitched into his socks. hehe",
    "He's a smart guy. Really good with numbers and logic and everything. But boooy does he suck at chess.",
    "He loves his suits. Even his pyjama is styled like a suit. Looks cute on him though.",
    "His favourite movie is Shrek 3.{w} No I don't know why he prefers that one over the clearly better Shrek 2.",
    "He sings in the shower. Not well. But he sings.",
    "He is a really good kisser. And I can say that from personal experience.",
    "That is not his natural hair color.",
    "He really wanted to be a professional league of legends player in college. But everyone told him he was too bad hehe",
    "That ass cheats at card games. No way in hell does he win every single time we play against other by normal means.",
    "I know for a {b}Fact{/b} he has tiny suits printed on his underwear. Seen them myself hehe",
    "His boss insists on them playing golf together. Asked him about 5 times already. But Rob keeps declining the invitation."
}

label drunk:

    $ active_character = d

    scene bg martin

    hide screen keyword_box

    menu ring_drunk:

        "Someone stuck a piece of paper to the doorbell. It reads \"Martin Cloverson\" "

        "Ring the doorbell":

            if drunk_goodbye == None:

                $ drunk_goodbye = False

            show screen keyword_box()

            show drunk neutral at slightleft
                    
            if drunk_visit == 0:
                
                "A tired looking young man answers the door after ringing the doorbell the second time."

                "He barely opens the door and looks at you suspiciously."

                $ collect_clue("martin", "introduction")

                d "I heard you the first time. No need to make so much noise this early in the morning..."

            else:

                if d.attitude < 0:

                    d neutral "Oh, you're back already..."

                    if not drunk_goodbye:

                        d "Would've cost nothing to say bye before leaving."

                else:

                    if not drunk_goodbye:

                        d neutral "You really left me standing here without comment and just left last time, eh? Ah whatever..."

                    d happy "Welcome back, Detective. Made any progress yet?"

                    show drunk neutral at slightleft

            $ drunk_visit += 1

            $ collect_clue("martin", "appearance")

            $ drunk_goodbye = False

            jump player_input
 
        "Leave":

            show screen keyword_box()

            call screen map()

label .dialogue_greeting:

    if not drunk_greeted:

        $ d.update_attitude(1)

        if not drunk_introduced:

            if d.attitude < 0:

                d "Yea yea, morning."

            else:

                d "Good morning, I'm Martin. What do you want this early in the morning?"

        else:

            if d.attitude < 0:

                d "Morning... Detective."

            else:

                d "Good morning, Detective, what can I do for you?"

    else:

        if d.attitude < 0:

            d "Morning, Detective..."

        else:

            d "Good morning, Detective. How can I help you?"

    $ drunk_greeted = True

    jump player_input

label .dialogue_introduction:

    if not drunk_introduced:

        $ d.update_attitude(1)

        if d.attitude < 0:

            d "Cool. What does a Detective want here?"

        else:

            if not drunk_greeted:

                d "Good morning, Detective. My name is Martin. Nice to meet you."

            else:

                d "Nice to meet you, Detective. I am Martin, can I help you with something?"

    else:

        if d.attitude < 0:

            d "Yes I know you're a Detective..."

        else:

            d "Being a Detective seems to be very important to you, huh? Well, for what it's worth I'm still Martin."

    $ drunk_introduced = True

    jump player_input

label .help:
label .help_request:

    if drunk_knowsmissing:

        if d.attitude < 0:

            d "I'm sorry about poor Liv going missing, but I can't do anything for you."

        else:

            d "I've seen her on Friday when I was at Grandmas place to take a look at her phone."

            if d.attitude > 3:

                d happy """
                It keeps surprising me that she still has it. The phone is always causing trouble for her and I don't even know who would call her...

                This time she thought she deleted her crossword app, but it turned out she just managed to put the icon into a different folder somehow.
                """

            d neutral """
            Liv was right there with us at the time. She even let me pet her a little.
            
            Grandma sent me away after giving me a box with spare sewing supplies. Apparently she still kept some extras upstairs.
            """
            
            $ collect_clue("martin", "lastseen")

            $ collect_clue("cat", "lastseen")

            if d.attitude > 3:

                d happy "But you know, I can't just keep asking her for help every time there's a hole in my clothes. So now I'm learning how to do it myself."

            show drunk neutral at slightleft

    else:

        if d.attitude < 0:

            d angry "I don't think I'd even {i}want{/i} to help you."

            show drunk neutral at slightleft

        else:

            d "Tell me what you need help with, maybe I can do something."

    jump player_input

label .cat_missing:

    d "Liv? Grandmas cat? Could've sworn I saw her on Friday..."

    $ collect_clue("martin", "lastseen")

    $ drunk_knowsmissing = True

    jump player_input

label .cat_duration:

    d "Since Friday? That is actually when I've last seen her."

    $ collect_clue("martin", "lastseen")

    $ drunk_knowsduration = True

    jump player_input

label .cat:
label .cat_about:
label .cat_behaviour:
label .cat_appearance:

    d """
    Liv's a white cat with dark spots. I think they were black once.
    
    Something between 1 and 50 years old... Can cats even get 50 years old?
    """

    if d.attitude > 3:

        d happy "Feisty little thing. Scratched me just last week."

    $ collect_clue("martin", "description")

    show drunk neutral at slightleft

    jump player_input

label .cat_location:

    d "I have no idea where she could be. Saw her on Friday, but not since."

    $ collect_clue("martin", "lastseen")

    if d.attitude > 3:

        d happy "I had a friend over for some drinks yesterday, so I barely left the house this weekend. Maybe I just missed her."

        show drunk neutral at slightleft

    jump player_input

label .cat_tips:

    if d.attitude < 0:

        "Martin stumbles back into his house and covers his mouth. After a couple of seconds he recovers enough to continue talking with you."

        $ subkey_blacklist.discard("hungover")

    else:

        d """
        I'm not really an expert in finding cats.
        
        She only likes one specific kind of food, so you could try to lure her out if you bring some? But you would need to know roughly where she is already for that to work...

        I don't think she has any favoured toys or something that would convince her to come to you on her own.

        Honestly the best suggestion is to listen for her and follow the \"meow\"s? She is an old cat, not a quiet one.
        """

        $ collect_clue("cat", "tipp2")

    jump player_input

label .cat_noise:

    if d.attitude > 0:

        d """
        Now that you mention it, I have heard meowing upstairs yesterday. Made it really hard to sleep.
        
        Already had a look around my entire house in case she snuck in here and got trapped somewhere. Didn't find her though.
        """

        $ collect_clue("cat", "noise2")

    else:

        "Martin looks really unwell for a second. Almost like he is about to vomit, but he catches himself in time."

        $ subkey_blacklist.discard("hungover")

    jump player_input

label .cat_relationship:

    if d.attitude < 0:

        d "She's my neighbours cat. What do you expect me to say?"

    else:

        d """
        Liv and I have a shaky truce going right now. 
        
        I only pet her occasionally and briefly. In return she only scratches me every now and then.
        """

    jump player_input

label .grandma:
label .grandma_name:

    if d.attitude < 0:

        d "Grandma is Grandma alright. You met the lady."

    else:

        d """
        Yo she's my Grandma...{w} Not by blood, but who cares? She took care of me.
        
        And not just me, Frank and Robert too. I dunno about her own family though. If she has one, they haven't visited in forever.
        """

        $ collect_clue("grandma", "robert_fact1")

    jump player_input

label .grandma_about:

    d "I don't remember her ever being younger. She was probably born as a grandma.{w} Probably came with cat too hehe"
    
    if d.attitude > 3:

        d happy """
        The only thing that isn't cliché grandma about her is that she doesn't knit. She tried it once, because she thought grandmas knit so she must too. It wasn't it really.
        
        I still have the socks she made me during that time, but those are strictly inside-only. Not even I would wear them outside and my style is basically the opposite of Robert.

        She probably wouldn't be half as bad at it if she wasn't so stubborn and got her glasses updated...{w} to those colorblind ones.
        """

        $ collect_clue("grandma", "martin_fact")

        show drunk neutral at slightleft

    jump player_input

label .neighbours:
label .neighbours_who:

    if d.attitude < 0:

        d "It's too early for this...{w} It's only three other houses, talk to them yourself."

    else:

        d """
        It's just four houses in this street. You've met me and it sounds like you know Grandma already.

        The other two houses are Franks family and the van Somethings. They aren't here anyway... Roberts parents.

        Frank and his kids should be out, since I can't hear any children screaming up and down the street. Maybe Christine is there to greet you. Nice woman.

        And of the other family, there is only Robert at home right now. He is watching the house for his parents, while they are out.
        """

    jump player_input

label .grandma_relationship:

    d """
    She took care of us boys when we were young. She's the best. An amazing baker.
    
    Except for her cheesecake. It might be the recipe though...{w} I tried to make it myself once. But only once.
    """

    if d.attitude > 3:

        d happy "The fire department told me I'm not allowed to try again."

        show drunk neutral at slightleft

    d """
    But her other stuff is to die for.

    Anyways, I try to go over as often as I can and help her out. I love her, I really do.
    """

    $ collect_clue("martin", "techsupport")

    jump player_input

label .robert_relationship:

    if d.attitude < 0:

        d "We both grew up in this street."

    else:

        d """
        Oh we go wayyyy back. Grew up here together. Got into all sorts of trouble together.
        
        Not so much anymore since he moved to the big city. Became a pencil pusher for some bank. But we still get into trouble whenever he comes back here occasionally.
        """

        $ collect_clue("robert", "martin_fren")

    jump player_input

label .christine_relationship:

    if d.attitude < 0:

        d "They're my neighbours. Not much to say here."

    else:

        d """
        Frank also grew up here. Christine moved in with him when they got married.
        
        I hang out with Frank occasionally, but I don't think Christine approves of that. Tries to keep her kids away from me as if I'm some big evil monster hehe"
        """

        $ collect_clue("christine", "martin_frank")

    jump player_input

label .martin:
label .martin_about:
label .martin_name:

    if d.attitude < 0:

        d "Not your business, Detective."

    else:

        d "My name is Martin, I'm 29. I work in a tech support call-center."

        if d.attitude > 3:

            d happy """
            My hobbies include video games and going out to the bar with friends.
            
            Last month I even got a gym membership...{w} I'll go next week I think.
            """

            $ collect_clue("martin", "self")

            show drunk neutral at slightleft

        d "Is that all?"

    jump player_input

label .martin_alcohol:
label .martin_hungover:

    if d.attitude < 0:

        d "Why would you care?"

    else:

        d "Oh I'm fine. Just a slight headache... Didn't even drink a lot, just couldn't sleep very well. With the noise and all..."

        $ collect_clue("martin", "hangover")

    jump player_input

label .robert:
label .robert_name:

    if d.attitude < 0:

        "For a second you are worried he might vomit on your shoes, but he gathers himself before something happens."

        $ subkey_blacklist.discard("hungover")

    else:

        d "Oh Robert's the best. Such a shame he moved away. He's a good drinking buddy."

        if d.attitude > 3:

            d happy """
            We grew up together, ya know? I mean Frank was also there. But Rob was my guy. We played video games together.

            For real it sucked when he moved away. Online is great, but I just prefer sitting next to him, ya know?
            """

            show drunk neutral at slightleft
        
        $ collect_clue("robert", "martin_fren")

        $ drunk_mentionrob = True

    jump player_input

label .robert_about:

    if d.attitude < 0:

        d "Why should I tell you about him? Maybe go over and ask him yourself."

    else:

        if not drunk_mentionrob:

            jump drunk.robert
        
        if not drunk_robdetails:
    
            d "Honestly, love that guy. Even though he works at the bank. He is no doubt the best guy there. Reliable, smart..."

            if d.attitude > 3:

                d happy "Do you wanna know a weird fun fact about him?"

                $ collect_clue("robert", "martin_funfacts")

                jump drunk.robert_details
            
        else:

            if d.attitude > 3:

                d happy "Oh you want another fun fact?"

                jump drunk.robert_details
            
            else:

                d "No more fun facts for now."

    jump player_input

label .robert_details:

    if len(drunk_funfacts) > 0:

        $ fact = drunk_funfacts.pop()

        d "[fact]"
    
    else:

        d "I am so sorry, Detective. I'm all out of fun facts... I'll try to gather more for your next visit."

    show drunk neutral at slightleft

    jump player_input

label .robert_parents:

    if d.attitude < 0:

        d "Not my business to talk about."

    else:

        d """
        I don't really know much about them. They probably know all about me, since I spent so much time at their house when I was younger.
        
        But I never really built much of a connection with the parents of my best friend. They are nice, but that's about all I know.
        """

    jump player_input

label .martin_sayshi:

    if not robert_sayhi:

        jump drunk.default

    else:

        d "You're supposed to tell {i}him{/i} Hi from me."

    jump player_input

label .christine:
label .christine_about:
label .christine_name:

    if d.attitude < 0:

        d "Eh..."

    else:

        d """
        She moved here a while ago once Frank and her got married. She's nice enough although a bit boring.
        
        She gets weird on weekends though...
        """

        if d.attitude > 3:

            d happy "Her kids are fun, but I'd prefer it if the small one stopped throwing his ball at my house on saturdays."

            show drunk neutral at slightleft

    jump player_input

label .christine_family:
label .christine_inlaws:

    if d.attitude < 0:

        d "How is that relevant?"

    else:

        d """
        I really only know Frank. Their two kids are kept well away from me, because their mother is too paranoid.
        
        And even then I only hang out with Frank occasionally, not like a deep connection really.
        """

        $ collect_clue("christine", "martin_frank")

    jump player_input

label .kids:
label .kids_about:  
label .kids_location:
label .josie:
label .josie_about:
label .josie_dinosaurs:
label .josie_location:
label .sam:
label .sam_about:
label .sam_handball:
label .sam_location:

    if d.attitude < 0:

        d "Not my business to talk about and not your business to ask about."

    else:

        d """
        I hear those kids all day when they are at home, but beyond that I don't know about them.
        
        I'm Just not that much of fan of children. It's mostly the noise. They are just too loud for me.{w} I mean Dinos are cool, but with a headache even the coolest Ankylosaurus is a bit too much. 
        
        Aside from that I'm glad for every day that don't manage to break my windows.
        """

        $ collect_clue("martin", "children")

    jump player_input

label .kids_noise:

    d "Urgh, don't talk about it. Their screams haunt me just thinking about it."

    jump player_input

label .culprit:
label .culprit_who:
label .culprit_grandma:
label .culprit_martin:
label .culprit_robert:
label .culprit_christine:
label .culprit_kids:

    if d.attitude < 0:

        d "Ah yes. The only logical conclusion, {i}Detective{/i}. Clearly someone stole the cat."

    else:

        d """
        Liv probably just went on a walk and is taking her time getting back home.
        
        Noone I know would hurt her or Grandma on purpose. If she isn't trapped in some house, she's just enjoying the scenery of wherever she wandered off to.
        """

        $ collect_clue("cat", "martin")

    jump player_input

label .dialogue_leaving:

    if d.attitude < 0:

        d "Don't come back."

    elif d.attitude > 3:

        d blush "Say \"Hi\" to Robert for me, will you?"

        $ collect_clue("robert", "hi")

        show drunk happy at slightleft

        $ robert_sayhi = True

        $ subkey_blacklist.discard("sayshi")

    else:

        d "Bye"

    hide drunk

    $ drunk_goodbye = True

    call screen map()

label .grandma_plants:
label .robert_call:
label .martin_relationship:
label .help_how:
label .help_confirmation:
label .christine_coffee:
label .default:

    if d.attitude < 0:

        d "I have no idea what you want."

    else:

        d "Yeah... I'm not really sure what you are trying to say."

    jump player_input

label .insult():

    d angry "Woah. No need for that kind of language..." 

    show drunk neutral at slightleft

    jump player_input
    