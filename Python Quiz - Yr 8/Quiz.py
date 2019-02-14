#Quiz Question

import time

time.sleep(1)
answer = input("What was the most popular programming language in 2017?: ")
answer = answer.title()
counter = 1

time.sleep(2)
if answer == "Python":
   print("Correct! You had" ,counter, "attempt, Well done.")

while answer != "Python":
    answer = input("Incorrect, try again: ")
    time.sleep(2)
    answer = answer.title()
    counter = counter + 1
time.sleep(2)
input("Press enter to exit program")
