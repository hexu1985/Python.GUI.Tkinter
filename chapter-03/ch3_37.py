from tkinter import * 
root = Tk()
root.title("ch3_37")
root.geometry("1280x800")

night = PhotoImage(file="1_cropped.png")
lab1 = Label(root,image=night)
lab1.place(x=20,y=30,width=500,height=500)

snow = PhotoImage(file="2_cropped.png")
lab2 = Label(root,image=snow)
lab2.place(x=50,y=550,width=650,height=200)
   
root.mainloop()

