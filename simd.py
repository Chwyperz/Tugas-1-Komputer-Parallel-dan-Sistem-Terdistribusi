

import numpy as np
import threading
import time

A = np.array([1, 2, 3, 4, 5])
B = np.array([10, 20, 30, 40, 50])
result = np.zeros(5, dtype=int)

def add_element(i):
    time.sleep(0.1)  
    result[i] = A[i] + B[i]
    print(f"  Element {i}: {A[i]} + {B[i]} = {result[i]}")

print("=== SIMD: Vectorized Addition ===")
print(f"A: {A.tolist()}")
print(f"B: {B.tolist()}")
print("\nSame instruction (ADD) applied to ALL elements")

threads = [threading.Thread(target=add_element, args=(i,)) for i in range(len(A))]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"\nResult: {result.tolist()}")
print("[SIMD] All elements processed in one go")
