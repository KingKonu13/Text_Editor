import file, unittest, cursor

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
        

class TestCurMethods(unittest.TestCase):
    
    def test_mv_left(self):
        fl = file.File(['Hi my name is Michael Konu.', 'I am 23.'])
        cur = cursor.Cur(fl)
        self.assertEqual(cur.cur_pos, (0,0))
        cur.mv_left()
        self.assertEqual(cur.cur_pos, (0,0))
        cur.cur_pos = (0,3)
        cur.mv_left()
        self.assertEqual(cur.cur_pos, (0,2)) 
        cur.cur_pos = (1,0)  
        cur.mv_left()
        self.assertEqual(cur.cur_pos, (0,len(fl.content[0])))
        cur.cur_pos = (0, len(fl.content[0]))
        cur.mv_left()
        self.assertEqual(cur.cur_pos, (0, len(fl.content[0])-1))
        cur.cur_pos = (1,3)
        cur.mv_left()
        self.assertEqual(cur.cur_pos, (1,2))
            
        
    def test_mv_right(self):
        fl = file.File(['Hi my name is Michael Konu.', 'I am 23.'])
        cur = cursor.Cur(fl)
        self.assertEqual(cur.cur_pos, (0,0))
        print(cur)
        cur.mv_right()
        print(cur)
        self.assertEqual(cur.cur_pos, (0,1))
        cur.cur_pos = (0,2)
        cur.mv_right()
        self.assertEquals(cur.cur_pos, (0,3))
        cur.cur_pos = (1,0)
        cur.mv_right()
        self.assertEqual(cur.cur_pos, (1,1))
        cur.cur_pos = (0,len(fl.content[0]))
        cur.mv_right()
        print(cur)
        self.assertEqual(cur.cur_pos, (1,0))
        cur.cur_pos = (1,8) # not solid (2,9)
        cur.mv_right()
        self.assertEqual(cur.cur_pos, (1,8))
        return
    
    def test_mv_down(self):
        pass
    
    def test_mv_up(self):
        pass