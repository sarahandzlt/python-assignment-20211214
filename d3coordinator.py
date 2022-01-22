# import numpy as np
# p1 = np.array(0.0, 0.0, 0.0)
# p2 = np.array()
# class Star implements Cmaprable<Start> {
# double x, y, z;
# double distance() { return Math.sqrt(x*x + y*y + z*z); }
#  public int compareTo(Start that) {return Double.compare(this.distance(), that.distance());}
# }

# List<Star> findClosestKStars(Iterator<Star> starts, int k) {
# PriorityQueue<Star> maxHeap = new PriorityQueue<>(k, Collections.reverseOrder());
# while (stars.hasNext()) {
#   Star star = stars.next();
#  maxHeap.add(star);
# if (maxHeap.size() == k + 1) {
#    maxHeap.poll();
# }
# }
# return Stream.generate(maxHeap::peek).limit(maxHeap.size()).collect(Collectors.toList());
# }

import math


class Point(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def calculateDist(self):
        distance = math.sqrt(sum([self.x ** 2, self.y ** 2, self.z ** 2]))
        return distance

    def __str__(self):
        return 'Point ' + str(self.x) + " " + str(self.y) + " " + str(self.z)

    def state(self):
        return '({x},{y},{z})'.format(x=self.x, y=self.y, z=self.z)


from collections import deque


class FIFOFrontier(object):
    def __init__(self):
        self.queue_nodes = deque()
        self.queue_states = set()
        self.min = 0
        self.max = 0

    def push(self, node):
        if node.state not in self.queue_states:
            self.queue_nodes.append(node)
            self.queue_states.add(node.state)

    def pop(self):
        node = self.queue_nodes.popleft()
        self.queue_states.remove(node.state)
        return node

    def is_not_empty(self):
        return len(self.queue_nodes) > 0


class QuestionDomain(object):
    def __init__(self, goal: Point, inter_point_list=[]):
        self.goal = goal
        self.inter_points = inter_point_list

    def get_goal(self):
        return self.goal

    def get_list(self):
        return self.inter_points


def parse_lines(str):
    lines = str.splitlines()
    inter_point_list = []
    point_count = 0
    goal = None
    for i in range(len(lines)):
        if i == 0:
            goal = parse_single_point(lines[i])
        elif i == 1:
            point_count = int(lines[i])
        else:
            pt = parse_single_point(lines[i])
            inter_point_list.append(pt)

    return QuestionDomain(goal, inter_point_list)


def parse_single_point(line):
    points = line.split(" ")
    return Point(float(points[0]), float(points[1]), float(points[2]))


def remove_from_point_list(pointlist, node):
    for pt in pointlist:
        if node.state() == pt.state():
            pointlist.remove(pt)
    return pointlist


def calc_dist(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2 + (p1.z - p2.z) ** 2)


def search(domain):
    start = Point(0, 0, 0)
    goal = domain.get_goal()
    pointlist = domain.get_list()

    explored = {}
    explored[start.state()] = start
    frontier = FIFOFrontier()
    frontier.push(start)
    while frontier.is_not_empty():
        node = frontier.pop()

        if is_goal(node, goal):
            break

        current_dist = calc_dist(node, goal)
        explored[node.state()] = node
        pointlist = remove_from_point_list(pointlist, node)
        for child in pointlist:
            if child.state() in explored.keys():
                continue
            step_dist = calc_dist(child, goal)
            #保证迫近目标，必须下一步的距离Euclidean距离更短
            if current_dist < step_dist:
                continue
            frontier.push(child)

    explored[goal.state()] = goal

    nodes = []
    nodes.extend(explored.values())
    node_max = 0
    node_min = 9999999
    # calc the values
    for i in range(len(nodes) - 1):
        for j in range(i + 1, len(nodes)):
            p1 = nodes[i]
            p2 = nodes[j]
            distance = calc_dist(p1, p2)
            node_max = max(node_max, distance)
            node_min = min(node_min, distance)
    # 喜欢输出max还是min都可以
    print("max:{mx} min:{mn}".format(mx=node_max, mn=node_min))


def is_goal(x: Point, y: Point):
    if x.state() == y.state():
        return True
    return False


def main():
    lines = "2.00 2.00 2.00\n" \
            + "3\n" \
            + "0.00 0.00 2.00\n" \
            + "0.00 2.00 2.00\n" \
            + "2.00 0.00 0.00\n"

    domain = parse_lines(lines)

    search(domain)

    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# # p1 = Point(0,0,0)
# p2 = Point(2, 1, 0)
# # p3 = Point(0,2,0)
# # p4 = Point(0,0,2)
# print(p2)
# calculateDist()
# if__name__ == '__main__':
# main()

# while(1<=N<=2000):
# x1=float(input("输入第一点x坐标"))
# y1=float(input("输入第一点y坐标"))
# z1=float(input("输入第一点z坐标"))
# x2=float(input("输入第二点x坐标"))
# y2=float(input("输入第二点y坐标"))
# z2=float(input("输入第一点z坐标"))
# print(math.sqrt(sum([self.x**2, self.y**2,self.z**2])))
# print(math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2))
