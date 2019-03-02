import string
from typing import NamedTuple, List, Tuple

class Node(NamedTuple):
    num_children: int
    num_metadata: int
    children: List['Node']
    metadata: List[int]

"""
2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
A----------------------------------
    B----------- C-----------
                     D-----

"""

def get_nodes(inputs: List[int], start:int) -> Tuple[Node, int]:
    num_children = inputs[start]
    num_metadata = inputs[start+1]

    children = []

    start = start+2
    print(start)
    for _ in range(num_children):
        child, start = get_nodes(inputs, start)
        children.append(child)

    metadata = inputs[start:start+num_metadata]

    return Node(num_children, num_metadata, children, metadata), (start + num_metadata)

def sum_all_metadata(node: Node) -> int:
    return sum(node.metadata) + sum(sum_all_metadata(child) for child in node.children)

def value(node: Node) -> int:
    if node.num_children == 0:
        return sum(node.metadata)
    else:
        child_values = {i:value(child) for i, child in enumerate(node.children)}
        return sum(child_values.get(i-1, 0) for i in node.metadata)


def main():
    letters = list(string.ascii_uppercase)
    # data = map(int, "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2".split())
    data = map(int, open('data.txt').readline().split())
    n, _ = get_nodes(list(data), 0)
    print(n)
    print(value(n))
    # print(sum_all_metadata(n[0]))
    return sum_all_metadata(n)

if __name__ == '__main__':
    v = main()

