from graphics import Window, Point, Line
from cell import Cell

def main():
    win = Window(800, 600)

    c = Cell(win)
    c.draw(50, 50, 100, 100)

    c2 = Cell(win)
    c2.draw(x1=100, y1=50, x2=150, y2=100)

    c.draw_move(c2,True)

    win.wait_for_close()


main()