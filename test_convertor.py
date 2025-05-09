import file, unittest

class TestFileMethods(unittest.TestCase): #inherit is implementing an is-a relationship: TestFileMethods is a TestCase class with extended behavior
    
    def test_str_to_ls(self):
        y = ['Hi my name is Michael Konu.', 'I am 23.']
        fl = file.File(y)
        fl.ls_to_str()
        self.assertEqual(fl.content, "Hi my name is Michael Konu.\nI am 23.")
        

    def test_ls_to_str(self):
        x = ['Hi my name is Michael Konu.', 'I am 23.']
        fl = file.File(x)
        fl.ls_to_str()
        self.assertEqual(fl.content, "Hi my name is Michael Konu.\nI am 23.")
    
    def test_delete(self): # had to rebuild this a bit, was passing in an inccorect tuple representing the cur position
        x = ['Hi my name is Michael Konu.', 'I am 23.']
        fl = file.File(x)
        fl.delete((0,2))
        self.assertEqual(fl.content, ['H my name is Michael Konu.', 'I am 23.'])
        
    def test_insert(self):
        x = ['Hi my name is Michael Konu.', 'I am 23.']
        fl = file.File(x)
        fl.insert((0,2), "o")
        self.assertEqual(fl.content, ['Hio my name is Michael Konu.', 'I am 23.'])