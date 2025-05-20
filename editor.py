import curses, file, cursor, curses.ascii


def main(stdscr: curses.window , fl: file.File, cur: cursor.Cur):
        while (True): # -> key combo quits ediotr, currently ctrl + C
            stdscr.clear()
            stdscr.addstr(0,0, fl.to_str())
            stdscr.move(cur.cur_pos[0],cur.cur_pos[1])
            k = stdscr.getch()
            if k == curses.KEY_LEFT:
                cur.mv_left()
                # pass in cur pos as args
            elif k == curses.KEY_RIGHT:
                cur.mv_right()
            elif k == curses.KEY_UP:
                cur.mv_up()
            elif k == curses.KEY_DOWN:
                cur.mv_down()         
            elif k == 127:
                fl.delete(cur.cur_pos)
                cur.mv_left()
            else:
                fl.insert(cur.cur_pos, chr(k)) ##
                cur.mv_right()
            

if __name__ == "__main__":
    fl = file.File(["I am 23.", "I am going to lunch.", "I am 30"])
    cur = cursor.Cur(fl)
    curses.wrapper(main, fl, cur) # -> creates a window obj and calls main with that window obj 

if __name__ == "__main__":
    main()
    
    
    
"""cursor display(tether cur logic to curses logic) and """