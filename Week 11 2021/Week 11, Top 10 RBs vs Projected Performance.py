# Stats provided by NFL Fantasy
# Week 11, Top 10 RBs vs Projected Performance

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(12, 6), dpi=80)

actualPoints = np.array([51.90,38.50,24.30,21.40,21.40,21.10,21.00,18.40,17.10,17.00])
projPoints = np.array([16.27,16.89,13.16,16.53,15.71,15.24,15.48,13.76,12.93,11.97])
players = np.array(["J. Taylor\n(IND)","A. Ekeler\n(LAC)","J. Mixon\n(CIN)","N. Chubb\n(CLE)",
                    "C. McCaffrey\n(CAR)","D. Swift\n(DET)","D. Cook\n(MIN)","J. Conner\n(ARI)",
                    "M. Gaskin\n(MIA)","D. Freeman\n(BAL)"])

plt.plot(players, actualPoints, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(projPoints, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.title("Week 11, Top 10 RBs vs Projected Performance")
plt.legend()
plt.grid()
plt.show()




