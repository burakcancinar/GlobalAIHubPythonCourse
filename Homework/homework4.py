Students=[]
for i in range(5):  # 5 student
    name=input("Enter student's name : ")
    midterm=float(input("Enter MidTerm Grade: "))
    project=float(input("Enter Project Grade: "))
    final=float(input("Enter Final Grade: "))
    PassingGrade=float((midterm*0.3)+(project*0.3)+(final*0.4))
    Students.append({'StudentName':name,'MidTerm':midterm,'ProjectGrade:':project,'FinalGrade':final,'passingGrade':PassingGrade})
print(Students)
Students.sort(key=lambda a:(-a['passingGrade']))
print("Sorted Values")
for i in Students:
    print(i['StudentName'],": ",i['passingGrade'])
    