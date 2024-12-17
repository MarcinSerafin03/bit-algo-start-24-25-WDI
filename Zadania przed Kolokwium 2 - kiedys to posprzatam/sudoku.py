def sudoku(T):
    def search_bad(T):
        for i in range(9):
            for j in range(9):
                for k in range(j,9):
                    if T[i][j]==T[i][k]:
                        return False
                    if T[j][i]==T[k][i]:
                        return False
        return True
    def swap_squares(T,y1,x1,y2,x2):
        for i in range(3):
            for j in range(3):
                T[y1*3+i][x1*3+j],T[y2*3+i][x2*3+j]=T[y2*3+i][x2*3+j],T[y1*3+i][x1*3+j]
    for y1 in range(3):
        for x1 in range(3):
            for y2 in range(3):
                for x2 in range(3):
                    swap_squares(T,y1,x1,y2,x2)
                    if search_bad(T):
                        return (y1*3+x1,y2*3+x2)
                    
T=[[8,1,2,7,5,3,6,4,9],
  [9,4,3,6,8,2,1,7,5],
  [6,7,5,4,9,1,2,8,3],
  [1,5,4,3,6,8,8,9,6],
  [3,6,9,9,1,7,7,2,1],
  [2,8,7,4,5,2,5,3,4],
  [5,2,1,9,7,4,2,3,7],
  [4,3,8,5,2,6,8,4,5],
  [7,9,6,3,1,8,1,6,9]]

print(sudoku(T))
    

