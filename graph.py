import matplot
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
label1 = [11.42,11.41,11.40,11.39,11.38,"","","","",""]
label2 = ["","","","","",11.36,11.35,11.34,11.33,11.32]
x1 = [900,1400,1205,1600,400,0,0,0,0,0]
x2 = [0,0,0,0,0,2700,1100,1100,1600,700]

finaldf = pd.DataFrame({"bid":x1, "ask" : x2, "citie1" : label1,"citie2" : label2})
fig, (ax0, ax01) = plt.subplots(1, 2)

ax = finaldf.plot(x="citie1",  y="bid", ax=ax01, kind="barh", legend = False, title = "ask", fontsize=8)
ax.invert_yaxis()
ax01.yaxis.tick_right()
ax.set(ylabel=' Price')
ax = finaldf.plot(x="citie2",  y="ask", ax=ax0, kind="barh", legend = False, title = "bid", fontsize=8)
ax.invert_yaxis()

ax.invert_xaxis()
ax.set(ylabel='')



ax.text(-16,11, 'SHARES', fontsize=15,  color='black')
