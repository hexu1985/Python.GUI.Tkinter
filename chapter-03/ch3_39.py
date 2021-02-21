from tkinter import * 
root = Tk()
root.title("ch3_38")
# root.geometry("1280x800")
root.geometry("128x800")

night = PhotoImage(file="1_cropped.png")
label = Label(root,image=night)
label.place(relx=0.1,rely=0.1,relheight=0.8)

root.mainloop()

