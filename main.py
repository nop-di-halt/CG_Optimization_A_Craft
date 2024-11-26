import sys
import math
import numpy as np
from map import Map
from robot import Robot

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
map = Map()
robots = []
routes = []

for i in range(10):
    line = input()
    map.update_map(line, i)

robot_count = int(input())

for i in range(robot_count):
    inputs = input().split()
    x = int(inputs[0])
    y = int(inputs[1])
    direction = inputs[2]
    robot = Robot(i, x, y, direction, map)
    robots.append(robot)

for r in robots:
    r.build_route()
    route = r.get_route()
    print(f"{r.id} {route}", file=sys.stderr, flush=True)
    if route:
        routes.append(route)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
# print(map.get_at(3, 4), file=sys.stderr, flush=True)
print(" ".join(routes))
