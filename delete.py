import file 

class Delete:
    def __init__(self,file, cur_pos):  # -> cur = (0,1)
        self.file = file
        self.cur = cur_pos 
        
    def delete(self):
        """ find the position of the cursor(n) and delete the (n-1) char 
        """
        x = self.file[self.cur[0]] #-> "hi"
        y = list(x).pop(self.cur[1]-1) #-> ["h"]
        z = "".join(y) # -> "h"
        self.file[self.cur[0]] = z
        

# d = Delete("hi",2) 
# help(d.delete)

# 