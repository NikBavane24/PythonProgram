

import tkinter as tk

main_window=tk.Tk()
#relief-flat,groove,ridge,solid,sunken
label=tk.Label(main_window,text="Hello Python",bg="grey",fg="blue",padx=100,pady=100,font="comicsansms 20 bold",borderwidth=10,relief="sunken")
label.pack()


#add image on interface
photo=tk.PhotoImage(file="img.png")
label1=tk.Label(image=photo)
label1.pack()
main_window.mainloop()