print("Enter the marks obtained (out of 100):-")
sub1 = int(input("English : "))
sub2 = int(input("Mathematics : "))
sub3 = int(input("Science : "))
sub4 = int(input("Computer : "))
sub5 = int(input("Social Studies : "))
total = sub1 + sub2 + sub3 + sub4 + sub5
avg = total//5
if avg>90 :
    grade = 'A'
elif avg>80 :
    grade = 'B'
elif avg>70 :
    grade = 'C'
elif avg>60 :
    grade = 'D'
elif avg>50 :
    grade = 'E'
else :
    grade = 'F'
print("Grade : ", grade)