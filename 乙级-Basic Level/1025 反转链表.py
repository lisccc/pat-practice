'''
给定一个常数 K 以及一个单链表 L，请编写程序将 L 中每 K 个结点反转。
例如：给定 L 为 1→2→3→4→5→6，K 为 3，则输出应该为 3→2→1→6→5→4；
    如果 K 为 4，则输出应该为 4→3→2→1→5→6，即最后不到 K 个元素不反转。

输入格式：
每个输入包含 1 个测试用例。每个测试用例第 1 行给出第 1 个结点的地址、结点总个数正整数 N ( ≤ 10^5 )、以及正整数 K ( ≤ N )，
即要求反转的子链结点的个数。结点的地址是 5 位非负整数，NULL 地址用 −1 表示。
接下来有 N 行，每行格式为：
Address Data Next
其中 Address 是结点地址，Data 是该结点保存的整数数据，Next 是下一结点的地址。
输出格式：
对每个测试用例，顺序输出反转后的链表，其上每个结点占一行，格式与输入相同。
输入样例：
00100 6 4
00000 4 99999
00100 1 12309
68237 6 -1
33218 3 00000
99999 5 68237
12309 2 33218
输出样例：
00000 4 33218
33218 3 12309
12309 2 00100
00100 1 99999
99999 5 68237
68237 6 -1
'''


class Node:
    def __init__(self, address, data, next_address):
        self.address = address
        self.data = data
        self.next = next_address

    def __str__(self):
        return ' '.join([self.address, self.data])


if __name__ == '__main__':
    start_address, n, k = input().split()
    k = int(k)
    nodes = []
    for i in range(int(n)):
        node = Node(*(input().split()))
        if node.address == start_address:
            current_node = node
        else:
            nodes.append(node)

    link = [current_node]
    while current_node.next != -1:
        for node in nodes:
            if node.address == current_node.next:
                link.append(node)
                nodes.remove(node)
                current_node = node
                break

    for i in range(0, len(link), k):
        if len(link) - i < k:
            break
        # 反转每 K 个结点
        link[i:i + k] = link[i:i + k][::-1]

    for i, node in enumerate(link):
        print(' '.join([node.address, node.data, link[i + 1].address if i + 1 < len(link) else '-1']))
