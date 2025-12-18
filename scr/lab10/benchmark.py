import time
import random
from structures import Stack, Queue
from linked_list import SinglyLinkedList

def measure_time(func, *args):

    start = time.perf_counter()
    func(*args)
    return time.perf_counter() - start

def test_stack_performance():

    print("Testing Stack performance...")
    
    # Push test
    stack = Stack()
    start = time.perf_counter()
    for i in range(10000):
        stack.push(i)
    push_time = time.perf_counter() - start
    
    # Pop test
    start = time.perf_counter()
    for _ in range(10000):
        stack.pop()
    pop_time = time.perf_counter() - start
    
    print(f"  Push 10,000 items: {push_time:.4f}s")
    print(f"  Pop 10,000 items:  {pop_time:.4f}s")
    return push_time + pop_time


def test_queue_performance():

    print("Testing Queue performance...")
    
    queue = Queue()
    start = time.perf_counter()
    for i in range(10000):
        queue.enqueue(i)
    enqueue_time = time.perf_counter() - start
    
    start = time.perf_counter()
    for _ in range(10000):
        queue.dequeue()
    dequeue_time = time.perf_counter() - start
    
    print(f"  Enqueue 10,000 items: {enqueue_time:.4f}s")
    print(f"  Dequeue 10,000 items: {dequeue_time:.4f}s")
    return enqueue_time + dequeue_time


def test_linked_list_performance():

    print("Testing Linked List performance...")
    
    sll = SinglyLinkedList()
    
    # Append test
    start = time.perf_counter()
    for i in range(5000):
        sll.append(i)
    append_time = time.perf_counter() - start
    
    # Prepend test
    sll2 = SinglyLinkedList()
    start = time.perf_counter()
    for i in range(5000):
        sll2.prepend(i)
    prepend_time = time.perf_counter() - start
    
    # Search test
    start = time.perf_counter()
    for i in range(100):
        sll.search(random.randint(0, 4999))
    search_time = time.perf_counter() - start
    
    print(f"  Append 5,000 items:  {append_time:.4f}s")
    print(f"  Prepend 5,000 items: {prepend_time:.4f}s")
    print(f"  Search 100 items:    {search_time:.4f}s")
    
    return append_time + prepend_time + search_time

def compare_all():
 
    print("\n" + "="*50)
    print("COMPARING ALL DATA STRUCTURES")
    print("="*50)
    
    # Test each structure
    stack_time = test_stack_performance()
    print()
    
    queue_time = test_queue_performance()
    print()
    
    ll_time = test_linked_list_performance()
    
    print("\n" + "="*50)
    print("SUMMARY")
    print("="*50)
    
    print(f"\nTotal time for operations:")
    print(f"  Stack:          {stack_time:.4f}s")
    print(f"  Queue:          {queue_time:.4f}s")
    print(f"  Linked List:    {ll_time:.4f}s")
    
    print(f"\nRelative speed (lower is faster):")
    fastest = min(stack_time, queue_time, ll_time)
    print(f"  Stack:          {stack_time/fastest:.2f}x")
    print(f"  Queue:          {queue_time/fastest:.2f}x")
    print(f"  Linked List:    {ll_time/fastest:.2f}x")


def simple_example():

    print("\n" + "="*50)
    print("SIMPLE USAGE EXAMPLES")
    print("="*50)
    
    # Stack example
    print("\n1. Stack Example:")
    stack = Stack()
    stack.push("First")
    stack.push("Second")
    stack.push("Third")
    print(f"   Stack: {stack}")
    print(f"   Pop: {stack.pop()}")
    print(f"   Peek: {stack.peek()}")
    
    # Queue example
    print("\n2. Queue Example:")
    queue = Queue()
    queue.enqueue("Task 1")
    queue.enqueue("Task 2")
    queue.enqueue("Task 3")
    print(f"   Queue: {queue}")
    print(f"   Dequeue: {queue.dequeue()}")
    print(f"   Next: {queue.peek()}")
    
    # Linked List example
    print("\n3. Linked List Example:")
    sll = SinglyLinkedList()
    sll.append(10)
    sll.append(20)
    sll.prepend(5)
    print(f"   List: {sll}")
    print(f"   Pretty: {sll.pretty_print()}")
    print(f"   Length: {len(sll)}")

def main():

    print("SIMPLE DATA STRUCTURE BENCHMARK")
    print("="*50)
    
    # Show examples
    simple_example()
    
    # Run comparison
    compare_all()
    
    print("\n" + "="*50)
    print("Benchmark Complete!")
    print("="*50)

if __name__ == "__main__":
    main()