import matplotlib.pyplot as plt

days = ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"]

# Average temperatures (in °C) calculated as the mean of high and low temperatures
temperatures = [(28.6 + 21.4)/2, (27.7 + 21.7)/2, (26.6 + 21.6)/2, (29.4 + 20.0)/2, (28.8 + 16.2)/2, (27.0 + 18.0)/2]

# Plotting the line graph
plt.figure(figsize=(10, 5))
plt.plot(days, temperatures, marker="o", linestyle="-", color="b", label="Average Temperature (°C)")

plt.xlabel("Days of the Week")
plt.ylabel("Average Temperature (°C)")
plt.title("Temperature Variations in Jessore Over a Week")
plt.legend()
plt.grid(True)

# Display the plot
plt.show()
