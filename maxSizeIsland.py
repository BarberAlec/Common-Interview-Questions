import numpy as np

class Island:
    def __init__(self, mapp):
        self.ROWS = len(mapp)
        self.COLS = len(mapp[0])
        self.visited = np.array([[False]*8]*8)
        self.map = mapp

    def isSafe(self, i, j):
        if(i >= 0 and i < self.ROWS):
            if(j >= 0 and j < self.COLS):
                return not self.visited[i,j] and self.map[i,j] == 1
        return False

    def searchIsland(self, i, j):
        self.visited[i,j] = True
        count = 1
        dirX = [-1, -1, -1,  0, 0,  1, 1, 1]
        dirY = [-1,  0,  1, -1, 1, -1, 0, 1]

        for k in range(8):
            if self.isSafe(i+dirX[k], j+dirY[k]):
                count += self.searchIsland(i+dirX[k], j+dirY[k])
        return count

    def howIslandSearch(self):
        count = 0
        size_list = []


        for i in range(self.ROWS):
            for j in range(self.COLS):
                if not self.visited[i,j] and self.map[i,j] == 1:
                    #print(self.visited)
                    '''Found first bit of vigin land(new island)'''
                    count += 1
                    size_list.append(self.searchIsland(i, j))

        print("Number of Islands: " + str(count))
        print("Largest Island Size: " + str(max(size_list)))


new_map = np.array([[1, 0, 0, 1], [1, 0, 0, 0], [1, 0, 0, 0], [0, 1, 0, 1]])
isle = Island(mapp=new_map)
isle.howIslandSearch()
