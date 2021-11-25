# Stats provided by NFL Fantasy
# Week 11, Top 10 Projected WRs vs Actual Performance

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(12, 6), dpi=80)

actualPoints = np.array([15.90,27.00,16.30,7.30,33.20,11.50,2.90,16.20,15.50,2.10])
projPoints = np.array([17.29,15.80,15.63,15.34,14.15,14.00,13.77,13.73,13.50,13.33])
players = np.array(["D. Samuel\n(SF)","D. Adams\n(GB)","S. Diggs\n(BUF)","A. Brown\n(TEN)",
                    "J. Jefferson\n(MIN)","J. Chase\n(CIN)","C. Lamb\n(DAL)","C. Godwin\n(TB)",
                    "T. Hill\n(KC)","D. Harris\n(NO)"])

plt.plot(players, actualPoints, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(projPoints, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.title("Week 11, Top 10 Projected WRs vs Actual Performance")
plt.legend()
plt.grid()
plt.show()