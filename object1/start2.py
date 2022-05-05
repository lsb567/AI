# 点对应状态，边对应行为

from sqlalchemy import intersect
from queue import PriorityQueue

points = [(0, 0), (34, 113), (75, 170), (75, 285), (60, 355), (34, 470), (160, 570), (240, 320), (240, 472), (190, 490),
          (340, 320), (440, 280), (440, 170), (460, 225), (425, 380), (340, 430), (340, 570), (530, 290), (505, 345),
          (425, 575), (485, 520), (585, 205), (650, 170), (585, 285), (505, 570), (720, 200), (720, 285), (660, 335),
          (650, 345), (650, 570), (665, 540), (735, 320), (715, 570), (755, 530), (775, 565)]

dd = float('inf')
Adj = [[float('inf') for i in range(35)] for j in range(35)]  # 初始化邻接矩阵
for i in range(35):  # A[i][i]=0 ：每个顶点和自身没有边
    Adj[i][i] = 0
# 边
Adj[1][2] = Adj[2][1] = int(pow(pow(points[1][0] - points[2][0], 2) + pow(points[1][1] - points[2][1], 2), 0.5))
Adj[1][3] = Adj[3][1] = int(pow(pow(points[1][0] - points[3][0], 2) + pow(points[1][1] - points[3][1], 2), 0.5))
Adj[3][10] = Adj[10][3] = int(pow(pow(points[3][0] - points[10][0], 2) + pow(points[3][1] - points[10][1], 2), 0.5))
Adj[10][14] = Adj[14][10] = int(pow(pow(points[10][0] - points[14][0], 2) + pow(points[10][1] - points[14][1], 2), 0.5))
Adj[14][20] = Adj[20][14] = int(pow(pow(points[14][0] - points[20][0], 2) + pow(points[14][1] - points[20][1], 2), 0.5))
Adj[20][24] = Adj[24][20] = int(pow(pow(points[20][0] - points[24][0], 2) + pow(points[20][1] - points[24][1], 2), 0.5))
Adj[24][29] = Adj[29][24] = int(pow(pow(points[24][0] - points[29][0], 2) + pow(points[24][1] - points[29][1], 2), 0.5))
Adj[29][32] = Adj[32][29] = int(pow(pow(points[29][0] - points[32][0], 2) + pow(points[29][1] - points[32][1], 2), 0.5))
Adj[32][34] = Adj[34][32] = int(pow(pow(points[32][0] - points[34][0], 2) + pow(points[32][1] - points[34][1], 2), 0.5))
Adj[14][18] = Adj[18][14] = int(pow(pow(points[14][0] - points[18][0], 2) + pow(points[14][1] - points[18][1], 2), 0.5))
Adj[18][28] = Adj[28][18] = int(pow(pow(points[18][0] - points[28][0], 2) + pow(points[18][1] - points[28][1], 2), 0.5))
Adj[28][30] = Adj[30][28] = int(pow(pow(points[28][0] - points[30][0], 2) + pow(points[28][1] - points[30][1], 2), 0.5))
Adj[30][32] = Adj[32][30] = int(pow(pow(points[30][0] - points[32][0], 2) + pow(points[30][1] - points[32][1], 2), 0.5))
Adj[2][12] = Adj[12][2] = int(pow(pow(points[2][0] - points[12][0], 2) + pow(points[2][1] - points[12][1], 2), 0.5))
Adj[12][23] = Adj[23][12] = int(pow(pow(points[12][0] - points[23][0], 2) + pow(points[12][1] - points[23][1], 2), 0.5))
Adj[23][27] = Adj[27][23] = int(pow(pow(points[23][0] - points[27][0], 2) + pow(points[23][1] - points[27][1], 2), 0.5))
Adj[27][30] = Adj[30][27] = int(pow(pow(points[27][0] - points[30][0], 2) + pow(points[27][1] - points[30][1], 2), 0.5))
Adj[27][31] = Adj[31][27] = int(pow(pow(points[27][0] - points[31][0], 2) + pow(points[27][1] - points[31][1], 2), 0.5))
Adj[31][33] = Adj[33][31] = int(pow(pow(points[31][0] - points[33][0], 2) + pow(points[31][1] - points[33][1], 2), 0.5))
Adj[33][34] = Adj[34][33] = int(pow(pow(points[33][0] - points[34][0], 2) + pow(points[33][1] - points[34][1], 2), 0.5))
Adj[12][28] = Adj[28][12] = int(pow(pow(points[12][0] - points[28][0], 2) + pow(points[12][1] - points[28][1], 2), 0.5))
Adj[1][12] = Adj[12][1] = int(pow(pow(points[1][0] - points[12][0], 2) + pow(points[1][1] - points[12][1], 2), 0.5))
Adj[12][13] = Adj[13][12] = int(pow(pow(points[12][0] - points[13][0], 2) + pow(points[12][1] - points[13][1], 2), 0.5))
Adj[13][17] = Adj[17][13] = int(pow(pow(points[13][0] - points[17][0], 2) + pow(points[13][1] - points[17][1], 2), 0.5))
Adj[17][28] = Adj[28][17] = int(pow(pow(points[17][0] - points[28][0], 2) + pow(points[17][1] - points[28][1], 2), 0.5))
Adj[28][31] = Adj[31][28] = int(pow(pow(points[28][0] - points[31][0], 2) + pow(points[28][1] - points[31][1], 2), 0.5))
Adj[23][27] = Adj[27][23] = int(pow(pow(points[23][0] - points[27][0], 2) + pow(points[23][1] - points[27][1], 2), 0.5))
Adj[27][31] = Adj[31][27] = int(pow(pow(points[27][0] - points[31][0], 2) + pow(points[27][1] - points[31][1], 2), 0.5))
Adj[12][28] = Adj[28][12] = int(pow(pow(points[12][0] - points[28][0], 2) + pow(points[12][1] - points[28][1], 2), 0.5))

class Problem():
    def __init__(self, points, Adj, start, goal):
        self.Adj = Adj  # 记录邻接矩阵备用
        self.Points = points  # 记录每个顶点坐标备用
        self.InitialState = start  # 起始状态
        self.GoalState = goal  # 目标状态

    def GoalTest(self, state):  # 测试是否达到目标
        if state == self.GoalState:
            return True

    def Action(self, state):  # 获取某状态下的行为集合
        states = []
        for i in range(state + 1, 35):
            if Adj[state][i] != float('inf'):
                states.append(i)
        return states

    def Result(self, state, action):  # 获取在某状态下采取某行为后的新状态
        return action

    def StepCost(self, state, action):  # 获取在某状态下采取某行为需要的费用
        return Adj[state][action]


class Node():
    def __init__(self, problem, parent=None, action=None):
        if parent is None:
            self.State = problem.InitialState
            self.Parent = None
            self.Action = None
            self.PathCost = 0
        else:
            self.State = problem.Result(parent.State, action)  # 子节点
            self.Parent = parent  # 生成此节点的父亲节点
            self.Action = action  # 生成此节点的行为
            self.PathCost = parent.PathCost + problem.StepCost(parent.State, action)  # 到此节点路径长度
        self.g = self.PathCost  # g信息
        self.h = distance(problem.Points[self.State], problem.Points[problem.GoalState])  # h信息  # 没有distance方法
        self.f = self.g + self.h  # f信息

    def __lt__(self, other):  # 优先队列判别条件
            return other.f > self.f


def distance(a, b):
    return int(pow(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2), 0.5))


def Solution(node):  # 从node的定义可知，根据node.parent可以回溯出整个解决方案所到达 的state和相应的action序列，因此可设计一个函数Solution(node)获得这些序列。
    res = []
    while node:
        res.append(node.State)
        node = node.Parent
    return res[::-1]


def Astar(problem):
    node = Node(problem)  # 起始节点
    if problem.GoalTest(node.State):
        return Solution(node)
    frontier = PriorityQueue()  # frontier:前沿; PriorityQueue():是一个优先队列，f值最小的节点将优先被探索
    frontier.put(node)  # 第一个节点进入
    explored = set()  # 存储正在或者已经探索的状态
    while frontier.qsize() > 0:  # qsize()：队列尺寸
        node = frontier.get()  # 取出前沿中的节点，前沿大小减一
        explored.add(node.State)  # 记录探索过的状态
        for action in problem.Action(node.State):  # 遍历对可采取的行为
            child = Node(problem, node, action)  # 生成子节点
            if child.State not in explored:
                if problem.GoalTest(child.State):  # 发现目标状态
                    return Solution(child)
                frontier.put(child)  # 子节点进入前沿
                explored.add(child.State)  # 前沿中的节点状态也要记录


if __name__ == '__main__':
    problem = Problem(points, Adj, 1, 34)
    res = Astar(problem)
    print(res)
