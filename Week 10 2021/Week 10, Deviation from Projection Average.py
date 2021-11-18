# Stats provided by NFL Fantasy
# Week 10, Deviation from Projection
# Averaging both the projected values and the actual values for both the top
# 10 RBs and WRs and the top 10 projected RBs and WRs

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(12, 6), dpi=80)

top10RBs = np.average(np.array([25.80,25.40,24.90,21.60,21.10,20.80,19.30,19.26,19.20,18.80]))
top10RBsProj = np.average(np.array([7.22,14.80,11.27,16.68,15.58,10.70,16.12,13.55,11.02,13.20]))

top10ProjRBs = np.average(np.array([13.40,15.30,21.60,19.30,15.00,21.10,4.40,25.40,10.60,13.20]))
top10ProjRBsProj = np.average(np.array([17.29,17.14,16.68,16.12,15.75,15.58,15.17,14.80,14.73,14.52]))

top10WRs = np.average(np.array([27.80,26.20,25.60,24.00,22.10,20.60,18.40,17.70,16.30,14.10]))
top10WRsProj = np.average(np.array([15.41,14.85,12.30,14.00,5.54,11.24,14.30,18.32,6.80,10.73]))

top10ProjWRs = np.average(np.array([17.70,11.30,2.80,27.80,26.20,4.10,18.40,13.20,24.00,9.20]))
top10ProjWRsProj = np.average(np.array([18.32,16.61,15.49,15.41,14.85,14.59,14.30,14.13,14.00,13.69]))

actualPoints = np.array([top10RBs,top10ProjRBs,top10WRs,top10ProjWRs])
projPoints = np.array([top10RBsProj,top10ProjRBsProj,top10WRsProj,top10ProjWRsProj])
labels = np.array(["Top 10\nRBs","Top 10 Proj.\nRBs","Top 10\nWRs","Top 10 Proj.\nWRs"])

plt.plot(labels, actualPoints, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(projPoints, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.title("Week 10, Devitation from Projection")
plt.legend()
plt.grid()
plt.show()



