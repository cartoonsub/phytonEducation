import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def solution(node, idx):
    if idx == 0:
        value = node.next_item.value
        next_item = node.next_item.next_item
        node.next_item = next_item
        node.value = value
        return node

    node_number = 0
    current_node = node
    while current_node is not None:
        node_number += 1
        if node_number != idx:
            current_node = current_node.next_item
            continue

        next_item = current_node.next_item.next_item
        current_node.next_item = next_item
        break
    
    return node


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 0)
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3

if __name__ == '__main__':
    test()