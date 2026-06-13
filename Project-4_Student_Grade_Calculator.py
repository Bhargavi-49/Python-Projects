subject1 = int(input("Please enter your Maths subject marks: "))
subject2 = int(input("Please enter your Physics subject marks: "))
subject3 = int(input("Please enter your Social subject marks : "))
subject4 = int(input("Please enter your English subject marks: "))
total = subject1 + subject2 + subject3 + subject4
average = (total) /4
print("Total marks:",total)
print("Average:",average)
if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
elif average >= 40:
    print("Grade: D")
else:
    print("Grade: Fail")
