import file

class Cur:
    "add row and column"
    def __init__(self,fl: file.File): 
        self.fl = fl
        self.cur_pos = (0,0) #row, column) ['Hi my name is Michael.', 'I am 23']

    def mv_left(self):
        len_line = len(self.fl.content[self.cur_pos[0]])
        
        if self.cur_pos == (0,0): # start 
            return
        
        if self.cur_pos[0] == 0 and self.cur_pos[1] != len_line: #first line, anywehre but start and end  
            self.cur_pos = (0,self.cur_pos[1]-1)
            return
        
        elif self.cur_pos[0] != 0 and self.cur_pos[1] == 0: #not first line, start of line 
            self.cur_pos = (self.cur_pos[0]-1, len(self.fl.content[self.cur_pos[0]-1]))
            return
            
        elif self.cur_pos[1] == len_line: #end of line 
            self.cur_pos = (self.cur_pos[0], self.cur_pos[1]-1)
            return
            
        else:
            self.cur_pos = (self.cur_pos[0], self.cur_pos[1]-1)
            return
            
    
    def mv_right(self):
        total_rows = len(self.fl.content)
        len_line = len(self.fl.content[self.cur_pos[0]]) # (2,9)
        
        if self.cur_pos[0] == total_rows - 1 and self.cur_pos[1] == len_line: #end of doc 
            return 
        
        if self.cur_pos == (0,0): #start 
            self.cur_pos = (0, self.cur_pos[1]+1)
            return # needded to terminate the funciton here 
            
        elif self.cur_pos[0] == 0 and self.cur_pos[1] != len_line: #first line, anywehre but start and end 
            self.cur_pos = (self.cur_pos[0], self.cur_pos[1]+1)
            return 
                
        elif self.cur_pos[0] != 0 and self.cur_pos[1] == 0: #not first line, start of line 
            self.cur_pos = (self.cur_pos[0], self.cur_pos[1]+1)
            return 
        
        elif self.cur_pos[1] == len_line : #end of line 
            self.cur_pos = (self.cur_pos[0]+1, 0)
            return
        
        else: # 5 char
            self.cur_pos = (self.cur_pos[0], self.cur_pos[1]+1)
            return
    
    def __str__(self):
        return f"this is the current cursor position: {self.cur_pos}"
    
    def mv_up(self):
        len_line = len(self.fl.content[self.cur_pos[0]])
        pass
    
    def mv_down(self):
        "calculate the current row and then increase it by one and hold the column constant "
        pass
    


"""1. tuples are read only in python""
"2. unit tests "
" end of file problem for mv right" 
"""
"threshold for wrapping is a 50 char diff btw consecutive lines"