# Author: Maadhyam Rawal


# Algorithm Description 
# Goal: Reduce the overall cost for each of the k groups.

# The algorithm works like this:
# Step:1 ----> Read the following inputs: array A, n (array size), and k (number of groups).
# Step:2 ----> Verify the input: Make sure that 1 ≤ k ≤ n.
# Step:3 ----> To enable O(1) range sum queries, create a prefix sum array.
# Step:4 ----> For group A[i..j-1], define a cost function as (sum)^2.
# Step:5 ----> Make use of dynamic_programming programming
#       - dynamic_programming[i][j] = the least cost needed to divide the first i elements into j groups.
#       - Base case: dynamic_programming[0][0] = 0 (cost of an empty array is 0).
#       - Transition: take into account all prior slices x for each i, j, and calculate:
#       - dynamic_programming[i][j] = min(dynamic_programming[x][j-1] + cost(x, i))
# Step:6 ----> To reconstruct the cut points, save the best cut index in a `transition` table.
# Step:7 ----> To recover the slices, go back from (n, k) after calculating the DP table.
# Step:8 ----> Provide the list of group boundaries, including 0 and n, along with the minimum cost.



n = int(input())
k = int(input())
A = list(map(int, input().split()))


if k < 1 or k > n or n != len(A):
    print("Invalid input!!")
    exit()


prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + A[i]


def sum_range(i, j):
    value = prefix[j] - prefix[i]
    return value


def group_value(i, j):
    value = sum_range(i, j) ** 2
    return value


dynamic_programming = [[float('inf')] * (k + 1) for _ in range(n + 1)]
transition = [[-1] * (k + 1) for _ in range(n + 1)]
dynamic_programming[0][0] = 0  # Base case


for i in range(1, n + 1):
    for j in range(1, k + 1):
        for x in range(j - 1, i):
            cost = dynamic_programming[x][j - 1] + group_value(x, i)
            if cost < dynamic_programming[i][j]:
                dynamic_programming[i][j] = cost
                transition[i][j] = x


slices = []

i=n
j=k

while j > 0:
    slices.append(i)
    i = transition[i][j]
    j =j - 1
slices.append(0)
slices.reverse()


print(dynamic_programming[n][k])
print(slices)


# Time Complexity Analysis

# Let:
# n = number of elements in the array
# k = number of groups

# 1. Prefix sum computation
# We loop once through the array to build the prefix sum---> O(n)

# 2. Dynamic Programming Table Filling
# We loop through:
#   i from 1 to n----------> O(n)
#   j from 1 to k----------> O(k)
#   x from j-1 to i-1------> O(n) [This is for the worst case for each (i, j)]
#   
# So total time for filling the DP table: O(n * k * n) = O(n^2 * k)

# 3. Backtracking through transition table to recover group boundaries
# We do this k times (once per group) → O(k)

# Final Total Time Complexity:
# O(n)-------> for prefix sums
# O(n^2*k)---> for DP table
# O(k)-------> for backtracking
# Overal;----> O(n^2 * k)         [dominated by DP]

# So the overall time complexity is O(n^2 * k)






# Teaching Materials Used

#  Dynamic Programming: Using the framework covered in Week 5 like the Knapsack problem 
#                       the algorithm constructs optimal subarray solutions.

#  Prefix Sums: As taught in array processing techniques,
#               these are used to calculate range sums in constant time.

#  Custom Cost Function: Non-linear optimisation is modelled by the squared sum cost, 
#                        which is similar to the problems given in exercises.

#  Backtracking: Techniques used are taken from the reconstruction of group boundaries 
#                from the dynamic programming table.

#  Lecture References: Lecture 1 (Grouping problems) Week 9 
#                      Week 5–6 (Dynamic Programming fundamentals)
