#min and max k elements in an array o(nlogn)
import heapq

def min_max_k_elements(arr, k):
    min_heap = []
    max_heap = []

    # Populate min-heap and max-heap
    for num in arr:
        heapq.heappush(min_heap, num)
        heapq.heappush(max_heap, -num)

        # Maintain heap size <= k
        if len(min_heap) > k:
            heapq.heappop(min_heap)
        if len(max_heap) > k:
            heapq.heappop(max_heap)

    # Extract elements from heaps
    min_elements = sorted(heapq.nlargest(k, min_heap))
    max_elements = sorted([-x for x in heapq.nlargest(k, max_heap)])

    return min_elements, max_elements

# Example usage:
arr = [4, 2, 7, 1, 9, 3, 5]
k = 3
min_elements, max_elements = min_max_k_elements(arr, k)

print(f"Min {k} elements: {min_elements}")
print(f"Max {k} elements: {max_elements}")
