class Node:
    __nextNode = None
    
    def __init__(self, value: int = 0) -> None:
        self.__nodeValue = value

    def __repr__(self) -> str:
        return f'[{self.__nodeValue}]'
    
    # GETTERS & SETTERS
    def setValue(self, value: int = 0) -> None:
        self.__nodeValue = value

    def getValue(self) -> int:
        return self.__nodeValue
    
    def __setNext(self, node: object) -> None:
        # [CAN BE ACCESSED USING 'Name Mangling']
        self.__nextNode = node

    def getNext(self) -> object:
        return self.__nextNode