### a space escape game using classes
### * Map (class)
### - next_scene
### - opening_scene
### * Engine
### - play
### * Scene
### - enter
### * Death
### * Central Corridor
### * Laser Weapon Armory
### * The Bridge
### * Escapde Pod

from sys import exit
from random import randint, seed
from Space_Dialog import DIALOGUE

seed(42)

## declare all the major classes

class Scene(object):
    def enter(self):
        print("This scene is not configured yet")
        print("Subclass it and implement enter")
        exit(1)
        

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
        
    def play(self):
        
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            
        current_scene.enter()
    
        

## death is just one of the scenes, so a child class

class Death(Scene):
    quips = [
        "You died.  You kinda suck at this.",
         "Your Mom would be proud...if she were smarter.",
         "Such a luser.",
         "I have a small puppy that's better at this.",
         "You're worse than your Dad's jokes."]
    def enter(self):
        q_idx = randint(0, len(self.quips)-1)
        print(self.quips[q_idx])
        exit(1)
    
        

class CentralCorridor(Scene):
    def enter(self):
        print(DIALOGUE['CentralCorridor_enter'])
        actions = ["Shoot", "Dodge", "Tell a joke"]
        print(f"Please choose your next move, available actions are {actions}")
          
        action = input("> ")

        if action == "Shoot":
            print(DIALOGUE["CentralCorridor_shoot"])
            return 'death'
        
        elif action == "Dodge":
            print(DIALOGUE['CentralCorridor_dodge'])
            return 'death'
        
        elif action == "Tell a joke":
            print(DIALOGUE['CentralCorridor_joke'])
            return 'laser_weapon_armory'
        
        else:
            print("Invalid action!")
            return 'central_corridor'

class LaserWeaponArmory(Scene):
    def enter(self):
        print(DIALOGUE['LaserWeaponArmory_enter'])
        
        code = f"{randint(1,9)}"
        guess = input("[keypad]>")
        try_times = 0
        
        while guess != code and try_times < 9:
            print("Try again!")
            try_times += 1
            guess = input("[keypad]>")
        
        if guess == code:
            print(DIALOGUE['LaserWeaponArmory_guess'])
            return 'the_bridge'
        else:
            print(DIALOGUE['LaserWeaponArmory_fail'])
            return 'death'
    
        
class TheBridge(Scene):
    def enter(self):
        print(DIALOGUE['TheBridge_enter'])
        actions = ['Throw bomb', 'Place bomb']
        print(f"Please choose your next move, available actions are {actions}" )
   
        action = input("> ")

        if action == "Throw bomb":
            print(DIALOGUE['TheBridge_throw_bomb'])
            return 'death'
            
        elif action == "Place bomb":
            print(DIALOGUE['TheBridge_place_bomb'])
            return 'escape_pod'           
        else:
            print("Invalid move!")
            return 'the_bridge'
        
class EscapePod(Scene):
    def enter(self):
        print(DIALOGUE['EscapePod_enter'])
        pod = randint(1,5)
        choice = input("[pod #]>")
        try:
            int(choice)
        except ValueError:
            print("Please type in valide intger!")
            
        if int(choice) != pod:
            print(DIALOGUE['EscapePod_death'].format(guess = choice))
            return 'death'
        else:
            print(DIALOGUE['EscapePod_escape'].format(guess = choice))
            return 'finished'

class Finished(Scene):
    def enter(self):
        print("You won! Well done!")
        return 'finished'      

class Map(object):
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'finished': Finished(),
        'death': Death()
    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene  

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)
        

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
    
