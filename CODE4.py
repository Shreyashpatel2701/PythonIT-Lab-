class Student :
    def displaygrade(self):
        Totalmarks=int(self.science_marks + self.maths_marks +self.english_marks)
        print(Totalmarks)
        Precentage = int(Totalmarks/3)
        if Precentage >= 75 :
            print(" GRADE : A")
            print(" STATUS : PASS")
        elif Precentage >=60 and Precentage < 75 :
            print(" GRADE : B")
            print(" STATUS : Pass ")
        elif Precentage >=50 and Precentage <60 :
            print(" GRADE : C")
            print(" STATUS : PASS")

    def __init__(self,name,id,age,maths_marks,scienece_marks,english_marks):
        self.name = name
        self.id=id
        self.age=age
        self.maths_marks=maths_marks
        self.science_marks=scienece_marks
        self.english_marks=english_marks


name = input("Enter Student Name \n")
id   = int(input("ENTER YOUR ID \n"))
Age = int(input("ENTER YOUR Age "))
Maths_marks = int(input("ENTER YOUR  MATHS_MARKS"))
Science_marks = int(input("ENTER YOUR SCIENCE MARKS"))
English_marks=int(input("ENTER YOUR ENGLISH MARKS "))

s1 = Student(name,id,Age,Maths_marks,Science_marks,English_marks)
print(s1.displaygrade())
