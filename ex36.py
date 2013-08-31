from sys import exit
inventory = {}
leftroom = {"janitor" : "janitors clothes", "broom" : "broomstick"}
rightroom_area = {"combination" : "39192"}
firstroom = {}
def endgame():
  print "The door opens, and a elevator apears.\nIt takes you to the ground floor and to the exit.\nCongratulations you have finished the game.\n\nCredits.\n\nEverything done by Vladimir Hadzic.\n\nBig help Milos Hadzic\n\nCast.\n\nMain Character: Bound Snake :P\n\nGuard: Glupi Miodrag Spasic(napravicu 100% da mozes da ga ubijes...Pizda.)\n\nBeta testers:\nMarko Burkic\nMilos Hadzic\nVladimir Hadzic\n\nThanks for playing."
  dead()
def combination_room():
  print "This door is locked with a 10 digit keypad.\n1.*Try the combination\n2. Choose other door."
  while True:
    first = raw_input("> ")
    if first == "1" and "combination" not in inventory:
      print "Type in the combination or go back to the hallway.\n1. leave the door alone."
      while True:
        combination = raw_input("> ")
        if combination == "39192":
          print "*click"
          endgame()
        elif combination == "1":
          hallway_leftroom_exit()
        else:
          print "wrong combination. Try again."
          combination
    if first == "1" and "combination" in inventory:
      print "Type in the combination or go back to the hallway.\n1. Look at the guards combination.\n2. Leave the door alone."
      while True:
        combination2 = raw_input("> ")
        if combination2 == "39192":
          print "*click"
          endgame()
        if combination2 == "1":
          print "the code is %r.\nType it in." % inventory["combination"]
          combination2
        elif combination2 == "2":
          hallway_leftroom_exit
        else:
          print "Wrong combination. Try again."

    elif first == "2":
      hallway_leftroom_exit()
    else:
      print "Use the numbers in front."
      first


def rightroom_block():
  if "combination" in inventory:
    print "You got the combination, it's a bad idea to go back there."
    hallway_leftroom_exit()
def janitor_room_block():
  if "janitor" in inventory:
    print "You already serched here."
    left_room()
  elif "broom" in inventory:
    print "You already serched here."
    left_room()
def rightroom():
  rightroom_block()
  print "You walk in dressed as a Janitor and see the guard.\nHe ask's you.\n4Guard: What you want?\n1. Tell him that you want the door combination.\n2. You need to clean his room, and he need's to get out.\n3. Tell him that his mother should've had an abortion.\n4. What is he doing, because you are bored."
  guard = False

  while True:
    question = raw_input("> ")
    if question == "1":
      print "Guard:?Why do you need my combination, And who are you?\n1.Easter bunny, and i need it to go to your mothers place and puts some eggs in her basket.\n2. Wouldn't you like to know?!"
      while True:
        question2 = raw_input("> ")
        if question2 == "1":
          print "Guard: HAHA, a joker eh'?Finaly someone with a sense of humor.\n1. I know what you mean friend. So? How about that combination?\n2. No i'm serious, i'm gona bang your mom, asshole.\n3. Uhhh, yes sir, i concur."
          while True:
            question3 = raw_input("> ")
            if question3 == "1":
              print "Guard: Yeah, yeah shure.Wait?!How come you don't know it?\n1. I'm new here.\n2. Forgot it, and i'm ashamed to ask my boss.\n3. Just give me the damn key you idiot."
              while True:
                question4 = raw_input("> ")
                if question4 == "1":
                  print "He looks a bit suspicious...\nGuard: So? Everyone has got to have it?\n1. Comon man, i've \"missplaced\" it, cut me some slack.\n2. You caught me, ms. Jessica Fletcher, i'm your man.\n3. Say, \"Fuck you\" and try to knock him out."
                  while True:
                    question5 = raw_input("> ")
                    if question5 == "1":
                      print "He looks you a bit better and connects the dots...\nYou got caought."
                      dead()
                    elif question5 == "2":
                      print "Guard: HAHAHAHAHA, you are ok man, i can see you hate that bitch too.Here you go.\nSince you don't have anything here to do, you go out in the hallway.Fast..."
                      inventory["combination"] = rightroom_area.pop("combination")
                      hallway_leftroom_exit()
                    elif question5 == "3":
                      print "Nice try, but a short one..."
                      dead()
                    else:
                      print "You must use numbers in front"
                elif question4 == "2":
                  print "Guard: Yeah John, he's an asshole, but still, you should have that combination.\n1. Well, what can i say? I fucked up.\n2. Don't lecture me rent-a-cop, give me the damn combination!\n3. It won't happen again."
                  while True:
                    question6 = raw_input("> ")
                    if question6 == "1":
                      print "He raises an eyebrow, and sees through your theatrics.\nAlarm sound...\nYour little adventure failed."
                      dead()
                    elif question6 == "2":
                      print "Guard: oh yeah, you little shit.\nHe steps up, and see your face doesn't match your credentials.\nYou got caought."
                      dead()
                    elif question6 == "3":
                      print "Guard: Make shure it doesn't. Here, i won't file a report.\nYou say thanks, and get out in the hallway."
                      inventory["combination"] = rightroom_area.pop("combination")
                      hallway_leftroom_exit()
                    else:
                      print "You must use numbers in front."
                elif question4 == "3":
                  print "He didn't like your comment, you got knocked the fuck out, and caought."
                  dead()
                else:
                  print "Use the numbers in front"
            elif question3 == "2":
              print "Guard: Why so serious?!He didn't like your comment, not one....BIT!"
              dead()
            elif question3 == "3":
              print "He seems more suspicious.Guard: What's your id number?\n1. Ask your mom, she knows.\n2.Euh....555123?\n3. It seems this is a good time for action!"
              while True:
                question7 = raw_input("> ")
                if question7 == "1":
                  print "He doesn't appreciate comments like that....\nYou see some blunt object for a second, and then you notice your are on the floor."
                  dead()
                elif question7 == "2":
                  print "Guard: That's correct.\n1. Really?"
                  while True:
                    next = raw_input("> ")

                    if next == "1":
                      print "No..."
                      dead()
                    else:
                      print "You must use the numbers in front."
                elif question7 == "3":
                  print "Well that was a nice try, but you failed."
                  dead()
                else:
                  print "You must use the numbers in front."
        elif question2 == "2":
          print "Guard: I would, now speak up?!\n1. I will,....FUCK YOU!*Try brute force!\n2. I...ehmmm...kinda' lost mine.\n3. Comon man i left it home, and need to do a quick errand."
          while True:
            question9 = raw_input("> ")
            if question9 == "1":
              print "Nice try, but you failed."
              dead()
            elif question9 == "2":
              print "Guard: Ehmmm... i won't give you mine, because you are gona lose mine too.\n1. I won't i promise!"
              while True:
                question10 = raw_input("> ")
                if question10 == "1":
                  print "Guard: Fuck your promise i head that before.\n1. *Try attacking him with your broom stick.\n2. Nah' man, i'm not trying to screw you over."
                  while True :
                    question11 = raw_input("> ")
                    if question11 == "1":
                      print "You try to attack him failed..."
                      dead()
                    elif question11 == "2":
                      print "Guard: I don't belive you. I'm going to report you.\n*You panicked, and try to attack him. You failed..."
                      dead()
            elif question9 == "3":
              print "Guard: What sort of errand? Maybe i can help?\n1. It's personal...\n2. No you can't i need to do it myslef.\n3. Give me the damn code!"
              while  True:
                question12 = raw_input("> ")
                if question12 == "1":
                  print "Guard: Sorry, but you must leave your personal life out of the workspace.\n1. Please...\n2. Fuck you...*attack."
                  while True:
                    question13 = raw_input("> ")
                    if question13 == "1":
                      print "Ok..., be quick. Don't losse mine also."
                      inventory["combination"] = rightroom_area.pop("combination")
                      hallway_leftroom_exit()
                    elif question13 == "2":
                      print "You failed..."
                      dead()
                    else:
                      print "Use the numbers in front."
                elif question12 == "2":
                  print "Guard: No dice then...Sorry."
                  dead()
                elif question12 == "3":
                  print "Guard: I don't like your atitude.\n1. Fuck you.\n2. Sorry, i'm not thinking straight. My kid is sick."
                  while True:
                    question14 = raw_input("> ")
                    if question14 == "1":
                      print "Well, he realy didn't like your atitude."
                      dead()
                    elif question14 == "2":
                      print "Guard: Oh shit...Is it serious?\n1. Deadly...\n2. He hasn't got much time"
                      while True:
                        question15 = raw_input("> ")
                        if question15 == "1":
                          print "*He found you comment a bit to dramatic, and didn't belive you..."
                          dead()
                        elif question15 == "2":
                          print "Guard: Oh man, damn...Sorry, didn't know the situation. Here.\n*He gives you the key as you are acting for an Oscar."
                          inventory["combination"] = rightroom_area.pop("combination")
                          hallway_leftroom_exit()
                        else:
                          print "You must use the numbers in front."
                    else:
                      print "You must use the numbers in front."
    elif question == "2" and not guard:
      print "Guard: I can't leave, don't worry it's clean enough."
      guard = True
      question
    elif question == "2" and guard:
      print "Guard: Don't bugg me again, i'm not moving."
      question
    elif question == "3":
      print "That's a bit assholish thing to say, but non the less.\nYou failed to get the code that way...\nPlus he kicked your ass, and sounded the alaram."
      dead()
    elif question == "4":
      print "Guard: Ahhhh, watching the game, they are killing us by two.\nI've got money riding on these assholes.\n1. Shouldn't you be watching the prissoner?\n2. I like the other team more,plus it seems that your team suck!\n3. Well ok then, carry on."
      guard2 = False
      kickass = False
      while True:
        question8 = raw_input("> ")
        if question8 == "1":
          print "Hah', that asshole ain't going nowhere."
          question8
        elif question8 == "2" and not guard2:
          print "Ye'? Good for you dickhead."
          guard2 = True
        elif question8 == "2" and guard2 and not kickass:
          print "Keep it up and i'll kick your ass."
          kickass = True
        elif question8 == "2" and kickass and guard2:
          print "Guard: Ok smartass, you asked for it...\nYou got your ass kicked."
          dead()
        elif question8 == "3":
          print "1. Tell him that you want the door combination.\n2. You need to clean his room, and he need's to get out.\n3.Tell him that his mother should've had an abortion.\n4.What is he doing, because you are bored."
          rightroom()
        else :
          print "You must use numbers in front."
    else:
      print "You must use numbers in front."


def guard_clothes():
  if "janitor" not in inventory:
   print "You should find a disguise first."
   hallway_leftroom_exit()
  elif "janitor" in inventory:
   rightroom()
def firstroom():
  print "You are back in the room where you woke up.\n1.Look around.\n2.Leave room."

  while True:
    firstroom_choice = raw_input("> ")
    if firstroom_choice == "1":
      print "Nothing of interest."
      firstroom_choice
    elif firstroom_choice == "2":
      hallway_leftroom_exit()
    else:
      print "You must use numbers in front."

def hallway_leftroom_exit():
  print "You are back in the hallway\n1. Loocked room\n2. Right room\n3. Starting room.\n4. Janitor's office."

  while True:
    hallway = raw_input("> ")
    if hallway == "1":
      combination_room()
    elif hallway == "2":
      guard_clothes()
    elif hallway == "3":
      firstroom()
    elif hallway == "4":
      left_room()
    else:
      print "You must use numbers in front."

def left_room():
  print "This room is looks like a small janitors office,\nwhat do you do?\n1. Look for the key pass\n2. Find something usefull\n3. Wait.\n4. Leave room."
  janitor = False

  while True:
    lroom = raw_input("> ")
    if lroom == "1":
      print "You didn't find a combination, try serching around"
    elif lroom == "2":
      janitor_room_block()
      print "You find a broomstick and janitor clothes"
      print "Do you wish to pick them up?\n1. Yes.\n2. No."
      choice = raw_input("> ")
      if choice == "1":
        inventory["broom"] = leftroom.pop("broom")
        inventory["janitor"] = leftroom.pop("janitor")
        print "What do you want to do now?\n1. Look around more?\n2. Leave room."
        while True:
           merc = True

           izbor = raw_input("> ")
           if izbor == "1":
               print "You don't find anyting else."
               izbor
           elif izbor == "2":
             hallway_leftroom_exit()
           else:
             print "You must use numbers in front."
             izbor
      elif choice == "2":
        print "What do you want to do?\n1. Look for the key pass\n2. Find something usefull\n3. Wait.\n4. Leave room."
        lroom
    elif lroom == "3":
      print "Nothing happens."
      lroom
    elif lroom == "4":
      hallway_leftroom_exit()
    else:
      print "You must use numbers in front."
      lroom
      
  dead()
def room_door_hallway():
  print "After you lose the cuffs.\nYou go throu the door and see three doors.\n1. Door in front has got a key pad\n2. Right door, you hear noises coming from this room. \n3. Left door"
  izbor = False

  while True:
    choice = raw_input("> ")
    if choice == "1":
      combination_room()
    elif choice == "2":
      print "The guard sees you and kills you"
      dead()
    elif choice == "3":
      left_room()
    else:
      print "You must use numbers in front."
      izbor = True
      choice


def rope():
  print "You notce your hands are bound, hard not to...\nYou try to break free, how would you do this?\nUse numbers in front of answers.\n1. Try to shimmy out\n2. Use your body's force to break the chair."
  cuffs = False

  while True:
    free = raw_input("> ")
    if free == "1" and cuffs:
      print "You can't shimmy anymore, try brute force."
    elif free == "1" and not cuffs:
      print "Almost there!..."
      cuffs = True      
    elif free == "2" and not cuffs:
      print "You broke the chair, but the guard heard you. Your escape failed."
      dead()
    elif free == "2" and cuffs:
      print "You are free."
      room_door_hallway()
    else:
      print "You must use numbers in front."

def reset():
  if "broom" in inventory or "janitor" in inventory:
    leftroom["broom"] = inventory.pop("broom")
    leftroom["janitor"] = inventory.pop("janitor")
    starting_room()
  elif "combination" in inventory:
    rightroom_area["combination"] = inventory.pop("combination")
  elif "janitor" not in inventory or "broom" not in inventory or "combination" not in inventory:
    starting_room()


def dead():
  print "Do you want to start again?\n1. Yes.\n2. No."
  uslov = False

  while True:
    mrtav = raw_input("> ")
    if mrtav == "1":
      reset()
    elif mrtav == "2":
      print "Thank you from playing."
      exit(0)
    else:
      print "You must choose using numbers in front."
      uslov = True


def starting_room():
  print "You wake up, tied to a chair, not much crosses your mind... \nexcept your will to live"
  print "Press enter to continue"


  next = raw_input("> ")

  if next == "":
    rope()
  else:
    rope()

starting_room()
