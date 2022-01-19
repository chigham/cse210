import random as rd

class dice:
    '''
    '''
    def __init__(self):
        self.sides_num = 6
        self.side = 0
        self.points = 0
        self.side_to_points = {
            '1': 100,
            '2': 0,
            '3': 0,
            '4': 0,
            '5': 50,
            '6': 0
        }
    
    def roll(self):
        '''
        '''
        #self.points = 0
        self.side = rd.randint(1, self.sides_num)
        self.points = self.side_to_points[str(self.side)]

class game:
    '''
    '''
    def __init__(self):
        self.score = 0
        self.num_dice = 5
        self.roll_again = 'y'
    
    def roll_dice(self, five_dice=[dice(), dice(), dice(), dice(), dice()]):
        '''
        '''
        while self.roll_again == 'y':
            
            # This is how you play the game
            self.roll_again = input('Roll dice? [y/n] ').lower()
            
            # Roll the dice, add score to your total
            if self.roll_again == 'y':
                
                print_results = ''
                for d in five_dice:
                    d.roll()
                    
                    # add side to the print_string, add points to total score
                    print_results += f'{d.side} '
                    self.score += d.points

                print(f'you rolled: {print_results}')
                print(f'score: {self.score}')
            
                # The game ends in a loss if you do not roll a 1 or a 5
                if 1 not in [five_dice[0].side, five_dice[1].side, five_dice[2].side, five_dice[3].side, five_dice[4].side] and 5 not in [five_dice[0].side, five_dice[1].side, five_dice[2].side, five_dice[3].side, five_dice[4].side]:
                    self.roll_again = 'n'
                    print(f'game over...you didn\'t roll a 1 or a 5\nyour final would have been {self.score}...\nbut you lose, way to go buddy')

            # Let the user end the game the correct way
            elif self.roll_again == 'n':
                print(f'game over...your final score is {self.score}')
            
            # Ignore incorrect input from the user
            else:
                self.roll_again = 'y'
                print('that\'s not an acceptable answer...try again')

