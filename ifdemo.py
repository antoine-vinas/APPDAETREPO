# If Demo


sub1grade = int(input("Enter Grade for Subject 1: "))
sub2grade = int(input("Enter Grade for Subject 2: "))
sub3grade = int(input("Enter Grade for Subject 3: "))
sub4grade = int(input("Enter Grade for Subject 4: "))
sub5grade = int(input("Enter Grade for Subject 5: "))


average = (sub1grade + sub2grade + sub3grade + sub4grade + sub5grade) / 5


print("Average Grade: ", average)


if average >= 90:
   print("You are excellent!")
elif average >= 70:
   print("You passed!")
   print("Congratulations!")
else:
   print("You failed!")