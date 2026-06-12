import matplotlib.pyplot as plt

# Sample data
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 200, 150, 90, 230]

# Create the chart
plt.plot(months, sales, marker="o", color="blue")

# Add labels
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

# Show it
plt.show()