from sys import exit

def gold_room():
  print "This room is full of gold. How much do you take?" # Kada pozoves gold room, dobices ovaj string na pocetku

  next = raw_input("> ") # Ovde ce traziti unos, koliko zlatnika hoces da uzmes
  if "0" in next or "1" in next:
    how_much = int(float(next))
  else:
    dead("Man, learn to type a number.")

  if how_much < 50:
    print "Nice, you're not greedy, you win!"
    exit(0)
  else:
    dead("You greedy bastard!")


def bear_room():
  print "There is a bear here."
  print "The bear has a bunch of honey."
  print "The fat bear is in frot of another door."
  print "How are you going to move the bear?"
  bear_moved = False

  while True:
    next = raw_input("> ")

    if next == "Take honey":
      dead("The bear look at you then slaps your face off.")
    elif next == "Taunt bear" and not bear_moved:
      print "The bear has moved from the door. you can go through it now."
      bear_moved = True
    elif next == "Taunt bear" and bear_moved:
      dead("The bear gets pissed off and chews your leg off.")
    elif next == "open door" and bear_moved:
      gold_room()
    else:
      print "I got no idea what that means."


def cthulhu_room():
  print "Here you seethe great evil Cthulhu."
  print "He, it, whatever stares at you and you go insane."
  print "Do you flee for your life or eat your head?"

  next = raw_input("> ")

  if "flee" in next:
    start()
  elif "head" in next:
    dead("Well that was tasty!")
  else:
    cthulhu_room()

def dead(why):
  print why, "Good job!"
  print "Do you want to start again? Yes or No?"
  dickhead = False

  while True:
    mrtav = raw_input("> ")
    if mrtav == "No" or mrtav == "no" or mrtav == "n" or mrtav == "N":
      print "Tnx for playing"
      exit(0)
    elif mrtav == "Yes" or mrtav == "yes" or mrtav == "y" or mrtav == "Y":
      start()
    else:
      print "You must choose Yes or No answers"
      dickhead = True
      mrtav
    


def start():
  print "You are in a dark room."
  print "There is a door to your right and left."
  print "Which one do you take?"

  next = raw_input("> ")

  if next == "left":
    bear_room()
  elif next == "right":
    cthulhu_room()
  else:
    dead("You stumble around the room until you starve.")

start()
