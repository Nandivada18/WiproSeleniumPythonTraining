import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Line plot using pandas
data = {
    "Day":["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Steps":[4000,5500,7000,6500,8000]
}
df = pd.DataFrame(data)
df.plot(x="Day",y="Steps",kind="line")
plt.title("Daily Steps count",fontname="Brush Script MT",fontsize=16)
plt.xlabel("Day", fontname="Brush Script MT",fontsize=16)
plt.ylabel("Steps", fontname="Brush Script MT",fontsize=16)

#get current axes
ax = plt.gca()
#setting the background color
ax.set_facecolor("yellow")
plt.show()

#font size changing