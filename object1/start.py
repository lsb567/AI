points = [(0, 0), (34, 213), (75, 170), (75, 285), (60, 355), (34, 470), (160, 570), (240, 320), (240, 472), (190, 490), (340, 320),
          (440, 280), (440, 170), (460, 225), (425, 380), (340, 430), (340, 570), (530, 290), (505, 345), (425, 575), (485, 520),
          (585, 205), (650, 170), (585, 285), (505, 570), (720, 200), (720, 285), (660, 335), (650, 345), (650, 570), (665, 540),
          (735, 320), (715, 570), (755, 530), (775, 565)]

dd = float('inf')
Adj = [[float('inf') for i in range(35)] for j in range(35)]  # 初始化邻接矩阵
for i in range(35):  # A[i][i]=0 ：每个顶点和自身没有边
    Adj[i][i] = 0
# 边
Adj[1][2] = Adj[2][1] = int(pow(pow(points[1][0]-points[2][0], 2) + pow(points[1][1]-points[2][1], 2), 0.5))
Adj[1][3] = Adj[3][1] = int(pow(pow(points[1][0]-points[3][0], 2) + pow(points[1][1]-points[3][1], 2), 0.5))
Adj[3][10] = Adj[10][3] = int(pow(pow(points[3][0]-points[10][0], 2) + pow(points[3][1]-points[10][1], 2), 0.5))
Adj[10][14] = Adj[14][10] = int(pow(pow(points[10][0]-points[14][0], 2) + pow(points[10][1]-points[14][1], 2), 0.5))
Adj[14][20] = Adj[20][14] = int(pow(pow(points[14][0]-points[20][0], 2) + pow(points[14][1]-points[20][1], 2), 0.5))
Adj[20][24] = Adj[24][20] = int(pow(pow(points[20][0]-points[24][0], 2) + pow(points[20][1]-points[24][1], 2), 0.5))
Adj[24][29] = Adj[29][24] = int(pow(pow(points[24][0]-points[29][0], 2) + pow(points[24][1]-points[29][1], 2), 0.5))
Adj[29][32] = Adj[32][29] = int(pow(pow(points[29][0]-points[32][0], 2) + pow(points[29][1]-points[32][1], 2), 0.5))
Adj[32][34] = Adj[34][32] = int(pow(pow(points[32][0]-points[34][0], 2) + pow(points[32][1]-points[34][1], 2), 0.5))
Adj[14][18] = Adj[18][14] = int(pow(pow(points[14][0]-points[18][0], 2) + pow(points[14][1]-points[18][1], 2), 0.5))
Adj[18][28] = Adj[28][18] = int(pow(pow(points[18][0]-points[28][0], 2) + pow(points[18][1]-points[28][1], 2), 0.5))
Adj[28][30] = Adj[30][28] = int(pow(pow(points[28][0]-points[30][0], 2) + pow(points[28][1]-points[30][1], 2), 0.5))
Adj[30][32] = Adj[32][30] = int(pow(pow(points[30][0]-points[32][0], 2) + pow(points[30][1]-points[32][1], 2), 0.5))
Adj[2][12] = Adj[12][2] = int(pow(pow(points[2][0]-points[12][0], 2) + pow(points[2][1]-points[12][1], 2), 0.5))
Adj[12][23] = Adj[23][12] = int(pow(pow(points[12][0]-points[23][0], 2) + pow(points[12][1]-points[23][1], 2), 0.5))
Adj[23][27] = Adj[27][23] = int(pow(pow(points[23][0]-points[27][0], 2) + pow(points[23][1]-points[27][1], 2), 0.5))
Adj[27][30] = Adj[30][27] = int(pow(pow(points[27][0]-points[30][0], 2) + pow(points[27][1]-points[30][1], 2), 0.5))
Adj[27][31] = Adj[31][27] = int(pow(pow(points[27][0]-points[31][0], 2) + pow(points[27][1]-points[31][1], 2), 0.5))
Adj[31][33] = Adj[33][31] = int(pow(pow(points[31][0]-points[33][0], 2) + pow(points[31][1]-points[33][1], 2), 0.5))
Adj[33][34] = Adj[34][33] = int(pow(pow(points[33][0]-points[34][0], 2) + pow(points[33][1]-points[34][1], 2), 0.5))
Adj[12][28] = Adj[28][12] = int(pow(pow(points[12][0]-points[28][0], 2) + pow(points[12][1]-points[28][1], 2), 0.5))
if __name__ == '__main__':
    print(points[1][0])
    print(points[23][1] < dd)
    print(Adj)