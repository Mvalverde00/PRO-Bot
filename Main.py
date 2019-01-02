import numpy as np
from PIL import ImageGrab, Image
import cv2
import time
from SendKeys import PressKey, ReleaseKey, W, A, S, D, ONE, TWO, THREE, FOUR
import random
import pytesseract
from DecodeText import decode
from scapy.all import *

isBattle = False
encountered_poke_stats = None

def process_pkt(pkt):
    """
    Turn packet into command
    """
    global isBattle
    global encountered_poke_stats
    if pkt.getlayer(Raw):
        data = pkt.getlayer('Raw').load
        #Data is received as byte.  convert to string to decode
        try:
            data = data.decode("utf-8")
        except:
            data = ""

        data = decode(data)
        data = data.replace("\r\n", "")
        data = data.split('|.\\')
        print(data)
        for command in data:
            try:
                if command[0] == "!":
                    isBattle = True
                    encountered_poke_stats = command
            except IndexError:
                pass
def parse_encountered_poke_stats(command):
    command = command[4:]
    params = command.split('|')
    return params
    
class State():
    def __init__(self):
        self.pokemon = []
    def update(self):
        pass
    def send_key(self, key):
        PressKey(key)
        time.sleep((random.randint(11,13) + random.random())/100)
        ReleaseKey(key)
        time.sleep((random.randint(11,13) + random.random())/100)
    def catch(self):
        pass
    def fight(self):
        pass
    def run(self):
        self.send_key(FOUR)
        
    
class Travel(State):
    """Moves player from infront of pokecenter to training area (e.g. patch of grass).
    """
    
    def __init__(self, AI : object, directions : list) -> None:
        """Initialize Travel object.

        Args:
            AI (object): Finite State Machine controller, used to change states
            directions (list): List of key presses (W,A,S,D) to travel from pokecenter to training area.  directions MUST BE REVERSIBLE.  You cannot jump over one way ledges or similar.
        
        """

        self.AI = AI
        self.directions = directions

        #int containing current index of self.directions
        self.direction_index = 0
    def update(self) -> None:
        global isBattle
        global encountered_poke_stats
        """Move player from pokecenter to training area.  Runs from any battles en route"""
        try:
            self.send_key(self.directions[self.direction_index])
            sniff(filter="host 46.28.207.53", prn=process_pkt, store=0, count=8, timeout=.3)
            if isBattle:
                isBattle = False

                print('Found a battle!')
                #If poke is shiny
                if encountered_poke_stats[5]:
                    self.catch()
                else:
                    time.sleep(6)
                    print('Attempting to run')
                    self.run()
                    
                encountered_poke_stats = None
            self.direction_index += 1
        except IndexError:
            pass
            #change states
                
    def battling(self):
        """Check if player is engaged in battle.

        Returns:
               True if in battle, False otherwise
        To Do:
             Possibly check image for box in center of screen.  Text is good, but player name might trigger battle reaction
               
        """
        pass
    def transitioning(self):
        """Check if player is transitioning between maps

        Returns:
               True if transitioning, False otherwise
               
        """
        pass

class Search(State):
    def __init__(self, AI : object) -> None:
        self.AI = AI
        self.counter = 0
    def update(self):
        if self.battling():
            time.sleep((random.randint(11,13) + random.random())/100)
            self.AI.change_state("Battle")
        else:
            if self.counter % 2 == 1:
                self.counter +=1
                PressKey(S)
                time.sleep((random.randint(11,13) + random.random())/100)
                ReleaseKey(S)
            else:
                self.counter +=1
                PressKey(W)
                time.sleep((random.randint(11,13) + random.random())/100)
                ReleaseKey(W)
    def battling(self):
        """Check if player is engaged in battle.

        Returns:
               True if in battle, False otherwise
        To Do:
             Possibly check image for box in center of screen.  Text is good, but player name might trigger battle reaction
               
        """
        pass


class Battle(State):
    def __init__(self, AI : object, wanted_pokemon : list) -> None:
        self.AI = AI
    def update(self):
        pokemon = self.battling()
        print(pokemon)
        if pokemon != "":
            if pokemon in self.pokemon:
                self.catch()
            else:
                self.battle()
        else:
            self.AI.change_state("Search")      
    def battling(self):
        """Check if player is engaged in battle.

        Returns:
               Name of pokemon, empty string if no pokemon
        To Do:
             Possibly check image for box in center of screen.  Text is good, but player name might trigger battle reaction
               
        """
        pass
    def catch(self):
        pass
    def battle(self):
        pass

class Heal():
    def __init__(self):
        pass

class AI():
    def __init__(self):
        self.states = {"Travel":Travel(self,[D,S,A,W,D,S,A,W,D,S,A,W,D,S,A,W,D,S,A,W,D,S,A,W]),
                       "Search":Search(self),
                       "Battle":Battle(self,["4","10"])}
        self.state = self.states["Travel"]
        self.running = False

        #self.last_time = time.time()
    def main(self):
        self.running = True
        while self.running:
            self.state.update()
    def change_state(self, state):
        self.state = self.states[state]
        print("Transitioned to state " + state)

if __name__ == "__main__":
    time.sleep(2)
    ai = AI()
    ai.main()
