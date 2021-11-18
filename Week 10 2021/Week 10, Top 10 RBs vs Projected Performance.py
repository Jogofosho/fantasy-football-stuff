# Stats provided by NFL Fantasy
# Week 10: Top 10 RBs vs Projected Performance

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(12, 6), dpi=80)

actualPoints = np.array([25.80,25.40,24.90,21.60,21.10,20.80,19.30,19.26,19.20,18.80])
projPoints = np.array([7.22,14.80,11.27,16.68,15.58,10.70,16.12,13.55,11.02,13.20])
players = np.array(["A. Dillon\n(GB)","R. Stevenson\n(NE)","D. Williams\n(KC)","J. Taylor\n(IND)","C. McCaffrey\n(CAR)",
                    "A. Gibson\n(WFT)","D. Cook\n(MIN)","E. Elliott\n(DAL)","D. Johnson\n(CLE)","M. Ingram\n(NO)"])

plt.plot(players, actualPoints, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(projPoints, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.title("Week 10, Top 10 RBs vs Projected Performance")
plt.legend()
plt.grid()
plt.show()





