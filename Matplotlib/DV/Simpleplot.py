import matplotlib.pyplot as plt
import pandas as pd

x = [1,2,3,4,5]
y = [1,4,9,16,25]

plt.plot(x,y)

#x axis label
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple plot')

#show method will display the data
plt.show()

#simple data
subjects = ["Maths", "Science","English", "History","Computer"]
marks = [85,78,92,74,88]

#Creates the Line graph
plt.plot(subjects,marks)

plt.title("student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# matplotlip with pandas integration
data = {
    "Month":["John", "Feb", "Mar", "Apr", "May"],
    "Sales":[100,150,130,170,160]
}
df = pd.DataFrame(data)
plt.plot(df["Month"],df["Sales"])
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()