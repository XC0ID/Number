n = int(input("Enter a positive integer: "))
if n <= 0:
  print("Please enter a number greater than 0.")
else:
    d = {i: i * i for i in range(1, n + 1)}
print(d)  
print("Invalid input! Please enter an integer.")
