# Group 9 - Currency Converter
# Members:
# Cynthia Anaba - 75092025
# Alvin Brocke - 69382025
# Joseph-Bryan - 80962025
# Godwin Abugbilla - 79592025

from tkinter import *
from tkinter import ttk
from tkinter import messagebox


root = Tk()
root.title('AU Currency Conversion')
root.geometry("500x500")

mynotebook = ttk.Notebook(root)
mynotebook.pack(pady=5)

currencyframe = Frame(mynotebook, width=500, height=500, bg="yellow")
conversionframe = Frame(mynotebook, width=500, height=500, bg ="blue")

currencyframe.pack(fill="both", expand=1)
conversionframe.pack(fill="both", expand=1)

mynotebook.add(currencyframe, text="Currencies")
mynotebook.add(conversionframe, text="Convert")

mynotebook.tab(1, state='disabled')

def lock():
	if not home_entry.get() or not conversionentry.get() or not rateentry.get():
		messagebox.showwarning("WARNING!", "You Didn't Fill Out All The Fields")	
	else:
		home_entry.config(state="disabled")
		conversionentry.config(state="disabled")
		rateentry.config(state="disabled")
		mynotebook.tab(1, state='normal')
		amount_label.config(text=f'Amount of {home_entry.get()} To Convert To {conversionentry.get()}')
		converted_label.config(text=f'Equals This Many {conversionentry.get()}')
		convert_button.config(text=f'Convert From {home_entry.get()}')
def unlock():

	home_entry.config(state="normal")
	conversionentry.config(state="normal")
	rateentry.config(state="normal")
	mynotebook.tab(1, state='disabled')
home = LabelFrame(currencyframe, text="Your Home Currency")
home.pack(pady=20)
home_entry = Entry(home, font=("Helvetica", 24))
home_entry.pack(pady=10, padx=10)


conversion = LabelFrame(currencyframe, text="Conversion Currency")
conversion.pack(pady=20)
conversionlabel = Label(conversion, text="Currency To Convert To...")
conversionlabel.pack(pady=10)
conversionentry = Entry(conversion, font=("Helvetica", 24))
conversionentry.pack(pady=10, padx=10)

ratelabel = Label(conversion, text="Current Conversion Rate...")
ratelabel.pack(pady=10)
rateentry = Entry(conversion, font=("Helvetica", 24))
rateentry.pack(pady=10, padx=10)

buttonframe = Frame(currencyframe)
buttonframe.pack(pady=20)

lockbutton = Button(buttonframe, text="Lock", command=lock)
lockbutton.grid(row=0, column=0, padx=10)
unlockbutton = Button(buttonframe, text="Unlock", command=unlock)
unlockbutton.grid(row=0, column=1, padx=10)

#Converter

def convert():
	converted_entry.delete(0, END)
	conversion = float(rateentry.get()) * float(amount_entry.get())
	conversion = round(conversion,2)
	conversion = '{:,}'.format(conversion)
	converted_entry.insert(0, f'${conversion}')	
def clear():
	amount_entry.delete(0, END)
	converted_entry.delete(0, END)

#Labels

amount_label = LabelFrame(conversionframe, text="Amount To Conver")
amount_label.pack(pady=20)

amount_entry = Entry(amount_label, font=("Helvetica", 24))
amount_entry.pack(pady=10, padx=10)

convert_button = Button(amount_label, text="Convert", command=convert)
convert_button.pack(pady=20)

converted_label = LabelFrame(conversionframe, text="Converted Currency")
converted_label.pack(pady=20)

# Converted entry
converted_entry = Entry(converted_label, font=("Helvetica", 24), bd=0, bg="systembuttonface")
converted_entry.pack(pady=10, padx=10)

# Clear Button
clear_button = Button(conversionframe, text="Clear", command=clear)
clear_button.pack(pady=20)

# Fake Label for spacing
spacer = Label(conversionframe, text="", width=70)
spacer.pack()


root.mainloop()