from getDatabase import *

class editActivity :

    def edit(self,ID,dicAct):

        nameAct = dicAct['nameAc']
        typeAct = dicAct['type']
        dateAct = dicAct['type']
        photoAct = dicAct['photo']
        advisorAct = dicAct['advisor']
        desAct = dicAct['des']
        fileAct = dicAct['fileDoc']

        add = Add_Method(ID)
        re = return_Method(ID)

        if nameAct != "":
            add.Act_name(nameAct)
            if typeAct != "":
                add.Act_type(typeAct,nameAct)
            if dateAct != "":
                add.Act_date(dateAct,nameAct)
            if photoAct != "":
                add.Act_photo(photoAct,nameAct)
            if advisorAct != "":
                add.Act_advisor(advisorAct,nameAct)
            if desAct != "":
                add.Act_des(desAct,nameAct)
            if fileAct != "":
                add.Act_file(fileAct,nameAct)
