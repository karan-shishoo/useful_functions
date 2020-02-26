#Setting up a rudimentary ListNode Class to build our LinkedList from
class ListNode:
  #Class only has 2 properties, the value the node holds and the next node in the list which defaults to None
  def __init__(self, value):
      self.value = value
      self.next = None

#function to reverse the LinkedList
def reverse_linked_list(head_node):
  #check to see if a list even exists
  if not head_node.next:
    return head_node
  #Save the head Node and next Node to use as the start to our loop
  current_node = head_node
  next_node = current_node.next
  #make the current head Node the tail
  current_node.next = None

  while next_node.next:
    temp_node = next_node.next
    next_node.next = current_node
    current_node = next_node
    next_node = temp_node

  next_node.next = current_node

  return next_node

#Function to print a LinkedList to check its state (only viable for small lists with str/int values)
def print_nodes(head_node):
  current_node = head_node
  node_builder = ""
  while current_node.next:
    node_builder += str(current_node.value) + " -> "
    current_node = current_node.next
  node_builder += str(current_node.value)
  return node_builder

#Creating a LinkedList to test the functions
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

#Code written by Karan Shishoo
