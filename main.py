import numpy as np
import random
import sys
np.set_printoptions(threshold=sys.maxsize)


def move_action(y,x):
    # 0 - up / 1 - right / 2 - down / 3 - left
    direction = random.randint(0,2)
    if(direction == 0):
        # print("Same position")
        return (y,x-1)
    elif(direction == 1):
        return (y,x+1)
    elif(direction == 2):
        return (y+1,x)
    else:
        # print("error")
        return (y,x)

def check_neighbors(y,x,matrix):
    if( x == 0 ):
        # print("aqui x==0")
        if(y == 0):
            if( matrix[y][x+1]==1 or matrix[y+1][x]==1 or matrix[y+1][x+1]==1):
                return True 
            else:
                return False    
        elif( y == (matrix.shape[0] - 1)):
            if( matrix[y-1][x]==1 or matrix[y-1][x+1]==1  or  matrix[y][x+1]==1):
                return True 
            else:
                return False
        else:    
            if( matrix[y-1][x]==1 or matrix[y-1][x+1]==1  or  matrix[y][x+1]==1 or matrix[y+1][x]==1 or matrix[y+1][x+1]==1):
                return True 
            else:
                return False

    elif( x == (matrix.shape[1] - 1)):
        # print("aqui x==MAX")
        if( y == 0):
            if(matrix[y][x-1]==1 or matrix[y+1][x-1]==1 or matrix[y+1][x]==1):
                return True 
            else:
                return False    
        elif( y == (matrix.shape[0] - 1)):
            if(matrix[y-1][x-1]==1 or matrix[y-1][x]==1  or matrix[y][x-1]==1):
                return True 
            else:
                return False 
        else:   
            if(matrix[y-1][x-1]==1 or matrix[y-1][x]==1  or matrix[y][x-1]==1 or matrix[y+1][x-1]==1 or matrix[y+1][x]==1):
                return True 
            else:
                return False    
    elif( y == 0):
        # print("aqui y==0")
        if( matrix[y][x-1]==1 or  matrix[y][x+1]==1 or matrix[y+1][x-1]==1 or matrix[y+1][x]==1 or matrix[y+1][x+1]==1):
            return True 
        else:
            return False
    elif( y == (matrix.shape[0] - 1)):
        # print("aqui y==MAX")
        if(matrix[y-1][x-1]==1 or matrix[y-1][x]==1 or matrix[y-1][x+1]==1 or matrix[y][x-1]==1 or  matrix[y][x+1]==1):
            return True 
        else:
            return False 
    else:
        if(matrix[y-1][x-1]==1 or matrix[y-1][x]==1 or matrix[y-1][x+1]==1 or matrix[y][x-1]==1 or  matrix[y][x+1]==1 or matrix[y+1][x-1]==1 or matrix[y+1][x]==1 or matrix[y+1][x+1]==1):
            # print("None")
            return True 
        else:
            return False    

    
def ald(hig,wid,concurrent_drops,max_drops):
    matrix = np.zeros((hig,wid))
    seeds_number = int(hig/10)
    destroy = 0
    if(seeds_number > (wid - 2)):
        print("Invalid inputs. Width is not large enough\n")
        return False
    seeds_distance = int((wid-2)/seeds_number)
    for s in range(0,seeds_number):
        matrix[hig-1][1 + seeds_distance * s] = 1
    for i in range(0,int(max_drops/concurrent_drops)):
        start_x = random.randint(0,(wid-1))
        start_y = 0
        matrix[start_y][start_x] = 1
        print(matrix)
        move = True
        while (move ==  True):
            next_pos = move_action(start_y,start_x)
            matrix[start_y][start_x] = 0
            if(next_pos[0] < 0 or next_pos[1] < 0):
                # print("Aqui", next_pos)
                destroy += 1
                move = False

            elif(next_pos[0] >= hig or next_pos[1] >= wid):
                # print("ou aqui", next_pos)
                destroy += 1
                move = False
            elif(check_neighbors(next_pos[0],next_pos[1],matrix) == True):
                move = False
                matrix[next_pos[0]][next_pos[1]] = 1
                start_y = next_pos[0]
                start_x = next_pos[1]
                # print("Turning seed: ", next_pos)
            else:
                matrix[next_pos[0]][next_pos[1]] = 1
                start_y = next_pos[0]
                start_x = next_pos[1]
                # print("seguiu para: ", next_pos)
                
            print(matrix)

            # move = False
    # print(matrix)
    # print(seeds_number, seeds_distance)
    print( "Drops destroyeds: ", destroy)
ald(30,24,1,1000)