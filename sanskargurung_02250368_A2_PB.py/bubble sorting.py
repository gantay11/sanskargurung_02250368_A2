# Bubble Sort to sort student names

student_names = ["Kado", "Bobchu", "Zamu", "Nado", "Lemo", "Sonam", "Tashi", "Pema", "Kinley",
                 "Tshering", "Wangmo", "Choden", "Yeshi", "Ugyen", "Dechen"]

print("Original Student Names:")
print(student_names)

# Bubble Sort Algorithm
for i in range(len(student_names)):
    for j in range(0, len(student_names) - i - 1):
        if student_names[j] > student_names[j + 1]:
            student_names[j], student_names[j + 1] = student_names[j + 1], student_names[j]

print("\nSorted Student Names (Alphabetically):")
print(student_names)


# Insertion Sort to sort test scores

scores = [78, 45, 92, 67, 88, 54, 73, 81, 69, 59,
          95, 62, 49, 84, 76, 90, 52, 71, 65, 87]

print("Original Scores:")
print(scores)

# Insertion Sort Algorithm
for i in range(1, len(scores)):
    key = scores[i]
    j = i - 1
    
    while j >= 0 and key < scores[j]:
        scores[j + 1] = scores[j]
        j -= 1
    scores[j + 1] = key

print("\nSorted Scores (Ascending):")
print(scores)

# Display Top 5 Scores (highest first)
print("\nTop 5 Scores:")
for i in range(1, 6):
    print(f"{i}. {scores[-i]}")
