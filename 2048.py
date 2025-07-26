# This Python code snippet is creating a 4x4 grid of zeros and then randomly placing either a 2 or a 4
# in one of the empty spots on the grid. Here's a breakdown of what the code does:
# This creates a 4x4 grid of zeros
import random

board = [
    [0, 0, 0, 0],  # Row 1
    [0, 0, 0, 0],  # Row 2
    [0, 0, 0, 0],  # Row 3
    [0, 0, 0, 0]   # Row 4
]

# Create an empty list to store all positions where we find zeros
empty_spots = []

# Loop through each row (0, 1, 2, 3)
for row_index in range(4):
    # Loop through each column (0, 1, 2, 3) within the current row
    for col_index in range(4):
        # Check if the current position contains a zero (empty spot)
        if board[row_index][col_index] == 0:
            # Add this empty position to our list as a tuple (row, column)
            empty_spots.append((row_index, col_index))
            # now you know the position is (row_index, col_index)

# Pick one random position from all the empty spots we found
random_position = random.choice(empty_spots)

# Extract the row number from the random position (first element of tuple)
row = random_position[0]

# Extract the column number from the random position (second element of tuple)
col = random_position[1]

# Place either a 2 or 4 randomly at the chosen position
board[row][col] = random.choice([2, 4])

empty_spots.remove(random_position)

random_position2 = random.choice(empty_spots)

row2 = random_position2[0]
col2 = random_position2[1]

board[row2][col2] = random.choice([2, 4])


column_0 = []
for row_index in range(4):
    column_0.append(board[row_index][0])

column_1 = []
for row_index in range(4):
    column_1.append(board[row_index][1])

column_2 = []
for row_index in range(4):
    column_2.append(board[row_index][2])

column_3 = []
for row_index in range(4):
    column_3.append(board[row_index][3])

def move_row_left(row):
    non_zero_numbers = []
    for number in row:
            if number != 0:
                non_zero_numbers.append(number)

    merged_numbers = []

    i = 0
    while i < len(non_zero_numbers):
        if i + 1 < len(non_zero_numbers) and non_zero_numbers[i] == non_zero_numbers[i + 1]:
            merged_numbers.append(non_zero_numbers[i] + non_zero_numbers[i + 1])
            i += 2
        else:
            merged_numbers.append(non_zero_numbers[i])
            i += 1

    while len(merged_numbers) < 4:
        merged_numbers.append(0)        
    return merged_numbers
    
def move_row_right(row):
    non_zero_numbers = []
    for number in row:
            if number != 0:
                non_zero_numbers.append(number)

    merged_numbers = []

    i = 0
    while i < len(non_zero_numbers):
        if i + 1 < len(non_zero_numbers) and non_zero_numbers[i] == non_zero_numbers[i + 1]:
            merged_numbers.append(non_zero_numbers[i] + non_zero_numbers[i + 1])
            i += 2
        else:
            merged_numbers.append(non_zero_numbers[i])
            i += 1

    while len(merged_numbers) < 4:
        merged_numbers.insert(0, 0)        
    return merged_numbers

def move_row_up(col):
    non_zero_numbers = []
    for number in col:
            if number != 0:
                non_zero_numbers.append(number)

    merged_numbers = []

    i = 0
    while i < len(non_zero_numbers):
        if i + 1 < len(non_zero_numbers) and non_zero_numbers[i] == non_zero_numbers[i + 1]:
            merged_numbers.append(non_zero_numbers[i] + non_zero_numbers[i + 1])
            i += 2
        else:
            merged_numbers.append(non_zero_numbers[i])
            i += 1

    while len(merged_numbers) < 4:
        merged_numbers.append(0)        
    return merged_numbers

def move_row_down(col):
    non_zero_numbers = []
    for number in col:
            if number != 0:
                non_zero_numbers.append(number)

    merged_numbers = []

    i = 0
    while i < len(non_zero_numbers):
        if i + 1 < len(non_zero_numbers) and non_zero_numbers[i] == non_zero_numbers[i + 1]:
            merged_numbers.append(non_zero_numbers[i] + non_zero_numbers[i + 1])
            i += 2
        else:
            merged_numbers.append(non_zero_numbers[i])
            i += 1

    while len(merged_numbers) < 4:
        merged_numbers.insert(0, 0)        
    return merged_numbers

for row in board:
    print(' '.join(str(cell) for cell in row))


