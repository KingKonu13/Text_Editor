import file

class Cur:
    def __init__(self,fl: file.File,): 
        self.fl = fl
        self.pos = (0,0)
        
        pass 

    def mv_left(self):
        if self.pos == (0,0):
            return
        if self.pos[1] == 0:
            self.pos[0] -= 1
            self.pos[1] = len(self.fl.content[self.pos[0]])
        else:
            self.pos[1] -= 1
        
        pass
    
    def mv_right(self):
        len_line = len(self.fl.content[self.pos[0]])
        if self.pos[1] == len_line:
            self.pos[0] += 1
            self.pos[1] = 0
        else:
            self.pos[1] += 1
            self.pos = (self.pos[0], self.pos[1]+1)
    
    def mv_up(self):
        pass
    
    def mv_down(self):
        pass
    

x = Cur(fl)
x.mv_left() 
x.pos == (2,2)


"""1. tuples are read only in python""
"2. unit tests "
" end of file problem for mv right" 
"""