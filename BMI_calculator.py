from tkinter import *
root = Tk()

root.title("Ideal Body Mass Index")
root.geometry("600x700")

# Sub-heading
Label_1 = Label(root, text="Enter your Weight, Height and Gender")
Label_1.place(x=150, y=0)


# Weight (Labels, Entry and Placement)
Label_2 = Label(root, text="Weight:")
Label_3 = Label(root,  text="Kilograms")
first_num = Entry(root)

Label_2.place(x=30, y=30)
Label_3.place(x=270, y=30)
first_num.place(x=100, y=30)


# Height (Labels, Entry and Placement)
Label_4 = Label(root, text="Height:")
Label_5 = Label(root,  text="cm")
second_num = Entry(root)

Label_4.place(x=30, y=70)
Label_5.place(x=270, y=70)
second_num.place(x=100, y=70)


# Age (Label, Entry and Placement)
Label_7 = Label(root, text="Age:")
age = Entry(root, state='readonly')

Label_7.place(x=270, y=105)
age.place(x=320, y=105)


# Gender (Selection and Placement)
Label_6 = Label(root, text="Gender")
option = ["Select", "Male", "Female"]

variable = StringVar(root)
variable.set(option[0])

def activate(value):
    variable.set(value)
    if value != "Select":
       age.config(state='normal')

    else:
        age.config(state='readonly')

opt = OptionMenu(root, variable, *option, command=activate)
opt.config(width=10, font=('Helvetica', 12))

Label_6.place(x=30, y=105)
opt.place(x=100, y=100)

# BMI
bmi = Label(root, text="BMI:",)
bmi.place(x=80, y=385)

bmi_field = Entry(root, state='readonly')
bmi_field.place(x=120, y=385)

ideal_bmi = Label(root, text='Ideal BMI:')
ideal_bmi.place(x=320, y=385)

ideal_field = Entry(root, state='readonly')
ideal_field.place(x=390, y=385)


# Category Labels AND Placement
category_head = Label(root, text="Category:")
category = Label(root, width=20)
category.place(x=360, y=460)
category_head.place(x=300, y=460)



# Definitions for Calculation
def bmi():
    float(first_num.get())
    float(second_num.get())
    if variable.get() == "Select":
        raise ValueError
    
    elif variable.get() == "Male":
        result = ((0.5 * float(first_num.get())) / ((float(second_num.get()) / 100)**2)) + 11.5
        result = round(result, 1)
        ideal_field.config(state='normal')
        ideal_field.insert(0, result)
        ideal_field.config(state='readonly')
        result_bmi = float(first_num.get()) / ((float(second_num.get()) / 100) ** 2)
        bmi_field.config(state='normal')
        bmi_field.insert(0, round(result_bmi, 1))
        bmi_field.config(state='readonly')

    elif variable.get() == "Female":
        result = ((0.5 * float(first_num.get())) / ((float(second_num.get()) / 100) ** 2)) + 0.03 * float(age.get()) + 11
        result = round(result, 1)
        ideal_field.config(state='normal')
        ideal_field.insert(0, result)
        ideal_field.config(state='readonly')
        result_bmi = float(first_num.get()) / ((float(second_num.get()) / 100) ** 2)
        bmi_field.config(state='normal')
        bmi_field.insert(0, round(result_bmi, 1))
        bmi_field.config(state='readonly')

    if result < 18.5:
       category.config(text='Underweight')

    elif 18.5 <= result < 25:
         category.config(text='Normal weight')

    elif 25 <= result < 30:
         category.config(text='Overweight')

    else:
        if result >= 30:
           category.config(text='Obese')

def delete():
    first_num.delete(0, END)
    second_num.delete(0, END)
    age.config(state='normal')
    bmi_field.config(state='normal')
    ideal_field.config(state='normal')
    age.delete(0, END)
    bmi_field.delete(0, END)
    ideal_field.delete(0, END)
    age.config(state='readonly')
    bmi_field.config(state='readonly')
    ideal_field.config(state='readonly')
    first_num.focus()
    variable.set(option[0])


#Clear button placement
clear = Button(root, text='Clear', command=delete)
clear.place(x=40, y=600)


#Exit Buttons
exit = Button(root, text='Exit', command='exit')
exit.place(x=500, y=600)
calculate = Button(root, text="Calculate your Ideal Body Mass Index", width=50, command=bmi)
calculate.place(x=120, y=290)

root.mainloop()
