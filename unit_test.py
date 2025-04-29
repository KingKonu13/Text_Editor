import file, delete, insert, unittest

class TestConvertor(unittest.TestCase):
    
    def test_str_to_ls(self):
        sentence = "Hi my name is Michael Konu.\nI am 23."
        file = file.Convertor(sentence)
        file_ls = file.str_to_ls() 
        self.assertEqual()
        

"""talk through writing unittests properly"""

sentence = "Hi my name is Michael Konu.\nI am 23."
expected_ls =  ['Hi my name is Michael Konu.', 'I am 23.']

file.Convertor(sentence).str_to_ls() 

== expected, "No"
