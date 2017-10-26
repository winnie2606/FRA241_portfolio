from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

db = create_engine('sqlite:///Database.db')
Base = declarative_base()

class Profile(Base):
    __tablename__ = 'Profile'
    id_student = Column(Integer,primary_key=True)
    Name = Column(String)
    Dateofbirth = Column(String)
    Birthplace = Column(String)
    Nationality = Column(String)
    Education = Column(String)
    Disease = Column(String)
    Relative = Column(String)
    PhoneforEmergency = Column(String)
    Phonestudent = Column(String)
    Address = Column(String)
    Email = Column(String)
    # activity = relationship("Activity")


class Activity(Base):
    __tablename__ = 'Activity'
    id_student = Column(Integer,primary_key=True)
    NameActivity = Column(String)
    Description = Column(String)
    Photo = Column(String)#change next time
    Type = Column(String)
    Advisor = Column(String)
    Date_Activity = Column(String)
    File = Column(String)#change next time
    Confirm = Column(String)
    # profile_id = Column(Integer, ForeignKey("Profile.id"))

# Session = sessionmaker(bind=db)
# session = Session()
# Base.metadata.create_all(db)
# query = session.query(Profile)

# sth = Profile(id_student = 59340500035,Name = "Panchalee",Dateofbirth = "12/21/41",Birthplace = "Hospital",Nationality = "Thai",Education = "Surin",Disease = "None",Relative = "mom",PhoneforEmergency = "3434343434",Phonestudent = "66666666" ,Address = "Surin",Email = "pop@gmail.com")
# session.add(sth)
# session.commit()

# query = session.query(Profile)
# for user in query.filter_by(Name='Panchalee'):
#     print(user.Email)

# addData = session.query(Profile).filter_by(id_student=59340500035).one()
# addData.Name = 'Panchalee'
# session.add(addData)
# session.commit()

Session = sessionmaker(bind=db)
session = Session()
Base.metadata.create_all(db)
query = session.query(Profile)
class Method:


    def __init__(self,data):

        self.data = data

    def cp_name(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            print(user.Name)
            return user.Name

    def cp_date(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            print(user.Dateofbirth)
            return user.Dateofbirth

    def cp_birth(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            print(user.Birthplace)
            return user.Birthplace

    def cp_nation(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            print(user.Nationality)
            return user.Nationality

    def cp_edu(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            print(user.Education)
            return user.Education

    def cp_disease(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            print(user.Disease)
            return user.Disease

    def cp_relative(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            print(user.Relative)
            return  user.Relative

    def cp_PhforEmer(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            print(user.PhoneforEmergency)
            return user.PhoneforEmergency

    def cp_Phstu(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            print(user.Phonestudent)
            return user.Phonestudent

    def cp_address(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            print(user.Address)
            return user.Address

    def cp_email(self):
        for user in query.filter_by(id_student = "{}".format(self.data)):
            print(user.Email)
            return user.Email
