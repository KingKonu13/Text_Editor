class Convertor:
    def __init__(self, content):
        self.content = content
        
    def str_to_ls(self):
        self.content = self.content.split("\n") 
    
    def ls_to_str(self):
        self.content = "\n".join(self.content)
        
    def __str__(self):
        return f"this is the current state of your file {self.content}"
        
if __name__ == "__main__":

    x = "hi my name is. \n I am 23."
    print(x)
    file = Convertor(x) # -> Creates a File Convertor obj
    file.str_to_ls()
    print(file)
    file.ls_to_str()
    print(file)



# move the testing to a set of unit tests
