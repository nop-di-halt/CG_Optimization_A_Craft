import sys
import math
import numpy as np
from map import Map
from robot import Robot
from maps import get_map

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

map = Map()
robots = []
routes = []
_map = get_map(2)

for i in range(10):
    line = _map["map"][i]
    map.update_map(line, i)

robot_count = _map["robot_count"]

for i in range(robot_count):
    inputs = _map["start_pos"][i]
    x = int(inputs[0])
    y = int(inputs[1])
    direction = inputs[2]
    robot = Robot(i, x, y, direction, map)
    robots.append(robot)

for r in robots:
    r.build_route()
    route = r.get_route()
    print(f"{r.id} score: {route[0]} {route[1]}", file=sys.stderr, flush=True)
    if route[1]:
        routes.append(route[1])
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
# print(map.get_at(3, 4), file=sys.stderr, flush=True)
print(" ".join(routes))
