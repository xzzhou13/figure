from random import randint

class Die():
    '''生成一个骰子的类'''

    def __init__(self,num_sides=6):
        '''骰子默认6面'''
        self.num_sides = num_sides

    def roll(self):
        '''返回一次投掷骰子的结果'''
        return randint(1, self.num_sides)
