import numpy as np
import matplotlib.pyplot as plt


def standard_deviation(V):
    d = np.sum(V["y"]) / V.shape[0]
    print(f"Durchschnitt: {d}")
    v = np.sum(np.power(V["y"]-d, 2)) / V.shape[0]
    print(f"Varianz: {v}")
    s = np.sqrt(v)
    print(f"Standardabweichung: {s}")
    print(f"Durchschnitt/Standardabweichung: {d/s}")


def mean(Vx, Vy):
    n = Vx[np.nonzero(Vx)].size
    return np.sum(np.array([y/x for x, y in zip(Vx, Vy) if (x != 0)]))/n


# Daten aus Datei einlesen
values = []
with open("derivative_values.txt", "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        x, y = line.split(" ")
        values.append((float(x), float(y)))

print(values)

# Durchschnitt, Varianz und Standardabweichung berechnen
dt = np.dtype([("x", float), ("y", float)])
V = np.array(values, dtype=dt)
standard_deviation(V)

# Daten anzeigen
xMin = -2.5
xMax = 2.5
k = mean(V["x"], V["y"])
print(f"k={k}")
x = np.linspace(xMin, xMax, 300, endpoint=False)
y = k * np.ones(shape=x.shape)

plt.xlabel("x")
plt.ylabel("Delta Y")
plt.plot(*zip(*values))
# plt.plot(x, y)
# plt.xlim(xMin, xMax)
plt.ylim(-0.02, 0.02)
# plt.draw()
plt.show()
