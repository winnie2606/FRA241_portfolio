from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from databaseSetup import *

engine = create_engine('sqlite:///Database.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

# ---------------------------add subject and grade------------------------------#
studenID = "59340500017"
term = "1/2559"
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "FRA141",Grade = "4" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "FRA161",Grade = "3.5" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "GEN101",Grade = "3" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "LNG101",Grade = "4" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "MTH101",Grade = "2.5" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "PHY103",Grade = "3" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "PHY191",Grade = "3.5" )
session.add(student)
# session.commit()

studenID = "59340500021"
term = "1/2559"
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "FRA141",Grade = "4" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "FRA161",Grade = "3.5" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "GEN101",Grade = "4" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "LNG101",Grade = "4" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "MTH101",Grade = "3.5" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "PHY103",Grade = "4" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "PHY191",Grade = "4" )
session.add(student)
# session.commit()

studenID = "59340500035"
term = "1/2559"
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "FRA141",Grade = "4" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "FRA161",Grade = "4" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "GEN101",Grade = "3.5" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "LNG102",Grade = "3.5" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "MTH101",Grade = "3.5" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "PHY103",Grade = "4" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "PHY191",Grade = "3.5" )
session.add(student)

studenID = "58340500011"
term = "1/2559"
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "FRA341",Grade = "2.5" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "FRA361",Grade = "4" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "GEN301",Grade = "3.5" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "LNG301",Grade = "3" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "MTH301",Grade = "3" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "PHY303",Grade = "2.5" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "PHY391",Grade = "3" )
session.add(student)

# session.commit()
#-------------------------------------------------------------------#
studenID = "59340500017"
term = "2/2559"
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "FRA121",Grade = "4" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "FRA142",Grade = "4" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "FRA162",Grade = "3.5" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "FRA163",Grade = "3" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "GEN111",Grade = "3.5" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "GEN121",Grade = "3.5" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "MTH102",Grade = "2.5" )
session.add(student)
# session.commit()

studenID = "59340500021"
term = "2/2559"
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "FRA121",Grade = "4" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "FRA142",Grade = "4" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "FRA162",Grade = "3.5" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "FRA163",Grade = "3.5" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "GEN111",Grade = "3.5" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "GEN121",Grade = "4" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "MTH102",Grade = "3.5" )
session.add(student)
# session.commit()

studenID = "59340500035"
term = "2/2559"
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "FRA121",Grade = "4" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "FRA142",Grade = "4" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "FRA162",Grade = "3.5" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "FRA163",Grade = "4" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "GEN111",Grade = "3.5" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "GEN121",Grade = "4" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "MTH102",Grade = "3.5" )
session.add(student)

studenID = "58340500011"
term = "2/2559"
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "FRA321",Grade = "4" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "FRA342",Grade = "4" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "FRA362",Grade = "3.5" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "FRA363",Grade = "3" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "GEN311",Grade = "3.5" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "GEN321",Grade = "3.5" )
session.add(student)
student = Academic(Student_ID = studenID,Term = term,
 ID_Subject = "MTH302",Grade = "2.5" )
session.add(student)
# session.commit()

#--------------------------------add GPA---------------------------------------#
term = "1/2559"
gpa = Gpa(Student_ID = "59340500017",Term =term,sum_credit =17,GPA ="3.38")
session.add(gpa)
gpa = Gpa(Student_ID = "59340500021",Term =term,sum_credit =17,GPA ="3.82")
session.add(gpa)
gpa = Gpa(Student_ID = "59340500035",Term =term,sum_credit =17,GPA ="3.76")
session.add(gpa)
gpa = Gpa(Student_ID = "58340500011",Term =term,sum_credit =18,GPA ="3.85")
session.add(gpa)
# session.commit()

term = "2/2559"
gpa = Gpa(Student_ID = "59340500017",Term =term,sum_credit =17,GPA ="3.47")
session.add(gpa)
gpa = Gpa(Student_ID = "59340500021",Term =term,sum_credit =17,GPA ="3.76")
session.add(gpa)
gpa = Gpa(Student_ID = "59340500035",Term =term,sum_credit =17,GPA ="3.79")
session.add(gpa)
gpa = Gpa(Student_ID = "58340500011",Term =term,sum_credit =18,GPA ="3.43")
session.add(gpa)
# session.commit()

#------------------------------add GPAX----------------------------------------#
gpaxx = Gpax(Student_ID ="59340500017",sum_all_credit =34,GPAX ="3.42")
session.add(gpaxx)
gpaxx = Gpax(Student_ID ="59340500021",sum_all_credit =34,GPAX ="3.79")
session.add(gpaxx)
gpaxx = Gpax(Student_ID ="59340500035",sum_all_credit =34,GPAX ="3.77")
session.add(gpaxx)
gpaxx = Gpax(Student_ID ="58340500011",sum_all_credit =35,GPAX ="3.53")
session.add(gpaxx)
# session.commit()

#----------------------------add subject---------------------------------------#

sub = Subject(ID_Subject ="FRA141",name_subject ="COMPUTER PROGRAMMING",
 Credit =3)
session.add(sub)
sub = Subject(ID_Subject ="FRA161",name_subject ="ROBOTICS EXPLORATION",
 Credit =3)
session.add(sub)
sub = Subject(ID_Subject ="GEN101",name_subject ="PHYSICAL EDUCATION",
 Credit =1)
session.add(sub)
sub = Subject(ID_Subject ="LNG101",name_subject ="GENERAL ENGLISH",
 Credit =3)
session.add(sub)
sub = Subject(ID_Subject ="LNG102",name_subject ="TECHNICAL ENGLISH",
 Credit =3)
session.add(sub)
sub = Subject(ID_Subject ="MTH101",name_subject ="MATHEMATICS I",
 Credit =3)
session.add(sub)
sub = Subject(ID_Subject ="PHY103",name_subject ="GENERAL PHYSICS",
 Credit =3)
session.add(sub)
sub = Subject(ID_Subject ="PHY191",name_subject ="GENERAL PHYSICS LABORATORY I",
 Credit =1)
session.add(sub)
sub = Subject(ID_Subject ="FRA121",name_subject ="ELECTRONIC CIRCUITS",
 Credit =3)
session.add(sub)
sub = Subject(ID_Subject ="FRA142",name_subject ="COMPUTER PROGRAMMING",
 Credit =3)
session.add(sub)
sub = Subject(ID_Subject ="FRA162",name_subject ="ROBOTICS AND AUTOMATION",
 Credit =1)
session.add(sub)
sub = Subject(ID_Subject ="FRA163",name_subject ="ROBOTICS MACHINE SHOP",
 Credit =1)
session.add(sub)
sub = Subject(ID_Subject ="GEN111",name_subject ="MAN AND ETHICS OF LIVING",
 Credit =3)
session.add(sub)
sub = Subject(ID_Subject ="GEN121",name_subject ="LEARNING AND PROBLEM SOLVING SKILLS",
 Credit =3)
session.add(sub)
sub = Subject(ID_Subject ="MTH102",name_subject ="MATHEMATICS II",
 Credit =3)
session.add(sub)

sub = Subject(ID_Subject ="FRA341",name_subject ="COMPUTER PROGRAMMING3",
              Credit =3)
session.add(sub)
sub = Subject(ID_Subject ="FRA361",name_subject ="ROBOTICS EXPLORATION3",
              Credit =3)
session.add(sub)
sub = Subject(ID_Subject ="GEN301",name_subject ="PHYSICAL EDUCATION3",
              Credit =1)
session.add(sub)
sub = Subject(ID_Subject ="LNG301",name_subject ="GENERAL ENGLISH3",
              Credit =3)
session.add(sub)
sub = Subject(ID_Subject ="MTH301",name_subject ="MATHEMATICS I3",
              Credit =3)
session.add(sub)
sub = Subject(ID_Subject ="PHY303",name_subject ="GENERAL PHYSICS3",
              Credit =3)
session.add(sub)
sub = Subject(ID_Subject ="PHY391",name_subject ="GENERAL PHYSICS LABORATORY I3",
              Credit =1)
session.add(sub)
# session.commit()
# -------------------------------------------------------------------#

sth = Profile(id_student = 59340500035,Name = "Panchalee",Surname  = "Sookprao", Sex = "Miss",Dateofbirth = "12/21/41",Birthplace = "Hospital",Nationality = "Thai",Education = "Surin",Relative = "mom",PhoneforEmergency = "3434343434",Phonestudent = "66666666" ,Address = "Surin",Email = "pop@gmail.com",Photo = "59340500035.jpg")
sth1 = Profile(id_student = 59340500021,Name = "Thipawan",Surname  = "Pairam", Sex = "Miss",Dateofbirth = "14/09/40",Birthplace = "Hospital1",Nationality = "Thai",Education = "Bungkan",Relative = "Dad",PhoneforEmergency = "0941234567",Phonestudent = "0867654321" ,Address = "Bungkan",Email = "pair@gmail.com",Photo = "59340500021.jpg")
sth2 = Profile(id_student = 59340500017,Name = "Natthaphon",Surname  = "Sudadech", Sex = "Mr", Dateofbirth = "05/03/39",Birthplace = "Hospital2",Nationality = "Thai",Education = "Bungkan",Relative = "Mom",PhoneforEmergency = "087654321",Phonestudent = "0865432111" ,Address = "Bungkan",Email = "mill@gmail.com",Photo = "59340500017.jpg")
sth3 = Profile(id_student = 58340500011,Name = "Chanittha",Surname  = "Techasombooranakit", Sex = "Miss", Dateofbirth = "11/10/39",Birthplace = "Hospital3",Nationality = "Thai",Education = "Banakok",Relative = "Dad",PhoneforEmergency = "067894332",Phonestudent = "087625434" ,Address = "Bangkok",Email = "winnie@gmail.com",Photo = "58340500011.jpg")
sth4 = Profile(id_student = 58340500014,Name = "Chawisorn",Surname  = "Samrit", Sex = "Mr", Dateofbirth = "21/01/39",Birthplace = "Hospital4",Nationality = "Thai",Education = "Banakok",Relative = "Mom",PhoneforEmergency = "09999999999",Phonestudent = "08799999" ,Address = "Bangkok",Email = "green@gmail.com",Photo = "58340500014.jpg")
sth5 = Profile(id_student = 57340500008,Name = "Chakputtana",Surname  = "Sangpradit", Sex = "Miss", Dateofbirth = "24/05/38",Birthplace = "Hospital5",Nationality = "Thai",Education = "Saraburi",Relative = "Dad",PhoneforEmergency = "0891111111",Phonestudent = "0871111111" ,Address = "Bangkok",Email = "sod@gmail.com",Photo = "57340500008.jpg")
sth6 = Profile(id_student = 57340500016,Name = "Nuttida",Surname  = "Peeklom", Sex = "Miss", Dateofbirth = "12/06/38",Birthplace = "Hospital6",Nationality = "Thai",Education = "Banakok",Relative = "Mom",PhoneforEmergency = "0812222222",Phonestudent = "078888888" ,Address = "Bangkok",Email = "tan@gmail.com",Photo = "57340500016.jpg")
sth7 = Profile(id_student = 60340500004,Name = "Kelwalee",Surname  = "rattanasakulthong", Sex = "Miss", Dateofbirth = "19/08/41",Birthplace = "Hospital7",Nationality = "Thai",Education = "Banakok",Relative = "Dad",PhoneforEmergency = "0934444444",Phonestudent = "0954444444" ,Address = "Bangkok",Email = "kel@gmail.com",Photo = "60340500004.jpg")
sth8 = Profile(id_student = 60340500050,Name = "Lanna",Surname  = "Foolek", Sex = "Miss", Dateofbirth = "30/05/41",Birthplace = "Hospital8",Nationality = "Thai",Education = "Banakok",Relative = "Mom",PhoneforEmergency = "0941111111",Phonestudent = "061111111" ,Address = "Bangkok",Email = "mai@gmail.com",Photo = "60340500050.jpg")

session.add(sth) #add sth into database.
session.add(sth1) #add sth into database.
session.add(sth2) #add sth into database.
session.add(sth3) #add sth into database.
session.add(sth4) #add sth into database.
session.add(sth5) #add sth into database.
session.add(sth6) #add sth into database.
session.add(sth7) #add sth into database.
session.add(sth8) #add sth into database.
sth = Activity(id_student = 59340500017,NameActivity = "Natthaphon",Description = "this is so fun.",Photo = "59340500017.jpg",Type = "Dynamics",Advisor = "Prof.Ton",Date_Activity = "14/12/60",File = "file of the Activity.",Confirm = "Not Confirm yet")
sth1 = Activity(id_student = 59340500021,NameActivity = "Thipawan",Description = "Receive a lot of knowledges.",Photo = "59340500021.jpg",Type = "Calculas",Advisor = "Prof.Somran",Date_Activity = "15/12/61",File = "file of the Activity1.",Confirm = "Confirm")
sth2 = Activity(id_student = 59340500035,NameActivity = "Panchalee",Description = "It is will be useful.",Photo = "59340500035.jpg",Type = "Digital",Advisor = "Prof.Pi",Date_Activity = "15/12/60",File = "file of the Activity2.",Confirm = "Confirm")
sth3 = Activity(id_student = 59340500035,NameActivity = "Tabletennnis.",Description = "Table tennis is good.",Photo = "59340500035.jpg",Type = "Sport",Advisor = "Prof.__",Date_Activity = "29/05/60",File = "file of the Activity3.",Confirm = "Confirm")
sth4 = Activity(id_student = 58340500011,NameActivity = "Project.",Description = "This project is very hard.",Photo = "58340500011.jpg",Type = "Research",Advisor = "Prof.__",Date_Activity = "19/10/61",File = "file of the Activity4.",Confirm = "Not Confirm yet")
sth5 = Activity(id_student = 57340500008,NameActivity = "FootballKMUTT.",Description = "This is my favorite sport.",Photo = "57340500008.jpg",Type = "Research",Advisor = "Prof.__",Date_Activity = "20/10/61",File = "file of the Activity5.",Confirm = "Confirm ")
sth6 = Activity(id_student = 57340500016,NameActivity = "Chorus.",Description = "This is my favorite hobbit.",Photo = "57340500016.jpg",Type = "Research",Advisor = "Prof.__",Date_Activity = "21/10/61",File = "file of the Activity6.",Confirm = "Not Confirm yet")
sth7 = Activity(id_student = 58340500014,NameActivity = "SuperRobot.",Description = "This is my favorite hobbit.",Photo = "58340500014.jpg",Type = "Research",Advisor = "Prof.__",Date_Activity = "22/10/61",File = "file of the Activity7.",Confirm = "Not Confirm yet")
sth8 = Activity(id_student = 60340500004,NameActivity = "CatRobot.",Description = "This is my favorite animal.",Photo = "60340500004.jpg",Type = "Research",Advisor = "Prof.__",Date_Activity = "23/10/61",File = "file of the Dynamic8.",Confirm = "Confirm")
sth9 = Activity(id_student = 60340500050,NameActivity = "DesignUI.",Description = "This is my favorite work.",Photo = "60340500050.jpg",Type = "Research",Advisor = "Prof.__",Date_Activity = "24/10/61",File = "file of the Activity9.",Confirm = "Not Confirm yet")

session.add(sth) #add sth into database.
session.add(sth1) #add sth into database.
session.add(sth2) #add sth into database.
session.add(sth3) #add sth into database.
session.add(sth4) #add sth into database.
session.add(sth5) #add sth into database.
session.add(sth6) #add sth into database.
session.add(sth7) #add sth into database.
session.add(sth8) #add sth into database.
session.add(sth9) #add sth into database.


sth = Disease(id_student = 59340500017,Disease = "gout")
sth1 = Disease(id_student = 59340500017,Disease = "hemorrhoids")
sth2 = Disease(id_student = 59340500017,Disease = "pneumonia")
sth3 = Disease(id_student = 58340500011,Disease = "headache")
session.add(sth) #add sth into database.
session.add(sth1) #add sth into database.
session.add(sth2) #add sth into database.
session.add(sth3) #add sth into database.

sth = Disease(id_student = 59340500035,Disease = "diarrhea")
sth1 = Disease(id_student = 59340500035,Disease = "enteritis")
session.add(sth) #add sth into database.
session.add(sth1) #add sth into database.

sth = Disease(id_student = 59340500021,Disease = "heart disease")
sth1 = Disease(id_student = 59340500021,Disease = "measles")
session.add(sth) #add sth into database.
session.add(sth1) #add sth into database.
# session.commit() #commit data that increase.

sth = Disease(id_student = 57340500008,Disease = "sick4.")
sth1 = Disease(id_student = 57340500016,Disease = "sick3.")
session.add(sth) #add sth into database.
session.add(sth1) #add sth into database.
# session.commit() #commit data that increase.

sth = Disease(id_student = 58340500014,Disease = "sick2.")
sth1 = Disease(id_student = 60340500004,Disease = "sick1.")
session.add(sth) #add sth into database.
session.add(sth1) #add sth into database.
# session.commit() #commit data that increase.

sth = Disease(id_student = 60340500050,Disease = "sick.")
session.add(sth) #add sth into database.
# session.commit() #commit data that increase.

sth = TeacherPW(id_teacher = 100 ,Name = "warasinee", Surname = "chaisangmongkon",T_Password = "100")
sth1 = TeacherPW(id_teacher = 200 ,Name = "bawornsak", Surname = "sakulkueakulsuk",T_Password = "200")
sth2 = TeacherPW(id_teacher = 300 ,Name = "Suriya", Surname = "Natsupakpong",T_Password = "300")
session.add(sth) #add sth into database.
session.add(sth1) #add sth into database.
session.add(sth2) #add sth into database.

sth = StudentPW(id_student = 59340500021,S_Password = "59340500021")
sth1 = StudentPW(id_student = 59340500035,S_Password = "59340500035")
sth2 = StudentPW(id_student = 59340500017,S_Password = "59340500017")
sth3 = StudentPW(id_student = 58340500011,S_Password = "58340500011")
sth4 = StudentPW(id_student = 58340500014,S_Password = "58340500014")
sth5 = StudentPW(id_student = 57340500008,S_Password = "57340500008")
sth6 = StudentPW(id_student = 57340500016,S_Password = "57340500016")
sth7 = StudentPW(id_student = 60340500004,S_Password = "57340500004")
sth8 = StudentPW(id_student = 60340500050,S_Password = "57340500050")
session.add(sth1) #add sth into database.
session.add(sth2) #add sth into database.
session.add(sth3) #add sth into database.
session.add(sth4) #add sth into database.
session.add(sth5) #add sth into database.
session.add(sth6) #add sth into database.
session.add(sth7) #add sth into database.
session.add(sth8) #add sth into database.
session.commit() #commit data that increase.







