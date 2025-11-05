# Sorted list of scores
scores = [45, 52, 58, 63, 67, 72, 75, 78, 82, 85, 88, 90, 92, 95, 98]

# Binary Search Function
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid + 1  # return 1-indexed position
        
        elif arr[mid] < target:
            low = mid + 1
        
        else:
            high = mid - 1
    
    return -1  # not found

# Main Program for binary search demo
print("Sorted Scores:", scores)
target = int(input("Enter score to search: "))

result = binary_search(scores, target)

if result != -1:
    print(f"✅ Score {target} found at position {result}")
else:
    print(f"❌ Score {target} not found")
