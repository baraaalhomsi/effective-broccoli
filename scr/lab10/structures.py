from collections import deque
from typing import Any, Optional


class Stack:
    
    def __init__(self) -> None:

        self._data: list[Any] = []
    
    def push(self, item: Any) -> None:

        self._data.append(item)
    
    def pop(self) -> Any:

        if self.is_empty():
            raise IndexError("not able to remove element from empty Stack")
        return self._data.pop()
    
    def peek(self) -> Optional[Any]:

        if self.is_empty():
            return None
        return self._data[-1]
    
    def is_empty(self) -> bool:

        return len(self._data) == 0
    
    def __len__(self) -> int:
  
        return len(self._data)
    
    def __str__(self) -> str:
 
        return f"Stack({self._data})"
    
    def __repr__(self) -> str:
      
        return f"Stack({self._data})"


class Queue:
    
    def __init__(self) -> None:
 
        self._data: deque[Any] = deque()
    
    def enqueue(self, item: Any) -> None:

        self._data.append(item)
    
    def dequeue(self) -> Any:

        if self.is_empty():
            raise IndexError("not able to remove element from empty Queue")
        return self._data.popleft()
    
    def peek(self) -> Optional[Any]: # return the first element
   
        if self.is_empty():
            return None
        return self._data[0]
    
    def is_empty(self) -> bool:

        return len(self._data) == 0
    
    def __len__(self) -> int:

        return len(self._data)
    
    def __str__(self) -> str:

        return f"Queue({list(self._data)})"
    
    def __repr__(self) -> str:

        return f"Queue({list(self._data)})"