import tkinter

root = tkinter.Tk()

def click_handler(event):
    # event also has x & y attributes
    if event.num == 2:
        print("RIGHT CLICK")

root.bind("<Button-1>", lambda x: print("LEFT CLICK"))
root.bind("<Button>", click_handler)

root.mainloop()