# sorting_program_fixed.py
student_names = ["Kado", "Bobchu", "Zamu", "Nado", "Lemo", "Tashi", "Pema",
                 "Sonam", "Kinley", "Dawa", "Ugyen", "Karma", "Yeshi", "Rinchen", "Choki"]
test_scores = [78, 45, 92, 67, 88, 54, 73, 82, 91, 59, 76, 85, 48, 93, 71, 89, 57, 80, 69, 62]
book_prices = [450, 230, 678, 125, 890, 300, 510, 280, 720, 150, 645, 410, 260, 560, 390]

# Quick sort recursive calls counter (module-level)
recursive_calls = 0


def bubble_sort(lst):
    """Return a new list sorted with bubble sort (ascending)."""
    arr = lst.copy()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Optimization: if no swaps in inner loop, list is sorted
        if not swapped:
            break
    return arr


def insertion_sort(lst):
    """Return a new list sorted with insertion sort (ascending)."""
    arr = lst.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def quick_sort(arr):
    global recursive_calls
    # Count this call if it will do work (len > 1)
    if len(arr) <= 1:
        return arr

    recursive_calls += 1  # count this partition/recursion step

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def print_menu():
    print("\n=== Sorting Algorithms Menu ===")
    print("Select a sorting operation (1-4):")
    print("1. Bubble Sort - Sort Student Names")
    print("2. Insertion Sort - Sort Test Scores")
    print("3. Quick Sort - Sort Book Prices")
    print("4. Exit program")


def safe_input(prompt):
    try:
        return input(prompt)
    except (EOFError, KeyboardInterrupt):
        print("\nInput interrupted. Exiting.")
        raise SystemExit


def main():
    global recursive_calls
    while True:
        print_menu()
        choice = safe_input("Enter your choice (1-4): ").strip()

        if choice == "1":
            print(f"\nOriginal names: {student_names}")
            sorted_names = bubble_sort(student_names)
            print(f"Sorted names (alphabetical): {sorted_names}")

        elif choice == "2":
            print(f"\nOriginal scores: {test_scores}")
            print("Performing Insertion Sort...")
            sorted_scores = insertion_sort(test_scores)
            print(f"Sorted scores (ascending): {sorted_scores}")
            # Top 5 scores (highest)
            top5 = sorted_scores[::-1][:5]
            print("\nTop 5 Scores:")
            for idx, score in enumerate(top5, start=1):
                print(f"{idx}. {score}")

        elif choice == "3":
            recursive_calls = 0  # reset counter
            print(f"\nOriginal prices: {book_prices}")
            sorted_prices = quick_sort(book_prices.copy())
            print(f"Sorted prices (ascending): {sorted_prices}")
            print(f"Recursive calls: {recursive_calls}")

        elif choice == "4":
            print("\nThank you for using the sorting program!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            again = input("Would you like to perform another sort? (y/n): ")
            if again.lower() != 'y':
                print("Thank you for using the sorting program!")
                break

if __name__ == "__main__":
    main()