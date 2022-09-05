class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Stack:
  def __init__(self):
    self.head = None
    self.top = None

  def push(self, data) -> None:
      if self.top is None:
        new_node = Node(data)
        self.top = new_node
      else:
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
  def pop(self) -> None:
      if self.top.next == None:
        self.top = None
      else:
        self.top = self.top.next


  def status(self):
    """
    It prints all the elements of stack.
    """
    result = ""
    temp = self.top
    while temp.next != None:
      print(temp.data,end="=>")
      temp = temp.next
    if temp.next == None:
      print(temp.data,end="=>")
      print(temp.next)



# Do not change the following code
stack = Stack()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "push":
    stack.push(int(data[i]))
  elif operations[i] == "pop":
    stack.pop()
stack.status()
