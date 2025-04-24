class Convertor:
    def __init__(self, content):
        self.content = content
        
        
    def str_to_ls(self):
        self.content = self.content.split()
    
    def ls_to_str(self):
        self.content = " ".join(self.content)
        
    def __str__(self):
       return f"this is the current state of your file {self.content}"
        
file = Convertor("hi my name is") # -> Creates a File Convertor obj
file.str_to_ls() # -> applies the split method to the str that I passed in and updates the object's self.str property 
 #-> should 
print(file)



