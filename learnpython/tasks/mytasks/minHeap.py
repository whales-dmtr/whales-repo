class Node:
    """
    Класс для отдельных элементов дерева
    """
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return str(self.data)


class MinHeap:
    """
    Двоичная куча (MinHeap)
    """
    def __init__(self):
        self.heap = []  # хранится в списке

    def insert(self, new_node):
        """
        Для вставки узлов в кучу
        """
        idx = 0
        for node in self.heap:
            if new_node.data < node.data:
                break
            idx += 1
        if idx == len(self.heap):
            self.heap.append(new_node)
            return new_node

        # просачивание (swap)
        added_el = self.heap[idx]
        self.heap[idx] = new_node
        for i in range(len(self.heap[idx:])):
            if (idx+i+1) <= len(self.heap)-1:
                previous_el = self.heap[idx+i+1]
                self.heap[idx+i+1] = added_el
            added_el = previous_el
        self.heap.append(added_el)
        return new_node

    def find(self, idx, show_node: bool):
        """
        Отрисовывает по индексу узел и его дочерние элементы 
        """
        # этот весь фукнционал можно запехнуть в __getitem__ чтобы можно было обращаться
        # с помощью [], но тогда нельзя будет контролировать отрисовку так что пока что так
        if show_node:  # отвечает за отрисовку
            left_child_idx = round(idx * 2 + 1)
            right_child_idx = round(idx * 2 + 2)

            max_len = max([len(str(left_child_idx)), len(str(right_child_idx))])
            if left_child_idx >= len(self.heap) and right_child_idx >= len(self.heap):
                print(' ' * 5 + str(self.heap[idx].data))
                print(' ' * 4 + '/' + ' ' + '\\')
                print(' ' * (max_len-4) + 'None' + '   ' + ' ' * (max_len-4) + 'None')
            elif left_child_idx >= len(self.heap):
                print(' ' * (max_len + 1) + str(self.heap[idx].data))
                print(' ' * (max_len) + '/' + ' ' + '\\')
                print(' ' * (max_len-4) + 'None' + '   ' + f"{self.heap[right_child_idx].data:0{max_len}}")
            elif right_child_idx >= len(self.heap):
                print(' ' * (max_len + 1) + str(self.heap[idx].data))
                print(' ' * (max_len) + '/' + ' ' + '\\')
                print(f"{self.heap[left_child_idx].data:0{max_len}}" + '   ' + ' ' * (max_len-4) + 'None' )
            else:
                print(' ' * (max_len + 1) + str(self.heap[idx].data))
                print(' ' * (max_len) + '/' + ' ' + '\\')
                print(f"{self.heap[left_child_idx].data:0{max_len}}" + '   ' + f"{self.heap[right_child_idx].data:0{max_len}}")

        return self.heap[idx]

    def __iter__(self):
        # итерация происхоидит по списку
        self.__idx = 0
        return self

    def __next__(self):
        if self.__idx >= len(self.heap):
            raise StopIteration
        node = self.heap[self.__idx]
        self.__idx += 1
        return node

    def __str__(self):
        """
        Просто выводит массив в котором хранится куча.
        красивый вывод всего дерева реализую завтра
        """
        return str([node.data for node in self.heap])


minheap = MinHeap()

# Порядок добавления узлов не важен, в куче всегда элементы будут 
# следовать принципу MinHeap - дочерние элементы меньше родительских
minheap.insert(Node(1))
minheap.insert(Node(4))
minheap.insert(Node(4))
minheap.insert(Node(3))
minheap.insert(Node(0))
minheap.insert(Node(2))

print(minheap)
# [0, 1, 2, 3, 4, 4]

minheap.find(0, True)
#   0
#  / \
# 1   2

for i in minheap:
    print(i)
# 0
# 1
# 2
# 3
# 4
# 4