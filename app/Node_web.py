class Node_web():

    def __init__(self,page= None,value = None,next =None,previous=None):
        self.page = page
        self.Next = next
        self.previous = previous
        self.value = value



    def __str__(self):
        return str(self.page)


