import random

class Game2048:
# constructor: initializes the empty grid with 2 "2"s in random tiles every time
    def __init__(self, row=4, col=4):
        self.row = row
        self.col = col

        # initialize you matrix representing the grid with zeros.
        self.grid = [[0]*self.row for i in range(self.col)]

        # initialize the game score
        self.score = 0

        # Create an attribute to make sure that the congratulations appears once
        self.first_win = 0

        # initialize 2 tiles with a 2
        self.RandomFillTile(2)
        self.RandomFillTile(2)

        # moving check for the sliding methods
        self.changed = False

# generates a 2 or 4 randomly with 3 times more chance to get a 2 than 4
    def random2or4(self):
        if random.random() > 0.90:
            return 4
        else:
            return 2

# retrieving the current score
    def getScore(self):
        return self.score

# adding "new" to the current score to update score as the numbers are added up
    def setScore(self, new):
        self.score += new

# Obtaining the number of empty tiles
    def getNbEmptyTiles(self):
        empty = 0
        for i in self.grid:
            for tile in i:
                if tile == 0:
                    empty += 1  # return the number of tiles that are empty
        return empty  # i.e. they contain zeros.

# Obtaining the list of empty tiles in a list of pairs (of coordinates i,j)
    def getListEmptyTiles(self):
        emptytiles = []
        for i in range(4):
            for j in range(4):
                if self.grid[i][j] == 0:
                    emptytiles.append([i, j])  # return a list of pairs where each pair
        return emptytiles                       # is the x,y coordinates of a tile that is empty

# Selecting a random empty tile and filling it with "init"
    def RandomFillTile(self, init):
        emptytiles = self.getListEmptyTiles()
        if len(emptytiles) != 0:
            tile = random.randint(0, len(emptytiles) - 1)
            (i, j) = emptytiles[tile]
            self.grid[i][j] = init


# printing the current game grid, score and number of empty tiles and current score
# The nested for loops are for printing only the empty tiles as opposed to the zeros of the original list
    def print(self):
        # Make a copy of the grid for printing so that the zeros does not show up.
        print_grid = [[0] * self.row for i in range(self.col)]
        for i in range(4):
            for j in range(4):
                print_grid[i][j] = self.grid[i][j]  # Make the print grid equal to the original one
                if print_grid[i][j] == 0:  # but make this one all blanks as opposed to zeros
                    print_grid[i][j] = ' '  # so that the printed grid does not show zeros

        line_line = '-----------------------------'
        print(line_line)
        print('|' + str(print_grid[0][3]).rjust(5) + ' |' + str(print_grid[1][3]).rjust(5) + ' |' + str(
            print_grid[2][3]).rjust(5) + ' |' + str(print_grid[3][3]).rjust(5) + ' | ')
        print(line_line)
        print('|' + str(print_grid[0][2]).rjust(5) + ' |' + str(print_grid[1][2]).rjust(5) + ' |' + str(
            print_grid[2][2]).rjust(5) + ' |' + str(print_grid[3][2]).rjust(5) + ' | ')
        print(line_line)
        print('|' + str(print_grid[0][1]).rjust(5) + ' |' + str(print_grid[1][1]).rjust(5) + ' |' + str(
            print_grid[2][1]).rjust(5) + ' |' + str(print_grid[3][1]).rjust(5) + ' | ')
        print(line_line)
        print('|' + str(print_grid[0][0]).rjust(5) + ' |' + str(print_grid[1][0]).rjust(5) + ' |' + str(
            print_grid[2][0]).rjust(5) + ' |' + str(print_grid[3][0]).rjust(5) + ' | ')
        print(line_line)
        print('Current Score: ' + str(self.getScore()) + ' || Empty cells: ' + str(self.getNbEmptyTiles()))
        print('--------------------------------------- ')


# check if the grid is collapsible horizontally or vertically
# collaborated with Jerry Bao
    def collapsible(self):
        # if self.getNbEmptyTiles() != 0:
        #     return True
        collapse = False

        new_grid = [[0]*self.row for i in range(self.col)]      # create a new list for the grid
        for i in range(4):
            for j in range(4):
                new_grid[i][j] = self.grid[i][j]  # make a copy of the original grid for modifications

        remove_0 = []  # create a list for the row list with the zeros removed
        for i in new_grid:
            for tile in i:
                remove_0 = [tile for tile in i if tile != 0]  # remove the zeros in the row list
            for j in range(len(remove_0) - 1):
                if remove_0[j] == remove_0[j + 1]:  # check if the items one by one to see if they are the same
                    collapse = True  # check if it's possible to merge tiles and assign True to collapse if it is

        new1_grid = [[0]*self.row for i in range(self.col)]     # create a new list for the grid
        for i in range(4):
            for j in range(4):
                new1_grid[j][i] = self.grid[i][j]  # make a copy of the original grid for modifications

        remove1_0 = []  # create a list for the column list with the zeros removed
        for i in new1_grid:
            for tile in i:
                remove1_0 = [tile for tile in i if tile != 0]  # remove the zeros in the row list
            for j in range(len(remove1_0) - 1):
                if remove1_0[j] == remove1_0[j + 1]:  # check if the items one by one to see if they are the same
                    collapse = True  # check whether there is a possibility to merge
        return collapse  # tiles and assign True to collapse if it is the case

# check if the grid contains 2048
    def win(self):
        win = False
        for i in range(4):
            for j in range(4):
                if self.grid[i][j] == 2048:
                    win = True  # return true if the value 2048 exists in any of the tiles in the grid
                    self.first_win += 1   # so that the player can continue after winning and 2048 gets ignored
        return win  # return false otherwise

# collapses the columns to the left and updates the grid and score
    def slideLeft(self):
        self.changed = False  # check if there were tiles that can slid left if yes return true
        for i in range(1, 4):  # if not return false
            for j in range(0, 4):
                if self.grid[i - 1][j] == 0 and self.grid[i][j] != 0:
                    self.changed = True
                elif self.grid[i - 1][j] == self.grid[i][j] and self.grid[i - 1][j] != 0:
                    self.changed = True

        for j in range(4):  # created a new list and appended all the non zero values
            new_list = []  # in a row to it
            for i in range(4):
                if self.grid[i][j] != 0:
                    new_list.append(self.grid[i][j])

            for i in range(1, len(new_list), +1):  # checking from left to right of the list
                if new_list[i] == new_list[i - 1]:  # if the two items are the same
                    total = new_list[i] + new_list[i - 1]  # total is equal to the sum of the two
                    new_list[i - 1] = total  # and assign it to the left most valid spot for the sum in the list
                    self.setScore(total)  # the total is the new score and it adds to the current score
                    new_list[i] = 0  # everything else in the list should be replaced with 0
                    break
            if 0 in new_list:  # if there is 0 in the list
                new_list.remove(0)  # remove all of them so that 2240 case won't have 0 in the middle after merge
            length = len(new_list)
            for num in range(4 - length):
                new_list.append(0)  # then append 0 to the list
            for item in range(4):
                self.grid[item][j] = new_list[item]  # assign the new sum item to actual grid in the appropriate place

# collapses the columns to the right and updates the grid and score
    def slideRight(self):
        self.changed = False  # check if there were tiles that can slid right if yes return true
        for i in range(0, 3):  # if not return false
            for j in range(0, 4):
                if self.grid[i + 1][j] == 0 and self.grid[i][j] != 0:
                    self.changed = True
                elif self.grid[i + 1][j] == self.grid[i][j] and self.grid[i + 1][j] != 0:
                    self.changed = True

        for j in range(4):  # created a new list and appended all the non zero values
            new_list = []  # in a row to it
            for i in range(4):
                if self.grid[i][j] != 0:
                    new_list.append(self.grid[i][j])

            for i in range(len(new_list) - 2, -1, -1):  # checking from right to left of the list
                if new_list[i] == new_list[i + 1]:  # if the two items are the same
                    total = new_list[i] + new_list[i + 1]  # total is equal to the sum of the two
                    new_list[i + 1] = total  # and assign it to the right most valid spot for the sum in the list
                    self.setScore(total)  # the total is the new score and it adds to the current score
                    new_list[i] = 0  # everything else in the list should be replaced with 0
                    break
            if 0 in new_list:  # if there is 0 in the list
                new_list.remove(0)  # remove all of them so that 0422 case won't have 0 in the middle after merge
            length = len(new_list)
            for num in range(4 - length):
                new_list.insert(0, 0)  # then insert 0 to the list in the front
            for item in range(4):
                self.grid[item][j] = new_list[item]  # assign the new sum item to actual grid in the appropriate place

# collapses the rows upwards and updates the grid and score
    def slideUp(self):
        self.changed = False  # check if there were tiles that can slid up if yes return true
        for i in range(0, 4):  # if not return false
            for j in range(0, 3):
                if self.grid[i][j + 1] == 0 and self.grid[i][j] != 0:
                    self.changed = True
                elif self.grid[i][j + 1] == self.grid[i][j] and self.grid[i][j + 1] != 0:
                    self.changed = True

        for i in range(4):  # created a new list and appended all the non zero values
            new_list = []  # in a column to it
            for j in range(4):
                if self.grid[i][j] != 0:
                    new_list.append(self.grid[i][j])

            for j in range(len(new_list) - 2, -1, -1):  # checking from right to left of the list
                if new_list[j] == new_list[j + 1]:  # if the two items are the same
                    total = new_list[j] + new_list[j + 1]  # total is equal to the sum of the two
                    new_list[j + 1] = total  # and assign it to the right most valid spot for the sum in the list
                    self.setScore(total)  # the total is the new score and it adds to the current score
                    new_list[j] = 0  # everything else in the list should be replaced with 0
                    break
            if 0 in new_list:  # if there is 0 in the list
                new_list.remove(0)  # remove all of them so that 0422 case won't have 0 in the middle after merge
            length = len(new_list)
            for num in range(4 - length):
                new_list.insert(0, 0)  # then insert 0 to the list in the front
            for item in range(4):
                self.grid[i][item] = new_list[item]  # assign the new sum item to actual grid in the appropriate place

# collapses the rows downwards and updates the grid and score
    def slideDown(self):
        self.changed = False  # check if there were tiles that can slid down if yes return true
        for i in range(0, 4):  # if not return false
            for j in range(1, 4):
                if self.grid[i][j - 1] == 0 and self.grid[i][j] != 0:
                    self.changed = True
                elif self.grid[i][j - 1] == self.grid[i][j] and self.grid[i][j - 1] != 0:
                    self.changed = True

        for i in range(4):  # created a new list and appended all the non zero values
            new_list = []  # in a column to it
            for j in range(4):
                if self.grid[i][j] != 0:
                    new_list.append(self.grid[i][j])

            for j in range(1, len(new_list), +1):  # checking from right to left of the list
                if new_list[j] == new_list[j - 1]:  # if the two items are the same
                    total = new_list[j] + new_list[j - 1]  # total is equal to the sum of the two
                    new_list[j - 1] = total  # and assign it to the left most valid spot for the sum in the list
                    self.setScore(total)  # the total is the new score and it adds to the current score
                    new_list[j] = 0  # everything else in the list should be replaced with 0
                    break
            if 0 in new_list:  # if there is 0 in the list
                new_list.remove(0)  # remove all of them so that 0422 case won't have 0 in the middle after merge
            length = len(new_list)
            for num in range(4 - length):
                new_list.append(0)  # then insert 0 to the list in the front
            for item in range(4):
                self.grid[i][item] = new_list[item]  # assign the new sum item to actual grid in the appropriate place


# End of Class Game2048

# main program to play the game with win/lose messages and entering prompt and generate random 2 or 4 after each input
Game = Game2048()
play_game = True
while play_game:
    Game.print()                               # print grid
    prompt = input('Enter direction: ')        # enter direction prompt
    if Game.win() and Game.first_win == 1:
        print('Congratulations! You win.')
        continue_after_win = input('Do you wish to continue playing?( y/n ): ')
        if continue_after_win == 'y':    # if the input is y, then player can continue even after winning
            play_game = True
        elif continue_after_win == 'n':     # if the input is n, then game ends
            play_game = False
    elif Game.getNbEmptyTiles() == 0 and Game.collapsible() == False:  # is the empty cell is 0 and can't be collapsed
        print('Sorry! Game Over. You lose.')                        # display sorry message and game ends
        play_game = False
    else:
        if prompt == 'exit':
            play_game = False
        elif prompt == 'w':                         # if the input is 'w', call slid up method
            Game.slideUp()
            if Game.changed:               # Check if game is collapsible or movable before adding in a new random int
                Game.RandomFillTile(Game.random2or4())  # and generate random 2 or 4
        elif prompt == 's':                 # if the input is 's', call slid down method
            Game.slideDown()
            if Game.changed:      # Check if game is collapsible or movable before adding in a new random int
                Game.RandomFillTile(Game.random2or4())          # and generate random 2 or 4
        elif prompt == 'a':                 # if the input is 'a', call slid left method
            Game.slideLeft()
            if Game.changed:               # Check if game is collapsible or movable before adding in a new random int
                Game.RandomFillTile(Game.random2or4())          # and generate random 2 or 4
        elif prompt == 'd':                     # if the input is 'd', call slid right method
            Game.slideRight()
            if Game.changed:              # Check if game is collapsible or movable before adding in a new random int
                Game.RandomFillTile(Game.random2or4())          # and generate random 2 or 4
        else:                                       # if input is not any of the above, then display 'invalid input'
            print('INVALID INPUT !')                # and the grid won't be change


















































































