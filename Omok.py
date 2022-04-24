# -*- coding: utf-8 -*-

board_tmp="""┌,┬,┬,┬,┬,┬,┬,┬,┬,┬,┬,┬,┬,┬,┬,┬,┬,┬,┬,┬,┬,┬,┬,┬,┬,┬,┬,┬,┬,┐,├,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┤,├,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┤,├,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┤,├,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┤,├,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┤,├,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┤,├,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┤,├,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┤,├,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┤,├,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┤,├,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┤,├,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┤,├,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┤,├,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┤,├,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┤,├,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┤,├,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┤,├,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┤,├,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┤,├,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┤,├,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┤,├,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┤,├,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┤,├,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┤,├,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┤,├,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┤,├,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┤,├,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┼,┤,└,┴,┴,┴,┴,┴,┴,┴,┴,┴,┴,┴,┴,┴,┴,┴,┴,┴,┴,┴,┴,┴,┴,┴,┴,┴,┴,┴,┴,┘"""

board = board_tmp.split(',').copy()

for i in range(30):
    print(' '.join(board[0+i*30:30+i*30]))

#%%
print('hello')