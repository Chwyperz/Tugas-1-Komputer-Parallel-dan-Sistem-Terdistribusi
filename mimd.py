# MIMD: Multiple processes, each with different data AND different task

from multiprocessing import Process, Queue

def task_sum(data, q):
    result = sum(data)
    print(f"  Process 1 | SUM  {data} = {result}")
    q.put(result)

def task_product(data, q):
    result = 1
    for x in data:
        result *= x
    print(f"  Process 2 | PRODUCT {data} = {result}")
    q.put(result)

if __name__ == "__main__":
    q = Queue()

    print("=== MIMD: Two Processes, Different Data & Task ===")
    p1 = Process(target=task_sum,     args=([1, 2, 3], q))
    p2 = Process(target=task_product, args=([4, 5, 6], q))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    results = [q.get() for _ in range(2)]
    print("Collected results:", results)