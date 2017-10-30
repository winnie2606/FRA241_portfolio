from getDatabase import *

class editProfile():
    def edit(self,ID,dicProfile):
        print(ID)
        print(dicProfile)
        name = dicProfile["name"]
        surname = dicProfile["surname"]
        nation = dicProfile["nation"]
        birth = dicProfile["bd"]
        birthplace = dicProfile["bp"]
        disease = dicProfile["dis"]
        emerphone = dicProfile["emerphone"]
        reletive = dicProfile["reletive"]
        phone = dicProfile["phone"]
        email = dicProfile["email"]
        address = dicProfile["address"]
        print (name,surname,nation,birth,birthplace,disease,emerphone,reletive,phone,address)

        add = Add_Method(ID)

        add.name(name)
        add.surname(surname)
        add.nation(nation)
        add.date(birth)
        add.birth(birthplace)
        add.disease(disease)
        add.phoneEmer(emerphone)
        add.relative(reletive)
        add.phonestu(phone)
        add.email(email)
        add.address(address)
