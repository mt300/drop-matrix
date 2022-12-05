import numpy as np
import random
import sys
np.set_printoptions(threshold=sys.maxsize)


def move_action(x,y):
    # 0 - up / 1 - right / 2 - down / 3 - left
    direction = random.randint(0,3)
    if(direction == 0):
        return (x,y-1)
    elif(direction == 1):
        return (x+1,y)
    elif(direction == 2):
        return (x,y+1)
    elif(direction == 3):
        return (x-1,y)
    else:
        print("error")
        return False

def check_neighbors(x,y,matrix):
    if( x == 0 ):
        if(y == 0):
            if( matrix[y][x+1] or matrix[y+1][x] or matrix[y+1][x+1]):
                return True 
            else:
                return False    
        elif( y == matrix.shape[1]):
            if( matrix[y-1][x] or matrix[y-1][x+1]  or  matrix[y][x+1]):
                return True 
            else:
                return False
        else:    
            if( matrix[y-1][x] or matrix[y-1][x+1]  or  matrix[y][x+1] or matrix[y+1][x] or matrix[y+1][x+1]):
                return True 
            else:
                return False

    elif( x == (matrix.shape[0] - 1)):
        if( y == 0):
            if(matrix[y][x-1] or matrix[y+1][x-1] or matrix[y+1][x]):
                return True 
            else:
                return False    
        elif( y == matrix.shape[1]):
            if(matrix[y-1][x-1] or matrix[y-1][x]  or matrix[y][x-1]):
                return True 
            else:
                return False 
        else:   
            if(matrix[y-1][x-1] or matrix[y-1][x]  or matrix[y][x-1] or matrix[y+1][x-1] or matrix[y+1][x]):
                return True 
            else:
                return False    
    elif( y == 0):
        if( matrix[y][x-1] or  matrix[y][x+1] or matrix[y+1][x-1] or matrix[y+1][x] or matrix[y+1][x+1]):
            return True 
        else:
            return False
    elif( y == (matrix.shape[1] - 1)):
        if(matrix[y-1][x-1] or matrix[y-1][x] or matrix[y-1][x+1] or matrix[y][x-1] or  matrix[y][x+1]):
            return True 
        else:
            return False 
    else:
        if(matrix[y-1][x-1] or matrix[y-1][x] or matrix[y-1][x+1] or matrix[y][x-1] or  matrix[y][x+1] or matrix[y+1][x-1] or matrix[y+1][x] or matrix[y+1][x+1]):
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
        # print(matrix)
        move = True
        while (move ==  True):
            next_pos = move_action(start_x,start_y)
            
            if(next_pos[0] < 0 or next_pos[1] < 0):
                print("Aqui", next_pos)
                destroy += 1
                move = False

            if(next_pos[0] >= wid or next_pos[1] >= hig):
                print("ou aqui", next_pos)
                destroy += 1
                move = False
            else:
                matrix[start_y][start_x] = 0
                matrix[next_pos[1]][next_pos[0]] = 1
                start_x = next_pos[0]
                start_y = next_pos[1]
                if(check_neighbors(next_pos[1],next_pos[0],matrix) == True):
                    move = False
            # print(matrix)

            # move = False
    print(matrix)
    print(seeds_number, seeds_distance)
    print( "Drops destroyeds: ", destroy)
ald(1000,1000,1,10000)