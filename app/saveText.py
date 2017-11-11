import os.path

class saveText():

    def create(self,ID,Profile,Activity = None):

        save_path = 'C:/Users/' + str(os.getlogin()) + '/Desktop'
        name_file = 'Protfolio_'+ str(ID) + '.txt'
        fileText = os.path.join(save_path, name_file)
        Text = open(fileText, "w")
        Text.write('Protfolio\n\n')

        Text.write('Profile\n')
        for profile in Profile:
            Text.write('Name : ' + str(profile['name']) + "  " + str(profile['sur']) + "\n")
            Text.write('Date of birth : ' + str(profile['dateofbirth']) + '\n')
            Text.write('Nationality : ' + str(profile['nation']) + '\n' )
            if profile['contact'] != None :
                Text.write('Contact\n')
                Text.write(str(profile['phone']) + '\n')
                Text.write(str(profile['email']) + '\n')
                Text.write(str(profile['address']) + '\n')
            if profile['dis'] != None:
                Text.write(str(profile['dis']) + '\n')
            if profile['birthplace'] != None:
                Text.write(str(profile['birthplace']) + '\n')
            if profile['gpax'] != None:
                Text.write("GPAX : " + str(profile['gpax']) + '\n\n')

        if Activity != [] :
            num = 0
            for Act in Activity:
                num += 1
                Text.write('-- Activity ' + str(num) + " --\n")
                Text.write('Name Activity : ' + str(Act['Name_Activity']) + "\n")
                Text.write('Type Activity : ' + str(Act['Type']) + "\n")
                Text.write('Date Activity : ' + str(Act['Date_Activity']) + "\n\n")


        Text.close
