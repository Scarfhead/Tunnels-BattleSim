import random
from random import randint
import tkinter as tk
from tkinter import *
from tkinter import ttk
damage = 0
health = 0
experience = 0
leftTally = 0
straightTally = 0
rightTally = 0
ghoul_health = 20
goblin_health = 10
ghost_health = 1
evilking_health = 30
firstwon = False

### Player Classes
class Knight:
    health = 40
    primaryAttack = "Slash"
    primaryDamage = 5
    secondaryAttack = "Block"
    secondaryRecieved = damage/2
class Cowboy:
    health = 25
    primaryAttack = "Buckshot"
    primaryDamage = 3
    secondaryAttack = "Roll Dodge"
    secondaryRecieved = 0
class Wizard:
    health = 10
    primaryAttack = "Fireball"
    primaryDamage = 7
    secondaryAttack = "Heal"
    secondaryRecieved = health + 5
### Enemy Classes
class Goblin:
    health = 10
    primaryAttack = "Claw"
    primaryDamage = 2
class Ghoul:
    health = 20
    primaryAttack = "Bludgeon"
    primaryDamage = 4
class Ghost:
    health = 1
    primaryAttack = "Haunt"
    primaryDamage = 1
class EvilKing:
    health = 25
    primaryAttack = "Royal Pierce"
    primaryDamage = 6
    secondaryAttack = "Block"
    secondaryRecieved = 0

###Room Environments
def first_room(style,health,experience):  
    direction = int(input("""

                                .--,                                               
                               :   /\                                .--,-``-.     
    ,----,                    /   ,  \        ,----,                /   /     '.   
  ,`--.' |    ,--.           /   /    \     .'   .' \         .--, / ../        ;  
 /    /  :   /  /|          ;   /  ,   \  ,----,'    |        |\  \\ ``\  .`-    ' 
:    |.' '  '  / '         /   /  / \   \ |    :  .  ;        ` \  `\___\/   \   : 
`----':  | /  / /         /   ;  /\  \   \;    |.'  /          \ \  \    \   :   | 
   '   ' ;/  / ,          \"""\ /  \  \ ; `----'/  ;            , \  \   /  /   /  
   |   | |\ '\ \           `---`    `--`    /  ;  /             / /` /   \  \   \  
   '   : ; \  \ '                          ;  /  /-,          ,` /  /___ /   :   | 
   |   | '  \  . |                        /  /  /.`|          | .  //   /\   /   : 
   '   : |   \__\.                      ./__;      :          ./__// ,,/  ',-    . 
   ;   |.'                              |   :    .'                \ ''\        ;  
   '---'                                ;   | .'                    \   \     .'   
                                        `---'                        `--`-,,-'   
                           
Current Health = """ + str(health) + """
Current Experience = """ + str(experience) + """     
                  
                          Choose your direction!
                            1: Left
                            2: Straight
                            3: Right    
                            4: Quit
    """))
    if direction < 4:
        encounterChance = random.randint(0,3)
        while health < 10:
            encounterChance = random.randint(2,3)
            continue
        else:
            enemies = ["goblin", "ghoul", "ghost", "health"]
            enemy = enemies[encounterChance]
            if enemy == "ghoul":
                if experience >= 20:
                    evilking_battle(style,health,experience)
                else:
                    ghoul_battle(style,health,experience)
            elif enemy == "goblin":
                if experience >= 20:
                    evilking_battle(style,health,experience)
                else:
                    goblin_battle(style,health,experience)
            elif enemy == "ghost":
                if experience >= 20:
                    evilking_battle(style,health,experience)
                else:
                    ghost_battle(style,health,experience)
            else:
                print("You found a health pack! +10 HEALTH!!!!")
                health = health + 5
                first_room(style,health,experience)
    elif direction == 4:
        print("Buhbye!")
        exit()
def first_to_second(style,health,experience,firstwon,steps):
    steps = 0
    direction = int(input("""
                                         ,---,  
                                  ,--.,`--.' |  
,-.----.                        ,--.'||   :  :  
\    /  \           ,--,    ,--,:  : |'   '  ;  
;   :    \        ,'_ /| ,`--.'`|  ' :|   |  |  
|   | .\ :   .--. |  | : |   :  :  | |'   :  ;  
.   : |: | ,'_ /| :  . | :   |   \ | :|   |  '  
|   |  \ : |  ' | |  . . |   : '  '; |'   :  |  
|   : .  / |  | ' |  | | '   ' ;.    ;;   |  ;  
;   | |  \ :  | | :  ' ; |   | | \   |`---'. |  
|   | ;\  \|  ; ' |  | ' '   : |  ; .' `--..`;  
:   ' | \.':  | : ;  ; | |   | '`--'  .--,_     
:   : :-'  '  :  `--'   \'   : |      |    |`.  
|   |.'    :  ,      .-./;   |.'      `-- -`, ; 
`---'       `--`----'    '---'          '---`"     
                           
Current Health = """ + str(health) + """
Current Experience = """ + str(experience) + """     
The Remaining Enemies are enraged their leader has been defeated, and attempt to rush you!                
The Previous Room is behind you, the next is only a few metres away, but there's enemies on all sides! Run for your life!
Press Enter to Run!"""))
    if direction == "":
        encounterChance = random.randint(0,2)
        enemies = ["goblin", "ghoul"]
        enemy = enemies[encounterChance]
        if enemy == "ghoul":
            enraged_ghoul_battle(style,health,experience,firstwon)
        elif enemy == "goblin":
            enraged_goblin_battle(style,health,experience,firstwon)
def second_room(style,health,experience):
    direction = direction

### First Room Enemies
def evilking_battle(style,health,experience):
    enemy = EvilKing
    evilking_health = 25
    print("""
                                                                                            ,---,  
                                                     ,--.                                ,`--.' |  
    ,---,.                     ,--,              ,--/  /|                                |   :  :  
  ,'  .' |            ,--,   ,--.'|           ,---,': / '  ,--,                          '   '  ;  
,---.'   |          ,--.'|   |  | :           :   : '/ / ,--.'|         ,---,            |   |  |  
|   |   .'     .---.|  |,    :  : '           |   '   ,  |  |,      ,-+-. /  |  ,----._,.'   :  ;  
:   :  |-,   /.  ./|`--'_    |  ' |           '   |  /   `--'_     ,--.'|'   | /   /  ' /|   |  '  
:   |  ;/| .-' . ' |,' ,'|   '  | |           |   ;  ;   ,' ,'|   |   |  ,"' ||   :     |'   :  |  
|   :   .'/___/ \: |'  | |   |  | :           :   '   \  '  | |   |   | /  | ||   | .\  .;   |  ;  
|   |  |-,.   \  ' .|  | :   '  : |__         |   |    ' |  | :   |   | |  | |.   ; ';  |`---'. |  
'   :  ;/| \   \   ''  : |__ |  | '.'|        '   : |.  \'  : |__ |   | |  |/ '   .   . | `--..`;  
|   |    \  \   \   |  | '.'|;  :    ;        |   | '_\.'|  | '.'||   | |--'   `---`-'| |.--,_     
|   :   .'   \   \ |;  :    ;|  ,   /         '   : |    ;  :    ;|   |/       .'__/\_: ||    |`.  
|   | ,'      '---" |  ,   /  ---`-'          ;   |,'    |  ,   / '---'        |   :    :`-- -`, ; 
`----'               ---`-'                   '---'       ---`-'                \   \  /   '---`"  
                                                                                 `--`-'            """)
    while evilking_health > 0:
        battleAction = int(input("                      Evil King Health = " + str(evilking_health) + " points" +
                                "\n \n                      What will you do? \n \n                      1: " + style.primaryAttack + "\n                      2: " + style.secondaryAttack + "\n                      3: RUN! \n \n                      YOUR HEALTH: " + str(health) + "\n\n "))
        if battleAction == 1:
            evilking_health = evilking_health - style.primaryDamage
            if evilking_health < 1:
                break
            else:
                evilking_attackChance = random.randint(0,3)
                if evilking_attackChance < 2:
                    print("The Evil King used " + enemy.primaryAttack + " and it landed!")
                    health = health - enemy.primaryDamage
                    if health <= 0:
                        death(style,health,experience)
                        break
                    else:
                        continue
                elif evilking_attackChance == 2:
                    print("The Evil King used " + enemy.primaryAttack + " and missed!")
                else:
                    print("The Evil King used " + enemy.secondaryAttack + " and negated your attack!")
                    evilking_health = evilking_health + style.primaryDamage
        if battleAction == 2:
            evilking_attackChance_attackChance = random.randint(0,3)
            if evilking_attackChance < 2:
                print("The Evil King used " + enemy.primaryAttack)
                if style == Knight:
                    print("\nYou managed to block it, but still took- \n" + str(enemy.primaryDamage/2) + " HEALTH")
                    health = health - (enemy.primaryDamage/2)
                    if health <= 0:
                        death(style,health,experience)
                        exit()
                    else:
                        continue
                elif style == Cowboy:
                    print("\nYou evaded! (and took no damage!)")
                elif style == Wizard:
                    print("The hit landed, but then you healed yourself! \n+3 HEALTH")
                    health = health + (Wizard.secondaryRecieved - 2)
            elif evilking_attackChance == 2:
                print("The Evil King used " + enemy.primaryAttack + " and missed!")
                if style == Knight:
                    print("\nWhat a pointless block, you should've attacked....")
                    health = health - 1
                elif style == Cowboy:
                    print("\nWhat a pointless evade, you should've attacked")
                elif style == Wizard:
                    print("Nice timing, you healed yourself! \n+5 HEALTH")
                    health = health + Wizard.secondaryRecieved
            else:
                print("The Evil King used " + enemy.secondaryAttack + "!!")
                if style == Knight or  style == Cowboy:
                    print("What are you both scared of?")
                elif style == Wizard:
                    print("Nice timing, you healed yourself! \n+5 HEALTH")
                    health = health + Wizard.secondaryRecieved
        if battleAction == 3:
            escape(style,health,experience)
    firstwon = True
    firstbossvictory(style,health,experience,firstwon)
def goblin_battle(style,health,experience):
    enemy = Goblin
    goblin_health = 10
    print("""
                                                                 ,---,  
                                                              ,`--.' |  
  ,----..                         ,--,                        |   :  :  
 /   /   \              ,---,   ,--.'|     ,--,               '   '  ;  
|   :     :    ,---.  ,---.'|   |  | :   ,--.'|         ,---, |   |  |  
.   |  ;. /   '   ,'\ |   | :   :  : '   |  |,      ,-+-. /  |'   :  ;  
.   ; /--`   /   /   |:   : :   |  ' |   `--'_     ,--.'|'   ||   |  '  
;   | ;  __ .   ; ,. ::     |,-.'  | |   ,' ,'|   |   |  ,"' |'   :  |  
|   : |.' .''   | |: :|   : '  ||  | :   '  | |   |   | /  | |;   |  ;  
.   | '_.' :'   | .; :|   |  / :'  : |__ |  | :   |   | |  | |`---'. |  
'   ; : \  ||   :    |'   : |: ||  | '.'|'  : |__ |   | |  |/  `--..`;  
'   | '/  .' \   \  / |   | '/ :;  :    ;|  | '.'||   | |--'  .--,_     
|   :    /    `----'  |   :    ||  ,   / ;  :    ;|   |/      |    |`.  
 \   \ .'             /    \  /  ---`-'  |  ,   / '---'       `-- -`, ; 
  `---`               `-'----'            ---`-'                '---`" """)
    while goblin_health > 0:
        battleAction = int(input("                      Goblin Health = " + str(goblin_health) + " points" +
                                "\n \n                      What will you do? \n \n                      1: " + style.primaryAttack + "\n                      2: " + style.secondaryAttack + "\n                      3: RUN! \n \n                      YOUR HEALTH: " + str(health) + "\n\n "))
        if battleAction == 1:
            goblin_health = goblin_health - style.primaryDamage
            if goblin_health < 1:
                break
            else:
                goblin_attackChance = random.randint(0,3)
                if goblin_attackChance < 2:
                    print("The Goblin used " + enemy.primaryAttack + " and it landed!")
                    health = health - enemy.primaryDamage
                    if health <= 0:
                        death(style,health,experience)
                        exit()
                    else:
                        continue
                else:
                    print("The Goblin used " + enemy.primaryAttack + " and missed!")
        if battleAction == 2:
            goblin_attackChance = random.randint(0,3)
            if goblin_attackChance < 2:
                print("The Goblin used " + enemy.primaryAttack)
                if style == Knight:
                    print("\nYou managed to block it, but still took- \n" + str(enemy.primaryDamage/2) + " HEALTH")
                    health = health - (enemy.primaryDamage/2)
                    if health <= 0:
                        death(style,health,experience)
                        exit()
                    else:
                        continue
                elif style == Cowboy:
                    print("\nYou evaded! (and took no damage!)")
                elif style == Wizard:
                    print("The hit landed, but then you healed yourself! \n+3 HEALTH")
                    health = health + (Wizard.secondaryRecieved - 2)
            else:
                print("The Goblin used " + enemy.primaryAttack + " and missed!")
                if style == Knight:
                    print("\nWhat a pointless block, you should've attacked....")
                elif style == Cowboy:
                    print("\nWhat a pointless evade, you should've attacked")
                elif style == Wizard:
                    print("Nice timing, you healed yourself! \n+5 HEALTH")
                    health = health + Wizard.secondaryRecieved
        if battleAction == 3:
            escape(style,health,experience)
    firstwon = False
    steps = 0
    victory(style,health,experience,firstwon,steps)
    first_room(style,health,experience)
def ghoul_battle(style,health,experience):
    enemy = Ghoul
    ghoul_health = 20
    print("""
                                                           ,---,  
                                                        ,`--.' |  
  ,----..     ,---,                              ,--,   |   :  :  
 /   /   \  ,--.' |                            ,--.'|   '   '  ;  
|   :     : |  |  :       ,---.           ,--, |  | :   |   |  |  
.   |  ;. / :  :  :      '   ,'\        ,'_ /| :  : '   '   :  ;  
.   ; /--`  :  |  |,--. /   /   |  .--. |  | : |  ' |   |   |  '  
;   | ;  __ |  :  '   |.   ; ,. :,'_ /| :  . | '  | |   '   :  |  
|   : |.' .'|  |   /' :'   | |: :|  ' | |  . . |  | :   ;   |  ;  
.   | '_.' :'  :  | | |'   | .; :|  | ' |  | | '  : |__ `---'. |  
'   ; : \  ||  |  ' | :|   :    |:  | : ;  ; | |  | '.'| `--..`;  
'   | '/  .'|  :  :_:,' \   \  / '  :  `--'   \;  :    ;.--,_     
|   :    /  |  | ,'      `----'  :  ,      .-./|  ,   / |    |`.  
 \   \ .'   `--''                 `--`----'     ---`-'  `-- -`, ; 
  `---`                                                   '---`"   """)
    while ghoul_health > 0:
        battleAction = int(input("                      Ghoul Health = " + str(ghoul_health) + " points" +
                                "\n \n                      What will you do? \n \n                      1: " + style.primaryAttack + "\n                      2: " + style.secondaryAttack + "\n                      3: RUN! \n \n                      YOUR HEALTH: " + str(health) + "\n\n "))
        if battleAction == 1:
            ghoul_health = ghoul_health - style.primaryDamage
            if ghoul_health < 1:
                break
            else:
                ghoul_attackChance = random.randint(0,3)
                if ghoul_attackChance < 2:
                    print("The Ghoul used " + enemy.primaryAttack + " and it landed! \n-2 HEALTH")
                    health = health - enemy.primaryDamage
                    if health <= 0:
                        death(style,health,experience)
                        exit()
                    else:
                        continue
                else:
                    print("The Ghoul used " + enemy.primaryAttack + " and missed!")
        if battleAction == 2:
            ghoul_attackChance = random.randint(0,3)
            if ghoul_attackChance < 2:
                print("The Ghoul used " + enemy.primaryAttack)
                if style == Knight:
                    print("\nYou managed to block it, but still took- \n" + str(enemy.primaryDamage/2) + " HEALTH")
                    health = health - (enemy.primaryDamage/2)
                    if health <= 0:
                        death(style,health,experience)
                        exit()
                    else:
                        continue
                elif style == Cowboy:
                    print("\nYou evaded! (and took no damage!)")
                elif style == Wizard:
                    print("The hit landed, but then you healed yourself! \n+3 HEALTH")
                    health = health + (style.secondaryRecieved - 2)
            else:
                print("The Ghoul used " + enemy.primaryAttack + " and missed!")
                if style == Knight:
                    print("\nWhat a pointless block, you should've attacked....")
                    health = health - enemy.primaryDamage
                elif style == Cowboy:
                    print("\nWhat a pointless evade, you should've attacked....")
                elif style == Wizard:
                    print("Nice timing, you healed yourself! \n+5 HEALTH!")
                    health = health + style.secondaryRecieved
            
        if battleAction == 3:
            escape(style,health,experience)
    firstwon = False
    steps = 0
    victory(style,health,experience,firstwon,steps)
    first_room(style,health,experience)
def ghost_battle(style,health,experience):
    enemy = Ghost
    ghost_health = 1
    print("""
                                                         ,---,  
                                                      ,`--.' |  
  ,----..     ,---,                            ___    |   :  :  
 /   /   \  ,--.' |                          ,--.'|_  '   '  ;  
|   :     : |  |  :       ,---.              |  | :,' |   |  |  
.   |  ;. / :  :  :      '   ,'\   .--.--.   :  : ' : '   :  ;  
.   ; /--`  :  |  |,--. /   /   | /  /    '.;__,'  /  |   |  '  
;   | ;  __ |  :  '   |.   ; ,. :|  :  /`./|  |   |   '   :  |  
|   : |.' .'|  |   /' :'   | |: :|  :  ;_  :__,'| :   ;   |  ;  
.   | '_.' :'  :  | | |'   | .; : \  \    `. '  : |__ `---'. |  
'   ; : \  ||  |  ' | :|   :    |  `----.   \|  | '.'| `--..`;  
'   | '/  .'|  :  :_:,' \   \  /  /  /`--'  /;  :    ;.--,_     
|   :    /  |  | ,'      `----'  '--'.     / |  ,   / |    |`.  
 \   \ .'   `--''                  `--'---'   ---`-'  `-- -`, ; 
  `---`                                                 '---`"  
                                                                """)
    while ghoul_health > 0:
        battleAction = int(input("                      Ghost Health = " + str(ghost_health) + " points" +
                                "\n \n                      What will you do? \n \n                      1: " + style.primaryAttack + "\n                      2: " + style.secondaryAttack + "\n                      3: RUN! \n \n                      YOUR HEALTH: " + str(health) + "\n\n "))
        if battleAction == 1:
            ghost_health = ghost_health
            print("You can't damage a Ghost!")
            if ghoul_health < 1:
                break
            else:
                ghoul_attackChance = random.randint(0,3)
                if ghoul_attackChance < 2:
                    print("The Ghost used " + enemy.primaryAttack + " and it landed! -" + str(enemy.primaryDamage) + " HEALTH")
                    health = health - enemy.primaryDamage
                    if health <= 0:
                        death(style,health,experience)
                        exit()
                    else:
                        continue
                else:
                    print("The Ghost used " + enemy.primaryAttack + " and missed!")
        if battleAction == 2:
            ghoul_attackChance = random.randint(0,3)
            if ghoul_attackChance < 2:
                print("The Ghost used " + enemy.primaryAttack)
                if style == Knight:
                    print("\nYou managed to block it, but still took- \n" + str(enemy.primaryDamage/2) + " HEALTH")
                    health = health - (enemy.primaryDamage/2)
                    if health <= 0:
                        death(style,health,experience)
                        exit()
                    else:
                        continue
                elif style == Cowboy:
                    print("\nYou evaded! (and took no damage!)")
                elif style == Wizard:
                    print("The hit landed, but then you healed yourself! \n+3 HEALTH")
                    health = health + (style.secondaryRecieved - 2)
            else:
                print("The Ghoul used " + enemy.primaryAttack + " and missed!")
                if style == Knight:
                    print("\nWhat a pointless block, you should've ran....")
                    health = health - enemy.primaryDamage
                elif style == Cowboy:
                    print("\nWhat a pointless evade, you should've ran....")
                elif style == Wizard:
                    print("Nice timing, you healed yourself! \n+5 HEALTH!")
                    health = health + style.secondaryRecieved
            
        if battleAction == 3:
            escape(style,health,experience)
    firstwon = False
    steps = 0
    victory(style,health,experience,firstwon)
    first_room(style,health,experience)

### Battle End Screens
def escape(style,health,experience):
    print("""
                                                                                     ,---,  
                                                ,-.----.                          ,`--.' |  
    ,---,.  .--.--.     ,----..     ,---,       \    /  \      ,---,.    ,---,    |   :  :  
  ,'  .' | /  /    '.  /   /   \   '  .' \      |   :    \   ,'  .' |  .'  .' `\  '   '  ;  
,---.'   ||  :  /`. / |   :     : /  ;    '.    |   |  .\ :,---.'   |,---.'     \ |   |  |  
|   |   .';  |  |--`  .   |  ;. /:  :       \   .   :  |: ||   |   .'|   |  .`\  |'   :  ;  
:   :  |-,|  :  ;_    .   ; /--` :  |   /\   \  |   |   \ ::   :  |-,:   : |  '  ||   |  '  
:   |  ;/| \  \    `. ;   | ;    |  :  ' ;.   : |   : .   /:   |  ;/||   ' '  ;  :'   :  |  
|   :   .'  `----.   \|   : |    |  |  ;/  \   \;   | |`-' |   :   .''   | ;  .  |;   |  ;  
|   |  |-,  __ \  \  |.   | '___ '  :  | \  \ ,'|   | ;    |   |  |-,|   | :  |  '`---'. |  
'   :  ;/| /  /`--'  /'   ; : .'||  |  '  '--'  :   ' |    '   :  ;/|'   : | /  ;  `--..`;  
|   |    \'--'.     / '   | '/  :|  :  :        :   : :    |   |    \|   | '` ,/  .--,_     
|   :   .'  `--'---'  |   :    / |  | ,'        |   | :    |   :   .';   :  .'    |    |`.  
|   | ,'               \   \ .'  `--''          `---'.|    |   | ,'  |   ,.'      `-- -`, ; 
`----'                  `---`                     `---`    `----'    '---'          '---`"  
                                -2 EXPERIENCE                                                                            
          """)
    experience = experience - 2
    first_room(style,health,experience)
def death(style,health,experience):
    print(""""
                                                                                                                              ,---,  
                 ,----..                                                                     ,`--.' |  
                /   /   \                            ,---,       ,---,    ,---,.    ,---,    |   :  :  
        ,---,  /   .     :          ,--,           .'  .' `\  ,`--.' |  ,'  .' |  .'  .' `\  '   '  ;  
       /_ ./| .   /   ;.  \       ,'_ /|         ,---.'     \ |   :  :,---.'   |,---.'     \ |   |  |  
 ,---, |  ' :.   ;   /  ` ;  .--. |  | :         |   |  .`\  |:   |  '|   |   .'|   |  .`\  |'   :  ;  
/___/ \.  : |;   |  ; \ ; |,'_ /| :  . |         :   : |  '  ||   :  |:   :  |-,:   : |  '  ||   |  '  
 .  \  \ ,' '|   :  | ; | '|  ' | |  . .         |   ' '  ;  :'   '  ;:   |  ;/||   ' '  ;  :'   :  |  
  \  ;  `  ,'.   |  ' ' ' :|  | ' |  | |         '   | ;  .  ||   |  ||   :   .''   | ;  .  |;   |  ;  
   \  \    ' '   ;  \; /  |:  | | :  ' ;         |   | :  |  ''   :  ;|   |  |-,|   | :  |  '`---'. |  
    '  \   |  \   \  ',  / |  ; ' |  | '         '   : | /  ; |   |  ''   :  ;/|'   : | /  ;  `--..`;  
     \  ;  ;   ;   :    /  :  | : ;  ; |         |   | '` ,/  '   :  ||   |    \|   | '` ,/  .--,_     
      :  \  \   \   \ .'   '  :  `--'   \        ;   :  .'    ;   |.' |   :   .';   :  .'    |    |`.  
       \  ' ;    `---`     :  ,      .-./        |   ,.'      '---'   |   | ,'  |   ,.'      `-- -`, ; 
        `--`                `--`----'            '---'                `----'    '---'          '---`"  
            As a """ + str(style) + " you died with " + str(experience) + """ experience...
                            Take a breather and try again another time!""")


def victory(style,health,experience,firstwon,steps):
    print("""
                                       ,----,                                     ,---,  
                                     ,/   .`|  ,----..                         ,`--.' |  
               ,---,  ,----..      ,`   .'  : /   /   \  ,-.----.              |   :  :  
       ,---.,`--.' | /   /   \   ;    ;     //   .     : \    /  \        ,---,'   '  ;  
      /__./||   :  :|   :     :.'___,/    ,'.   /   ;.  \;   :    \      /_ ./||   |  |  
 ,---.;  ; |:   |  '.   |  ;. /|    :     |.   ;   /  ` ;|   | .\ :,---, |  ' :'   :  ;  
/___/ \  | ||   :  |.   ; /--` ;    |.';  ;;   |  ; \ ; |.   : |: /___/ \.  : ||   |  '  
\   ;  \ ' |'   '  ;;   | ;    `----'  |  ||   :  | ; | '|   |  \ :.  \  \ ,' ''   :  |  
 \   \  \: ||   |  ||   : |        '   :  ;.   |  ' ' ' :|   : .  / \  ;  `  ,';   |  ;  
  ;   \  ' .'   :  ;.   | '___     |   |  ''   ;  \; /  |;   | |  \  \  \    ' `---'. |  
   \   \   '|   |  ''   ; : .'|    '   :  | \   \  ',  / |   | ;\  \  '  \   |  `--..`;  
    \   `  ;'   :  |'   | '/  :    ;   |.'   ;   :    /  :   ' | \.'   \  ;  ; .--,_     
     :   \ |;   |.' |   :    /     '---'      \   \ .'   :   : :-'      :  \  \|    |`.  
      '---" '---'    \   \ .'                  `---`     |   |.'         \  ' ;`-- -`, ; 
                      `---`                              `---'            `--`   '---`"  
                                +5 EXPERIENCE!                                                        
        """)
    experience = experience + 5
    if firstwon == False:
        first_room(style,health,experience)
    elif firstwon == True:
        steps += 1
        if steps == 4:
            second_room(style,health,experience)
        else:
            first_to_second(style,health,experience,firstwon,steps)
def firstbossvictory(style,health,experience,firstwon):
    print("""
                                               ,----,                                                        
                                             ,/   .`|                       ,----..                          
    ,---,.   ,---,,-.----.    .--.--.      ,`   .'  :            ,---,.    /   /   \   .--.--.    .--.--.    
  ,'  .' |,`--.' |\    /  \  /  /    '.  ;    ;     /          ,'  .'  \  /   .     : /  /    '. /  /    '.  
,---.'   ||   :  :;   :    \|  :  /`. /.'___,/    ,'         ,---.' .' | .   /   ;.  \  :  /`. /|  :  /`. /  
|   |   .':   |  '|   | .\ :;  |  |--` |    :     |          |   |  |: |.   ;   /  ` ;  |  |--` ;  |  |--`   
:   :  :  |   :  |.   : |: ||  :  ;_   ;    |.';  ;          :   :  :  /;   |  ; \ ; |  :  ;_   |  :  ;_     
:   |  |-,'   '  ;|   |  \ : \  \    `.`----'  |  |          :   |    ; |   :  | ; | '\  \    `. \  \    `.  
|   :  ;/||   |  ||   : .  /  `----.   \   '   :  ;          |   :     \.   |  ' ' ' : `----.   \ `----.   \ 
|   |   .''   :  ;;   | |  \  __ \  \  |   |   |  '          |   |   . |'   ;  \; /  | __ \  \  | __ \  \  | 
'   :  '  |   |  '|   | ;\  \/  /`--'  /   '   :  |          '   :  '; | \   \  ',  / /  /`--'  //  /`--'  / 
|   |  |  '   :  |:   ' | \.'--'.     /    ;   |.'           |   |  | ;   ;   :    / '--'.     /'--'.     /  
|   :  \  ;   |.' :   : :-'   `--'---'     '---'             |   :   /     \   \ .'    `--'---'   `--'---'   
|   | ,'  '---'   |   |.'                                    |   | ,'       `---`                            
`----'            `---'                                      `----'                                          
                                                                 ,----,                         ,---,        
                                                               ,/   .`|                      ,`--.' |        
    ,---,        ,---,.    ,---,.    ,---,.   ,---,          ,`   .'  :   ,---,.    ,---,    |   :  :        
  .'  .' `\    ,'  .' |  ,'  .' |  ,'  .' |  '  .' \       ;    ;     / ,'  .' |  .'  .' `\  '   '  ;        
,---.'     \ ,---.'   |,---.'   |,---.'   | /  ;    '.   .'___,/    ,',---.'   |,---.'     \ |   |  |        
|   |  .`\  ||   |   .'|   |   .'|   |   .':  :       \  |    :     | |   |   .'|   |  .`\  |'   :  ;        
:   : |  '  |:   :  |-,:   :  :  :   :  |-,:  |   /\   \ ;    |.';  ; :   :  |-,:   : |  '  ||   |  '        
|   ' '  ;  ::   |  ;/|:   |  |-,:   |  ;/||  :  ' ;.   :`----'  |  | :   |  ;/||   ' '  ;  :'   :  |        
'   | ;  .  ||   :   .'|   :  ;/||   :   .'|  |  ;/  \   \   '   :  ; |   :   .''   | ;  .  |;   |  ;        
|   | :  |  '|   |  |-,|   |   .'|   |  |-,'  :  | \  \ ,'   |   |  ' |   |  |-,|   | :  |  '`---'. |        
'   : | /  ; '   :  ;/|'   :  '  '   :  ;/||  |  '  '--'     '   :  | '   :  ;/|'   : | /  ;  `--..`;        
|   | '` ,/  |   |    \|   |  |  |   |    \|  :  :           ;   |.'  |   |    \|   | '` ,/  .--,_           
;   :  .'    |   :   .'|   :  \  |   :   .'|  | ,'           '---'    |   :   .';   :  .'    |    |`.        
|   ,.'      |   | ,'  |   | ,'  |   | ,'  `--''                      |   | ,'  |   ,.'      `-- -`, ;       
'---'        `----'    `----'    `----'                               `----'    '---'          '---`"        
                                        +10 EXPERIENCE!""")
    experience += 10
    firstwon = True
    steps = 0
    first_to_second(style,health,experience,firstwon,steps)
### Main Program Start.
start = input("""
              
        ,----,                                                   ,--,              
      ,/   .`|                     ,--.         ,--.          ,---.'|              
    ,`   .'  :                   ,--.'|       ,--.'|    ,---,.|   | :   .--.--.    
  ;    ;     /       ,--,    ,--,:  : |   ,--,:  : |  ,'  .' |:   : |  /  /    '.        
.'___,/    ,'      ,'_ /| ,`--.'`|  ' :,`--.'`|  ' :,---.'   ||   ' : |  :  /`. /        
|    :     |  .--. |  | : |   :  :  | ||   :  :  | ||   |   .';   ; ' ;  |  |--`   
;    |.';  ;,'_ /| :  . | :   |   \ | ::   |   \ | ::   :  |-,'   | |_|  :  ;_     
`----'  |  ||  ' | |  . . |   : '  '; ||   : '  '; |:   |  ;/||   | :.'\  \    `.  
    '   :  ;|  | ' |  | | '   ' ;.    ;'   ' ;.    ;|   :   .''   :    ;`----.   \ 
    |   |  ':  | | :  ' ; |   | | \   ||   | | \   ||   |  |-,|   |  ./ __ \  \  | 
    '   :  ||  ; ' |  | ' '   : |  ; .''   : |  ; .''   :  ;/|;   : ;  /  /`--'  / 
    ;   |.' :  | : ;  ; | |   | '`--'  |   | '`--'  |   |    \|   ,/  '--'.     /  
    '---'   '  :  `--'   \'   : |      '   : |      |   :   .''---'     `--'---'   
            :  ,      .-./;   |.'      ;   |.'      |   | ,'                       
             `--`----'    '---'        '---'        `----'                        

A Game about Tunnels, depending on your direction, you'll fight an array of different,
such as ghouls, ghosts and goblins!! Gain experience with each battle in an effort to
                                    face the boss!

              
                                
                                Press Enter to start!
                                           """)
if start == "":
    Class = int(input("""                           Choose your style!
                                1: Knight
                                2: Cowboy
                                3: Wizard         
"""))
    window = tk.Tk()
    if Class == 1:
        style = Knight
        health = style.health
    elif Class == 2:
        style = Cowboy
        health = style.health
    elif Class == 3:
        style = Wizard
        health = style.health
    else:
        print("Choose from an EXISTING class bro.")
    Password = str(input(""" Enter your password (Leave it blank if you don't have one)"""))
    if Password == "":
        first_room(style,health,experience) 
    else:
        print("You're too early for this feature!")
else:
    print("Buhbye!")
        