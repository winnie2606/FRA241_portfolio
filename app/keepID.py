class keepID():

    def __init__(self, ID=None, Password=None):
        self.ID = ID
        self.Password = Password

    def Print_ID(self):
        print(self.ID)
        print(self.Password)

    def reset_keepID(self):
        self.ID = None
        self.Password = None
