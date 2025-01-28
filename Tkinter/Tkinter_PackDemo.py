import tkinter as tk

main_window=tk.Tk()
main_window.geometry("500x300")
label1=tk.Label(main_window,text="Hello Python 1",bg="black",fg="white")
label1.pack(side=tk.BOTTOM,fill=tk.X)
label2=tk.Label(main_window,text="Hello Python 2",bg="green",fg="black")
label2.pack(side=tk.RIGHT,fill=tk.Y)

main_window.mainloop()