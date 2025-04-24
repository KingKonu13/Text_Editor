class Delete:
    def __init__(self,file):
        self.file = file
        
    def delete(self):
        """ find the position of the cursor(n) and delete the (n-1) char 
        """