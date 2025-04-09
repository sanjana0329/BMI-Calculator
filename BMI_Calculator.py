from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk


#the main window
root = Tk()
root.title('BMI Calculator')
root.geometry('580x750+500+20')
root.resizable(False,False)
root.configure(bg='#FFC0CB')


def BMI():
    h = float(Height.get())
    w = float(Weight.get())
    #convert height into meter
    m=h/100
    bmi = round(float(w/m**2),2)
    label1.config(text=bmi)


    if bmi<= 18.5:
        label2.config(text='Underweight!')
        label3.config(text='You have lower weight then \n normal body!')


    elif bmi> 18.5 and bmi<=25:
        label2.config(text='Normal!')
        label3.config(text='It indicates that you are healthy!')

    elif bmi>25 and bmi<=30:
        label2.config(text='Overweight!')
        label3.config(text='It indicates that you  a person is \n slightly overweight! \n A doctor may advise to lose some \n weight for health reasons.')

    else :
        label2.config(text='Obes!')
        label3.config(text='Health may be at risk, if you do not \n lose weight!')

    



    
#icon for the window
icon = Image.open("C:/Users/hp/Downloads/BIM.png")
icon = icon.resize((40,40))
icon = ImageTk.PhotoImage(icon)
root.iconphoto(False, icon)


#display top image
top = PhotoImage(file="C:/Users/hp/Desktop/text.png")
top_img = Label(root, image=top, background='#FFFFFF')
top_img.place(x=-10, y=-15)



#function to get the name
def get_name(event=None):
    name = name_entry.get()

#function to get the AGE
def get_age(event=None):
    age = age_entry.get()

#label and text box  for NAME

Name = StringVar()
Age = StringVar()

name_label = Label(root, text='Name : ',fg='gray', bg='pink', font=('Arial', 14))
name_label.grid(row=1, column=0, padx=10, pady=(115,7), sticky='w')

#widget entry for entrying the name
name_entry = Entry(root, font=('Arial', 14), width=30)
name_entry.grid(row=1, column=1, padx=10, pady=(115,7))
Name.set(get_name())


#bind the focus-in event to entry widget
name_entry.bind('<FocusIn>', get_name)


#label and text box  for AGE

age_label = Label(root, text='Age : ',fg='gray', bg='pink', font=('Arial', 14))
age_label.grid(row=2, column=0, padx=10, pady=5, sticky='w')

#widget entry for entrying the AGE
age_entry = Entry(root, font=('Arial', 14), width=30)
age_entry.grid(row=2, column=1, padx=10, pady=5)
Age.set(get_age())

#bind the focus-in event to entry widget
age_entry.bind('<FocusIn>', get_age)




#label and text box  for GENDER
gender_label = Label(root, text='Gender :', fg='gray', bg='pink', font=('Arial', 14))
gender_label.grid(row=1, column=3, padx=10, pady=(115,4), sticky='n')

#stringVar for gender selection
gender_var = StringVar(value=" ")#default

#gender radio button
gender_male = Radiobutton(root, text='Male', variable=gender_var, value='Male', bg='pink', font=('Arial',14))
gender_male.grid(row=2, column=3, padx=10, pady=5, sticky='w')

gender_female = Radiobutton(root, text='Female', variable=gender_var, value='Female', bg='pink', font=('Arial',14))
gender_female.grid(row=3, column=3, padx=10, pady=5, sticky='w')





##############SLIDER1
current_value = tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_change(event):
    Height.set(get_current_value())
    
    img = Image.open("C:/Users/hp/Downloads/bluestick.png")

    size = int(float(get_current_value()))+150
    resized_img = img.resize((55,10+size))
    photo2 = ImageTk.PhotoImage(resized_img)
    secondimage.config(image=photo2)
    secondimage.place(x=100, y=714-size)
    secondimage.image = photo2    
    secondimage.lift() 

style = ttk.Style()
style.configure("TScale", background='white')
slider = ttk.Scale(root, from_=0, to=220, orient='horizontal', style='TScale',
                   command=slider_change, variable=current_value)
slider.place(x=100, y=238)


##############SLIDER2
current_value2 = tk.DoubleVar()

def get_current_value2():
    return '{: .2f}'.format(current_value2.get())

def slider_change2(event):
    Weight.set(get_current_value2())

style2 = ttk.Style()
style2.configure("TScale", background='white')
slider2 = ttk.Scale(root, from_=0, to=220, orient='horizontal', style='TScale',
                   command=slider_change2, variable=current_value2)
slider2.place(x=310, y=238)





#Entry box
Height = StringVar()
Weight = StringVar()

height_label = Label(root, text='Height : ',fg='gray', bg='pink', font=('Arial', 14))
height_label.place(x=10, y=205)
height_label1 = Label(root, text='(cm)',fg='gray', bg='pink', font=('Arial', 14))
height_label1.place(x=10, y=235)

height = Entry(root, textvariable=Height, width=11, font='arial 14', bg='white', fg='black', bd=0)
height.place(x=100, y=205)
Height.set(get_current_value()) 

weight_label = Label(root, text='Weight : ',fg='gray', bg='pink', font=('Arial', 14))
weight_label.place(x=230, y=205)
Weight_label1 = Label(root, text='(Kg)',fg='gray', bg='pink', font=('Arial', 14))
Weight_label1.place(x=230, y=235)


weight = Entry(root, textvariable=Weight, width=11, font='arial 14', bg='white', fg='black', bd=0)
weight.place(x=310, y=205)
Weight.set(get_current_value2())

secondimage = Label(root,bg="pink")
secondimage.place(x=70, y=714)



#Scale image
scale = PhotoImage(file='C:/Users/hp/Downloads/Untitled.png')
Label(root, image = scale, bg='pink').place(x=20,y=280)

scale_image = Label(root)
scale_image.place(x=70,y=580)


Button(root, text='View Result', width=12, height=1, font='arial 14 bold', bg='pink', fg='grey', command=BMI).place(x=175, y=292)

label1 = Label(root, font='arial 20 bold',bg='#C6B1FF', fg='black')
label1.place(x=350, y=295)

label2 = Label(root, font='arial 40 bold',bg='#C6B1FF', fg='grey')
label2.place(x=190, y=380)

label3 = Label(root, font='arial 15 bold',bg='#C6B1FF', fg='grey')
label3.place(x=190, y=480)

root.mainloop()
