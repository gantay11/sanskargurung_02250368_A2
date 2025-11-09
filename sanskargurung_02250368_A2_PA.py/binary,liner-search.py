# Sample data
student_ids = [1001, 1005, 1002, 1008, 1003, 1010, 1004, 1009, 1007, 1012, 1013, 1015, 1006, 1011, 1014, 1016, 1017, 1018, 1019, 1020]
sorted_scores = [45, 52, 58, 63, 67, 72, 75, 78, 82, 85, 88, 90, 92, 95, 98, 100, 102, 105, 108, 110]

# Linear Search function
def linear_search(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i + 1, comparisons  # return 1-indexed position
    return -1, comparisons

# Binary Search function
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    comparisons = 0
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid + 1, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, comparisons

# Main Program
while True:
    print("\n=== Searching Algorithms Menu ===")
    print("1. Linear Search - Find Student ID")
    print("2. Binary Search - Find Score")
    print("3. Exit program")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        print(f"Searching in the list: {student_ids}")
        target = int(input("Enter Student ID to search: "))
        pos, comp = linear_search(student_ids, target)
        if pos != -1:
            print(f"Result: Student ID {target} found at position {pos} Comparisons made: {comp}")
        else:
            print(f"Result: Student ID {target} not found. Comparisons made: {comp}")

    elif choice == "2":
        print(f"Sorted scores: {sorted_scores}")
        target = int(input("Enter score to search: "))
        pos, comp = binary_search(sorted_scores, target)
        if pos != -1:
            print(f"Result: Score {target} found at position {pos} Comparisons made: {comp}")
        else:
            print(f"Result: Score {target} not found. Comparisons made: {comp}")

    elif choice == "3":
        print("sorry your in wrong way! Try again later")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

    again = input("Try again?your number is not here (y/n): ")
    if again.lower() != 'y':
        print("Thank you for your time!")
        break
