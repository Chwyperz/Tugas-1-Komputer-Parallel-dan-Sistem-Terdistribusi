# SISD: One instruction, one data, one step at a time

A = [1, 2, 3, 4, 5]
B = [10, 20, 30, 40, 50]
result = []

print("=== SISD: Serial Addition ===")
for i in range(len(A)):
    r = A[i] + B[i]
    result.append(r)
    print(f"  Step {i+1}: {A[i]} + {B[i]} = {r}")

print("Result:", result)