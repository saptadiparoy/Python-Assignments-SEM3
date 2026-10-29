import matplotlib.pyplot as plt

#sample data
customers = ["C101", "C1O2", "C103" ,"C104", "C105", "C106"]
charges = [300, 500, 400, 350, 700, 650]
tenure = [12,3,9,6,10,5]
churn = ["No", "Yes", "No", "No", "Yes", "No" ]

#churn
yes_count = churn.count("Yes")
no_count = churn.count("No")

#One window for all graphs
plt.figure(figsize = (14,9))

#bar graph
plt.subplot(2,3,1)
plt.bar(customers, charges)
plt.xlabel("Customer ID")
plt.ylabel("Charges")
plt.title("Bar Graph")
plt.xticks(rotation = 60)

#Histogram
plt.subplot(2,3,2)
plt.hist(charges, bins = 5, edgecolor = "pink")
plt.xlabel("Monthly Charge")
plt.ylabel("No. of Customers")
plt.title("Histogram")

#pie chart
plt.subplot(2,3,3)
plt.pie([yes_count, no_count],
        labels= ["Churn Yes", "Churn No"],
        autopct = "%1.1f%%",
        startangle = 60)
plt.title("Pie Chart")

#Scatter plot
plt.subplot(2,3,4)
plt.scatter(tenure, charges)
plt.xlabel("Tenure")
plt.ylabel("Charges")
plt.title("Scatter Plot")

#line graph
plt.subplot(2,3,5)
plt.plot(customers, charges, marker = "+")
plt.xlabel("customer id")
plt.ylabel("charges")
plt.title("Line Graph")
plt.xticks(rotation = 50)

plt.tight_layout()
plt.show()