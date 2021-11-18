# Stats provided by NFL Fantasy
# Week 10: Top 10 Projected WRs vs. Actual Performance

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(12, 6), dpi=80)

actualPoints = np.array([17.70,11.30,2.80,27.80,26.20,4.10,18.40,13.20,24.00,9.20])
projPoints = np.array([18.32,16.61,15.49,15.41,14.85,14.59,14.30,14.13,14.00,13.69])
players = np.array(["C. Kupp\n(LAR)","D. Adams\n(GB)","A.J. Brown\n(TEN)","D. Samuel\n(SF)",
                    "S. Diggs\n(BUF)","D. Metcalf\n(SEA)","J. Jefferson\n(MIN)","M. Evans\n(TB)",
                    "T. Hill\n(KC)","C. Godwin\n(TB)"])

plt.plot(players, actualPoints, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(projPoints, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.title("Week 10, Top 10 Projected WRs vs Actual")
plt.legend()
plt.grid()
plt.show()



