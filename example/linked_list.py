from pyal.list.linked_list import LinkedList

def display_list(list: LinkedList):
  iter = list.begin()
  while iter is not list.end():
    print(iter(), end=" ")
    iter = iter.next()
  print()

def main():
  list = LinkedList()

  list.push_back(1)
  list.push_back(2)
  list.push_back(3)
  list.push_back(4)
  display_list(list)

  list.insert_element(list.begin(), 100)
  iter = list.begin()
  print(f"After inserting 100 to the first position, "
        f"the first element becomes {iter()}")

  last_element = list.pop_back()
  print(f"The last element is {last_element}")       # 4

  list.insert_element(list.rbegin(), 0)
  print(f"Insert 0 before the last element")
  display_list(list)

if __name__ == "__main__":
  main()