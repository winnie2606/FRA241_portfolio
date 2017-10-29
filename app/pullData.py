from FunctionAdd import Method


class pullData():

    def __init__(self, profile=None, academic=None, activity=None):
        self.profile = profile
        self.academic = academic
        self.activity = activity

    def Profile(self, getID):
        m = Method(getID)
        self.profile = [{'name':m.cp_name(),'birthD':m.cp_date(),'birthP':m.cp_birth(),
                    'nation':m.cp_nation(),'edu':m.cp_edu(),'dis':m.cp_disease(),'relative':m.cp_relative(),
                    'phoneEmer':m.cp_PhforEmer(),'cont':m.cp_Phstu(),'address':m.cp_address(),'email':m.cp_email()}]
        return self.profile

    def Activity(self, getID):
        m = Method(getID)
        self.activity = [None]
        return self.activity

    def Academic(self, getID):
        m = Method(getID)
        self.academic = [None]
        return self.academic

    def dataActivity(self, getID):
        m = Method(getID)
        self.dataactivity = [None]
        return self.dataactivity
