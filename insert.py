class Insert:
    def __init__(self,file, cur, char):
        self.file = file
        self.cur = cur 
        self.char = char

    def insert(self):
        """"" find the position of the cursor(n), move the cursor to the right one index, insert the char at the(n-1) position
        """
        x = self.file[self.cur[0]] #-> "hi"
        y = list(x).insert(self.cur[1], self.char) 
        z = "".join(y) # -> "h"
        self.file[self.cur[0]] = z
        # write the logic here 