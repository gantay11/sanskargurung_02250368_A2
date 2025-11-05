# Part A: Searching Algorithms Implementation (Linear Search)

# Hard-coded list of 20 student IDs
student_ids = [1001, 1005, 1002, 1008, 1003, 1010, 1004, 1009, 1011, 1012,
               1006, 1013, 1014, 1007, 1015, 1016, 1017, 1018, 1019, 1020]


# Linear Search Function
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i + 1  # return 1-indexed position
    return -1


# Main Program
while True:
    print("\n==== Student Search Menu ====")
    print("1. Linear Search Student ID")
    print("2. Exit")
    
    choice = input("Enter your choice (1-2): ")
    
    if choice == '1':
        print("\nStudent IDs List:", student_ids)
        try:
            target = int(input("Enter Student ID to search: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        
        result = linear_search(student_ids, target)
        
        if result != -1:
            print(f"✅ Student ID {target} found at position {result}")
        else:
            print(f"❌ Student ID {target} not found.")
    
    elif choice == '2':
        print("Exiting program... Goodbye!")
        break
    
    else:
        print("Invalid choice! Please select 1 or 2.")
