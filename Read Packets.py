from scapy.all import *
from DecodeText import decode
import time

conf.use_pcap = True
TCP.payload_guess = []
"""

#
    Description:
       Movement of player
    Args:
       0: direction of movement: u,d,l,r (up, down, left, right)
!
    Description:
        Encountered Battle
    Args:
       0: Oppenent Pokemon's Pokedex ID
       1: Opponent Current HP
       2: Opponent Level
       3: NO IDEA- seems to always be 1
       4: Battle Start Message (A wild <pokemon name> attacks!)
       5: Is Shiny (0 = No, 1 = Yes)
       6: Trainer Name ("" if no trainer)
       7: Is NPC Battle (1 = Yes, "" = No)
       8: Number of pokemon ("" if wild battle)
       9: Opponent Gender
       10: NO IDEA- sometimes is blank, sometimes is None
       11: **  Already Caught
       12: NO IDEA
a
    Description:
        Battle event
    Args:
        0: My Pokemon's Current HP
        1: Opponent Pokemon's Current HP
        2: My Pokemon's Max HP
        3: Opponent Pokemon's Max HP
        4: Battle Text
        5: Random number?
        6: Opponent Pokemon's Level
"""

def process_pkt(pkt):
    """
    Turn packet into command
    """
    if pkt.getlayer(Raw):
        data = pkt.getlayer(Raw).load
        #Data is received as byte.  convert to string to decode
        try:
            data = data.decode("utf-8")
        except:
            data = ""

        data = decode(data)
        data = data.replace("\r\n", "")
        data = data.split('|.\\')
        return data
def display_command(pkt):
    commands = process_pkt(pkt)
    if commands != None:
        for command in commands:
            if command != None and command != "":
                if command[0] == "!":
                    command = command[4:]
                    params = command.split('|')
                    print(command)
                    counter = 0
                    for param in params:
                        print(str(counter) + " : "  + param)
                        counter += 1
                    print("-"*50)
                if command[0] == "a":
                    command = command[4:]
                    params = command.split('|')
                    counter = 0
                    for param in params:
                        print(str(counter) + " : "  + param)
                        counter += 1
                    print("-"*50)

def display_command2(pkt):
    commands = process_pkt(pkt)
    if commands != None:
        for command in commands:
            if command != None:
                print(command)


while True:
    #Returns a list.  We only examine 1 packet at a time, so we only want first element of list
    sniff(filter="host 46.28.207.53", prn=display_command2, store=0)
        #if data[0] == 'a' or data[0] == '!' or data[0] == '#':
            #print(data)


