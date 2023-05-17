from node.implementation import Node
class Stack:
    # PRIVATE ATTRIBUTES
    __top = None
    __length = 0
    __empty = True
    
    # REPRESENTATION
    def __repr__(self) -> str:
        if self.__empty:
            return 'EMPTY!'
        representation = ''
        currentNode = self.__top
        while currentNode is not None:
            representation += f'[{currentNode.getValue()}]'
            representation += '\n---\n'
            currentNode = currentNode.getNext()
        return representation
    
    # PRIVATE METHODS
    def __construct(self, node: Node) -> None:
        self.__top = node
        self.__length = 1
        self.__empty = False

    def __destruct(self) -> None:
        self.__top = None
        self.__length = 0
        self.__empty = True

    def __changeNext(self, node: Node, nextNode: Node) -> None:
        # [ACCESSING __setNext(node) METHOD USING 'Name Mangling']
        node._Node__setNext(nextNode)

    # GETTERS
    def getTop(self) -> Node:
        return self.__top
    
    def getLength(self) -> int:
        return self.__length
    
    def isEmpty(self) -> bool:
        return self.__empty
    
    # STACKS BASIC OPERATIONS
    def push(self, node: Node=Node()) -> None:
        # Time Complexity: O(1)
        if not isinstance(node, Node):
            node = Node(node)
        if self.__empty:
            self.__construct(node)
        else:
            self.__changeNext(node, self.__top)
            self.__top = node
            self.__length += 1

    def pop(self) -> None:
        # Time Complexity: O(1)
        if self.__empty:
            return
        elif self.__length == 1:
            self.__destruct()
        else:
            self.__top = self.__top.getNext()
            self.__length -= 1