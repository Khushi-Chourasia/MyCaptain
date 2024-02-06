n = int(input("Enter the number of subjects :-"))
total = 0
for i in range(1,n+1):
    marks = int(input("Enter the marks for subject " + str(i) + ":"))
    total+= marks
avg = total//n
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