import numpy as np

print("This program goes from degrees to radians.")
degrees = float(input("Enter the angle in degrees: "))
print("The angle is equivalent to: ", ((degrees*np.pi)/180)," radians")
