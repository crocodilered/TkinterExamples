from tkinter import *
from random import *


class RedDotsCanvas(object):
    """
    Class demonstrates tkinter canvas working.
    It draws red dots on canvas.
    In case of mouseclick it starts to draw selected dot in green color.
    """
    def __init__(self, width: int, height: int, dot_size: int = 1, refresh_rate: int = 1000):
        """
        Constructor of.
        :param width: Width of screen in pixels.
        :param height: Height of screen in pixels.
        :param dot_size: Size of dot in pixels.
        :param refresh_rate: Graphics refresh rate in milliseconds.
        """
        # Dot size in pixels
        self.__dot_size = dot_size
        # Canvas size in pixels
        self.__real_size = (width, height)
        # Canvas size in dots
        self.__virtual_size = (int(width/dot_size), int(height/dot_size))
        # Screen refresh rate in milliseconds
        self.__refresh_rate = refresh_rate

        # Screen buffer
        self.__buffer = None
        # Clicked dots coordinates
        self.__clicked_dots = []

        # Init tkinter
        self.__root = Tk()
        self.__canvas = Canvas(self.__root, width=self.__real_size[0], height=self.__real_size[1])
        self.__canvas.bind("<Button-1>", self.__event_canvas_mouseclick)
        self.__canvas.pack()
        self.__run()
        self.__root.mainloop()

    def __generate_buffer(self):
        """
        Generate data to draw.
        :return: 2d-array of 0..1 values.
        """
        r = []
        for i in range(0, self.__virtual_size[0]):
            r.append([])
            for j in range(0, self.__virtual_size[1]):
                r[i].append(random())
        return r

    def __draw(self):
        """
        Draw screen depends of internally generated data
        :return:
        """
        self.__canvas.delete("all")
        for i in range(0, self.__virtual_size[0]):
            for j in range(0, self.__virtual_size[1]):
                color_mask = "#00%02x00" if (i, j) in self.__clicked_dots else "#%02x0000"
                color_value = int(255 * self.__buffer[i][j])
                x = i * self.__dot_size
                y = j * self.__dot_size
                self.__canvas.create_rectangle(x, y, x + self.__dot_size, y + self.__dot_size,
                                               fill=color_mask % color_value)
        self.__canvas.update()

    def __event_canvas_mouseclick(self, event):
        """
        Method to handle mouseclick event
        :param event:
        :return:
        """
        # We got real x and y here. Must translate em to virtual ones.
        x_virtual = int(event.x / self.__dot_size)
        y_virtual = int(event.y / self.__dot_size)
        self.__clicked_dots.append((x_virtual, y_virtual))

    def __run(self):
        """
        Wrapper for system loop.
        :return:
        """
        self.__buffer = self.__generate_buffer()
        self.__draw()
        self.__root.after(self.__refresh_rate, self.__run)


red_dots_canvas = RedDotsCanvas(200, 200, 10)