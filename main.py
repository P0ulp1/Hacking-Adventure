print('''
                         ______......------.
  ______......------''''''                   -.
  \                                            -.
  |\                                             -.
  | \                                              -.
  |  \                                               -.
  |   \                                                - __
  |    \                         ______......------'''''' |
  |   __\______......------''''''  o   ______......---.o  |
  |   | .  o -=-- . |O|O| . O     '    ||o o o       ||   |
  |   |o                               ||____......---|   |
  |   |       ____.... ....---         ||''|____||_.  |   |
  |   |       ....---- ----''          ||''       ||  |  '.
  |   ||'.    ....---- ----''          ||o o o       ||  '. |
  |   |'. |   ....---- ----''          ||____......---|   | |
  |   | | |   ....---- ----''          ||''  |____||_.|   | |
  |   | | |   ....---- ----''          ||''          ||   | |
  |   | | |   ....---- ----''          ||o o o       ||   | |
  |   | | |   ....---- ----''          ||____......---|   | |
  |   | | |   ....---- ----''          ||''  |____||_.|   | |
  |   | | |                            ||''          ||  .'.'
  |   | | |   ____....----''  |        ||o o o       ||  _|
  |   |.'.'  |   ___....---   |        ||____......---| (_
  |   |_     |____....----''  |        ||''  |____||_.|  _|
  :    _)    |     __....-.   |        ||''          || (_
   :  |_     |     |_....-'   |   grp  ||o o o       ||   |
    '  _)    |____....----''  |  --''  ||____......---|  o|
    '.|      | ___....----'': |   /\   ||''  |____||_.|   |
     '|o     | |__....----''  |  /__\  :.''              _|
      |  .   :____....----''     ______......------''    
      |   _____......------''   
       '' 

''')
print("Welcome to Hacking Adventure.")
print("Your mission is to find the flag inside the server.")
print("INSTRUCTIONS : You just have to choose and type the word in 'single brackets' the way you want things to happen.")

choice = input("How do you want to sneak inside the server park ? Type 'front' or 'back'\n").lower()
if choice == "front":
    print("There was a camera who saw you enter. Game Over.")
elif choice == "back":
    print("You sneak from the back of the building.")
    choice = input("You arrive in front of two doors, wich one do you enter ? The 'black' one or the 'white' one ?\n").lower()
    if choice == "white":
        print("It was the guards room, it was written on the door ! Don't you know how to read ? Game Over.")
    elif choice == "black":
        print("You're in the server storage room, but they are 3 servers and you don't know wich one you're after.")
        choice = input("Wich server do you want to hack ? 'one' 'two' or 'three'\n").lower()
        if choice == "one":
            print("After hacking, you go back to your warehouse and plug the USB key containing the data in your computer. You downloaded a Disney Movie from the server. Game Over.")
        elif choice == "two":
            print("This server is too much secured for your skills, while you're attempting to bruteforce the password, a guard comes by and arrest you. Game Over.")
        elif choice == "three":
            print("Great job ! You successfully hacked your way into the Data Center ! YOU WIN")
        else:
            print("What are you doing ??? You've screwed the whole operation at the end. Game Over.")
