import os
import os.path

save_path = 'C:/Users/' + str(os.getlogin()) + '/Desktop'

os.chdir(save_path)
os.mkdir('forUploadToPortfolio')
