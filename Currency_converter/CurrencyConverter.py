
import tkinter as tk
import tkinter.ttk as ttk

base_url="https://exchangeratesapi.io/latest"

def convert_pressed():
    amount=input_text.get()
    from_curr=source_value.get()
    to_curr=target_value.get()
    main_url=base_url+"?base="+from_curr+"&symbols"+from_curr+","+to_curr
    print(main_url)

if __name__=='__main__':
    main_window=tk.Tk()
    main_window.title("Currency Converter")
    main_window.geometry("420x200")
    label=tk.Label(main_window,text="Welcome to Live Currency Converter",fg="white",bg="blue",relief=tk.RAISED,borderwidth=3)
    label.config(font=("Courier",15,"bold"))
    main_window.grid_columnconfigure(0,weight=1)
    label.grid(row=1)

    input_text=tk.StringVar()
    currency_field=tk.Entry(main_window,justify="right",textvariable=input_text)
    currency_field.grid(row=2, padx=5,pady=5)

    Country_code = ["INR","USD","CAD","CNY","DKK","EUR"]
    source_value = tk.StringVar()
    source_value_selection=ttk.Combobox(main_window,values=Country_code,textvariable=source_value)
    source_value_selection.grid(row=3)


    target_value=tk.StringVar()
    target_value_selection = ttk.Combobox(main_window, values=Country_code,textvariable=target_value)
    target_value_selection.grid(row=4)

    convert_button=tk.Button(main_window,text="Convert",height=1,width=7,command=lambda :convert_pressed())
    convert_button.grid(row=5)

    conversion_label=tk.Label(text="")
    conversion_label.grid(row=6)







    main_window.mainloop()