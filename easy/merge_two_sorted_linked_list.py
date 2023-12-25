class Node:
    def __init__(self, item=None) -> None:
        self.item = item
        self.next = None

class SinglyLinkedList:
    def merge_lists(l1: Node, l2: Node) -> Node:
        linked_list = Node()
        tail = linked_list

        while l1 and l2:
            if l1.item < l2.item:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        if l1:
            tail.next = l1

        if l2:
            tail.next = l2

        return linked_list.next

    @staticmethod
    def print_list(head: Node) -> None:
        current = head
        while current:
            print(current.item, end=" ")
            current = current.next
        print()

if __name__ == "__main__":
    list1 = Node(1)
    list1.next = Node(3)
    list1.next.next = Node(5)

    list2 = Node(2)
    list2.next = Node(4)
    list2.next.next = Node(6)

    merged_list = SinglyLinkedList.merge_lists(list1, list2)
    SinglyLinkedList.print_list(merged_list)

