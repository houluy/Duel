from custom import *
from yaml import load

config_file = 'config.yml'
with open(config_file, 'r') as f:
    basic_data = load(f)

# Pandora with Pandora's box
# Damocles with Th Sword of Damocles
# Muse with Th Book of Memory
# Sphinx with Riddle of Sphinx
# Noah with Noah's Ark
# Adam with Forbidden Fruit
# Pygmalion with Ivory Nymph
# Judas with Th Kiss of Judas

class EnergyNotEnoughError(Exception):
    pass

class Species:
    def __init__(self):

        #Primary attributes(change)
        self._energy = basic_data.get('ENERGY')
        self._blood = basic_data.get('BLOOD')
    
        #Primary attributes(no change)
        self._defense = basic_data.get('DEF')

        self._atk = 0

        #Skill attibutes
        self._love = 0
        self._evil = 0

        #Skill
        self._skill = []

        self._states = {}
        self._actions_name = {
            1: "Physical Attack",
            2: "Pistol Attack",
            3: "Defend",
            4: "Gain",
            5: "Show States",
        }

        self._actions = {
            1: self.attack,
            2: self.attack,
            3: self.defend,
            4: self.gain,
            5: self._print_states,
        }

    def __str__(self):
        return self._form_stats()

    def _form_stats(self):
        self._states = dict(blood=self._blood, energy=self._energy, \
            atk=self._atk, defense=self._defense)
        return '''
            blood: %(blood)s
            energy: %(energy)s
            attack force: %(atk)s
            defense: %(defense)s
        ''' % self._states

    def _print_states(self):
        print(str(self))

    def show_actions(self):
        return self._actions_name

    def get_actions(self):
        return self._actions
    
    def attack(self, atk_type):
        '''Attack enemy'''
        energy_consume = basic_data.get('{}_ENERGY_DEMAND'.format(atk_type))
        atk = basic_data.get('{}'.format(atk_type))
        if self._energy < energy_consume:
            raise EnergyNotEnoughError('Insufficient Energy')
        self._energy -= energy_consume
        self._atk += atk
        return self._atk

    def hurt(self, attack_force):
        '''Hurt!!'''
        self._blood -= max((attack_force - self._defense), 0)
        return self._die()

    def skill_attack(self, skill):
        '''Use a skill to attack'''
        self._energy -= 3

    def gain(self):
        '''Accumulate energy'''
        self._energy += basic_data.get('ACCUM')
        self._defense -= basic_data.get('ACCUM_DEF_LOSS')

    def deadly_accumulate(self):
        '''Accumulate more energy with less defense'''
        self._energy += basic_data.get('DEADLY_ACCUM')
        self._defense -= basic_data.get('DEADLY_DEF_LOSS')

    def defend(self):
        '''Defend for one turn'''
        self._defense += basic_data.get('DEF_ADD')

    def big_guardian(self):
        '''Defend for one turn with energy'''
        if (self._energy < 2):
            raise EnergyNotEnoughError('Your energy is not enough!')
        self._defense += basic_data.get('BIG_DEF_ADD')
        self._energy -= basic_data.get('BIG_DEF_ENEGY_DEMAND')

    def _die(self):
        return True if (self._blood <= 0) else False

    def back_to(self):
        self._defense = basic_data.get('DEF')
        self._atk = 0

    def get_atk(self):
        return self._atk

class Pandora(Species):
    def __init__(self):
        super().__init__()

class Damocles(Species):
    def __init__(self):
        super().__init__()
        
if __name__ == '__main__':
    sp = Species()
