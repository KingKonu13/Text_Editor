import curses, file, cursor, curses.ascii

def main(stdscr: curses.window , fl: file.File, cur: cursor.Cur):
        stdscr.addstr('Enter some keys to see what curses returns, Ctrl+c closes')
        while (True): # -> key combo quits ediotr, currently ctrl + C
            stdscr.move(2,0)
            k = stdscr.getch()
            if k == curses.KEY_LEFT:
                stdscr.addstr('Left')
                cur.mv_left()
            elif k == curses.KEY_RIGHT:
                stdscr.addstr('Right')
                cur.mv_right()
            elif k == curses.KEY_UP:
                stdscr.addstr("Up")
                cur.mv_up()
            elif k == curses.KEY_DOWN:
                stdscr.addstr("Down")
                cur.mv_down()         
            elif k == 127:
                fl.delete(cur.pos)
            else:
                fl.insert(cur.pos, chr(k))
                print(fl)
            

if __name__ == "__main__":
    fl = file.File(["I am 23.”, “I am going to lunch."])
    cur = cursor.Cur(fl)
    curses.wrapper(main, fl, cur) # -> creates a window obj and calls main with that window obj 

if __name__ == "__main__":
    main()