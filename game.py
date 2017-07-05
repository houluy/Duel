from custom import *
import sys
from pprint import pprint

'''
1. gain energy
2. defend
3. attack
'''

class Game():
    def __init__(self, player1='Pandara', player2='Damocles'):
        self.player1 = species_dic[player1]()
        self.player2 = species_dic[player2]()
        self.player_list = [self.player1, self.player2]
        self.game_round = 0

    def get_input(self):
        action = input('Please input your action:')
        return action

    def make_action(self, player):
        action = self.get_input()
        if (action == 'q'):
            print('GoodBye')
            sys.exit(0)
        elif (action not in ['1', '2', '3']):
            print('input error!')
            sys.exit(0)
        else:
            return player.get_actions().get(str(action))

    def play(self):
        attack_list = []
        die_list = [False]*2
        for ind in range(1, 3):
            current_player = self.player_list[ind - 1]
            print()
            print('Player {}\'s attributes:'.format(ind))
            print(str(current_player))
            while True:
                print('Player {}, choose action: '.format(ind))
                pprint(current_player.show_actions())
                action = self.get_input()
                if (action == 'q'):
                    sys.exit(0)
                try:
                    result = current_player.get_actions().get(int(action))
                    if (int(action) == 1):
                        result = result('ATK')
                    elif (int(action) == 2):
                        result = result('PISTOL')
                    elif (int(action) == 5):
                        result()
                        continue
                    else:
                        result()
                except Exception as e:
                    print(e)
                else:
                    break
            attack_list.append(current_player.get_atk())
        print(attack_list)
        for ind in range(2):
            current_player = self.player_list[ind]
            damage = attack_list[1 - ind]
            result = current_player.hurt(damage)
            current_player.back_to()
            if result:
                die_list[ind] = True
        if True in die_list:
            for ind, dieornot in enumerate(die_list):
                if dieornot:
                    print('Player {} is killed'.format(ind + 1))
            sys.exit(0)
        

    def run(self):
        while True:
            self.play()
            self.game_round += 1

if __name__ == '__main__':
    game = Game()
    game.run()
