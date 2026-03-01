# MISD: Multiple instructions on the SAME data

import numpy as np

data = np.array([1, 2, 3, 4, 5])

print("=== MISD: Multiple Operations, Same Data ===")
print("Input:", data)
print(f"  Processor 1 (SUM):  {np.sum(data)}")
print(f"  Processor 2 (MEAN): {np.mean(data)}")
print(f"  Processor 3 (MAX):  {np.max(data)}")
print(f"  Processor 4 (MIN):  {np.min(data)}")