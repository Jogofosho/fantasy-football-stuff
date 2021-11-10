import numpy as np
import matplotlib.pyplot as plt

pointsFor = [84.10,163.26,119.48,137.24,141.08,108.08,154.48,68.76,85.34]
pointsAgainst = [121.38,128.10,127.12,152.62,174.78,142.80,103.44,104.50,86.78]

pf = np.array(pointsFor)
pa = np.array(pointsAgainst)
diff = pf - pa

xpoints = []
for i in range(1,10):
    xpoints.append(str(i))

ypoints = diff


plt.plot(xpoints, ypoints, 'o', ls = "-")
plt.axhline(0, c='r')
plt.xlabel("Week")
plt.ylabel("Differential")
plt.show

