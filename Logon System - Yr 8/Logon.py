import time

print ("Welcome please enter your credentials for the server: FOR")
print ("*************************************************************************")
time.sleep(1)
print ("Please enter your Username on FOR")
username = input()

if username == "shepl084.309":
    print ("Correct")
else:
    print ("Access Denied")
  
print ("Please enter your Password on FOR")
password = input()
if password == "Google" and username == "shepl084.309":
    print ("Correct")
    time.sleep(5)
    print ("Welcome", username)

else:
    print ("Access Denied")
    time.sleep(2)
    print ("Please enter your backup key")
    phonecode = input()
    time.sleep(1)

    if phonecode == "6789":
        print ("Correct")
        print ("Other Credentials Incorrect")
        input("Please press enter to exit Log On")
        
    else:
        print ("Access Denied")
        time.sleep(1)
        print("Credentials Incorrect")

input("Press enter to exit program")
