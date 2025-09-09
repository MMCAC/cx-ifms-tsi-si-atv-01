import math

р = [5.4, 3.7, 1.5, 0.2]
g = [7.2, 3.6, 6.1, 2.5]
result = 0

for x in range(0,4):
      result = result + (p[x] - g[x])**2

result = math.sqrt(result)

print(result)
