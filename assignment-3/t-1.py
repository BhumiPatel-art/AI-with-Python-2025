import matplotlib.pyplot as plt

x = range(-5, 6)
y1 = [2*i + 1 for i in x]
y2 = [2*i + 2 for i in x]
y3 = [2*i + 3 for i in x]

plt.plot(x, y1, "r-", label="y = 2x + 1")   # red solid line
plt.plot(x, y2, "g--", label="y = 2x + 2")  # green dashed line
plt.plot(x, y3, "b:", label="y = 2x + 3")   # blue dotted line

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Graphs of y = 2x + c (c = 1, 2, 3)")

plt.legend()
plt.grid(True)

plt.show()
