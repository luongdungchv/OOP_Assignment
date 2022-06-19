from random import random
lines = []
with open("input.txt") as f:
    lines = f.readlines()


def getIntersections():
    res = set()
    for i in lines:
        parts = i.split()

        dict = {}
        for j in parts:
            try:
                index = j.index("_")
            except:
                continue
            vert = j[:index]

            if (vert in dict):
                dict[vert] += 1
            else:
                dict[vert] = 1
        for j in dict.keys():
            if dict[j] >= 2:
                res.add(j)
    return res


def writeIntersections():
    lines = []

    for i in getIntersections():
        rand = round(random() * 3, 1)
        lines.append(f"{i} {rand}\n")
    with open("vertices.txt", "w") as f:
        f.writelines(lines)


def writeEdges():
    verts = getIntersections()
    res = []
    for i in lines:
        all_parts = i.split()
        if len(all_parts) < 3:
            continue
        part1 = all_parts[0]
        try:
            index = part1.index("_")
        except:
            continue
        vert1 = part1[:index]

        part2 = i.split()[2]
        try:
            index = part2.index("_")
        except:
            continue
        vert2 = part2[:index]

        if vert2 in verts:
            res.append(f"{vert1}${vert1}{vert2} {all_parts[1]}\n")
            res.append(f"{vert1}{vert2}${vert2} 0\n")
        else:
            res.append(f"{vert1}${vert2} {all_parts[1]}\n")

    with open("edges.txt", "w") as f:
        f.writelines(res)
    return res

# print(len(getIntersections()))
