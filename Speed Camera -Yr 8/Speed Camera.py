#Code for police speed camera

speed = int(input("Enter driver's speed: "))

if speed >= 75:
    print("Issue Speeding fine")
elif speed <= 70:
  print("Warning Speeding fine")
elif speed >= 60:
  print ("Warning Speeding fine")
else:
  print("Everything is fine")
