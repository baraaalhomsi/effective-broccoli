from typing import Any, Optional, Iterator

class Node:
    
    def __init__(self, value: Any) -> None:

        self.value: Any = value
        self.next: Optional['Node'] = None
    
    def __str__(self) -> str:

        return f"[{self.value}]"
    
    def __repr__(self) -> str:

        return f"Node({self.value})"


class SinglyLinkedList:
    
    def __init__(self) -> None:

        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size: int = 0
    
    def append(self, value: Any) -> None:

        new_node = Node(value)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self._size += 1
    
    def prepend(self, value: Any) -> None:

        new_node = Node(value)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self._size += 1
    
    def insert(self, idx: int, value: Any) -> None:

        if idx < 0 or idx > self._size:
            raise IndexError(f"the index {idx} out of the range {self._size}]")
        
        if idx == 0:
            self.prepend(value)
        elif idx == self._size:
            self.append(value)
        else:
            new_node = Node(value)
            current = self.head
            for _ in range(idx - 1):
                current = current.next
            
            new_node.next = current.next
            current.next = new_node
            self._size += 1
    
    def remove(self, value: Any) -> bool:

        if self.is_empty():
            return False
        
        # remove the first element
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return True
        
        # find the node that precedes the node to be remove
        current = self.head
        while current.next is not None and current.next.value != value:
            current = current.next
        
        # if there is not value
        if current.next is None:
            return False
        
        # remove the node
        current.next = current.next.next
        
        # uptade the tail if the last element was removed
        if current.next is None:
            self.tail = current
        
        self._size -= 1
        return True
    
    def remove_at(self, idx: int) -> Any:
 
        if idx < 0 or idx >= self._size:
            raise IndexError(f"the index {idx} out of the range {self._size - 1}]")
        
        if idx == 0:
            removed_value = self.head.value
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            current = self.head
            for _ in range(idx - 1):
                current = current.next
            
            removed_value = current.next.value
            current.next = current.next.next
            
            if current.next is None:
                self.tail = current
        
        self._size -= 1
        return removed_value
    
    def search(self, value: Any) -> bool:

        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False
    
    def get(self, idx: int) -> Any:

        if idx < 0 or idx >= self._size:
            raise IndexError(f"the index {idx} out of the range {self._size - 1}]")
        
        current = self.head
        for _ in range(idx):
            current = current.next
        
        return current.value
    
    def is_empty(self) -> bool:
 
        return self._size == 0
    
    def __iter__(self) -> Iterator[Any]:
   
        current = self.head
        while current is not None:
            yield current.value
            current = current.next
    
    def __len__(self) -> int:

        return self._size
    
    def __str__(self) -> str:
     
        if self.is_empty():
            return "SinglyLinkedList([])"
        
        parts = []
        current = self.head
        while current is not None:
            parts.append(f"[{current.value}]")
            current = current.next
        
        return "SinglyLinkedList(" + " -> ".join(parts) + ")"
    
    def __repr__(self) -> str:
    
        values = list(self)
        return f"SinglyLinkedList({values})"
    
    def pretty_print(self) -> str:
       
        if self.is_empty():
            return "Empty List"
        
        result = []
        current = self.head
        while current is not None:
            result.append(f"[{current.value}]")
            current = current.next
        
        return " -> ".join(result) + " -> None"