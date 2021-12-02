# Stats provided by NFL Fantasy
# Week 12, Top 10 Projected WRs vs Actual Performance

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(12, 6), dpi=80)

actual_points = np.array([15.10,11.26,14.40,20.30,16.90,2.70,14.00,3.10,12.00,1.80])
proj_points = np.array([18.00,16.64,16.60,15.28,15.04,14.53,13.99,13.77,13.11,13.02])
players = np.array(["C. Kupp\n(LAR)","J. Jefferson\n(MIN)","D. Adams\n(GB)","D. Samuel\n(SF)",
                    "S. Diggs\n(BUF)","C. Godwin\n(TB)","D. Johnson\n(PIT)","M. Evans\n(TB)",
                    "K. Allen\n(LAC)","D. Metcalf\n(SEA)"])

plt.plot(players, actual_points, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(proj_points, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.title("Week 12, Top 10 RBs vs Projected Performance")
plt.legend()
plt.grid()
plt.show()
