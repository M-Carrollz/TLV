# Characters

define Nar = Character("{i}Batman (Internal Monologue)")
define Bat = Character("Batman")
define Bru = Character("Bruce Wayne")
define Fox = Character("Lucius Fox")
define Alf = Character("Alfred Pennyworth")

define Gor = Character("Commissioner Gordon", color="#112255")
define Mar = Character("Officer Martinez", color="#5f6e78")

define GNN = Character("GNN Anchor", color="#cc0000")

define Mys = Character("Mysterious Woman")

define Ame = Character("Amelia Crowne II")
define Vam = Character("Vamp", color="#c11145")
define Cat = Character("Selina Kyle", color="#5d5555")
define Ivy = Character("Poison Ivy", color="#5ca904")
define Har = Character("Harley Quinn", color="#9c0018")
define Sir = Character("The Siren")

define Pen = Character("Oswald Cobblepot")
define Sal = Character("Salvatore Maroni")

define Hen = Character("Henchmen")
define Thu = Character("Thug")

#------------------------------------------------------------------------------------------------------------

#Flags
define Motel_flag = False
define Detective_Motel1 = False
define Detective_Motel2 = False
define Detective_Motel3 = False
define Detective_Motel4 = False
define Detective_Motel5 = False

define Matchbook_flag = False

define Alfred_flag1 = False
define Fox_flag1 = False

define IcebergLobby_flag1 = False
define IcerbergSecurity_flag1 = False

#------------------------------------------------------------------------------------------------------------

image fg_rain:
    "rain_001_a01"
    pause 0.1
    "rain_002_a01"
    pause 0.1
    "rain_003_a01"
    pause 0.1
    "rain_004_a01"
    pause 0.1
    repeat

#------------------------------------------------------------------------------------------------------------
# Screens
#------------------------------------------------------------------------------------------------------------

screen EastEndMotel_Screen:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5805
        ypos 0.722
        idle "motelmatchbook_idle"
        hover "motelmatchbook_hover"
        action Jump("EEMotelMatchbook")

        #hovered Show("displayTextScreen",
        #    displayText = "Examine matchbook")
        #unhovered Hide("displayTextScreen")
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5095
        ypos 0.718
        idle "motellustdust_idle"
        hover "motellustdust_hover"
        action Jump("EEMotelLustDust")
        
        #hovered Show("displayTextScreen",
        #    displayText = "Examine lines of drugs")
        #unhovered Hide("displayTextScreen")
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.2418
        ypos 0.835
        idle "motelcum_idle"
        hover "motelcum_hover"
        action Jump("EEMotelCum")
        
        #hovered Show("displayTextScreen",
        #    displayText = "Examine fluid trail")
        #unhovered Hide("displayTextScreen")
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.58218
        ypos 0.58785
        idle "motelhamiltonhilldead_idle"
        hover "motelhamiltonhilldead_hover"
        action Jump("EEMotelBody")
        
        #hovered Show("displayTextScreen",
        #    displayText = "Examine corpse")
        #unhovered Hide("displayTextScreen")
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.6693
        ypos 0.466
        idle "motelwallet_idle"
        hover "motelwallet_hover"
        action Jump("EEMotelWallet")
        
        #hovered Show("displayTextScreen",
        #    displayText = "Examine wallet")
        #unhovered Hide("displayTextScreen")


#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

label start:
    scene black
    pause 1.0
    Nar "It's been two years..."
    pause 1.5
    scene bg_gothamclocktower_batsignal_off_a01
    show fg_rain
    with dissolve
    Nar "Two years since I return from exhile..."
    Nar "Two years in my fight to clean up the streets of Gotham."

    scene bg_gothamclocktowerinsert_batsignal_off_a01
    show fg_rain
    Nar "I set out to end organised crime in the city, and over a year ago the first crime family was dismantled."
    Nar "Once one syndicate had been toppled, the rest fell like dominoes."
    Nar "One, after another, the crime bosses felt the same fear they'd inflicted on the city for decades."
    Nar "Carmine Falcone, Salvatore Maroni, Carl Grissom, Tony Zucco... They're all in Blackgate now."

    Nar "Taking them down has left my body beaten and bruised."
    Nar "Venom, the toxic adrenaline concotion used by Bane, that I once used only as a last resort, has now become a crutch of mine to keep me in the crime-fighting game."
    Nar "And everytime a mob boss fell, someone worse took their place."
    Nar "Now Cobblepot and Sionis run the organised crime in the Greater Gotham Area..."
    Nar "But the goons and thugs of the fallen crime bosses now run with violent criminals like the Joker."

    Nar "Sometimes I wonder if what I'm doing is actually helping the people of Gotham... or just bringing them more darkness..."
    Nar "But then I remember: only in the dark can you see true light shine."
    Nar "The police corruption is now over with Gordon as commissioner and Havery Dent as the newly elected DA." 
    Nar "Criminals now have more to fear than what lies in the shadows."
    
    Nar "Gotham is fighting back!"
    
    scene bg_gothamclocktowermidnight_a01
    show fg_rain
    "{i}The Clock Strikes Midnight."
    Nar "February 13th, Valentine's Eve."

    scene black
    with dissolve
    pause 0.5
    scene bg_titlepage_001_a01
    with dissolve
    pause 0.5
    scene bg_titlepage_002_a01
    with dissolve
    pause 2.0
    scene black
    with dissolve
    pause 0.5

    scene bg_pawnshop_a03
    show fg_rain
    with dissolve
    "{i}Rain pours on the gotham city streets."
    scene bg_pawnshop_gnn_a01
    show fg_rain
    with dissolve
    pause 0.5
    scene bg_pawnshop_breakingnews_a01
    show fg_rain
    "{i}\*Jingle plays on TV\*"
    "GNN Breaking News!"
    
    scene bg_gnn_001_a01

    GNN "Breaking News this hour."
    scene bg_gnn_lustdust_001_a01
    GNN "GCPD is reporting the first fatality from the new party drug \"Lust Dust\" that has recently flooded Lower Gotham in the lead up to Valentine's Day."
    GNN "The drug is said to send users into an uncontrollable lust in which the user will either submit to any whim of their partner or send them into a predatory state."
    GNN "Lust Dust has been directly linked to the recent spike in sex-based crime across the city."
    GNN "GCPD has yet to comment on the nature of the fatality that took place at the East End Motel just a few hours ago, other than to link the death to the drug."
    scene bg_gnn_001_a01
    GNN "We reached out to GCPD and the Office of the Mayor for comment but they have declined to comment on an ongoing investigation."

label StartPart2:
    scene bg_gothamclocktowerinsert_batsignal_off_a01
    pause 0.5
    scene bg_gothamclocktowerinsert_batsignal_on_a01
    show fg_rain
    with dissolve
    Bat "My city needs me..."

label MapChoice1:
    scene black
    menu:
        "Meet Gordon at the East End Motel":
            jump EastEndMotel
        "Visit the Bat Signal at the GCPD HQ":
            jump GCPDHQ1

label GCPDHQ1:
    scene bg_gcpd_batsignal_on_a01
    show fg_rain
    Bat "No-one's here. I should meet Gordon at the crime scene in East End."
    jump MapChoice1

label EastEndMotel:
    if Motel_flag:
        jump MotelRenactment
    else:
        jump EastEndMotelDiscussion

label EastEndMotelDiscussion:
    scene black 

    Mar "Gordon!"
    Mar "He's through here..."

    scene bg_eastendmotel_001_a01

    Gor "Thanks for coming."
    Gor "Hamilton Hill, The disgraced former Mayor."
    Gor "The intial Corner Report says that he overdose on Lust dust." 
    Gor "His heart gave out having sex."
    Mar "What a way to go! Getting fucked to death..."
    Mar "Better than that corrupt attempted cop killer deserved!"
    Bat "Who was the parter?"
    Gor "Unkown." 
    Gor "Mrs. Hill was out of town..."
    Bat "Then who rented the room?"
    Gor "Rented out in the name of \"Cash\"."

    "Batman nods, before taking in the room, searching it for clues or evidence."
    

label EastEndMotel_Detective:
    if Detective_Motel1:
        if Detective_Motel2:
            if Detective_Motel3:
                if Detective_Motel4:
                    if Detective_Motel5:
                        jump MotelRenactment
                    else: 
                        jump EastEndMotel_Detective2
                else: 
                    jump EastEndMotel_Detective2
            else: 
                jump EastEndMotel_Detective2
        else: 
            jump EastEndMotel_Detective2
    else: 
        jump EastEndMotel_Detective2

    
label EastEndMotel_Detective2:
    call screen EastEndMotel_Screen

label EEMotelLustDust:
    Nar "Crushed Lust Dust tablets. Looks like these were crushed by someone who knew what they were doing..." 
    Nar "...with Hamilton Hill running on an anti-drug platform it seems like the mysterious sexual parter might have broken them up."
    Nar "Shame they were all broken up, we still don't know what the uncrushed tablets look like." 
    Nar "Other than that they seem to come in a variety of different bright colours..."
    Nar "I'll have to get this test, might be able to trace the ingredients to find the source."
    $ Detective_Motel1 = True
    jump EastEndMotel_Detective

label EEMotelBody:
    Nar "Lipstick marks on the shirt collar, neck..."
    Nar "and all over the base of gentials."
    Nar "It looks like the mysterious woman was the instigator."
    $ Detective_Motel2 = True
    jump EastEndMotel_Detective

label EEMotelCum:
    Nar "The trail of semen looks like he came inside her whilst dying."
    Nar "Seems like she wasn't panicked or in a rush at all..."
    $ Detective_Motel3 = True
    jump EastEndMotel_Detective

label EEMotelWallet:
    Nar "Wallet is still here and is full of cash..."
    Nar "That rules out a robbery gone wrong, and suggests that our mysterious woman isn't a lady of the night."
    $ Detective_Motel4 = True
    jump EastEndMotel_Detective
    
label EEMotelMatchbook:
    Nar "A Matchbook. This feels out of place, like it was planted."
    Nar "Iceberg Lounge. I'll have to take a visit."
    $ Detective_Motel5 = True
    jump EastEndMotel_Detective

label MotelRenactment:
    scene black 

    Nar "I think I've peiced together what happened here..."
    Nar "It looks like the unknown woman seduced Hamilton at the Iceberg Lounge..."
    Nar "Then they came back here."
    Nar "She cut up the Lust Dust and gave him a lethal dose."
    Nar "She stradled him and started kissing his neck."
    Nar "then she worked her way down his chest."
    Nar "she kissed and licked his shaft."
    Nar "The mysterious woman then got on top of him..."
    Nar "and fucked him..."
    Nar "for hours..."
    Nar "and hours..."
    Nar "on end."
    Nar "until he climaxed..."
    Nar "and died."
    Nar "Before she calmly got up..."
    Nar "... and walked out."
    if Motel_flag:
        if Matchbook_flag:
            jump MapChoice3
        else:
            jump MapChoice2
    else:
        jump EastEndMotelContinued

label EastEndMotelContinued:
    scene bg_eastendmotel_001_a01

    Bat "Looks like we're searching for a femme fatale, this seems like it might have been orchestrated."
    Gor "Are you saying... this is murder?"
    Bat "I am."
    Gor "Ugh... The Press is going to have a field day with this."
    Gor "What's the...?"
    Gor "Hmph."
    Mar "Happy Hunting Batman."
    $ Motel_flag = True
    jump MapChoice2Discussion

#------------------------------------------------------------------------------------------------------------

label MapChoice2Discussion:
    scene black 

    Nar "The matchbox is from the Iceberg Lounge. I should take a visit... "
    Nar "Although something about that matchbox doesn't fit the crime, it felt out of place... like it was staged."
    Nar "I should swing by Wayne Tower, see if Lucius is able to find out more about Lust Dust from the sample I gathered from the Motel."
    Nar "I could also go see Alfred and get him to pour over the logs. He might be able to see if any of this matches the MO of someone I've already come up against."

label MapChoice2:
    menu:
        "Visit GCPD HQ":
            jump GCPDHQ2
        "Visit Alfred at Wayne Manor":
            if Alfred_flag1:
                "Alfred needs time to look over the logs, I should check back later."
                jump MapChoice2
            else:
                jump Alfred1
        "Examine the Matchbook":
            jump Matchbook
        "Visit the Iceberg Lounge":
            jump IcebergLoungeLobby1
        "Revist the East End Motel":
            jump EastEndMotel
        "Visit Lucius Fox at Wayne Tower":
            if Fox_flag1:
                "Lucius needs time to test the samples, I should check back later."
                jump MapChoice2
            else:
                jump Fox1

#------------------------------------------------------------------------------------------------------------

label GCPDHQ2:
    scene bg_gcpd_batsignal_off_a01
    show fg_rain
    Bat "No-one's here. I should follow up on my other leads."
    if Matchbook_flag:
        jump MapChoice3
    else:
        jump MapChoice2

label Alfred1:
    scene black 

    Alf "Welcome home Mr. Wayne!"
    Alf "Please tell me you're not here for another dose of Venom?"
    Alf "I know your body is beaten up but we {i}really{/i} need to limit it's use to emergencies."
    Bru "Alfred, we've discussed this and I agree it's only to be used as a last resort..." 
    Bru "But that's not why I'm here..." 
    Bru "I need you to pour over the logs. We're looking for a femme fatale who uses love or lust based chemical compounds to influence and kill powerful men."
    Alf "I'll see what I can conjure up for you. It'll take a few hours..." 
    Alf "But in the meantime I'll also use some of my old SIGINT contacts to see if what I can find out."
    Bru "Thanks Alfred, where would I be without you?"
    Alf "Dead in a ditch I'm sure."
    $ Alfred_flag1 = True
    if Matchbook_flag:
        jump MapChoice3
    else:
        jump MapChoice2

label Fox1:
    "add Scene"

    $ Fox_flag1 = True
    if Matchbook_flag:
        jump MapChoice3
    else:
        jump MapChoice2

label Matchbook:
    scene black 

    "A Matchbox from the Iceberg Lounge. Cobblepot's seedy underground nightclub. A hive of scum and villany..."
    "Batman opens the match box."
    "Inside there's a message for the Batman with an address in the Bowery, another high crime neighbourhood in Lower Gotham."
    Bat "Looks like someone is sending me a message..."
    Bat "Time to go spring the trap."
    jump MapChoice3

#------------------------------------------------------------------------------------------------------------

label IcebergLoungeLobby1:
    scene black 

    Nar "If Hamilton and the mysterious woman were here they might have been caught on the CCTV, I should check the club security office."
    Nar "It might also be worth talking to Oswald, see if the Penguin knows anything about Love Dust."

label IcebergLobbyMenu1:
    if IcebergLobby_flag1:
        menu:
            "Security Room":
                jump IcebergLoungeSecurityOffice
            "Find Cobblepot":
                "Cobblepot has given me a few leads, I should followup on them."
                jump IcebergLobbyMenu1
            "Leave the Iceberg Lounge":
                if Matchbook_flag:
                    jump MapChoice3
                else:
                    jump MapChoice2
    else:
        menu:
            "Security Room":
                jump IcebergLoungeSecurityOffice
            "Find Cobblepot":
                jump IcebergLoungeOswald1
            "Leave the Iceberg Lounge":
                if Matchbook_flag:
                    jump MapChoice3
                else:
                    jump MapChoice2


label IcebergLoungeSecurityOffice:
    scene black 

    Hen "Hey! You can't come in..."
    "Batman thrust a powerful jab into the henchmen's cranium that knocks him out cold."
    Nar "Better check the security feed to see if we can see the disgraced Mayor leave with his femme fatale mistress..."
    #Add Choice here (can select the current recording or the archive tapes)
    "Batman scrubs the current recording until he finds the vision of Hamilton leaving with his mysterious mistress."
    Nar "That raven-haired woman must be our mysterious sexual partner..."
    Nar "Hmmm... Her face is hidden in this footage."
    Nar "I should ask around to see if anyone knows more or see if I can find some other evidence while I'm here."
    #Add Choice here (can leave or take a look at the archive tapes)
    jump IcebergLobbyMenu1

label IcebergLoungeOswald1:
    scene black 

    Hen "Hey! Stop Him! He's going for the boss!"
    "A Henchmen throws a wild haymaker at Batman who blocks it..." 
    "Before smashing the henchmen's head into a table covered in drinks."
    Hen "I'll fucking kill him!"
    Pen "You wouldn't stand a chance, so shut up and get \'smashed mouth\' over ther some ice for that concussion!"
    Pen "You see... Mr. Batman.. he's here for a chat..."
    Pen "Overdosing former Mayor's don't look so good on the front page of the Gotham Gazette."
    Pen "Mr. Batman, why don't you ah... step into my office..."

    Pen "Look, ya got me... and by ya got me I mean the wrong guy."
    $ IcebergLobby_flag1 = True
    jump IcebergLobbyMenu1

#------------------------------------------------------------------------------------------------------------

label MapChoice3:
menu:
        "Visit GCPD HQ":
            jump GCPDHQ2
        "Visit Alfred at Wayne Manor":
            if Alfred_flag1:
                "Alfred needs time to look over the logs, I should check back later"
                jump MapChoice3
            else:
                jump Alfred1
        #"Visit Bowery Appartment":
            #jump BoweryAppartment
        "Visit the Iceberg Lounge":
            jump IcebergLoungeLobby1
        "Revist the East End Motel":
            jump EastEndMotel
        #"Visit Lucius Fox at Wayne Tower":
            #jump Fox1

#------------------------------------------------------------------------------------------------------------

label BlackgateSalvatore:
    scene black 

    Sal "Hmph. Gaurd!" 
    Sal "It's the Batman, Gotham's Most wanted Vilgalante..." 
    Sal "Surely there's an arrest warrant out for this.... Freak!"
    "The Prison Guard looks at Salvatore before turning away unfazed by Maroni's comment."
    Sal "Actually big guy, I'd say belong in Arkham; a guy dressed as bat clearly has issues."
    "Batman doesn't react."
    Sal "What's the matter? Cat got you tongue?"
    Bat "Carmine Faclone. Why'd you do it?"
    Sal "He looked at me funny..."
    Bat "I know about the congical visit Sal! And that you're wife was in Blüdhaven." 
    Bat "After the visit you were describe as hypnotised... so who was she?"
    "Maroni's tough guy fascade fades away."
    Sal "Look.. I don't know who she is... I'm in prison and a pretty little thing said she wnated to have sex with me. I wasn't going to pass up on a good thing."
    Sal "But I'll told you what i told the warden"
    Sal "She did something to me..."
    Bat "Tell me. From the beginning."

    Sal "{i}So... I get escorted into the congical suite, this pale petite brunette is waiting for me in a skimpy outfit."
    Sal "{i}I took in the sights..."
    Sal "{i}I went to talke but she didn't let me speak..."
    Mys "Just let me do all the work."
    Sal "{i}She got on her knees in front of me."
    Sal "{i}Undid my pants, freeing my dick."
    Sal "{i}She then lick my shaft..."
    Sal "{i}Focused on my knob..."
    Sal "{i}Before she took me in her mouth."
    Sal "{i}Before long she was deep throating me..."
    Sal "{i}Let me tell you... the girl knows how to use her throat..."
    Sal "{i}was the best blowjob I've ever had..."
    Sal "{i}Felt like her throat was gripping my cock as it made her gag a little."

    Sal "{i}She eventually got up lifted up her skimpy little dress and pointed her cute little ass at me."
    Sal "{i}Needless to say... I didn't need any further of an invitation."
    Sal "{i}I walked up and I slide my cock over her tight ass..."
    Sal "{i}Until it slid in between her ass cheeks and started to glide over her little asshole and tight dripping wet pussy."
    Sal "{i}She trust back at me when the head was positioned over her tight little hole..."
    Sal "{i}Pushing me inside her."
    Sal "{i}She moaned for me... it sounded incredibly sexy."
    Sal "{i}I can not understate how sexy her moan sounded... it drove me wild!"
   
    #Add more detials
    # Sal "{i}" 

    Sal "{i}She moaned in a really high pitched squeal as we were both getting close..."
    Sal "{i}and another as I came inside her..."
    Sal "{i}From there it's a blur... but it felt like I was no longer in control."
    Sal "{i}She whispered something in in my ear..."
    Sal "{i}and the visit was over."
    Sal "{i}From there I went straight to Falcone's Cell..."
    Sal "{i}...pulled out my shiv..." 
    Sal "{i}and went to town on him."
    Sal "{i}But it felt like I was a passenger, like I watched it all play out."

    Sal "...And that's what happened."
    Sal "Now... you going to put in a good word so I get congical visitation rights back?"
    Bat "I never said I'd help you."
    Sal "True... but if she comes back I'll have more details to give you, new leads for the World's Greatest Detective to follow..."
    Sal "You love that kind of shit."
    Bat "Guard! We're done here."
    "The Prison Gaurd takes Maroni away."
    "Maroni smiles knowing he might have the Caped Crusader helping him get laid."

    #Choice Tell the Warden to reinstate the Congical Visits or ignore Maroni's Request.
    menu Maroni_Choice:
        "Speak to the Warden for Maroni":
            jump WardenMaroni
        "Ignore Maroni's Request":
            jump MapChoice6
        
label WardenMaroni:
    scene black 
    
    Bat " "

label MapChoice6:
