from tkinter import *

window = Tk()
window.title("SI Calculator")

window.geometry("400x400")
window.configure(bg="lightcyan")

def calculate_intrest():
    p = float(principal.get())
    r = float(rateofintrest.get())
    t = float(timeperiod.get())
    i = (p*r*t)/100 + p
    intrest = round(i,2)

    result_label.destroy()
    
    output_msg = Label(result_frame,text=f"Your amount after intrest is {intrest}",bg="lightcyan",font=("Calibri",12),width=42)
    output_msg.place(x=20,y=20)
    output_msg.pack()

heading_label = Label(window,text="SI Calculator",fg="black",bg="lightcyan",font=("Calibri",20),bd=5)
heading_label.place(x=50,y=20)

principal_label = Label(window,text="Enter Principal :  ",fg="black",bg="lightcyan",font=("Calibri",12),bd=1)
principal_label.place(x=20,y=90)
principal = Entry(window,text="",bd=2,width=22)
principal.place(x=170,y=92)

rateofintrestlabel = Label(window,text="Enter ROI in % :  ",fg="black",bg="lightcyan",font=("Calibri",12),bd=1)
rateofintrestlabel.place(x=20,y=120)
rateofintrest = Entry(window,text="",bd=2,width=22)
rateofintrest.place(x=170,y=122)

timeperiod_label = Label(window,text="Time Period(Years) :  ",fg="black",bg="lightcyan",font=("Calibri",12),bd=1)
timeperiod_label.place(x=20,y=150)
timeperiod = Entry(window,text="",bd=2,width=22)
timeperiod.place(x=170,y=152)

calculate_btn = Button(window,text="Calculate",fg="black",bg="cyan",font=("Calibri",12),bd=4,command=calculate_intrest)
calculate_btn.place(x=165,y=200)

result_frame = LabelFrame(window,text="Result",bg="lightcyan",font=("Calibri",20))
result_frame.pack(padx=20,pady=20)
result_frame.place(x=20,y=300)

result_label = Label(result_frame,text="",bg="lightcyan",font=("Calibri",20),width=33)
result_label.place(x=20,y=20)
result_label.pack()

window.mainloop()