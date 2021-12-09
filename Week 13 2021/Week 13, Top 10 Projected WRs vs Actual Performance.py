"""
Stats provided by NFL Fantasy
Week 13, Top 10 Projected WRs vs Actual Performance
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(12, 6), dpi=80)

actual_points = np.array([22.90,30.10,3.20,7.10,19.90,26.50,14.70,5.20,22.70,2.50])
proj_points = np.array([18.49,17.50,14.64,14.05,13.72,13.30,13.19,12.80,12.70,12.65])
players = np.array(["C. Kupp\n(LAR)","J. Jefferson\n(MIN)","T. Hill\n(KC)","S. Diggs\n(BUF)",
                    "K Allen\n(LAC)","D. Johnson\n(PIT)","H. Renfrow\n(LA)","D. Mooney\n(CHI)",
                    "C. Godwin\n(TB)","D. Smith\n(PHI)"])

plt.plot(players, actual_points, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(proj_points, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.title("Week 13, Top 10 Projected WRs vs Actual Performance")
plt.legend()
plt.grid()
plt.show()


