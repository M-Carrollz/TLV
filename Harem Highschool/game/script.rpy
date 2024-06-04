# ------------------------------------------------------------------- Characters -------------------------------------------------------------------
define PC = Character("Player Character")

define Bec = Character("Rebecca")
define BecThoughts = Character("Rebecca \(Thoughts\)")
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

# ----------------------------------------------------------------- Character Stats -----------------------------------------------------------------

init:
    $ Bec_Lust = 0
    $ Bec_Affection = 0


# ------------------------------------------------------------------- Flags -------------------------------------------------------------------

define Bec1_Flag = False
define Bec2_Flag = False
define BecSecret1_Flag = False



# -------- Sexts Flags --------
define BecSexts_Flag = False

# ------------------------------------------------------------------- The game starts here. -------------------------------------------------------------------

label start:

    scene black
    "Day 1"
    "The alarm clock beeps 6AM."
    PC "{i}(mutters){/i} ...five more minutes..."
    "{i}Brain... no work... too tired... can't even remember my own name."
    #Player Provides name
    "The alarm clock continues to beep incessantly."
    PC "{i}(muttering){/i} Please... 5 more mins... then I swear I'll get up."
    "I suddenly snap out of it"
    PC "Ohhh fuuuuuuck..." 
    PC "Yeah thats right, I'm alone now."
    "I manage to crack half a smile, shaking my head in a tired disbelief."
    PC "*sigh*"
    PC "I better get up."
    "I throw off the sheets and sit on the edge of the bed struggling to find the energy to get up whilst simultaneously also fighting to stay awake."
    "{i}Today is the first day of Senior Year, Year 12, 12th Grade, Upper 6th... whatever they call it where I live, I don't fucking remember... I'm too tired for this shit."
    "{i}I am NOT a morning person..."

    "I finally stumble out of bed and get the morning ablutions done."
    "Shower, Shit, Shave... hopefully not in that order but I still waking up, so needless to say I'm in autopilot mode and I'm hoping to hell they know what they are doing at this time of day..."
    "In the fog of my sleep deprived brain I continue with my morning routine: eat some breakfast, get dressed and with my car in the shop, I head off to jump on the bus."

label Day1BusMorning:

    scene black
    PC "{i}(muttering to myself){/i} Ughh... 18, with a licence and still on the bus... stupid idiot broke my car..."
    "{i}WAIT ONE GOD DAMN MINUTE..."
    "{i}Why the fuck didn't I get a courtesy car!?"
    "I open my phone; quickly going to my car insurance website to read the terms and conditions, somehow suddenly wide awake and filled with rage."
    "{i}Ohhhh... gotta be 25 to rent a car..."
    PC "Well fuck..."

label Day1SchoolMorning:

    scene black
    "I walk into school bright and early like I always..."
    PC "Hang the fuck on... why am I here this early?"
    "{i}I used to get here early as my parents would drop me off early before heading to work, but I got here on my own."
    PC "*sigh* Fuck... Idiot!"
    "I curse at myself unable to believe my own stupidity before looking up to my usual morning hangout."
    "{i}Ahh well it's not all bad..."
    "I look over and see a beautiful brunette sitting on the bench."
    #show off Bec
    "She looks over at me and smiles instantly."
    Bec "Name!!"
    "She runs over and throws her arms around me, holding me tightly."
    Bec "It's been too long! I've missed my favourite morning person!"
    "We both laugh."
    PC "Neither of us are morning people and you know it!"
    Bec "{i}(laughs){/i} True... but here we are..."
    PC "One day we'll both get a sleep in."
    Bec "That would be nice..."
    Bec "But that would mean I don't get to have you all to myself for our morning catch up."

    menu:
        "\"I wouldn't say that... we could be sleeping in together?\"":
            jump Day1MorningFlirt
        "\"Ohhh I'm sure I'd find another way to catch up with, you're worth the effort!\"":
            jump Day1MorningGoodGuy

label Day1MorningFlirt:
    Bec "You flirt..."
    PC "With you, Always."
    Bec "Well not always, just when you have me all to yourself."
    Bec "Otherwise you'd get me in trouble with Dan."
    PC "...and we wouldn't want that."
    "We both smile knowing that we shouldn't be saying these things but in our playfullness we've always stopped short of some imaginary second boundry that keeps her relationship unsullied."
    #Lust and Affection are both Increased
    $ Bec_Lust += 1
    $ Bec_Affection += 1
    jump Day1SchoolMorningCont

label Day1MorningGoodGuy:
    Bec "Nawww... you're soo nice to me."
    Bec "But yeah we'd definetly need to find a way to catch up if we missed the mornings together."
    PC "100\%"
    PC "Can't go around not knowing how you are each day... that'd be crazy!"
    "We both laugh and smile"
    #Affection is Increased
    $ Bec_Affection += 1

label Day1SchoolMorningCont:
    PC "How was your time off?"
    Bec "It was really good!"
    PC "Yeah? What'd you get up to?"
    Bec "Spent some time with the family, saw Dan a bunch..."
    Bec "Ohh and I saw Katie a few times."
    PC "Ohh I saw Katie a couple times over the break as well!"
    Bec "Yeah she told me she'd seen you a bit."
    if Bec_Lust >= 1:
        Bec "You really do have a thing for girls that are off limits huh?"
        jump Day1SchoolMorningFlirt
    else:
        Bec "I miss her here with us school, it's a shame she's going to that all girls school now."
        PC "Same." 
        PC "It just doesn't feel right not seeing her every day."
        jump Day1SchoolMorningCont2

label Day1SchoolMorningFlirt:
    PC "Just because you're taken {i}doesn't{/i} mean you're off limits..."
    Bec "Oh really?"
    PC "Yeah. It just makes it more of a challenge..."
    PC "...and a little extra naughty, wouldn't you agree?"
    "She smiles and looks at me with sultry eyes."
    Bec "I'd have to agree, it's a little {i}naughty{/i}... but also kinda nice."
    "I smile back her, both of us basking in the warm glow of mutal flirtation."
    PC "Well... if that's the case, I better keep at the challenge I've been set."
    Bec "Please do."
    #Lust and Affection are both Increased
    $ Bec_Lust += 1
    $ Bec_Affection += 1
    
label Day1SchoolMorningCont2:
    "We pause for a moment of comfortable silence."
    PC "Soooo... How are things with Dan? Still going strong I hope?"
    "She gives me a look suggesting I'm not being 100\% truthful."
    PC "No, seriously how are two going? Is he treating you right?"
    menu:
        "Wait for her to Answer":
            jump Day1SchoolMorningCont3
        "\"Cause if he's not... I know a guy who'll treat you the princess you are?\"":
            Bec "Really? Would they get me a tiara?"
            PC "Yep, and carry you around princess style."
            Bec "You'll simply have to introduce me one day then."
            PC "I'll do my best."
            "We smile enjoying our little fantasy."
            PC "But I do actually want to know, he's a part of your life afterall. So how are things?"
            #Lust and Affection are both Increased
            $ Bec_Lust += 1
            $ Bec_Affection += 1
            jump Day1SchoolMorningCont3

label Day1SchoolMorningCont3:
    Bec "Yeah we're going ok I suppose..."
    Bec "Although... if I'm honest, and keep this between you and me..."
    menu:
        "\"Of course!\"":
            Bec "Thanks."
        "\"Don't worry... I can keep a secret\"":
            Bec "Haha. I bet you can."
            $ BecSecret1_Flag = True
            #Lust And Affection are Increased
            $ Bec_Lust += 1
            $ Bec_Affection += 1
    Bec "Anyway he's been kinda pestering me for sex lately..."
    Bec "...and I know we've been dating for ages now... but, I dunno, every time he brings it up he seems like an excited puppy about to play with a new toy..."
    Bec "He doesn't seem like he cares to make it something I want to do... and I don't want to give my virginity to someone as a present or an obligation to them..."
    Bec "I wanna loose it in the moment."
    Bec "Does that make sense?"

label Day1SchoolMorningSexTalk:
    if Bec1_Flag:
        if Bec2_Flag:
            jump Day1SchoolMorningEnd
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
            PC "That's awful... and manipulative!"
            if Bec_Lust >= 1:
                PC "and look... I know that's coming from me flirting with you when you're dating Dan, It's an asshole act and I know it. I'd stop if you ever asked me to..." 
                "She smiles and laughs."
                PC "But you gotta make him realise that he's not guaranteed sex just because he's dating you!"
                Bec "I know..."
                #Affection is Increased
                $ Bec_Affection += 1
                jump Day1SchoolMorningSexTalk
            else:
                PC "You gotta make him realise that he's not guaranteed sex just because he's dating you!"
                Bec "I know..."
                #affection is increased
                $ Bec_Affection += 1
                jump Day1SchoolMorningSexTalk

        "I don't get where his heads at.":
            PC "I don't get where his heads at."
            PC "That's never going to get you in the mood."
            Bec "Right!?"
            $ Bec1_Flag = True
            if Bec_Lust >= 3:
                    PC "Like if I was to about to take someone's virginity I'd want to take them out on a date."
                    PC "Make it an absolute magical night, a perfect night..."
                    PC "One they would look back on fondly for the rest of their lives..."
                    PC "...and then when we get back home and start making out..."
                    PC "I'd kiss them all over, play with them, make sure they're super wet..."
                    BecThoughts "Mmmmm... I'm starting to get a bit wet just hearing this..."
                    #Show Bec Getting wet
                    #Lust is Increased Significantly
                    $ Bec_Lust += 5
                    PC "I'd look into her eyes and ask what she wants..."
                    PC "...and if she wants me to continue I'd give her a night to remember, focusing 100\% on her wants, needs and desires."
                    BecThoughts "Noooooo... Don't stop talking, that was fucking hot!"
                    Bec "See that's what I want!"
                    BecThoughts "Why'd he have to stop? I'm so going to have to masturbate over this conversation tonight."
                    menu:
                        "\"Well maybe we can make it a reality some day?\"":
                            if Bec_Lust >9 :
                                Bec "Hmmm.. We'll just have to wait and see..."
                                jump Day1SchoolMorningSexTalk
                                #Lust is Increased
                                $ Bec_Lust += 2
                            else:
                                Bec "Wow! You can't just say that!"
                                Bec "I let you get way with a lot of shit but that's going over the line."
                                #Affection & Lust are decreased
                                $ Bec_Lust -= 1
                                $ Bec_Affection -= 1
                                #Ends the conversation.
                                jump Day1SchoolMorningEnd
                        "\"Then I hope that one day you get that, no matter who ends up being the lucky guy.\"":
                            Bec "Thanks me too..."
                            #Affection is Increased
                            $ Bec_Affection += 1
                            if Bec_Lust >= 9:
                                Bec "The way you described that was pretty hot by the way..."
                                PC "Haha. Thanks."
                                menu:
                                    "\"I'd be happy to write naughty stories for you anytime.\"":
                                        "Rebecca bites her lip."
                                        Bec "Really?"
                                        PC "Of course."
                                        if BecSecret1_Flag:
                                            PC "It'd be another of our secrets..."
                                            Bec "Man I'm in sooo much trouble if Dan ever finds out about this..."
                                            "Rebecca gives you her phone number."
                                            Bec "Maybe text me tonight?"
                                            #Affection & Lust Increased
                                            $ Bec_Lust += 1
                                            $ Bec_Affection += 1
                                            $ BecSexts_Flag = True
                                            jump Day1SchoolMorningSexTalk
                                        else:
                                            Bec "Man I'm in sooo much trouble if Dan ever finds out about this.."
                                            "Rebecca gives you her phone number."
                                            Bec "Maybe text me tonight?"
                                            #Lust Increased
                                            $ Bec_Lust += 1
                                            $ BecSexts_Flag = True
                                            jump Day1SchoolMorningSexTalk
                                    "\"Maybe one day we'll get to live out the fantasy...\"":
                                        Bec "Maybe we will..."
                                        #Affection & Lust Increased
                                        $ Bec_Lust += 1
                                        $ Bec_Affection += 1
                                        jump Day1SchoolMorningSexTalk
                            else:
                                jump Day1SchoolMorningSexTalk
            else:
                "The air hangs for a moment as we linger on a somewhat uncomfortable silence."
                PC "You might have to start thinking of something or someone else if he's not going to put in the work..."
                menu:
                    "\"Or just find someone that will...\"":
                        PC "Or just find someone that will..."
                        Bec "Haha. Know anyone?"
                        menu:
                            "\"You're looking at him\"":
                                if Bec_Affection >= 5:
                                    Bec "Ohh and he's cute too..."
                                    "We both laugh softly."
                                    #Affection & Lust Increased
                                    $ Bec_Lust += 1
                                    $ Bec_Affection += 1
                                    jump Day1SchoolMorningSexTalk
                                else:
                                    Bec "Wooooh! Were'd that come from."
                                    Bec "Not cool man."
                                    #Affection is decreased
                                    $ Bec_Affection -= 1
                                    #Ends the conversation.
                                    jump Day1SchoolMorningEnd
                            "\"I might know a guy who'd treat you right...\"":
                                Bec "Ohh really? Is he nearby?"
                                PC "Ohh he's close, real close."
                                #Affection & Lust are Increased
                                $ Bec_Lust += 1
                                $ Bec_Affection += 1
                                jump Day1SchoolMorningSexTalk
                            "\"Any guy would be lucky to have you\"":
                                "She blushes"
                                Bec "Thanks."
                                #Affection is Increased
                                $ Bec_Affection += 1
                                jump Day1SchoolMorningSexTalk
                    "Say Nothing":
                        Bec "You don't think thinking of someone else during sex is wrong?"
                        Bec "Like isn't it cheating?"
                        #Menu
        "\"Hang on, He's pressuring you into Sex?\"":
            PC "Hang on, He's pressuring you into Sex?"
            $ Bec2_Flag = True


label Day1SchoolMorningEnd:
    "The Current End"

label Day1Homeroom:
    "I enter into homeroom, keen to find out my schedule for the year."
    #Talk with Steph about walking hom togteher and your car getting wrecked outside your own home

label Day1P1Maths:
    #Mathsbuddy & Texts from Hayley?

label Day1SchoolAssembly:
    #Would have English Class with Kayla
    #The School Play is announced
    #Charlotte and Eloise ask if you're going to join. Bec will also.
    #Charlotte also invites you to Her and Eloise's Join Party where they will be legal.
    #She says her current ID say's shes 18 or over (Show fake ID) - No Sex with until after the party.

label Day1Lunch:
    "??"

    
return