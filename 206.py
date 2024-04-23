# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
# 定义链表节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    curr = head
    while curr:
        next_temp = curr.next  # 保存下一个节点
        curr.next = prev       # 反转当前节点的指针
        prev = curr            # 移动prev到当前节点
        curr = next_temp       # 移动curr到下一个节点
    return prev  # prev现在指向新的头节点

# 创建链表 1 -> 2 -> 3 -> 4 -> 5
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5







