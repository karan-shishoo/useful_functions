class ListNode:
  def __init__(self, value):
      self.value = value
      self.next = None


def reverse_linked_list(head_node):
  current_node = head_node
  next_node = current_node.next
  current_node.next = None

  while next_node.next:
    temp_node = next_node.next
    next_node.next = current_node
    current_node = next_node
    next_node = temp_node

  next_node.next = current_node

  return next_node

def print_nodes(head_node):
  current_node = head_node
  node_builder = ""
  while current_node.next:
    node_builder += str(current_node.value) + " -> "
    current_node = current_node.next
  node_builder += str(current_node.value)
  return node_builder


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e

print(print_nodes(a))
print(print_nodes(reverse_linked_list(a)))
