def rotate_row_left(row, n=1):
    return [row[n:],row[:n]]

original_row = [1, 2, 3, 4, 5]
rotated_row = rotate_row_left(original_row)
print(rotated_row)
