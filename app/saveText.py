import os.path

class text():

    def create(self,ID,Profile,Activity = None):

        save_path = 'C:/Users/' + str(os.getlogin()) + '/Desktop'
        name_file = 'Protfolio_'+ str(ID) + '.txt'
        fileText = os.path.join(save_path, name_file)
        Text = open(fileText, "w")
        Text.write('Protfolio\n\n')

        Text.write('Profile\n')
        for profile in Profile:
            Text.write('Name : ' + str(profile[name]) + "  " + str(profile[sur]) + "\n")
            Text.write('Date of birth : ' + str(profile[dateofbirth]) + '\n')



        Text.close


'''save
[{'contact': 'CONTACT', 'dateofbirth': '29/05/1997',
 'nation': 'Thai', 'birthplace': 'BIRTH PLACE : hospital',
'phone': 'PHONE : 0896103901', 'gpax': '3.77', 'dis': 'CONGENITAL DISEASE : -',
 'name': 'Palop', 'sur': 'Perzz', 'address': 'ADDRESS : my room', 'email':
  'EMAIL : Palop@mail.com'}]

[{'File': 'file of the Digital', 'Type': 'Digital', 'Name_Activity':
 'Panchalee', 'Confirm': 'Not Confirm yet', 'Description': 'It is will be useful.',
  'Date_Activity': '15/12/60', 'Advisor': 'Prof.Pi', 'Photo': 'Popperzz.jpg'},

  {'File': 'file of the table tennis', 'Type': 'Sport', 'Name_Activity':
  'Tabletennnis.', 'Confirm': 'Confirm', 'Description': 'Table tennis is good.',
  'Date_Activity': '29/05/60', 'Advisor': 'Prof.__', 'Photo': 'Popperzztennis.jpg'},

  {'File': None, 'Type': '123', 'Name_Activity': 'game', 'Confirm': None,
  'Description': '65', 'Date_Activity': '234', 'Advisor': '345', 'Photo': None},
   {'File': None, 'Type': 'a', 'Name_Activity': 'hi', 'Confirm': None,
    'Description': 'd', 'Date_Activity': 'b', 'Advisor': 'c', 'Photo': None}]
    '''
