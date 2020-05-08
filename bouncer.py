age=input("enter the age")
if age:
    age=int(age)
    if age >= 21:
        print("you are good to enter and can drink!")
    elif age >= 18:
        print("you can enter,but need a wristband!")
    else:
        print("you cant come in ...sorry, you are too young")
else:
     print("please enter an age!")
     