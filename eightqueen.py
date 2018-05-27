class NQueens:
    def __init__(self,size):
        self.size = size
        self.solutions = 0
        self.solve()
        self.tmp = "tmp"

    def solve(self):
        positions = [-1]*self.size
        self.put_queen(positions,0)
        print self.tmp 
        print "There are " , self.solutions 


    def put_queen(self, positions, target_row):
        if target_row == self.size:
            self.tmp = self.show_last_board(positions)
            self.solutions += 1
        else:
            for column in range(self.size):
                if self.check_place(positions, target_row,column):
                    positions[target_row] = column 
                    self.put_queen(positions,target_row+1)

    def check_place(self, positions, ocuppied_rows, column):
        for i in range(ocuppied_rows):
            if positions[i] == column or positions[i]-i == column - ocuppied_rows or positions[i] + i == column + ocuppied_rows:
                return False
        return True


    def show_last_board(self,positions):
        lines = ""
        for row in range(self.size):
            line = ""
            for column in range(self.size):
                if positions[row] == column:
                    line += "Q "
                else:
                    line += ". "
            lines=lines+line+"\n"
        return lines

def main():
    NQueens(8)

if __name__ == "__main__":
    main()
