'''
输入：地图的大小、起始点、终点

输出:路径序列、路径图片
'''
import sys, os
sys.path.append(os.path.abspath(os.path.join(__file__, "../../../")))
from utils import Grid, Map, SearchFactory

def planning_with_A_star(my_map, start, goal):
    env = Grid(my_map[0],my_map[1])
    search = SearchFactory()
    planner = search("a_star", start=start, goal=goal, env=env)
    return planner.run()

if __name__ == '__main__':
    my_map = eval(input())
    start = eval(input())
    goal = eval(input())
    
    path = planning_with_A_star(my_map, start, goal)
    path.reverse()
    print(path)