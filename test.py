# Practice removing zeros from a single row

# Example row from 2048 game
test_row = [2, 0, 4, 0]

# Create a new list to store non-zero numbers
non_zero_numbers = []

# Loop through each number in the row
for number in test_row:
    # If the number is not zero, add it to our new list
    if number != 0:
        non_zero_numbers.append(number)

print("Original row:", test_row)
print("Without zeros:", non_zero_numbers)






# Practice merging adjacent identical tiles

# Example: [2, 2, 4] should become [4, 4]
non_zero_numbers = [2, 2, 4]

# Create a new list to store merged numbers
merged_numbers = []

# Loop through the list, but stop before the last number
i = 0
while i < len(non_zero_numbers):
    # Check if current number equals next number
    if i + 1 < len(non_zero_numbers) and non_zero_numbers[i] == non_zero_numbers[i + 1]:
        # Merge them by adding
        merged_numbers.append(non_zero_numbers[i] + non_zero_numbers[i + 1])
        # Skip the next number since we used it
        i += 2
    else:
        # No merge, just add the current number
        merged_numbers.append(non_zero_numbers[i])
        i += 1

print("Before merging:", non_zero_numbers)
print("After merging:", merged_numbers)

# Add zeros to make the row length 4
while len(merged_numbers) < 4:
    merged_numbers.append(0)

print("Final row:", merged_numbers)

# Test with a known board instead of random placement
board = [
    [2, 0, 2, 0],  # Row 0 - should become [4, 0, 0, 0]
    [0, 0, 0, 0],  # Row 1 - should stay [0, 0, 0, 0]
    [0, 0, 0, 0],  # Row 2 - should stay [0, 0, 0, 0]
    [0, 0, 0, 0]   # Row 3 - should stay [0, 0, 0, 0]
]

current_row = board[0]  # Get just [2, 0, 2, 0]

# Step 1: Remove zeros from THIS row only
non_zero_numbers = []
for number in current_row:  # Loop through [2, 0, 2, 0]
    if number != 0:
        non_zero_numbers.append(number)

print("After removing zeros:", non_zero_numbers)