# Quick Sort to Sort Book Prices

# Hardcoded list of 15 book prices
book_prices = [450, 230, 678, 125, 890, 320, 510, 150, 760, 299, 410, 600, 85, 700, 520]

recursive_calls = 0  # global counter to count recursive calls

def quick_sort(arr):
    global recursive_calls
    recursive_calls += 1

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# Display original list
print("Original prices:", book_prices)

# Perform Quick Sort
sorted_prices = quick_sort(book_prices)

print("Sorted prices:", sorted_prices)
print("Recursive calls:", recursive_calls)
