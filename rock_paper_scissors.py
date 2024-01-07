moves = ['rock', 'paper', 'scissors']
from random import choice 

class Player:
    memory = [] 
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.memory.append([my_move, their_move]) 

class RandomPlayer(Player):
    def move(self):
        return choice(moves)  

class HumanPlayer(Player):
    def move(self):
        move = input('Enter a move: ') 
        while move not in moves:
            move = input('Invalid move, Enter a move: ')
        
        return move

class ReflectPlayer(Player):
    def move(self):
        if self.memory: 
            return self.memory[-1][1] 
        else:
            return choice(moves) 

class CyclePlayer(Player):
    def move(self):
        if self.memory: 
            prev_move = self.memory[-1][0]
            return 'paper' if prev_move == "rock" else 'scissors' if prev_move == "paper" else "rock"
        else:
            return choice(moves)

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        one_win = beats(move1, move2) 
        two_win = beats(move2, move1) 

        return 1 if one_win else 2 if two_win else 0 

    def play_game(self):
        print("Game start!")
        game_stat = []
        for round in range(3):
            print(f"Round {round}:")
            win_status = self.play_round()
            game_stat.append(win_status)
            print(f'Player{win_status} wins' if win_status != 0 else "Players draw") 
        print(
            f'''
Player 1 wins {game_stat.count(1)} time(s)
Player 2 wins {game_stat.count(2)} time(s)
Players tie {game_stat.count(0)} time(s)
            '''
        )

        if game_stat.count(1) > game_stat.count(2): print("PLAYER 1 WINS")
        elif game_stat.count(1) < game_stat.count(2): print("PLAYER 2 WINS")
        else: print('DRAW')
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()