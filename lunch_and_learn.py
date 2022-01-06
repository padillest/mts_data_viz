# Importing libraries 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import plotly.express as px 

# Reading in the CSV file
df = pd.read_csv("daily_shelter_occupancy_2020.csv")

# Creating a copy of the dataframe 
data = df.copy()

# Plotting a simple line using matplotlib
plt.plot([1,2,3], [2,4,6])

# Calling the plot made in the background 
plt.show()

# Storing the x- and y-values, and adding labels to the graph 

# Creating a list of x- and y-values
x = [1,2,3]
y = [1,4,9]

# Plotting the variables 
plt.plot(x, y)

# Adding x- and y-axis labels 
plt.xlabel("X-Values")
plt.ylabel("X-Values Squared")

# Adding a title 
plt.title("Our Basic Graph")

# Calling the plot
plt.show()

# Adding a legend to the graph 

x = [1,2,3]
y = [1,4,9]

# Creating a second set of values 
x2 = [1,2,3]
y2 = [4,6,8]

# Plotting both lines on the same graph 
plt.plot(x, y, label="First Line")
plt.plot(x2, y2, label="Second Line")

# Adding x- and y-axis labels 
plt.xlabel("X-Values")
plt.ylabel("X-Values Squared")

# Adding a title 
plt.title("Our Basic Graph")

# Adding a legend
plt.legend()

# Calling the plot
plt.show()

# Cleaning and visualizing the dataset

# Lowering the column names 
data.columns = data.columns.str.lower()

# Converting the date column to a datetime object and storing the month as a new variable
data = data.assign(month=pd.to_datetime(data["occupancy_date"]).dt.month)

# Creating a new dataframe of the sum of the occupancies per month
monthly_occupancy = data.groupby(by="month").sum()

# Creating a bar graph with custom x-ticks 

# Plotting the bar graph
monthly_occupancy.plot.bar(y="occupancy",
                          legend=None)

# Creating the x-tick positions
positions = [0, 1, 2, 3, 
             4, 5, 6, 7, 
             8, 9, 10, 11]

# Creating a list of the names for the new x-ticks
months = ["Jan", "Feb", "Mar", "Apr",
          "May", "Jun", "Jul", "Aug",
          "Sep", "Oct", "Nov", "Dec"]

# Adding labels to the graph
plt.xlabel("Month")
plt.ylabel("Occupancy")
plt.title("Monthly Occupancy in Toronto 2020")

# Altering the x-ticks to display the new labels, on a rotation
plt.xticks(ticks=positions, 
           labels=months,
           rotation=45)

# Showing the final graph
plt.show()

# Comparing monthly occupancy differences 

# Refining for the January and December sector occupancy 
jan_sector_occupancy = data[data["month"]==1].groupby(by="sector").sum()
dec_sector_occupancy = data[data["month"]==12].groupby(by="sector").sum()

# Plotting two subplots of the monthly data

# Creating a figure 
fig = plt.figure(figsize=(16,16))

# Creating the first subplot

# Plots a graph within the first subplot space
ax1 = fig.add_subplot(121)

# Creating a list of sector groups 
sector_group = ["Co-ed", 
                "Families", 
                "Men",
                "Women", 
                "Youth"]

# Plots a pie graph, emphasizing the youth group, and adding a percentage 
ax1.pie(jan_sector_occupancy["occupancy"],
        labels=sector_group,
        explode=(0, 0, 0, 0, 0.2),
        autopct="%1.1f%%")

# Adding a title for the first plot 
plt.title("Toronto Occupancy Distribution - January 2020")

# Plots a graph within the second subplot space
ax2 = fig.add_subplot(122)

# Plots a pie graph, emphasizing the youth group, and adding a percentage 
ax2.pie(dec_sector_occupancy["occupancy"],
        labels=sector_group,
        explode=(0, 0, 0, 0, 0.2),
        autopct="%1.1f%%")

# Adding a title for the second plot
plt.title("Toronto Occupancy Distribution - December 2020")

# Showing the subplots 
plt.show()

# Creating an interactive plot 

# Grouping the data by the organization name and the sector and summing the yearly occupancy
group_organization_sector = data.groupby(by=["organization_name", 
                                             "sector"]).sum().reset_index()

# Ploting a Plotly Sunburst Plot 
fig = px.sunburst(group_organization_sector,
                  path=["organization_name", "sector"],
                  values="occupancy")

# Showing the plot
fig.show()






