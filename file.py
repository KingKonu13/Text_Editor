class File: 
    
    _DELIMITER = "\n"
    
    def __init__(self, file_content: list):
        if isinstance(file_content, list):
            self.file_content = file_content 
        else:
            raise ValueError("please pass in a list type for the content arg")

    def str_to_ls(self):
        self.file_content = self.file_content.split(self._DELIMITER) 
    
    def ls_to_str(self):
        self.file_content = f"{self._DELIMITER}".join(self.file_content)
        
    def __str__(self):
        return f"this is the current state of your file: {self.file_content}"
    
    def delete(self, cur_pos,):
        """ find the position of the cur(n) and delete the char at (n-1)
        """
        line_str = self.file_content[cur_pos[0]] #-> "hi"
        line_ls = list(line_str)
        line_ls.pop(cur_pos[1]-1) #-> ["h"]
        new_line_str = "".join(line_ls) # -> "h"
        self.file_content[cur_pos[0]] = new_line_str
        
    def insert(self, cur_pos: tuple, char=""): # decided aginst handling tracking the cursor repositioning here and will handle in cursor management
        """"" find the position of the cursor(n), move the cursor to the right one index, insert the char at the(n-1) position
        """
        line_str = self.file_content[cur_pos[0]] #-> "hi"
        line_ls = list(line_str)
        line_ls.insert(cur_pos[1], char) 
        z = "".join(line_ls) # -> "h"
        self.file_content[cur_pos[0]] = z


