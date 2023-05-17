from node.implementation import Node
class Queue:
    # PRIVATE ATTRIBUTES
    __front = None
    __back = None
    __length = 0
    __empty = True
    
    # REPRESENTATION
    def __repr__(self) -> str:
        if self.__empty:
            return 'EMPTY!'
        representation = 'FRONT->'
        currentNode = self.__front
        while currentNode is not None:
            representation += f'[{currentNode.getValue()}]'
            currentNode = currentNode.getNext()
        return representation
    
    # PRIVATE METHODS
    def __construct(self, node: Node) -> None:
        self.__front = node
        self.__back = node
        self.__length = 1
        self.__empty = False

    def __destruct(self) -> None:
        self.__front = None
        self.__back = None
        self.__length = 0
        self.__empty = True

    def __changeNext(self, node: Node, nextNode: Node) -> None:
        # [ACCESSING __setNext(node) METHOD USING 'Name Mangling']
        node._Node__setNext(nextNode)

    # GETTERS
    def getFront(self) -> Node:
        return self.__front
    
    def getBack(self) -> Node:
        return self.__back
    
    def getLength(self) -> int:
        return self.__length
    
    def isEmpty(self) -> bool:
        return self.__empty
    
    # QUEUES BASIC OPERATIONS
    def enqueue(self, node: Node=Node()) -> None:
        # Time Complexity: O(1)
        if not isinstance(node, Node):
            node = Node(node)
        if self.__empty:
            self.__construct(node)
        else:
            self.__changeNext(self.__back, node)
            self.__back = node
            self.__length += 1

    def dequeue(self):
        # Time Complexity: O(1)
        if self.__empty:
            return
        elif self.__length == 1:
            self.__destruct()
        else:
            self.__front = self.__front.getNext()
            self.__length -= 1