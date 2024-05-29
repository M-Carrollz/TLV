# ------------------------------------------------------------------- Characters -------------------------------------------------------------------
define PC = Character("Player Character")

define Bec = Character("Rebecca")
deinfe BecThoughts = Character("Rebecca \(Thoughts\)")
define Ste = Character("Stephanie")
define Hay = Character("Hayley")
define Kay = Character("Kayla")
define Kat = Character("Katie")
define Ame = Character("Amelia")
define Sar = Character("Sarah")
define Ash = Character("Ashley")

define Cha = Character("Charlotte")
define Elo = Character("Eloise")

define Kath = Character("Katherine")
define Jam = Character("Jamie")

define Tea = Character ("Teacher")

# ------------------------------------------------------------------- Flags -------------------------------------------------------------------

define Bec1_Flag = False
define Bex1_Flag = False
define Bex2_Flag = False
define BecSecret1_Flag = False



# -------- Sexts Flags --------
define BecSexts_Flag = False

# ------------------------------------------------------------------- The game starts here. -------------------------------------------------------------------

label Day1BedroomMorning:

    scene black
    "Day 1"
    "The alarm clock beeps 6AM."
    PC "{i}(mutters){/i} ...five more minutes..."
    "{i}Brain... no work.. too tired... can't even remember my own name."
    #Player Provides name
   "The alarm clock continues to beep incessantly."
   PC "{i}(muttering){/i} Please... 5 more mins... then I swear I'll get up."
    "I suddenly snap out of it"
    PC "ohhh fuuuuuuck... yeah thats right, I'm alone now."
    "I smile and chuckle to myself."
    PC "/*Sigh/*"
    PC "I better get up."
    "I throw off the sheets and sit on the edge of the bed struggling to stay awake."
    "{i}Today is the first day of senior year, Year 12, 12th Grade, Upper 6th... whatever they call it where I live, I don't fucking remember... I'm too tired for this shit."
    "{i}I am NOT a morning person..."

    "I finally stumble out of bed and get the morning ablutions done."
    "Shower, Shit, Shave... hopefully not in that order but I still waking up, so needless to say I'm in autopilot mode and I'm hoping to hell they know what they are doing at this time of day..."
    "In the fog of my sleep deprived brain I continue with my morning routine: eat some breakfast, get dressed and with my car in the shop I head off to jump on the bus."

label Day1BusMorning:

    scene black
    PC "{i}(muttering to myself){/i} Ugh... 18, with a licence and still on the bus... stupid idiot broke my car..."
     "{i}WAIT ONE GOD DAMN MINUTE..."
     "{i}Why the fuck didn't I get a courtesy car!?"
     "I open my phone; quickly going to my car insurance website to read the terms and conditions suddenly wide awake and filled with rage."
     "{i}ohhhh... gotta be 25 to rent a car..."
     PC "Well fuck..."

label Day1SchoolMorning:

    scene black
    "I walk into school bright and early like I always..."
    PC "Hang the fuck on... why am I heare this early?"
    "{i}I used to get here early as my parents would drop me off early before heading to work, but I got here on my own."
    PC "/*Sigh/* Fuck... Idiot!"
    "{i}Ahh well it's not all bad..."
    "I look over and see a beautiful brunette sitting on the bench."
    #show off Bec
    "She looks over at me and instantly smiles."
    Bec "Name!!"
    "she runs over and throws her arms around me, holding me tightly"
    Bec "It's been too long! I've missed my favourite morning person!"
    "We both laugh."
    PC "Neither of us are morning people and you know it!"
    Bec "{i}(laughs){/i} True but here we are..."
    PC "One day we'll both get a sleep in"
    Bec "That would be nice..."
    Bec "But that would mean I don't get to have my morning catch up alone with you."

    menu:
        "\"I wouldn't say that.. we could be sleeping in together?\"":
            jump Day1MorningFlirt
        "\"Ohhh I'm sure I'd find another way to catch up with, you're worth the effort!\"":
            jump Day1MorningGoodGuy

label Day1MorningFlirt:
    Bec "You Flirt..."
    PC "With you, Always."
    Bec "Well not always, just when you have me all to yourself."
    Bec "Otherwise you'd get me in trouble with Dan."
    PC "and we wouldn't want that."
    "we both smile knowing that we shouldn't be sayign these things but we've stopped short of some imaginary second boundry that keeps her relationship unsullied."
    $ Bec1_Flag = True
    #Lust and Affection are both Increased
    jump Day1SchoolMorningCont

label Day1MorningGoodGuy:
    Bec "Nawww... you're soo nice to me."
    Bec "But yeah we'd definetly need to find a way to catch up if we missed the mornings together."
    PC "100%"
    PC "Can't go around not knowing how you are each day... that'd be crazy!"
    "we both laugh and smile"
    #Affection is Increased

label Day1SchoolMorningCont:
    PC "How was your time off?"
    Bec "It was really good!"
    PC "Yeah? What'd you get up to?"
    Bec "Spent some time with the family, saw Dan a bunch... Ohh and I saw katie a few times."
    PC "Ohh I saw Katie a couple times over the break as well!"
    Bec "Yeah she told me she'd seen you a bit."
    if Bec1_Flag:
        Bec "You really do have a thing for girls that are off limits huh?"
        jump Day1SchoolMorningFlirt:
    else:
        Bec "I miss her here with us school, it's a shame she's going to that all girls school now."
        PC "Same." 
        PC "It just doesn't feel right not seeing her every day."
        jump Day1SchoolMorningCont2

label Day1SchoolMorningFlirt:
    PC "Just because you're taken doesn't mean you're off limits..."
    Bec "Oh really?"
    PC "Yeah... It just makes it more of a challenge..."
    PC "... and a little extra naughty, wouldn't you agree?"
    "She smiles and looks at me with sultry eyes."
    Bec "I'd have to agree it's... a little {i}naughty{/i}... but also kinda nice."
    "I smile back her, both of us basking in the warm glow of mutal flirtation."
    PC "Well... if that's the case, I better keep at the challenge I've been set."
    Bec "Please do."
    #Lust and Affection are both Increased
    
label Day1SchoolMorningCont2:
    "We pause for a moment of comfortable silence."
    PC "Soooo... How are things with Dan? Still going strong I hope?"
    "She gives me a look suggesting I'm not being 100% truthful."
    PC "No, seriously how are two going? Is he treating you right?"
    menu:
        "Wait for her to Answer":
            jump Day1SchoolMorningCont3
        "\"Cause if he's not... I know a guy who'll treat you the princess you are?\"":
            Bec ""

            $ Bec1_Flag = True
            jump Day1SchoolMorningCont3

label Day1SchoolMorningCont3:
    Bec "Yeah we're going ok I suppose..."
    Bec "Although... if I'm honest, and keep this between you and me..."
    menu:
        "\"Of course!\"":
            Bec "Thanks."
        "\"Don't worry...I can keep a secret\"":
            Bec "Haha. I bet you can."
            $ BecSecret1_Flag = True
            #Lust And Affection are Increased
    Bec "Anyway he's been kinda pestering me for sex lately..."
    Bec "and I know we've been dating for ages now... but, I dunno, every time he brings it up he seems like an excited puppy about to play with a new toy..."
    Bec "He doesn't seem like her cares to make it something I want to do... and I don't want to give my virginity to someone as a present or an obligation to them..."
    Bec "I wanna loose it in the moment."
    Bec "Does that make sense?"

label Day1SchoolMorningSexTalk:
    if Bex1_Flag:
        if if Bex2_Flag:
            jump ??
        else:
            jump Day1SchoolMorningSexTalkCont
    else:
        jump Day1SchoolMorningSexTalkCont

label Day1SchoolMorningSexTalkCont:
    menu:
        "\"Yeah I get it\"":
            PC "Yeah I get it."
            PC "You only get one first time. It should be special."
            PC "It should be something memorable, that you're going to remember forever!"
            Bec "That's exactly how I feel!"
            Bec "Dan doesn't get it... He makes it seem like I'm being a bad girlfriend when I deny him sex that I'm not interested in."
            PC "That's awful.... And manipulative!"
            if Bec1_Flag:
                PC "and look... I know that's coming from me flirting with you when you're dating Dan, It's an asshole act and I know it but I'd stop if you ever asked me to..." 
                "She smiles and laughs."
                PC "but you gotta make him realise that he's not guaranteed sex just because he's dating you!"
                Bec "I know..."
                #Affection is Increased
                jump Day1SchoolMorningSexTalk
            else:
                PC "You gotta make him realise that he's not guaranteed sex just because he's dating you!"
                Bec "I know..."
                #affection is increased
                jump Day1SchoolMorningSexTalk

        "I don't get where his heads at.":
            PC "I don't get where his heads at."
            PC "That's never going ton get you in the mood."
            Bec "Right!?"
            $ Bex1_Flag = True
            if Bec1_Flag:
                    PC "Like if I was to about to take someone's virginity I'd want to take them out on a date."
                    PC "Make it an absolute magical night, a perfect night..."
                    PC "One they would look back on fondly for the rest of their lives..."
                    PC "and then when we get back home and start making out..."
                    PC "I'd kiss them all over, play with them, make sure they're super wet..."
                    BecThoughts "Mmmmm... I'm starting to get a bit wet just hearing this..."
                    #Show Bec Getting wet
                    #Lust is Increased Significantly
                    PC "I'd look into her eyes and ask what she wants..."
                    PC "and if she wants me to continue I'd give her a night to remember, focusing 100% on her wants, needs and desires."
                    BecThoughts "Noooooo... Don't stop talking, that was fucking hot!"
                    BecThoughts "Why'd he have to stop? I'm so going to have to masturbate over this conversation tonight."
                    Bec "See that's what I want!"
                    menu:
                        "Well maybe we can make it a reality some day?":
                            if Bec2_Flag:
                                Bec "Hmmm.. We'll just have to wait and see..."
                                #Lust is Increased
                            else:
                                Bec "Wow! You can't just say that!"
                                Bec "I let you get way with a lot of shit but that's going over the line."
                                #Affection & Lust are decreased
                                #Ends the conversation.
                        "\"Then I hope that one day you get that, no matter who ends up being the lucky guy.\"":
                            Bec "Thanks me too.."
                            #Affection is Increased
                            if Bec2_Flag:
                                Bec "The way you described that was pretty hot by the way..."
                                PC "Haha. Thanks."
                                menu:
                                    "I'd be happy to write naughty stories for you anytime":
                                        PC "I'd be happy to write naughty stories for you anytime"
                                        "Rebecca bites her lip."
                                        Bec "Really?"
                                        PC "Of course."
                                        if BecSecret1_Flag:
                                            PC "It'd be another of our secrets"
                                            Bec "Man I'm in sooo much trouble if Dan ever finds out about this.."
                                            "Rebecca gives you her phone number."
                                            Bec "Maybe text me tonight?"
                                            #Affection & Lust Increased
                                            $ BecSexts_Flag = True
                                            jump Day1SchoolMorningSexTalk
                                        else:
                                            Bec "Man I'm in sooo much trouble if Dan ever finds out about this.."
                                            "Rebecca gives you her phone number."
                                            Bec "Maybe text me tonight?"
                                            #Lust Increased
                                            $ BecSexts_Flag = True
                                            jump Day1SchoolMorningSexTalk
                                    "Maybe one day we'll get to live out the fantasy...":
                                        PC "Maybe one day we'll get to live out the fantasy..."
                                        Bec "Maybe we will..."
                                        #Affection & Lust Increased
                                        jump Day1SchoolMorningSexTalk
            else:
                "The air hangs for a moment as we linger on a somewhat uncomfortable silence."
                PC "You might have to start thinking of something or someone else if he's not going to put in the work..."
                menu:
                    "\"Or find someone that will...\"":
                        PC "Or find someone that will..."
                        Bec "Haha. Know anyone?"
                        menu:
                            "\"You're looking at him\"":
                                PC "You're looking at him"
                                Bec "Wooooh! Were'd that come from."
                                Bec "Not cool man."
                                #Affection is decreased
                                #Ends the conversation.
                            "\"I might know a guy who'd treat you right...\"":
                                PC ""
                                Bec "Ohh really? Is he nearby?"
                                PC "Ohh he's close, real close"
                                #Affection & Lust are Increased
                                jump Day1SchoolMorningSexTalk
                            "\"Any Guy would be lucky to have you\"":
                                PC "Any guy would be lucky to have you!"
                                "She blushes"
                                Bec "Thanks."
                                #Affection is Increased
                                jump Day1SchoolMorningSexTalk
                    "Say Nothing":
        "\"Hang on, He's pressuring you into Sex?\"":
            PC "Hang on, He's pressuring you into Sex?"



return