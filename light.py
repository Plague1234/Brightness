#######################################################
#             Made By : Bl4ckJ4ck                     #
#             Contact : jacktheripperkilla84@gmail.com#
#             Have a night day :)                     #
#######################################################

import os, sys
os.system("clear")
os.system("figlet -f shadow L   i   g   h   t ")

#FUNCTIONS

def add():
  ad = input("\nHow many brightness add? : ")
  if ad == "10" or ad == "20" or ad == "30" or ad == "40" or ad == "50" or ad == "60" or ad == "70" or ad == "80" or ad == "90" or ad == "100":
    os.system("light -A " + ad)
    print("\n\nOKAY! brightness add " + ad)
    sys.exit()
  else:
    print("\n ERROR Bitch!\n use /dev/brain!")
    sys.exit()

def down():
  do = input("\nHow many brightness down? : ")
  if do == "10" or do == "20" or do == "30" or do == "40" or do == "50" or do == "60" or do == "70" or do == "80" or do == "90" or do == "100":
    os.system("light -U " + do)
    print("\n\nOKAY brightness add " + do)
    sys.exit()
  else:
    print("\n ERROR Bitch!\n use /dev/brain!")
    sys.exit()

print
lg = input("\n\nAdd/Down: ")
print

if lg == "add" or lg == "Add" or lg == "ADD":
  add()

elif lg == "down" or lg == "Down" or lg == "DOWN":
  down()

else:
  print("\n ERROR WRONG INPUT!")
  sys.exit()
