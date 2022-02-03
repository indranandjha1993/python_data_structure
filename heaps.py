import heapq
"""
 Heap is a special tree structure in which each parent node is less than or equal to its child node. Then it is called
 a Min Heap. If each parent node is greater than or equal to its child node then it is called a max heap. It is very
 useful is implementing priority queues where the queue item with higher weightage is given more priority in processing.

 A heap is created by using python’s inbuilt library named heapq. This library has the relevant functions to carry out
 various operations on heap data structure. Below is a list of these functions.

    1) heapify − This function converts a regular list to a heap. In the resulting heap the smallest element gets pushed
     to the index position 0. But rest of the data elements are not necessarily sorted.
    2) heappush − This function adds an element to the heap without altering the current heap.
    3) heappop − This function returns the smallest data element from the heap.
    4) heapreplace − This function replaces the smallest data element with a new value supplied in the function.
"""

# creating a heap
H = [12, 9, 78, 25, 66]
heapq.heapify(H)

print(H)


# Insert element into heap
"""
    Inserting a data element to a heap always adds the element at the last index. But we can apply heapify function
    again to bring the newly added element to the first index only if it smallest in value.
    In the below example we insert the number 8.
"""

heapq.heappush(H, 8)
print(H)


# Removing element to heap
heapq.heappop(H)
print(H)

# Update element to heap
heapq.heapreplace(H, 2)
print(H)



