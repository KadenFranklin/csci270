# The script of the game goes in this file.

define c = Character("Chet")
define d = Character("Doc")
define ep = Character("Easy Pete")
define s = Character("Sunny")
define t = Character("Trudy")
define v = Character("Victor")

label start:

    scene bg room:
         xalign 0.9
         yalign 1.0
         size (1280, 920)
    
    show doc_mitchell:
         xalign .5
         yalign .3
         size (350, 240)
    
    $ count = 0
    
    $ stolen = False

    d "Woah there you're up already? "
    
    d "Don't get up too quick, take it easy, you were shot in the head."
    
    d "You been out 3 days, you're a lucky."
    
    d "I didn't think that you were gonna make, when that robot brought you to me."
    
    d "Yup said he found you in a grave, don't know who did it or for what reason."
    
    d "Now tell me what do you remember?"
    
    menu:            
        "I remember nothing. Not even my name":
            d "Well other than the amnesia, your body has recovered remarkably fast."        
            
        "I remember the alamo":
            d "Well other than the amnesia, your body has recovered remarkably fast."        
          
        "I remember a man, in a checkered suit. He's the one who shot me, he took something from me, something important I just dont remember what.":
            d "Well other than the amnesia, your body has recovered remarkably fast."        
            
    d "As a formality I have to give you a pyschological evaluation before I can let you leave."

    d "Just tell me what you see in each of these pictures."
    
    show doc_1:
         xalign .5
         yalign .3
         size (350, 240)
    
    menu:            
        "I see two ducks kissing.":
            d "Alright then."        
            
        "I see my mother and father":
            d "Okie doke."        
            
        "A very large ant.":
            d "Got it."        
            
    show doc_2:
         xalign .5
         yalign .3
         size (350, 240)
    
    menu:            
         "I think it is a book.":
            d "Alright then."        

         "The barrel of a gun.":
            d "Okie doke."        

         "I see a well, used for drawing water.":
            d "Got it."        
            
    show doc_3:
         xalign .5
         yalign .3
         size (350, 240)
    
    menu:            
         "A persons hands":
            d "Alright then"        

         "Two men praying":
            d "Okie doke."        

         "I see a former loved one.":
            d "Got it"        

    d "Well all things considered you don't seem too bad off."
    
    d "I'll let you get on your way. But just so you know we got some troube going around town."
    
    d "I don't think its the same people that roughed you up, some gang."
    
    d "If you're willing to stick around we'd sure appreciate it, but I understand if you need to be getting on your own way."
    
    d "See you around stranger."
    
    scene bg room:
         xalign 0.9
         yalign 1.0
         size (1280, 920)
    
    "This doctor seems like a nice man. He definitely gave me more attention than he needed to."
    
    "Before I get on my way I wonder if there is anything of his that will help me out."
    
    menu:            
        "Steal as much from the doctors house as you can possibly carry. And then leave.":
            $ count += 1
            
            $ stolen = True
            
            "You walk around the doctors house casually putting stuff in your pockets until you cannot fit any more."
            
            "The doctor sits there cold, emotionless, and sips an empty cup of coffee, almost as though he deos not notice you."
            
            jump goodsprings
            
        "Leave the doctors house.":
            
            "You walk outside."
            
            jump goodsprings

    
label goodsprings:

    scene bg goodsprings:
         xalign 0.9
         yalign 1.0
         size (1280, 920)
    
    "As the sun hits your eyes you are greeted with a somber sight."

    "A barren wasteland appears before you."
    
    "You do not remember if this was the world you lived in before, but it is the one you live in now."
    
    "A seemingly friendly robot approaches you"
    
    show victor:
         xalign 0.5
         yalign .3
         size (240, 240)

    v "Well Howdy Partner!!"
    
    v "I was the one that dug you up out the ground. You seem a lot better now."
    
    v "Look I know you probably got business to attend to, and the doc already told you about the powder gang."
    
    v "And if you stick around, i'd be more than happy to help escort you out of town. And help if the gang tries anything."
    
    v "So I won't waste your time, here are the people that could help you."
    
    menu:
        "Talk to Chet":
            jump chet
        
        "Talk to Easy Pete":
            jump easy_pete
            
        "Talk to Sunny":
            jump sunny
        
        "Talk to Trudy":
            jump trudy

        "Leave town to the East.":
             jump leave_east

        "Leave town to the East.":
             jump leave_west


label goodsprings_2:

    scene bg goodsprings:
         xalign 0.9
         yalign 1.0
         size (1280, 920)
 
    "back to the center of town I guess."

    menu:
         "Talk to Chet":
             jump chet
            
         "Talk to Easy Pete":
             jump easy_pete
                
         "Talk to Sunny":
             jump sunny
            
         "Talk to Trudy":
             jump trudy

         "Leave town to the East.":
             jump leave_east

         "Leave town to the West.":
             jump leave_west


label chet:

    scene bg goodsprings:
         xalign 0.9
         yalign 1.0
         size (1280, 920)
    
    show chet:
         xalign 0.5
         yalign .3
         size (240, 240)
    
    c "Hey there, I'm chet. I am the towns general merchant."
    
    if stolen:
        menu:
             "Why actually yes I do here you go.":
            
                $ count += 1
            
                c "perfect, Here have something that will help you defeat the gang."
            
                jump goodsprings_2
    
    else:
        "I am sorry I don't have anything to trade."
        
        c "That's quite a shame."
        
        jump goodsprings_2
    
    
label easy_pete:

    scene bg goodsprings:
         xalign 0.9
         yalign 1.0
         size (1280, 920)
    
    show easy_pete:
         xalign 0.5
         yalign .3
         size (240, 240)
    
    ep "Hey there stranger. You're that one that almost got buried a couple days ago right."
    
    ep "You're the most exciting thing to happen to this town since the NCR started their trade route."
    
    ep "Here, since it seems like you're looking to help out around here, have some dynamite. It'll help you if you encounter the powder gangers. "
    
    $ count += 1
    
    jump goodsprings_2
    

label sunny:

    scene bg saloon:
         xalign 0.9
         yalign 1.0
         size (1280, 920)
    
    show sunny:
         xalign 0.5
         yalign .3
         size (240, 240)
		 
	play music "Fallout NewVegas Radio.mp3"
    
    s "Hey there stranger. you're the type that needs no introduction, but my name is sunny."
    
    s "do ya wanna help me out with our gecko problem?"
    
    menu:
         "Nah I am good.":
        
            jump goodsprings_2
            
         "Sure I'll help out":
        
            s "Sweet, they are just outside by the water well."
            
            scene bg goodsprings:
                xalign 0.9
                yalign 1.0
                size (1280, 920)
            
            show sunny:
                xalign 0.5
                yalign .3
                size (240, 240)
            
            s "They're right over there."
            
            show gecko:
                xalign 0.9
                yalign 1.0
                size (240, 240)

            $ count += 1
            
            s "You got 'em, nice job."
            
            jump goodsprings_2
    
    
label trudy:
    scene bg saloon:
         xalign 0.9
         yalign 1.0
         size (1280, 920)
		 
	play music "Fallout NewVegas Radio.mp3"
    
    show trudy:
         xalign 0.5
         yalign .3
         size (240, 240)
    
    t "Hey there. my names trudy, I'm the inkeep."
    
    t "I heard you're sticking around to help us with the powder gang."
    
    t "smart move. They're off to the west of town. They're also not that bright, and look tougher than they'll ever be."
    
    t "That's all I can offer you is some solid info, can't give you any emotional or tangible support."
    
    t "I'll see you around now."
    
    $ count += 1
    
    jump goodsprings_2
    
    
label leave_east:

    scene black:
         xalign 0.9
         yalign 1.0
         size (1280, 920)
		 
	play music "Fallout NewVegas Ending.mp3"

    "you walk off leaving the town to the east."
    
    "You walk for about an hour before coming to a narrow road between two hills."
    
    "You proceed."
    
    "As you continue and pass through the valley, you notice some creatures in the distance."
    
    "They notice you too and start sprinting in your direction."
    
    "It is clear that you cannot outrun them. And you are no match to fight them."
    
    "If only you had helped the town with their problems, maybe you would't have chosen this path"
        
    "{b}Bad Ending{/b}."

    return


label leave_west:

    scene black:
         xalign 0.9
         yalign 1.0
         size (1280, 920)
		 
	play music "Fallout NewVegas Ending.mp3"
    
    "you walk off leaving the town to the west."
    
    "You encounter the powder gang."
    
    show powder_gang:
         xalign 0.5
         yalign .3
         size (240, 240)
    
    if count > 2:
        
        "They are a viscious bunch but with the tools your newfound friends have armed you with you were well equiped to deal with them."

        "You defeat them with victors help and experience gained from your time in town."

        "You walk away from goodsprings, unknowing of where you are headed, or if you will ever be back."
        
        "{b}Good ending{/b}."

        return
        
    elif count < 2:

        "They are too much for you to deal with on your own."
        
        "They end up capturing you and invading good springs."
        
        "If only you had gotten some help from the town when you got the chance."
        
        "{b}Bad Ending{/b}."

        return
        
