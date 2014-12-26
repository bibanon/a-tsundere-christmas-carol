# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg white = "white.png"
image bg black = Solid(color("#000000"))
image snowlight = SnowBlossom("snowflake.png", 1000, 20, (100, 200), (100, 600))
image snow = SnowBlossom("snowflake.png", 50, 50, (20, 10), (200, 10))
image board1 = "board1.png"
image board2 = "board2.png"
image board3:
    contains:
        "board3.png" with hpunch
        0.2
        "board3.png" with hpunch
        0.2
        repeat
image board4 = "board4.png"
image board5 = "board5.png"
image board6 = "board6.png"
image board7 = "board7.png"
image board8 = "board8.png"
image board9 = "board9.png"
image board10 = "board10.png"
image board105:
    contains:
        "board5"
        alpha 0
        linear 1.0 alpha 0.8
        linear 1.0 alpha 0
        repeat

image board11 = "board11.png"
image board12 = "board12.png"
image board13 = "board13.png"
image board14 = "board14.png"
image board15 = "board15.png"
image board16 = "board16.png"
image board17 = "board17.png"
image board18 = "board18.png"
image board19 = "board19.png"
image night = "night.png"
image lines = "lines.png"
image phone:
    contains:
        "phone.png"
        yalign 0.5
        rotate 0
        linear 1.0 rotate -5 xalign 1.0
        linear 2.0 rotate 5 xalign 0.1
        linear 1.0 rotate 0 xalign 0.5
        repeat
image tarou normal = "tarou_normal.png"
image tarou happy = "tarou_happy.png"
image santa = "santa.png"
image santaattack:
    contains:
        "tarouyoung_happy.png"
        xalign 2.0
        yalign 0.5
        rotate 60
        linear 0.5 xalign 0.4
        linear 0.1 rotate 0 yalign 0.62
    contains:
        "santa.png"
        xalign 0.4
        yalign 0.5
        rotate 0
        0.5
        linear 1.0 xalign -2.0 yalign 0.4 rotate -45

image tarou flip normal:
    contains:
        "tarou_normal.png"
        xzoom-1
        xalign 0.5
        yalign 1.0
image tsun pj flip night embarrassed:
    contains:
        "tsun pj night embarrassed"
        xzoom-1
        xalign 0.1
        yalign 0.6
image tsun pj flip embarrassed:
    contains:
        "tsun pj embarrassed"
        xzoom-1
        xalign 0.1
        yalign 0.6
image tsun pj flip shock:
    contains:
        "tsun pj shock"
        xzoom-1
        xalign 0.1
        yalign 0.6      
image tsun pj flip hmph:
    contains:
        "tsun pj hmph"
        xzoom-1
        xalign 0.1
        yalign 0.6              
image tsun pj flip night hmph:
    contains:
        "tsun pj night hmph"
        xzoom-1
        xalign 0.1
        yalign 0.6        
        
image tsun normal = "tsun_normal.png"
image tsun shock = "tsun_shock.png"
image tsun shout = "tsun_shout.png"
image tsun night shock = im.MatrixColor("tsun_shock.png",
                                         im.matrix.brightness(-.2) * im.matrix.tint(0.6, 0.7, 0.9) * im.matrix.saturation(0.7) * im.matrix.contrast(0.8))
image tsun night normal = im.MatrixColor("tsun_normal.png",
                                         im.matrix.brightness(-.2) * im.matrix.tint(0.6, 0.7, 0.9) * im.matrix.saturation(0.7) * im.matrix.contrast(0.8))
image tsun pj tired = "tsun_pj_tired.png"
image tsun pj embarrassed = "tsun_pj_embarrassed.png"
image tsun pj shock = "tsun_pj_shock.png"
image tsun pj hmph = "tsun_pj_hmph.png"
image tsun pj shout = "tsun_pj_shout.png"
image tsun pj night tired = im.MatrixColor("tsun_pj_tired.png",
                                         im.matrix.brightness(-.2) * im.matrix.tint(0.6, 0.7, 0.9) * im.matrix.saturation(0.7) * im.matrix.contrast(0.8))
image tsun pj night shock = im.MatrixColor("tsun_pj_shock.png",
                                         im.matrix.brightness(-.2) * im.matrix.tint(0.6, 0.7, 0.9) * im.matrix.saturation(0.7) * im.matrix.contrast(0.8))
image tsun pj night embarrassed = im.MatrixColor("tsun_pj_embarrassed.png",
                                         im.matrix.brightness(-.2) * im.matrix.tint(0.6, 0.7, 0.9) * im.matrix.saturation(0.7) * im.matrix.contrast(0.8))
image tsun pj night shout = im.MatrixColor("tsun_pj_shout.png",
                                         im.matrix.brightness(-.2) * im.matrix.tint(0.6, 0.7, 0.9) * im.matrix.saturation(0.7) * im.matrix.contrast(0.8))
image tsun pj night hmph = im.MatrixColor("tsun_pj_hmph.png",
                                         im.matrix.brightness(-.2) * im.matrix.tint(0.6, 0.7, 0.9) * im.matrix.saturation(0.7) * im.matrix.contrast(0.8))
image tsunyoung shock = "tsun_young_shock.png"
image tsunyoung pout = "tsun_young_pout.png"
image tsun flip shout:
    contains:
        "tsun_shout.png"
        xzoom-1
        yalign 1.0
        xalign 0.5
        linear 1.5 xalign 2.0

# Declare characters used by this game.
define narrator = Character(" ", color="#000000", what_xalign=0.5, what_text_align=0.5)
define a = Character('Ami-chan', color="#FFE4FC", what_xalign=0.5, what_text_align=0.5, who_xalign=0.5, who_text_align=0.5, window_xalign=0.5)
define ay = Character('Young Ami-chan', color="#FFE4FC", what_xalign=0.5, what_text_align=0.5, who_xalign=0.5, who_text_align=0.5, window_xalign=0.5)
define ao = Character('Older Ami-chan', color="#FFE4FC", what_xalign=0.5, what_text_align=0.5, who_xalign=0.5, who_text_align=0.5, window_xalign=0.5)
define t = Character('Tarou-kun', color="#E4E8FF", what_xalign=0.5, what_text_align=0.5, who_xalign=0.5, who_text_align=0.5, window_xalign=0.5)
define ty = Character('Young Tarou-kun', color="#E4E8FF", what_xalign=0.5, what_text_align=0.5, who_xalign=0.5, who_text_align=0.5, window_xalign=0.5)
define ghost = Character('???', color="ffffff", what_xalign=0.5, what_text_align=0.5, who_xalign=0.5, who_text_align=0.5, window_xalign=0.5)
define k = Character('Kamina', color="#A52A2A", what_xalign=0.5, what_text_align=0.5, who_xalign=0.5, who_text_align=0.5, window_xalign=0.5)
define qb = Character('Kyubey', color="FFFFFF", what_xalign=0.5, what_text_align=0.5, who_xalign=0.5, who_text_align=0.5, window_xalign=0.5)
define k3 = Character('Kubo', color="FF0000", what_xalign=0.5, what_text_align=0.5, who_xalign=0.5, who_text_align=0.5, window_xalign=0.5)

define center = Position(xpos=0.5, ypos=0.71)
define right05 = Position(xpos=0.92)
define right1 = Position(xpos=0.9, ypos=0.75)
define right12 = Position(xpos=0.88)
define right15 = Position(xpos=0.85)
define right2 = Position(xpos=0.8)
define right25 = Position(xpos=0.75)
define right27 = Position(xpos=0.725)
define right3 = Position(xpos=0.7, ypos=0.71)
define right35 = Position(xpos=0.79, ypos=0.68)
define right36 = Position(xpos=0.79, ypos=0.75)
define right39 = Position(xpos=1.1, ypos=0.98)
define right4 = Position(xpos=0.6)
define right45 = Position(xpos=0.55, ypos=0.71)
define center1 = Position(xpos=0.5, ypos=0.75)
define center2 = Position(xpos=0.55, ypos=0.75)
define center5 = Position(xalign=0.4, yalign=0.5)
define pickup = Position(xpos=0.5, ypos=1.1)
define rightend = Position(xpos=0.99)
define lefttank = Position(xpos=0.1, ypos=1.1)
define left05 = Position(xpos=0.08)
define left1 = Position(xpos=0.1, ypos=0.75)
define left12 = Position(xpos=0.12)
define left15 = Position(xpos=0.15)
define left17 = Position(xpos=0.45, ypos=0.75)
define left2 = Position(xpos=0.2)
define left25 = Position(xpos=0.25)
define left3 = Position(xpos=0.3, ypos=0.71)
define left35 = Position(xpos=0.35)
define left37 = Position(xpos=0.37)
define left4 = Position(xpos=0.4, ypos=0.71)
define left45 = Position(xpos=0.45)  

define flash = Fade(.25, 0, .75, color="#fff")

init python:    
    renpy.music.register_channel("soundfx", "sfx", True)

# The game starts here.
label start:
    stop music fadeout 1.0
    scene bg white
    with dissolve
    
    "It was a gently snowing Christmas eve, and the faintest traces of snow began to fall on the city, each snowflake like a soft, floating, aimless kiss."
    
    play music "snow.mp3"
    play soundfx "walk.ogg"
    scene board1
    with dissolve
    show tsun normal at right3
    show tarou normal at left3
    show snow
    show lines
    
    "Two childhood friends of each sixteen years, barely adults and yet barely still children, were slowly walking home."
    "While they may have been childhood friends, it was merely the fact that they had known each other for a while."
    "Their families weren't especially close, and there was no sort of arrangement to celebrate together. They would soon part ways at the next crossing."
    
    show tarou normal at left4 with ease
    
    t "....."
    "Tarou-kun seemed like he had something to say. His feet were hesitant and his walk weighted down. Ami-chan wondered what was on his mind."
    
    stop soundfx
    show tarou normal at center with ease
    
    t "...Hey, Ami-chan."
    
    show tsun normal at right45 with ease
    show tsun shout
    play sound "collapse.ogg"
    show tsun shout at right3 with ease
    
    "Caught off-guard by his sudden stop, Ami-chan walked abruptly into Tarou-kun's back."
    a "W-What was that for-"
    
    show tsun normal
    show tarou flip normal
    
    "She began to rebuke him, but noticed that he seemed serious."
    "She decided to let him speak."
    t "What sort of things are you doing tomorrow?"
    a "Hmmm, for Christmas, you mean? Well, nothing really."
    t "Then..."
    
    show tsun shock
    
    t "Ami-chan. You know... I'd be really happy if you could spend Christmas eve with me."
    a "E-E-Ehhhhhhhh?!"
    "Ami-chan just felt like her mind had just been turned into a punching bag and used for speed training by Mike Tyson."
    "Did, did Tarou-kun just ask her to spend Christmas eve with him? Seriously?"
    "Obviously, the answer was yes."
    "If only her thoughts were that straightforward."
    "This was a Christmas... d-d-date, wasn't it?"
    "She didn't know what to feel."
    "She never expected Tarou-kun to ask so openly."
    "But more importantly, she needed to respond."
    "Was she happy about it? How was she supposed to know that?"
    "If she accepted, wouldn't that mean that she actually felt like that and then the two of them would be and tomorrow they would--"    
    a "J-J..."    
    "Her words were tripping over themselves."
    
    show tsun shout
    
    a "Just what do you think you're asking!!!"    
    "She finally stammered out."    
    a "D-Don't push your luck. There's absolutely no way I like you enough to do that sort of thing with you!! Tarou-kun, you dummy! Just die!"
    " {size=+45}           Baka! Humbug! {/size}"
    
    play sound "run.ogg"
    show tsun flip shout
    
    "Ami-chan ran furiously all the way home."    
    "Tarou-kun didn't chase her, not did he seem upset."
    
    stop music fadeout 3.0
    
    "He simply watched her run with the eyes of someone resigned to his fate."
    
    scene black
    with dissolve
    scene night
    show snowlight
    show board2
    with dissolve
    show tsun shock at center1
    
    "Later that night, as Ami-chan was about to go to bed, she was still thinking about what Tarou-kun had asked her."    
    a "Really, the nerve of him...!"    
    "She was pretty angry."
    
    show tsun normal with dissolve
    
    "But she was also a bit sad."
    "She felt she overreacted far too much to Tarou-kun's invitation."    
    "It wasn't as if she disliked him... he just surprised her with something that sudden."    
    "She decided to call him up and apologize a bit."
    "No, no, no, it was too embarassing after all, especially after all she said today."    
    "Tarou-kun was tough. He was usually a confident guy and he knew she was like this sometimes."
    
    show board4 behind tsun
    show tsun night normal
    hide board2
    
    "Quietly, she turned the light out."
    "He'd be fine when she next saw him. Thinking this, she prepared to go to sleep."
    
    show board3 behind tsun
    with dissolve
    show tsun night shock
    hide board4
    
    play soundfx "rumble.ogg"
    play sound "monster.ogg"
    play music "ghost.mp3"
    show phone
    with dissolve
    with hpunch
    with vpunch
    
    "Then a ghost appeared from the telephone, as the computer screen started flashing."
    ghost "I will warn you that this night of Christmas eve, you shall be visited by three spirits, who will show you visions of past, present and future."
    ghost "Heed their advice, contemplate on what you see, and ensure that you do not regret your actions on this day or from now on."
    
    hide phone
    with dissolve
    stop soundfx fadeout 1.0
    show board4 behind tsun
    with dissolve
    hide board3
    
    "And with that, the ghost vanished, leaving Ami-chan alone in the dead of night."    
    "What could the mysterious message have meant?"    
    "Actions this day? Did they mean with Tarou-kun? Was this all some trick he was playing on her?"    
    " {size=+45}           Baka! Humbug! {/size}"    
    "She would never in a million years do something as embarassing as go on a Christmas date with him. She was definitely, absolutely sure about that."    
    "Now, what had it said about three more ghosts?"    
    "Well, she supposed it couldn't be helped."    
    "Not knowing what to do, Ami-chan went to sleep."
    
    stop music fadeout 3.0
    scene bg black
    with fade

    "Later on that night . . ."
    
    scene night
    show snowlight
    show board5
    with dissolve
    show tsun pj night tired at right1
    
    "It was the middle of the night, and Ami-chan woke up to visit the bathroom."    
    "Tarou-kun's request was still the main thing on her mind, to such an extent that she wondered whether the telephone ghost was just a bad dream."
    
    play sound "flash.ogg"
    show board6 behind tsun with flash
    hide board5
    show tsun pj night shock
    play music "rowrow.wav"
    
    k "I AM THE GHOST OF CHRISTMAS PAST."    
    "With an impact like colliding meteorites, strong enough to make Ami-chan fall backwards, a giant figure burst out from behind her bathtub curtains."    
    k "ARE YOU READY FOR THIS, KID? WE'RE GONNA FLY BACK TO YOUR PAST AND KICK SOME SENSE INTO YOU."    
    "Glowing a fantastic pure white, like burning magnesium, the figure stepped out of the tub and stood in front of her, reaching for her hand."    
    a "No, wait, I'm not ready--!"    
    k "LET'S GO!"
    
    play sound "flash.ogg"
    scene bg white
    with dissolve
    
    "There was a flash of white and they both disappeared."
    
    scene board7
    with dissolve
    show tsun pj embarrassed at right35
    
    "This was a memory from when they first met, she realised."    
    "Come to think of it, it was a Christmas exactly eight years ago. Ami-chan had been taking a tour around a meat factory when she'd slipped on a stray sirloin and fallen off the walkway, right into the jaws of the industrial meat grinder."    
    "Without hesitating a moment, Tarou-kun, who was also on the tour, instantly leapt after her and grabbed her hand, saving her from being minced to pieces."    
    "It was the start of a friendship that would last eight years into the future."    
    k "You started becoming interested in him at that time, didn't you?"
    
    show tsun pj shock
    
    "His words made Ami-chan blush."    
    a "...Hmph! Well, it's obvious, isn't it? Anyone would become interested in someone who saved them from the jaws of an industrial meat grinder. It's not like he was special, or anything."    
    k "Hahah."     
    "The ghost patted her hard on the head."     
    k "Well, fair enough. A man's gotta do more than just that to show a girl he's special."
    
    play sound "flash.ogg"
    scene bg white
    with dissolve
    show night
    show board8
    show tsun pj embarrassed at right36
    show tsunyoung shock at center2
    
    "It was another memory, the Christmas from the year after that."    
    "Tarou-kun had bought her the present she'd really wanted for a long time - a giant stuffed rabbit with 250 carat diamond eyes."    
    ay "You're amazing, Tarou-kun"    
    "Her younger self had said. "    
    ay "I feel really bad that the present I got you isn't worth anywhere near as much..."    
    ty "Haha, don't worry about it."     
    "He was carefree as ever. "    
    ty "Ami-chan, your smiling face is a fine present for me."
    
    show tsunyoung pout at center2
    
    ay "...That still isn't worth how much you paid for this."     
    "Ami-chan pouted back."    
    ty "In that case, you should keep smiling for the rest of the year. That'll be more than worth it."    
    "It was a bit later that Ami-chan found out he'd had to work hard to earn all the money for her present."    
    "She remembered asking him about it, and the bemused look on his face, as if he was a mischievous kid who'd been found out."    
    "He never did tell her just how long he worked for it."    
    k "You've still got it, right?"     
    a "...Yeah, of course."    
    k "That's good."
    
    scene bg white
    with dissolve
    scene board9
    with dissolve
    show tsun pj embarrassed at right36
    show tsunyoung shock at center2
    show santa at center5
    
    "The next scene, from two years later."    
    "It was a group sleepover with everyone from class on Christmas, and they had been attacked by an assassin disguised as Santa Claus."
    
    hide santa
    show santaattack
    play sound "punch.ogg"
    
    "Quickly protecting Ami-chan from harm, Tarou-kun leapt forward and hit him with a surprise attack."    
    "After a long battle, Tarou-kun was victorious and the assassin subdued."
    
    show tsunyoung shock at left17 with ease
    show tsun pj flip hmph at right39
    
    a "...Geh!"
    "Ami-chan turned away as she saw her past self run up and give Tarou-kun a hug."    
    k "You used to be pretty sweet on him, didn't you?"    
    k "Not just here, but you always clung to him during school and on the way home, and he was all you used to talk about-"    
    a "No, no, no, no! I'm not listening! There's no way I did something like that!"     
    "She cut him off."    
    k "The proof's right in front of you, little miss."
    
    show tsun pj flip embarrassed at right39
    
    a "Okay, well maybe I did a bit, but that's just because he was cool and talented and did lots of interesting stuff! It wasn't as if he was special to me, or anything! It was just admiration as a friend, that's all!"    
    k "Heh, so you admired him? Well, that's fair enough, given all he'd done. It sure was cute, though, the way you doted on him."
    
    show tsun pj flip shock at right39
    
    a "Shut up shut up shut up!"         
    " She tried hitting him, but her hand simply passed through his body. It was kind of creepy"
    
    show tsun pj flip embarrassed at right39
    
    a "Besides, it's all in the past!"    
    k "Why'd it all stop, then?"     
    "A clear and simple question, yet it made Ami-chan look away once again."    
    a "That's... that's because..."    
    "To put it bluntly, she was embarassed. People teased her about their relationship. She was too self-conscious. She didn't want to be seen as that kind of lovestruck girl. After all, it was just... admiration. Of course, she can't have been in love with him."    
    "He was Tarou-kun, who she'd known since she was eight."    
    "There was no way it could happen, right?"    
    "So, to end the misconceptions, she seperated herself from him. They were just ordinary friends."
    
    show tsun pj flip hmph at right39
    
    a "...It's none of your business."    
    a "She finally told the ghost."
    
    scene bg white
    with dissolve
    
    scene night
    show snowlight
    show board6
    with dissolve
    show tsun pj night embarrassed at right1
    
    k "Well, that's it for me."     
    "The ghost of Christmas past stretched lazily."    
    k "How was your trip down memory lane, kid?"
    
    show tsun pj night hmph at right1
    
    a "...It wasn't anything special."     
    "She shrugged."    
    k "Hahah, by your definitions of 'nothing special', I'll take that as a fine compliment. He laughed."    
    k "Hey, Ami-chan. Want me to give you some advice?"    
    a "Not really."    
    k "I think the answer to what you should do will become clearer once you realize just how much that boy thinks of you."
    
    show tsun pj night embarrassed at right1
    
    a "...I used to think that I knew that."     
    "She mumbled"
    a "But... now I'm not sure if I'm ready for things like romance, or l-love..."    
    k "Heheh."
    "The ghost laughed again. He seemed like a pretty carefree person."    
    k "Girls like you have a real iron guard on their hearts. You never let out what you really feel. Maybe you don't even know yourself."    
    k "That boy, though... I'm sure he'll be able to break through."    
    k "He's already let you into his heart. If you stand back, you can watch as he drills into yours."    
    k "...Yeah, you need to let him drill into you."
    
    show tsun pj night shout at right1
    
    a "Don't phrase it in such a stupid way!!"    
    k "And once he's in your heart,"     
    "It seemed the ghost was ignoring her"    
    k "I hope you take good care of him."
    
    show tsun pj night hmph at right1
    
    a "...Don't... don't decide that on your own, stupid---"    
    k "Take care with the other two ghosts. They can both be quite a handful."    
    
    
    stop music fadeout 3.0
    play sound "flash.ogg"
    show bg white with dissolve
    hide board6
    
    "There was another flash, and he was gone."
    
    show board5 behind tsun with dissolve
    hide bg white
    show tsun pj night embarrassed at right1
    
    "Ami-chan found herself once again in the frame of her bathroom door, exactly where she fell."    
    "There was no way she could pass that experience just now off as a dream."    
    "Which meant, of course, that she was probably in store to meet two more ghosts after this."    
    "She frantically turned her head, searching for anything out of the ordinary--"    
    "And saw them."
   
    play music "ghost.mp3"
    show board10 behind tsun with dissolve
    hide board5
    show tsun pj night shock at right1
    
    "A pair of eyes above the sink, glowing with a fierce solemnity."    
    qb "Greetings. I am the ghost of Christmas present."
    qb "I am sure you are capable enough to have figured out the system, so we can proceed immediately to the task."    
    qb "I will show you a scene, a single scene, that is taking place at this very moment."    
    qb "Pay careful attention. It would be a bit unfortunate if you didn't understand at all."
    
    play sound "flash.ogg"
    scene bg white
    with dissolve
    
    a "What... what is this?"    
    "Once again, after a flash of white, Ami-chan found herself watching a new scene."
    
    scene night
    show snowlight
    show board11
    with dissolve
    show tsun pj flip night embarrassed
    
    "This time, an unfamiliar one."    
    qb "As you can see, we are currently witnessing the actions of Tarou-kun."    
    "The ghost explained."    
    a "N, No way this is Tarou-kun..."    
    "The room was almost impossibly dark, save for the rectangle of light, the computer monitor's silent scream, radiating out into the room"    
    "Tarou-kun sat at his desk, purposelessly typing away. Engaging in hollow conversations with an empty world, listening for an echo. Then there were his eyes"    
    "Eyes that had soaked up countless whispers of some alien, unforgiven coldness, that stared into mind-forged voids as he sat alone."    
    "This wasn't the energetic Tarou-kun that she knew."    
    "She couldn't comprehend what had caused such a drastic change in him."    
    "Sure, even if he really... l-liked Ami-chan... he wasn't the sort of person to get this depressed over a declined invitation."    
    "Even though it was practically a confession."    
    "Tarou-kun wouldn't stay down over that."    
    a "Why... even on Christmas eve... why is he all alone?"    
    qb "It seems you are unaware of that boy's circumstances."     
    "The ghost calmly spoke."
    qb "You are aware his parents passed away two years ago?"    
    a "Yeah... But he still has a little sister..."    
    qb "Yesterday, she collapsed and was sent to hospital for emergency surgery. Tarou-kun wasn't allowed to see her. She is currently in critical condition with an uncertain chance of survival."    
    a "What? He never said anything about that--"    
    qb "As strange as it was, he had a reason. He wanted to always seem infallible to you."    
    qb "He did not want you to worry about him. Looking at him now, though, it seems clear that someone worrying would be an appropriate response."
    
    show tsun pj flip night hmph
    
    a "T-That doesn't make sense"    
    "Ami-chan frantically tried to deny it. She had to deny something about this whole twisted situation."    
    a "If he really wanted me not to worry, why did he invite me over for Christmas?"    
    a "Was he planning to tell me then? Even if not, I would have noticed his sister wasn't there!"    
    qb "Well, it's true that was a slightly irrational decision of his. I suppose it is because in the end, Tarou-kun is only human."    
    qb "For an instant, this evening, he felt so isolated that he couldn't help but reach out. At that moment, and tonight, he is truly at his weakest"    
    qb "Fortunately, your denial caused him to realise his error. This is why he did not pursue you."
    
    show tsun pj flip night embarrassed
    
    a "But... still... Tarou-kun... I know him... he's braver than this..."    
    qb "The scenes shown to you by Christmas Past were, of course, in the past. In truth, Tarou-kun was never particularly brave."    
    qb "The primary motivator for his charisma was always the desire to stay strong for the target of his affections"    
    qb "If you are being slow, that person is you. This is not your fault, but in the time he does not spend with you, he is notably less confident."
    
    play sound "flash.ogg"
    scene bg white
    with dissolve
    scene night
    show snowlight
    show board10
    with dissolve
    show tsun pj night embarrassed at right1
    
    a "No way..."     
    "She whispered, back in her bathroom. "    
    a "...I need to call him."    
    qb "I will leave you to it."
    
    show board105 behind tsun
    with dissolve
    
    "The ghost's image flickered."     
    qb "But perhaps you would benefit from this bit of reflection:"    
    qb "Human emotions are volatile and difficult to interpret. With what feelings will you make your call?"    
    qb "An affection on equal level with his? Simple concern? Or, as he would most resent, mere pity?"
    
    show tsun pj night hmph at right1
    
    a "...I'm not pitying him."     
    a "I'll help him. ...Because I'm concerned, of course."    
    qb "If that is what you say, then so be it."
    
    show board5 behind tsun
    with dissolve
    hide board105
    hide board10
    show tsun pj night embarrassed at right1
    
    "The ghost finally faded into the darkness."
    
    stop music fadeout 3.0
    scene bg black
    with dissolve
    
    "Several minutes later . . ."
    
    scene night
    show snowlight
    show board4
    with dissolve
    show tsun pj night embarrassed at center1
    
    a "...He's not answering."    
    "Ami-chan was a bit wary about using the phone after the event earlier, but she eventually gathered the courage to dial Tarou-kun's number."    
    "However, it seemed that her efforts were in vain."    
    "She decided she would visit him on Christmas, after all."    
    "...But even then, what would she say to him? Wouldn't she make it worse? She still didn't know how to answer his feelings."
    
    play sound "monster.ogg"
    play music "final.mp3"
    show tsun pj night shout at center1
    
    "A strange feeling brushed down her back. She had already felt it three times that night."    
    a "...I know you're there, ghost. I, It's not like I'm scared or anything... but come out where I can see you."
    k3 "I'm already here."
    
    show board12 behind tsun
    with dissolve
    hide board4
    show tsun pj night shock at center1
    
    a "E-Ehhh?!"    
    "Impossible. The voice had appeared from right behind her."
    a "H, how?"     
    "Ami-chan cried as she spun around. "    
    a "I didn't sense your ghostly aura at all!"    
    k3 "Naive."
    "The ghost spoke plainly. "    
    k3 "Just because I'm the Ghost of Christmas Future, did you assume I was going to be a ghost?"    
    a "Of course I would, idiot!"    
    k3 "In this world, the only idiots are the unprepared."    
    a "Are you making this up as you go along?"    
    k3 "Silence. Now, observe. I will show you the future which you have carved for yourself."
    
    play sound "flash.ogg"
    scene bg white
    with dissolve
    scene night
    show snowlight
    show board13
    with dissolve
    
    a "This is... Tarou-kun's room?"
    
    show board14
    with fade
    hide board13
    
    a "Wait... what's that?"
    
    show board15
    with fade
    hide board14
    
    a "It can't be-"
    
    show board16
    with fade
    hide board15
    
    a "Stop"
    
    show board17
    with fade
    hide board16
    
    a "Stop."
    
    stop music fadeout 3.0
    scene bg black
    with dissolve
    
    a "STOP!!!"
    
    scene bg white
    with dissolve
    play soundfx "wind.ogg"
    
    "A new scene"    
    "Tarou-kun's life ended soon after he was informed of his little sister's death."    
    "Ami-chan was informed of this in turn."    
    "To be honest, Ami-chan didn't even need to be shown this scene of the future."    
    "That was because every tear, every cry, and every movement,"    
    "Ami-chan understood them."    
    "Even if it hadn't happened yet, it was going to be a reality. And she had seen it first-hand."    
    "The Ami-chan in the vision cried. Ami-chan knew the end of every sentence before they even began."    
    ao "Tarou-kun! Why did--"    
    a "--you think that you were alone?"    
    ao "Didn't you realise--"    
    a "--that I would have been there?"    
    ao "...No. Of course--"    
    a "--he didn't. Because I never told him."    
    ao "It's all--"    
    a "--my fault."    
    ao "If only I'd--"    
    a "--been more honest."    
    
    stop soundfx fadeout 3.0
    show expression Text(_("The Heart"), size=30, yalign=0.5, xalign=0.5, text_xalign=0.5, drop_shadow=(2, 2)) as text
    with dissolve
    pause 1.0
    
    k3 "Do you see now?"
    
    play music "ending.mp3"
    
    k3 "This is what's important. Listen to it."    
    k3 "Cut out all the background noise."    
    k3 "You care for this boy. That much is obvious."    
    k3 "But how deep does that affection run? Is it enough to save him?"    
    k3 "Be honest."
    
    hide expression Text(_("The Heart"), size=30, yalign=0.5, xalign=0.5, text_xalign=0.5, drop_shadow=(2, 2)) as text
    with dissolve
    pause 0.3
    
    show tsun pj embarrassed at center
    with dissolve
    
    a "...Fine. Let me think about it."
    a "Tarou-kun is my important friend. I can start from there."    
    a "Is that all there is to it?"    
    a "No. There's more."    
    a "Well, he's certainly in a pretty pitiful state right now, but I don't think that's it."    
    a "I don't want to help him just because of that."    
    a "It's something more positive."    
    a "It doesn't actually matter whether he's sad or cheerful. Either way, it would be nice if I was with him."    
    a "I guess I can say there's nothing about him I dislike."
    
    show tsun pj hmph
    with dissolve
    
    a "....."
    a "Really, in the end, I know exactly what answer these ghosts are trying to make me say."    
    a "And I know it's probably true."    
    a "I want to deny it."    
    a "But there's no point. Especially in front of an omniscient ghost. I said I'd be honest. Just this once."    
    a "...I... I'm in love with T, T, Tarou-kun."
    
    show tsun pj shout
    with hpunch
    with vpunch
    
    a "AAAAAAAAHHH! IT'S EMBARASSING EMBARASSING EMBARASSING EMBARASSING EMBARASSING!"    
    a "AFTER ALL THAT SELF-DOUBT AND POINTLESS ANGST I JUST REALISED SOMETHING EVERYONE ELSE PROBABLY FIGURED OUT RIGHT AT THE START! "    
    a "AFTER ALL THAT FIGHTING AND THOSE INSULTS, IT TURNS OUT I'M ACTUALLY IN LOVE WITH HIM!"    
    a "I'M LIKE THE STUPID LOVE INTEREST IN SOME BAD ROMANCE COMEDY!"    
    a "WHY AM I SUCH AN IDIOT?! DID I THINK THAT TINGLY FEELING IN MY CHEST WAS HEARTBURN OR SOMETHING?"    
    a "I CAN FEEL EVERY SHALLOW PRETENSE AND ACT I'VE PUT UP CRUMBLING AND COMING BACK TO SMACK ME IN THE FACE!"    
    a "'IT'S NOT AS IF I DID IT FOR YOU, OR ANYTHING'?! WHAT KIND OF LINE IS THAT? WHAT THE HELL, ME?"    
    a "I FEEL LIKE I'M GOING TO SET ON FIRE SOMEONE JUST BURY ME IN THE MARIANAS TRENCH RIGHT NOW"    
    a "IT'S EMBARASSING EMBARASSING EMBARASSING EMBARASSING EMBARASSING EMBARASSING EMBARASSING EMBARASSING!"
    
    show tsun pj embarrassed
    with dissolve
    
    "But she soon got over it."
    
    scene night
    show snowlight
    show board12
    with dissolve
    show tsun pj night embarrassed at center1
    
    k3 "I see you've reached your decision."    
    a "I have. Thank you, ghosts."
    k3 "You are very welcome."
    a "I just have one question, though..."
    k3 "Yes?"    
    a "That future you showed me... I'm pretty sure Tarou-kun was wearing the exact same clothes as he did today."    
    k3 "That's because the character designer was lazy and only gave you two outfits each."
    
    show tsun pj night shout
    
    a "Stop joking around!"
    k3 "You are naive. Just because I showed you the future, did you just assume it was the distant-"    
    a "Just tell me!"
    
    show tsun pj night shock
    
    k3 "His sister is already dead. The scene you saw will happen in roughly ten minutes."    
    a "...Wait, what?"
    
    scene bg black
    with dissolve
    scene night
    show snowlight
    show board14
    with dissolve
    
    "Tarou-kun was sad."    
    "He was alone on Christmas."    
    "His sister was dead."    
    "It felt like the world had expanded out around him and an empty darkness had filled the gaps."    
    "Any way he walked, he would only be met with nothing."    
    "In the end, there was only one way out."    
    "Of course, he was wrong, but here, right now, in his cold bedroom on Christmas eve, with all his family dead, this was the only way he could see."    
    "Push it away. Push it all away."
    
    play sound "break.ogg"
    
    "Something shattered downstairs. A window. A burglar?"    
    "Well, it didn't matter."    
    "Soon, nothing would matter. And all would be good. Once nothing mattered, there would be nothing that could make things worse if it went wrong."    
    "Push it away. Push it all away."
    
    scene bg white
    with dissolve
    
    "Suddenly, the room filled with light."
    
    scene night
    show snowlight
    show board18
    show tsun pj flip embarrassed
    with dissolve
    
    a "Tarou-kun! Listen up, because I'm only telling you this once!"
    
    show tsun pj flip hmph
    
    a "Actually, I like you! Like, the super-like type!"    
    t "Love?"    
    a "Y, Yeah! That! Don't forget it!"    
    a "Even when I act angry or annoyed with you, that's just another way of me saying I like you!"    
    a "Because I like you so much that when you treat me nicely, I get so happy that I have to distract myself or else I'd get totally lost!"
    
    show tsun pj flip embarrassed
    
    a "When I get angry and blush, it means you're doing a good job!"
    
    show tsun pj flip hmph
    
    a "Ah, but there will be times when I'm actually angry, so be careful!"
    a "But most of the time it should be okay, because I like you!"    
    a "D, Do you understand?"    
    "Tarou-kun blinked once."    
    t "I understand."
    
    show board19 behind tsun
    with dissolve
    
    "And smiled."    
    t "I like you too, Ami-chan."
    
    show tsun pj flip embarrassed
    
    a "W, W, Well, I knew that, of course!"     
    "Ami-chan's blush had swept completely over her face."    
    t "Did you really?"    
    a "Y, Yeah, some ghosts told me!"    
    t "I see"
    
    show tsun pj flip shock
    
    a "So, because you're my b, b, boyfriend now, you can't kill yourself!"    
    t "Okay."
    
    show tsun pj flip embarrassed
    
    a "And I'm really sorry to hear about your sister!"    
    t "Thank you."
    a "I'll help you through all your trauma and stuff, so don't kill yourself!"    
    t "I already said I won't."
    
    show tsun pj flip hmph
    
    a "I need to double check!"
    t "That's very like you, Ami-chan."
    a "I, It's not like I doubted you or anything, but--!"
    "It seemed somehow, they would be able to sort things out."    
    "Their real journey begins here, but really, once you've saved each other from suicide and meat grinders, it's probably going to be smooth sailing from them on."
    
    scene bg white
    with dissolve
    
    t "Hey, Ami-chan."    
    a "Yeah?"    
    t "Thanks for finally being honest with yourself."    
    a "...S, Stop it Tarou-kun..."
    
    stop music fadeout 3.0
    show expression Text(_("Merry Christmas Anons"), size=30, yalign=0.5, xalign=0.5, text_xalign=0.5, drop_shadow=(2, 2)) as text
    with dissolve
    pause 3.0
    
    scene bg black
    with dissolve

    return
