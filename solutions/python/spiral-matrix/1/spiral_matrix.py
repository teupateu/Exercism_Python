def spiral_matrix(size):
    matrix = [[0 for _ in range(size)] for _ in range(size)] 
    num = 1
    move = 0 #A counter to keep track of where we are in the right-down-left-up sequence
    i = j = 0
    #Checking that we have not filled the matrix yet
    while num <= size ** 2:
        #Filling the matrix from left to right
        while move % 4 == 0:
            #If we reach the edge of the matrix or an already filled spot
            if j >= size or matrix[i][j] != 0:
                move += 1
                j -= 1
                i += 1
            else:
                matrix[i][j] = num
                j += 1
                num += 1
        #Filling the matrix from up to down
        while move % 4 == 1:
            if i >= size or matrix[i][j] != 0:
                move += 1
                i -= 1
                j -= 1
            else:
                matrix[i][j] = num
                i += 1
                num += 1
        #Filling the matrix from right to left
        while move % 4 == 2:
            if j < 0 or matrix[i][j] != 0:
                move += 1
                j += 1
                i -= 1
            else:
                matrix[i][j] = num
                j -= 1
                num += 1
        #Filling the matrix from down to up
        while move % 4 == 3:
            if i < 0 or matrix[i][j] != 0:
                move += 1
                i += 1
                j += 1
            else:
                matrix[i][j] = num
                i -= 1
                num += 1
    return matrix