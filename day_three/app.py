import itertools


def read_data():
    with open('data.txt', 'r') as f:
        content = f.readlines()
        content = list(map(lambda x: x.replace('\n', ''), content))
        return content

def test_data():
    return [
        '#1 @ 1,3: 4x4',
        '#2 @ 3,1: 4x4',
        '#3 @ 5,5: 2x2'
    ]


def format(claim):
    x = claim.find('@ ') + 2
    y = claim.find(',') + 1
    x_distance = claim.find(': ') + 2
    y_distance = claim.find('x')

    x_start = int(claim[x:y-1])

    x_range = int(claim[x_distance:y_distance])
    y_range = int(claim[y_distance+1:])

    x_end = x_start + x_range
    y_start = int(claim[y:x_distance - 2])
    y_end = y_start + y_range
    obj = {
        'x': (x_start, x_end),
        'y': (y_start, y_end),
    }

    return obj

def coordinates(claim_obj):
    coordinates = []
    for x in range(*claim_obj['x']):
        for y in range(*claim_obj['y']):
            coordinates.append((x, y))
    return coordinates

def gen_grid(x_size=1000, y_size=1000):
    return [['0' for x in range(x_size)] for x in range(y_size)]

def print_grid(grid):
    for row in grid:
        print(row)

def main():
    data = read_data()
    formatted = list(map(lambda e: format(e), data))

    grid = gen_grid()
    claim_coords = list(map(lambda c: coordinates(c),formatted))

    count = 0
    for i, elf_coords in enumerate(claim_coords):
        for used in elf_coords:
            cell = grid[used[1]][used[0]]
            if cell == '0':
                grid[used[1]][used[0]] = str(i+1)
            else:
                count += 1
                grid[used[1]][used[0]] = 'X'

    flattened = list(itertools.chain(*grid))
    print(flattened.count('X'))
    # print_grid(grid)



if __name__ == '__main__':
  main()