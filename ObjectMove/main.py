from tkinter import *


class ObjectMove(object):
    """
    Class demonstrates tkinter canvas working.
    Here we can move and resize (auto) circle with mouse clicks.
    """
    def __init__(self, width: int, height: int, dot_size: int = 10):
        """
        Constructor of.
        :param width: Width of screen in pixels.
        :param height: Height of screen in pixels.
        """

        self.__root = Tk()
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.bind("<Button-1>", self.__event_canvas_mouseclick)
        self.__canvas.pack()
        self.__object = self.__canvas.create_oval(2, 2, 2 + dot_size, 2 + dot_size, fill="#ffcc00")
        self.__root.mainloop()

    def __event_canvas_mouseclick(self, event):
        """
        Method to handle mouseclick event.
        Here we just move rectangle.
        :param event:
        :return:
        """
        x1, y1, x2, y2 = self.__canvas.coords(self.__object)
        self.__canvas.coords(self.__object, x1, y1, x2 + 10, y2 + 10)
        self.__canvas.move(self.__object, event.x - x1, event.y - y1)


ObjectMove(200, 200)
