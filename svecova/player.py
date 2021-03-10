import random

PATTERNS = [
    ( 1000000000, 'xxxxx'),
    (-1000000000, 'ooooo'),
    ( 10000000, ' xxxx '),
    (-10000000, ' oooo '),
    ( 7000000, 'xoooox'),
    (-7000000, 'oxxxxo'),
    ( 5000000, 'xxxx '),
    (-5000000, 'oooo '),
    ( 5000000, ' xxxx'),
    (-5000000, ' oooo'),
    ( 2000000, 'x xxx'),
    (-2000000, 'o ooo'),
    ( 2000000, 'xxx x'),
    (-2000000, 'ooo o'),
    ( 1000000, 'xx xx'),
    (-1000000, 'oo oo'),
    ( 200000, 'xooo'),
    (-200000, 'oxxx'),
    ( 200000, 'oxoo'),
    (-200000, 'xoxx'),
    ( 100000, 'xooo x'),
    (-100000, 'oxxx o'),
    ( 100000, '  xxx  '),
    (-100000, '  ooo  '),
    ( 50000, 'xxx  '),
    (-50000, 'ooo  '),
    ( 50000, ' xxx '),
    (-50000, ' ooo '),
    ( 50000, '  xxx'),
    (-50000, '  ooo'),
    ( 20000, ' x xx '),
    (-20000, ' o oo '),
    ( 20000, ' xx x '),
    (-20000, ' oo o '),
    ( 10000, 'x xx '),
    (-10000, 'o oo '),
    ( 10000, 'xx x '),
    (-10000, 'oo o '),
    ( 10000, ' x xx'),
    (-10000, ' o oo'),
    ( 10000, ' xx x'),
    (-10000, ' oo o'),
    ( 1000, 'xoo  x'),
    (-1000, 'oxx  o'),
    ( 1000, 'x oo x'),
    (-1000, 'o xx o'),
    ( 1000, 'x  oox'),
    (-1000, 'o  xxo'),
    ( 1000, '   xx   '),
    (-1000, '   oo   '),
    ( 500, 'xx   '),
    (-500, 'oo   '),
    ( 500, ' xx  '),
    (-500, ' oo  '),
    ( 500, '  xx '),
    (-500, '  oo '),
    ( 500, '   xx'),
    (-500, '   oo'),
    ( 200, '  x x  '),
    (-200, '  o o  '),
    ( 10, '       x       '),
    (-10, '       o       '),
    ( 9, '      x      '),
    (-9, '      o      '),
   
]
class Board:
    SIZE = 15

    def generate_rows(self):
        rows = []
        for i in range(self.SIZE):
            row = []
            for j in range(self.SIZE):
                row.append(0)
            rows.append(row)
        return rows

    def generate_diagonals(self):
        diagonals = []
        delka = 1
        for i in range(self.SIZE):
            diagonal = []
            for j in range(delka):
                diagonal.append(0)
            diagonals.append(diagonal)
            delka += 1
        delka = 14
        for i in range(self.SIZE - 1):
            diagonal = []
            for j in range(delka):
                diagonal.append(0)
            diagonals.append(diagonal)
            delka -= 1
        return diagonals

    def __init__(self):
        self.rows = self.generate_rows()
        self.columns = self.generate_rows()
        self.diagonals_descending = self.generate_diagonals()
        self.diagonals_ascending = self.generate_diagonals()

    def row_to_string(self, row):
        output = ''
        for i in row:
            if (i == 0):
                output += ' '
            if (i == 1):
                output += 'x'
            if (i == -1):
                output += 'o'
        return output
        
    def evaluate_row(self, row):
        string_row = self.row_to_string(row)
        total_score = 0
        for pattern in PATTERNS:
            score, p = pattern
            if p in string_row:
                #print(f'found pattern {p} in {row}')
                total_score += score
                #total_score = total_score + score
        return total_score

    def evaluate_position(self):
        total_score = 0
        for row in self.rows:
            total_score += self.evaluate_row(row)
        for column in self.columns:
            total_score += self.evaluate_row(column)
        for di_des in self.diagonals_descending:
            total_score += self.evaluate_row(di_des)
        for di_asc in self.diagonals_ascending:
            total_score += self.evaluate_row(di_asc)
        return total_score

    def new_turn(self, row, column, player):
        self.rows[row][column] = player
        self.columns[column][row] = player
        ascending_diagonal_number = row + column
        if (row + column < self.SIZE):
            self.diagonals_ascending[ascending_diagonal_number][column] = player
        else:
            self.diagonals_ascending[ascending_diagonal_number][self.SIZE - 1 - row] = player
        descending_diagonal_number = self.SIZE - 1 - row + column
        if (descending_diagonal_number < 15):
            self.diagonals_descending[descending_diagonal_number][column] = player
        else:
            self.diagonals_descending[descending_diagonal_number][row] = player
        #self.print_all()

    def is_close_to_others(self, row, column):
        if column > 0 and self.rows[row][column - 1] != 0: return True
        if column > 0 and row > 0 and self.rows[row - 1][column - 1] != 0: return True
        if row > 0 and self.rows[row - 1][column] != 0: return True
        if column < 14 and self.rows[row][column + 1] != 0: return True
        if column < 14 and row < 14 and self.rows[row + 1][column + 1] != 0: return True
        if row < 14 and self.rows[row + 1][column] != 0: return True
        if column > 1 and self.rows[row][column - 2] != 0: return True
        if column > 1 and row > 1 and self.rows[row - 2][column - 2] != 0: return True
        if row > 1 and self.rows[row - 2][column] != 0: return True
        if column < 13 and self.rows[row][column + 2] != 0: return True
        if column < 13 and row < 13 and self.rows[row + 2][column + 2] != 0: return True
        if row < 13 and self.rows[row + 2][column] != 0: return True
        return False

    def get(self, row, col):
        return self.rows[row][col]

    def print_all(self):
        print('rows')
        for row in self.rows:
            print(row)
        print('cols')
        for col in self.columns:
            print(col)
        print('desc')
        for d in self.diagonals_descending:
            print(d)
        print('asc')
        for d in self.diagonals_ascending:
            print(d)

class Player:
    def __init__(self, player_sign):
        self.sign = 1
        self.opponent_sign = -1
        self.name = 'Hana Svecova'
        self.board = Board()
        random.seed(17)

    def pick_random_valid_turn(self):
        while True:
            row = random.randint(0, 14)
            col = random.randint(0, 14)
            if (self.board.get(row, col) == 0): return (row, col)

    def pick_best_opponent_turn(self):
        best_score = float('inf')
        best_turn = None
        for row in range(15):
            for col in range(15):
                if (self.board.get(row, col) != 0): continue                # pokud je místo prázdné
                if (not self.board.is_close_to_others(row, col)): continue
                self.board.new_turn(row, col, self.opponent_sign)            # zkusí dosadit na každé místo -1
                score = self.board.evaluate_position()                       # vypočítá score
                if score < best_score:
                    best_turn = (row, col)
                    best_score = score
                self.board.new_turn(row, col, 0)  # vrátí do tabulky opět 0
        print (best_turn)
        print (best_score)
        return best_turn

    def pick_best_turn(self):
        best_score = -float('inf')
        best_turn = None
        for row in range(15):
            for col in range(15):
                if (self.board.get(row, col) != 0): continue
                if (not self.board.is_close_to_others(row, col)): continue
                self.board.new_turn(row, col, self.sign)
                #op_row, op_col = self.pick_best_opponent_turn()
                #self.board.new_turn(op_row, op_col, self.opponent_sign) # zapsat do tabulky protihráčův tah
                score = self.board.evaluate_position()
                if score > best_score:
                    best_turn = (row, col)
                    best_score = score
                #self.board.new_turn(op_row, op_col, 0)
                self.board.new_turn(row, col, 0)
        print (best_score)
        return best_turn

    def play(self, opponent_move):
        if opponent_move != None:
            row, col = opponent_move
            self.board.new_turn(row, col, self.opponent_sign)
            
        #my_turn_row, my_turn_col = self.pick_random_valid_turn()
        my_turn_row, my_turn_col = self.pick_best_turn()
        self.board.new_turn(my_turn_row, my_turn_col, self.sign)
        return my_turn_row, my_turn_col
