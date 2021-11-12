import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(12, 6), dpi=80)

actualPoints = np.array([23.90,20.10,19.30,19.10,17.80,16.50,16.40,16.10,15.70,15.60])
projPoints = np.array([3.86,9.77,4.41,8.06,1.13,8.75,11.30,12.32,6.24,7.05])

players = np.array(["E. Moore", "D. Smith", "O. Zaccheaus", "D. Mooney", "M. Turner", 
                    "T. Patrick", "K. Allen", "M. Brown", "B. Aiyuk", "D. Peoples-Jones"])

plt.plot(players, actualPoints, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(projPoints, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.title("Week 9 Top WRs: Projected vs. Actual")
plt.legend()
plt.grid()
plt.show()




