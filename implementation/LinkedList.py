from node.implementation import Node

class LinkedList:
    # PRIVATE ATTRIBUTES
    __head = None
    __tail = None
    __empty = True
    __length = 0

    # REPRESENTATION
    def __repr__(self) -> str:
        if self.__empty:
            return 'EMPTY!'
        representation = ''
        currentNode = self.__head
        while currentNode is not None:
            representation += f'[{currentNode.getValue()}]-->'
            currentNode = currentNode.getNext()
        representation += 'None'
        return representation
    
    # GETTERS
    def getHead(self) -> Node:
        return self.__head
    
    def getTail(self) -> Node:
        return self.__tail
    
    def isEmpty(self) -> bool:
        return self.__empty
    
    def getLength(self) -> int:
        return self.__length
    
    # PRIVATE METHODS
    def __construct(self, node: Node) -> None:
        self.__head = node
        self.__tail = node
        self.__empty = False
        self.__length = 1

    def __destruct(self) -> None:
        self.__head = None
        self.__tail = None
        self.__empty = True
        self.__length = 0

    def __changeNext(self, node: Node, nextNode: Node) -> None:
        # [ACCESSING __setNext(node) METHOD USING 'Name Mangling']
        node._Node__setNext(nextNode)

    # LINKED LISTS BASIC OPERATIONS
    def access(self, index: int=0) -> Node:
        # Time Complexity: O(n)
        if self.__empty:
            return 'EMPTY!'
        if index < 0 or index >= self.__length:
            raise IndexError('Index out of range!')
        currentIndex = 0
        currentNode = self.__head
        while currentNode is not None:
            if currentIndex == index:
                return currentNode
            currentNode = currentNode.getNext()
            currentIndex += 1

    def search(self, value: int) -> bool:
        # Linear Search Algorithm
        # Time Complexity: O(n)
        if self.__empty:
            return False
        currentNode = self.__head
        while currentNode is not None:
            if currentNode.getValue() == value:
                return True
            currentNode = currentNode.getNext()
        return False
    
    def insert(self, index: int=None, node: Node=Node()) -> None:
        # Time Complexity: O(n)
        if not isinstance(node, Node):
            node = Node(node)
        if index is None:
            index = self.__length
        if index <= 0:
            self.prepend(node)
        elif index >= self.__length:
            self.append(node)
        else:
            currentIndex = 0
            previousNode = None
            currentNode = self.__head
            while True:
                if currentIndex == index:
                    self.__changeNext(previousNode, node)
                    self.__changeNext(node, currentNode)
                    self.__length += 1
                    return
                previousNode = currentNode
                currentNode = currentNode.getNext()
                currentIndex += 1

    def append(self, node: Node=Node()) -> None:
        # Time Complexity: O(1)
        if not isinstance(node, Node):
            node = Node(node)
        if self.__empty:
            self.__construct(node)
        else:
            self.__changeNext(self.__tail, node)
            self.__tail = node
            self.__length += 1

    def prepend(self, node: Node=Node()) -> None:
        # Time Complexity: O(1)
        if not isinstance(node, Node):
            node = Node(node)
        if self.__empty:
            self.__construct(node)
        else:
            self.__changeNext(node, self.__head)
            self.__head = node
            self.__length += 1

    def remove(self, index: int=None) -> None:
        # Time Complexity: O(n)
        if index is None:
            index = self.__length
        if index <= 0:
            self.shift()
        elif index >= self.__length:
            self.pop()
        else:
            currentIndex = 0
            previousNode = None
            currentNode = self.__head
            while True:
                if currentIndex == index:
                    currentNodeNext = currentNode.getNext()
                    self.__changeNext(previousNode, currentNodeNext)
                    self.__length -= 1
                    return
                previousNode = currentNode
                currentNode = currentNode.getNext()
                currentIndex += 1

    def pop(self) -> None:
        # Time Complexity: O(n)
        if self.__empty:
            return
        else:
            if self.__length == 1:
                self.__destruct()
            else:
                previousNode = None
                currentNode = self.__head
                while True:
                    if currentNode.getNext() is None:
                        self.__changeNext(previousNode, None)
                        self.__tail = previousNode
                        self.__length -= 1
                        return
                    previousNode = currentNode
                    currentNode = currentNode.getNext()

    def shift(self) -> None:
        # Time Complexity: O(1)
        if self.__empty:
            return
        else:
            if self.__length == 1:
                self.__destruct()
            else:
                self.__head = self.__head.getNext()
                self.__length -= 1