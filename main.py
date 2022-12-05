import numpy as np
import random
import sys
np.set_printoptions(threshold=sys.maxsize)


# Funcao que gera o movimento da particula. Recebe coordenadas atuais e retorna tupla da coordenada final da gota
def move_action(y,x):
    # 0 - up / 1 - right / 2 - down / 3 - left
    direction = random.randint(0,3)
    if(direction == 0):
        # print("Same position")
        return (y+1,x)
    elif(direction == 1):
        return (y,x+1)
    elif(direction == 2):
        return (y+1,x)
    elif(direction == 3):
        return (y,x-1)
    else:
        # No caso de um valor invalido retorna as coordenadas atuais
        return (y,x)

# Funcao para checar os vizinhos da gota. Levando em conta a sua posição atual
# recebe as coordenadas atuais e a matriz e retorna True se houverem vizinhos e False se nao houverem
def check_neighbors(y,x,matrix):
    if( x == 0 ):
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
        if( matrix[y][x-1]==1 or  matrix[y][x+1]==1 or matrix[y+1][x-1]==1 or matrix[y+1][x]==1 or matrix[y+1][x+1]==1):
            return True 
        else:
            return False
    elif( y == (matrix.shape[0] - 1)):
        if(matrix[y-1][x-1]==1 or matrix[y-1][x]==1 or matrix[y-1][x+1]==1 or matrix[y][x-1]==1 or  matrix[y][x+1]==1):
            return True 
        else:
            return False 
    else:
        if(matrix[y-1][x-1]==1 or matrix[y-1][x]==1 or matrix[y-1][x+1]==1 or matrix[y][x-1]==1 or  matrix[y][x+1]==1 or matrix[y+1][x-1]==1 or matrix[y+1][x]==1 or matrix[y+1][x+1]==1):
            return True 
        else:
            return False    

# Funcao ald para geração de clusters a partir de gotas com movimento aleatorio
# Recebe altura e largura da matriz, a quantidade de gotas simultaneas e o maximo de gotas geradas
# Imprime a matriz final e gera um arquivo matrix.txt com o resultado
def ald(hig,wid,concurrent_drops,max_drops):
    #condicoes iniciais
    matrix = np.zeros((hig,wid))
    seeds_number = int(hig/10)
    destroy = 0
    #distribuindo seeds
    if(seeds_number > (wid - 2)):
        print("Invalid inputs. Width is not large enough\n")
        return False
    seeds_distance = int((wid-2)/seeds_number)
    for s in range(0,seeds_number):
        matrix[hig-1][1 + seeds_distance * s] = 1
    #iterando sobre as gotas
    for i in range(0,max_drops):
        start_x = random.randint(0,(wid-1))
        start_y = 0
        matrix[start_y][start_x] = 1
        move = True
        # movimentando cada gota
        while (move ==  True):
            next_pos = move_action(start_y,start_x)
            matrix[start_y][start_x] = 0
            if(next_pos[0] < 0 or next_pos[1] < 0):
                destroy += 1
                move = False

            elif(next_pos[0] >= hig or next_pos[1] >= wid):
                
                destroy += 1
                move = False
            elif(check_neighbors(next_pos[0],next_pos[1],matrix) == True):
                move = False
                matrix[next_pos[0]][next_pos[1]] = 1
                start_y = next_pos[0]
                start_x = next_pos[1]
            else:
                matrix[next_pos[0]][next_pos[1]] = 1
                start_y = next_pos[0]
                start_x = next_pos[1]
                
    print(matrix)
    np.savetxt("matrix.txt",matrix)
ald(30,24,1,1000)