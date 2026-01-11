from typing import Any


import math

def day8():
    arr_test = read_data('./data/day8_test.txt')
    arr_full = read_data('./data/day8.txt')
    solve_8a(arr_test, 10)  # 40
    # solve_8a(arr_full, 1000) # 112230

# brute force
def solve_8a(arr: list[tuple[int, int, int]], num_of_connections: int):
    distances: list[tuple[float, list[int, int, int], list[int, int, int]]] = []
    nums = len(arr)
    for i in range(nums):
        for j in range(i+1, nums):
            x1, y1, z1 = arr[i]
            x2, y2, z2 = arr[j]
            dist = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
            tt = (dist, i, j, arr[i], arr[j]) # tt = (dist, arr[i], arr[j]) use i and j instead of arr[i] and arr[j]
            distances.append(tt)

    distances.sort(key=lambda x: x[0])

    circuits: list[set[str]] = []
    num_of_connections = len(distances)
    for distance, box1, box2, pos1, pos2 in distances[0:num_of_connections+1]:
        # key1 = f"{box1[0]}-{box1[1]}-{box1[2]}"
        # key2 = f"{box2[0]}-{box2[1]}-{box2[2]}"
        key1 = box1
        key2 = box2

        isDuplicate = False        
        idx1 = -1
        idx2 = -1   
        # search through all circuits first.
        for i in range(len(circuits)):
            circuit = circuits[i]
            if key1 in circuit and key2 in circuit:
                isDuplicate = True
                break
            if key1 in circuit:
                idx1 = i
            if key2 in circuit:
                idx2 = i

        if isDuplicate:
            # do nothing. duplicate junctions
            continue

        print(f"distance: {distance}, pos1: {box1}, pos2: {box2}")

        if idx1 >= 0 and idx2 >= 0:
            # join circuits
            circuit1 = circuits[idx1]
            circuit2 = circuits[idx2]
            circuit1.add(key2)
            circuit2.add(key1)
            # join circuits 1 and 2
            circuits[idx1] = circuit1.union(circuit2)
            # remove the duplicate circuit
            circuits.pop(idx2)

            if len(circuits) == 1:
                print(f"part-b done. {key1} - {key2}")
        else:
            if idx1 == -1 and idx2 == -1:
                # new circuit
                new_set = set[str]()
                new_set.add(key1)
                new_set.add(key2)
                circuits.append(new_set)

            if idx1 >= 0:
                circuit1 = circuits[idx1]
                circuit1.add(key2)

            if idx2 >= 0:
                circuit2 = circuits[idx2]
                circuit2.add(key1)

    sorted_circuits = sorted(circuits, key=lambda x: len(x), reverse=True)
    sorted_lens = [len(circuit) for circuit in sorted_circuits]

    result = sorted_lens[0] * sorted_lens[1] * sorted_lens[2]    
    print(sorted_lens)
    print(f"Result: {result}")


def read_data(filepath: str) -> list[list[int, int, int]]:
    with open(filepath) as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))

    arr = []
    for line in lines:
        item = line.split(',')
        arr.append([int(item[0]), int(item[1]), int(item[2])])

    return arr

if __name__ == "__main__":
    day8()