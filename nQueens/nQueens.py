import time

def generateNQueens(n):
	return [[' ' for i in range(n)]  for j in range(n)]

def printNQueens(lst):
    my_st = ''
    for i in range(len(lst)):
        my_st += '.'.join(lst[i])
	my_st += '\n'
    return my_st

def check_horizontal(lst,row):
	st = ''.join(lst[row]).replace(' ','')
	if len(st) > 0 :
		return False
	return True

def check_vertical(lst,column):
    for i in range(len(lst)):
        if lst[i][column] == 'Q':
            return False
    return True

def check_diagonal(lst,row,column):
    length = len(lst)
    for i in range(length):
        if row - i >= 0:
            if column - i >= 0:
                if lst[row - i][column - i] == 'Q': return False
            if column + i < length:
                if lst[row - i][column + i] == 'Q':return False
        if row + i < length:
            if column - i >= 0:
                if lst[row + i][column - i] == 'Q': return False
            if column + i < length:
                if lst[row + i][column + i] == 'Q':return False
    return True

def check_NQueen(lst,row,column):
    if check_horizontal(lst,row) and check_vertical(lst,column) and check_diagonal(lst,row,column):
        return True
    return False


def NQueen_recur(lst,column):
    global counter
    for i in range(len(lst)):
        if check_NQueen(lst,i,column):
            #print printNQueens(lst)
	    #time.sleep(1)
            lst[i][column] = 'Q'
            if column == len(lst)-1:
		counter += 1
		Queen_Graph[counter] =  str(printNQueens(lst))
		lst[i][column] = ' '
            if column+1 < len(lst):
                track = NQueen_recur(lst,column+1)
            	if track == None:
                	lst[i][column] = ' '
    return None

def All_NQueens(Queen_Graph):
	for i in range(1,len(Queen_Graph)+1):
		print i
		print Queen_Graph[i]
		print '-'*100

lst = generateNQueens(int(raw_input("Type the value of N for NQueens : ")))
temp_lst = lst[:][:]
counter  = 0
Queen_Graph = {}
NQueen_recur(lst,0)
All_NQueens(Queen_Graph)
