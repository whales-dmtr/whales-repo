class Node:
    """Класс для узлов в связанном списке"""

    def __init__(self, data):
        self.data = data  # элемент
        self.next = None  # следующий элемент

    def __str__(self):
        return str(self.data)


class LinkedList:
    """
    Класс для самого связанного списка.
    Здесь важно понимать, что этот класс хранит только первый элемент (head),
    и затем по нему можно перейти к любому элементу.
    """

    def __init__(self):
        self.head = None  # Изначально первый элемент не задан
        # его нужно установить ручками

    def __str__(self):
        """Алгоритм для генерации связного списка по первому элементу"""
        node = self.head  # ссылка на первый объект
        nodes = []  # элементы связанного списка
        while node != None:  # проверяем, если node - None, это последний узел
            nodes.append(str(node.data))  # добавляем элемент в nodes
            node = node.next  # переходим к следующему элементу
        # добавляем в конец None, ведь на нем цыкл закончился
        nodes.append('None')
        return " -> ".join(nodes)  # красииииво выводим список

    def __iter__(self):
        node = self.head
        while node != None:
            yield node
            node = node.next

    def appendleft(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def append(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = new_node

    def pop(self):
        for key, node in enumerate(self):
            pass
        deleted_node = self.get_nodes_list()[key]
        self.get_nodes_list()[key-1].next = None
        return deleted_node

    def popleft(self):
        deleted_node = self.head
        self.head = self.head.next
        return deleted_node

    def get_nodes_list(self):
        node = self.head
        nodes = []
        while node != None:
            nodes.append(node)
            node = node.next
        return nodes

    def __getitem__(self, idx):
        return self.get_nodes_list()[idx]

    def __setitem__(self, idx, new_node):
        if idx != len(self.get_nodes_list())-1:
            new_node.next = self.get_nodes_list()[idx+1]
        if idx != 0:
            self.get_nodes_list()[idx-1].next = new_node
        else:
            self.head = new_node


class UpgratedNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.previous = None


class UpgratedLinkedList(LinkedList):
    def appendleft(self, new_node):
        self.head.previous = new_node
        new_node.next = self.head
        self.head = new_node

    def __str__(self):
        node = self.head
        nodes = ['None']
        while node.next != None:
            nodes.append(str(node.data))
            node = node.next
        else:
            while node.previous != None:
                nodes.append(str(node.data))
                node = node.previous
            nodes.append('None')
        return " -> ".join(nodes)


next_nodes = [
    UpgratedNode(25),
    UpgratedNode(26),
    UpgratedNode(27),
    UpgratedNode(28)
]

previous_nodes = [
    UpgratedNode(14),
    UpgratedNode(13),
    UpgratedNode(12),
    UpgratedNode(11)
]

ullist = UpgratedLinkedList()

for i in next_nodes:
    ullist.append(i)

for i in previous_nodes:
    ullist.appendleft(i)

print(ullist)
# None -> 11 -> 12 -> 13 -> 14 -> 25 -> 26 -> 27 -> None
