from LIFO import SStack
from random import randint

def Stack_KT(size, start): #size为整数，方形棋盘的边长;start由用户输入起始点
    value_matrix = [[0]*size for i in range(size)]  #给棋盘上的点赋值，越难走到的点的数值越大
    for i in range(1,size-1):
        value_matrix[1][i] += 1
        value_matrix[size-2][i] += 1
        value_matrix[i][1] += 1
        value_matrix[i][size-2] += 1
    for i in range(size):
        value_matrix[0][i] += 2
        value_matrix[size-1][i] += 2
        value_matrix[i][0] += 2
        value_matrix[i][size-1] += 2
    direction = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]

    def mark(matrix, pos):
        matrix[pos[0]][pos[1]] = 1
    def legal(pos):     #该位置是否是合法的，在棋盘上的位置
        return 0 <= pos[0]< size and 0 <= pos[1] < size
    def passable(matrix, pos):  #该点是否可以通行
        return matrix[pos[0]][pos[1]] == 0
    def print_path(stack):  #返回路径
        path = []
        while not stack.is_empty():
            path.append(stack.pop()[0])
        path.reverse()
        print(path)
        
    def next_step(pos): #返回到达难度从难到易的表
        def value(p):
            return value_matrix[p[0]][p[1]]
        lst = []
        for i in range(8):
            nextp = (pos[0]+direction[i][0], pos[1]+direction[i][1])
            if legal(nextp):
                lst.append(nextp)
        lst.sort(key=value, reverse=True) #降序,难度大的先走
        return lst

    st = SStack()
    chessboard = [[0]*size for i in range(size)]
    mark(chessboard, start)
    finished = 1    #记录棋盘已走过点的数量
    st.push((start, 0, next_step(start)))

    while not st.is_empty():
        found = 0    #记录检索是否找到，0代表无法前进，1代表存在走下一步的方案,每次循环都先把变量置0
        pos, nxt, direc_list= st.pop()
        for i in range(nxt, len(direc_list)): #搜寻下一个可到达的点
            nextp = (direc_list[i][0], direc_list[i][1])
            if passable(chessboard, nextp):
                finished += 1
                found = 1
                if finished == size * size:
                    print("Path Found")
                    st.push((pos, 0, direc_list))
                    st.push((nextp, 0, next_step(nextp)))
                    print_path(st)
                    return
                st.push((pos, i+1, direc_list))
                mark(chessboard, pos)
                st.push((nextp, 0, next_step(nextp)))
                break  #找到后，退出for循环
        if not found:    #if not found
            chessboard[pos[0]][pos[1]] = 0   #下标恢复
            finished -= 1       #到达状态减一
    print("No Path Found")

Stack_KT(8,(2,3))
