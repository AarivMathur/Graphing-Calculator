import matplotlib.pyplot as plt

def squared_values(x):
    return x * x

x = input().split(',')
y = input().split(',')

plt.plot(x, y)
plt.show()