import math

def day8():
    arr = read_data('./data/day8_test.txt')
    solve_8a(arr)

# brute force
def solve_8a(arr: list[tuple[int, int, int]]):
    distances: list[tuple[float, list[int, int, int], list[int, int, int]]] = []
    nums = len(arr)
    for i in range(nums):
        for j in range(i+1, nums):
            x1, y1, z1 = arr[i]
            x2, y2, z2 = arr[j]
            dist = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
            tt = (dist, arr[i], arr[j])
            distances.append(tt)

    distances.sort(key=lambda x: x[0])

    circuits: list[set[str]] = []
    for distance, box1, box2 in distances[0:10]:
        key1 = f"{box1[0]}-{box1[1]}-{box1[2]}"
        key2 = f"{box2[0]}-{box2[1]}-{box2[2]}"

        isDuplicate = False
        circuit1: list[set] = None
        circuit2: list[set] = None
        for circuit in circuits:
            if key1 in circuit and key2 in circuit:
                isDuplicate = True
                break
            if key1 in circuit: 
                circuit1 = circuit
            if key2 in circuit:
                circuit2 = circuit

        if isDuplicate:
            # do nothing. duplicate junctions
            continue

        if circuit1 and circuit2:
            # this is a cross linked circuit
            circuit1.add(key2)
            circuit2.add(key1)
            # join circuits 1 and 2
            circuit1 = circuit1.union(circuit2)
            circuit2.clear()
        else:
            if circuit1 is None and circuit2 is None:
                # new circuit
                new_set = set()
                new_set.add(key1)
                new_set.add(key2)
                circuits.append(new_set)

            if circuit1 is not None:
                circuit1.add(key2)

            if circuit2 is not None:
                circuit2.add(key1)

    for circuit in circuits:
        print(circuit)

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