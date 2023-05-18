import random
import time

def solution_alphabet(riddle):
    output_str = list(riddle)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if output_str[0] == '?':
        output_str[0] = 'a'
    for i in range(1, len(output_str) - 1):

        if output_str[i] == '?':

            prev_ch = output_str[i - 1]
            next_ch = output_str[i + 1]
            
            for char in alphabet:
                if char != prev_ch and char != next_ch:
                    output_str[i] = char
                    break
    if output_str[-1] == '?':
        output_str[-1] = 'a'
        if output_str[-1] == output_str[-2]:
            for char in alphabet:
                if char != output_str[-2]:
                    output_str[-1] = char
                    break
    return ''.join(output_str)


def solution_unoptimized(A):
    N = len(A)
    result = 0
    for i in range(N):
        for j in range(i, N):
            if A[i] != A[j]:
                result = max(result, j - i)
    return result

def solution_optimized(A):
    lookup = {}
    result = 0
    lookup[A[0]] = 0
    for idx, val in enumerate(A):
        if idx == 0:
            continue
        if val in lookup:
            result = max(result, (idx-1) - lookup[val])
        lookup[val] = idx
    return result

def generate_input_file(filename, num_count):
    with open(filename, 'w') as file:
        for _ in range(num_count):
            file.write(str(random.randint(10000, 100000)) + '\n')

# Read input text file and test the solution function
def test_solution(filename):
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]

        t_start = time.perf_counter()
        max_distance_optimized = solution_optimized(numbers)
        t_end = time.perf_counter()

        t_start_unoptimized = time.perf_counter()
        max_distance_unoptimized = solution_unoptimized(numbers)
        t_end_unoptimized = time.perf_counter()

        
        # Print the result and execution time
        print(f"Maximum Distance: {max_distance_optimized}")
        print(f"Execution Time for normal solution: {t_end - t_start} seconds")

        print(f"Maximum Distance: {max_distance_unoptimized}")
        print(f"Execution Time for normal solution: {t_end_unoptimized - t_start_unoptimized} seconds")



# Generate input file with random numbers
input_filename = 'input.txt'
number_count = 80000
generate_input_file(input_filename, number_count)


print('Sample Test  ------------------>')
print(solution_alphabet('ab?ac?'))
print(solution_optimized([4,6,2,2,6,6,4]))
print('End sample Test  ------------------>')

# Test the solution function using the generated input file
test_solution(input_filename)