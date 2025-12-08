from itertools import combinations
import numpy as np
from collections import namedtuple

lines = open("./input.txt", "r").readlines()
boxes = [[int(x) for x in line.strip().split(",")]for line in lines]

combinations = combinations(boxes, 2)

Combination = namedtuple("Combination", ["box1", "box2", "distance"])

combinations = [Combination(tuple(combination[0]), tuple(combination[1]), float(np.linalg.norm(np.array(combination[0]) - np.array(combination[1])))) for combination in combinations]
nets = [set([tuple(box)]) for box in boxes]

combinations = [b[:2] for b in sorted(combinations, key=lambda c: c.distance)]

for i, (box1, box2) in enumerate(combinations):
    net1 = next((net for net in nets if box1 in net))
    net2 = next((net for net in nets if box2 in net))

    if net1 is not net2:
        net1.update(net2)
        nets.remove(net2)
    if i + 1 == 1000:
        net_cnt = sorted([len(net) for net in nets])[-3:]
        print(f"After {i + 1} largest 3 nets: {net_cnt}: solution part1 =", np.prod(net_cnt))
    if (len(nets) == 1):
        print(f"After connecting: {(box1, box2)} all boxes are powered - result box1.x * box2.x =", box1[0] * box2[0])
        break