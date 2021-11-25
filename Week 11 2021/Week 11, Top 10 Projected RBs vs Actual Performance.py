# Stats provided by NFL Fantasy
# Week 11, Top 10 Projected RBs vs Actual Performance

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(12, 6), dpi=80)

actualPoints = np.array([14.40,38.50,21.40,51.90,21.40,21.00,21.10,12.70,10.40,6.30])
projPoints = np.array([17.07,16.89,16.53,16.27,15.71,15.48,15.24,15.12,14.91,14.32])
players = np.array(["N. Harris\n(PIT)","A. Ekeler\n(LAC)","N. Chubb\n(CLE)","J. Taylor\n(IND)",
                    "C. McCaffrey\n(CAR)","D. Cook\n(MIN)","D. Swift\n(DET)","A. Dillon\n(GB)",
                    "L. Fournette\n(TB)","J. Wilson\n(SF)"])

plt.plot(players, actualPoints, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(projPoints, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.title("Week 11, Top 10 Projected RBs vs Actual Performance")
plt.legend()
plt.grid()
plt.show()