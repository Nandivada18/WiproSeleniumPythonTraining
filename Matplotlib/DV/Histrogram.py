import matplotlib.pyplot as plt
import pandas as pd

#Histogram using pandas
data = {
    "Day":["mon","tues","wed","thurs","fri","sat"],
    "Steps":[100,200,500,60,800,750]
}
df = pd.DataFrame(data)
df.plot(x="Day",y="Steps",kind="hist")
plt.title("Steps by Day")
plt.xlabel("Day")
plt.ylabel("Steps")
plt.show()


#Histogram using the numpy
import numpy as np
import matplotlib.pyplot as plt
x =np.array([1,2,3,4,5])
#y -axis data
y =x*2
plt.hist(x,y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Histogram plot")
plt.show()