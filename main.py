import tkinter as tk
import sys
import string
import random



root=tk.Tk()
root.geometry("520x300")
root.title("pwgen")

def is_inputok(input):
    if input.isdigit():
        num=int(input)
        return 3 < num <= 100
    return False
banDigit=tk.BooleanVar()
banLower=tk.BooleanVar()
banUpper=tk.BooleanVar()
banSymbol=tk.BooleanVar()

def ranchar():
    chars=''
    if banDigit.get() == False:
          chars+=string.digits
    if banLower.get() == False:
          chars+=string.ascii_lowercase
    if banUpper.get() == False:
          chars+=string.ascii_uppercase
    if banSymbol.get() == False:
          chars+=string.punctuation
    if chars=='':
        return ''
    else:
        return random.choice(chars)
    
      
def press():
    if(is_inputok(entry.get())):
        pw1.delete(0.,tk.END)
        pw2.delete(0.,tk.END)
        pw3.delete(0.,tk.END)
        pw4.delete(0.,tk.END)
        pw5.delete(0.,tk.END)
        for i in range(0,int(entry.get())):
                       pw1.insert(0.,ranchar())
                       pw2.insert(0.,ranchar())
                       pw3.insert(0.,ranchar())
                       pw4.insert(0.,ranchar())
                       pw5.insert(0.,ranchar())

chframe=tk.Frame(root)
label=tk.Label(root,text="指定した桁数のパスワードを生成するよ~(3~100桁)")

chDigit=tk.Checkbutton(chframe,text='数字なし',variable=banDigit)
chLower=tk.Checkbutton(chframe,text='小文字なし',variable=banLower)
chUpper=tk.Checkbutton(chframe,text='大文字なし',variable=banUpper)
chSymbol=tk.Checkbutton(chframe,text='記号なし',variable=banSymbol)

entry=tk.Entry(root,font=('Arial 20'),width=7,justify=tk.CENTER)
button=tk.Button(root,text="Generate",width=16,height=2,font=('Arial 16'),background='#dddddd',command=press)
exitbtn=tk.Button(root,text="EXIT",width=8,height=1,font=('Arial 14'),background='#dddddd',command=root.destroy)

pw1=tk.Text(height=1,width=50,font=('Arial 12'))
pw2=tk.Text(height=1,width=50,font=('Arial 12'))
pw3=tk.Text(height=1,width=50,font=('Arial 12'))
pw4=tk.Text(height=1,width=50,font=('Arial 12'))
pw5=tk.Text(height=1,width=50,font=('Arial 12'))

label.pack()
chframe.pack(anchor='center')
chDigit.pack(side=tk.LEFT)
chLower.pack(side=tk.LEFT)
chUpper.pack(side=tk.LEFT)
chSymbol.pack(side=tk.LEFT)
entry.pack()
button.pack()
pw1.pack()
pw2.pack()
pw3.pack()
pw4.pack()
pw5.pack()
exitbtn.pack(anchor=tk.E)

    
root.resizable(False,False)
root.mainloop()
