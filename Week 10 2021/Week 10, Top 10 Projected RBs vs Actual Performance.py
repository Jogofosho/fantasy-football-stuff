# Stats provided by NFL Fantasy
# Week 10: Top 10 Projected RBs vs Actual Performance

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(13, 6), dpi=80)

actualPoints = np.array([13.40,15.30,21.60,19.30,15.00,21.10,4.40,25.40,10.60,13.20])
projPoints = np.array([17.29,17.14,16.68,16.12,15.75,15.58,15.17,14.80,14.73,14.52])
players = np.array(["A. Ekeler\n(LAC)","N. Harris\n(PIT)","J. Taylor\n(IND)","D. Cook\n(MIN)","D. Swift\n(DET)",
                    "C.McCaffrey\n(CAR)","C. Patterson\n(ATL)","R. Stevenson\n(NE)","A. Jones\n(GB)","L.Fournette\n(TB)"])

plt.plot(players, actualPoints, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(projPoints, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.title("Week 10, Top 10 Projected RBs vs Actual")
plt.legend()
plt.grid()
plt.show()

