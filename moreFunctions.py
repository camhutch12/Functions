import math

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


def parabola(page, size):
    for x in range(size):
        y = x * x / size
        plot(page, x, y)
        plot(page, -x, y)


def circle(page, radius, g, h, colour='red'):
    page.create_oval(g + radius, h + radius, g - radius, h - radius, outline=colour, width=2)
    # for x in range(g*100, (g + radius)*100):
    #     x/=100
    #     print(x)
    #     y = h + (math.sqrt(radius ** 2 - ((x - g) ** 2)))
    #     plot(page,x,y)
    #     plot(page,x,2*h-y)
    #     plot(page,2*g-x,y)
    #     plot(page,2*g-x,2*h-y)


def draw_axes(page):
    page.update()  # call the canvas update method to access width and height
    x_orgin = canvas.winfo_width() / 2  # devides values by 2
    y_orgin = canvas.winfo_width() / 2
    page.configure(scrollregion=(-x_orgin, -y_orgin, x_orgin, y_orgin))
    page.create_line(-x_orgin, 0, x_orgin, 0, fill='black')
    page.create_line(0, y_orgin, 0, -y_orgin, fill="black")
    print(locals())  # prints all the variable in that function )
    # this locals() is good for debugging


def plot(page, x, y):
    page.create_line(x, -y, x + 1, -y + 1, fill='red')


'''starts the gui this is a blank screen '''
mainWindow = tkinter.Tk()

mainWindow.title("Parabole")
mainWindow.geometry("640x480")
'''canvas allows for basic shapes and has 0,0 on the top left '''
canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

draw_axes(canvas)

parabola(canvas, 200, )
parabola(canvas, 100, )
circle(canvas, 100, 100, 100, 'blue')
circle(canvas, 100, 100, -100)
circle(canvas, 100, -100, 100, 'blue')
circle(canvas, 100, -100, -100)
circle(canvas, 10, 30, 30)
circle(canvas, 10, -30, 30, 'blue')
circle(canvas, 10, 30, -30)
circle(canvas, 10, -30, -30)
circle(canvas, 30, 0, 0)
mainWindow.mainloop()
