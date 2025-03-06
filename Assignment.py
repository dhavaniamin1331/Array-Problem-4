def min_flips(arr):
    count_zeros = arr.count(0) # Count occurrences of 0 
    count_ones = arr.count(1) # Count occurences of 1
    return min(count_zeros, count_ones) # Minimum flips needed 

# Example usage 
arr = [0, 1, 0, 1, 1, 0, 0, 1] # Example input
print("Minimum flips required:", min_flips(arr))