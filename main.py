import time
import random
import matplotlib.pyplot as plt

from searching import linear_search, binary_search


# různé velikosti vstupu
sizes = [50, 200, 800, 1500, 3000, 7000, 12000, 20000]

linear_times = []
binary_times = []

repeats = 50

for size in sizes:
    data = list(range(size))

    total_linear = 0
    total_binary = 0

    for _ in range(repeats):
        target = random.randint(0, size - 1)

        start = time.time()
        linear_search(data, target)
        total_linear += time.time() - start

        start = time.time()
        binary_search(data, target)
        total_binary += time.time() - start

    linear_times.append(total_linear / repeats)
    binary_times.append(total_binary / repeats)


plt.plot(sizes, linear_times, label="Linear search")
plt.plot(sizes, binary_times, label="Binary search")

plt.xlabel("Velikost vstupu")
plt.ylabel("Průměrný čas (s)")
plt.title("Porovnání sekvenčního a binárního vyhledávání")
plt.legend()

plt.show()