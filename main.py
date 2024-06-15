from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

from myEncrypt import password_encrypt, password_decrypt

#----------------window-------------------------------------
window=Tk()
window.title("Secret Notes")
window.minsize(width=300,height=600)
window.config(padx=30,pady=30)
#----------------image-------------------------------------
myImage=Image.open("secret.png").resize((200,200))
img = ImageTk.PhotoImage(myImage)
panel = Label(window, image = img)
panel.grid(row=0, column=1)
#----------------Title Label-------------------------------------
labelTitle=Label(text="Enter Your Title",font=("Arial", 16))
labelTitle.config(padx=5,pady=5)
labelTitle.grid(row=1,column=1)
#----------------Title Entry-------------------------------------
entryTitle=Entry(width=30)
entryTitle.grid(row=2,column=1)
#----------------Text Label-------------------------------------
labelText=Label(text="Enter Your Secret",font=("Arial", 16))
labelText.config(padx=5,pady=5)
labelText.grid(row=3,column=1)
#----------------Text-------------------------------------
secretText=Text(width=30,height=20)
secretText.grid(row=4,column=1)

def encryption():
    title=entryTitle.get()
    text=secretText.get("1.0",END)
    password = entryMasterkey.get()
    try:
        if title=="" or text=="" or password=="":
            messagebox.showwarning("Warning", "Please fill all blanks before encryption !!!")
        else:
            result=password_encrypt(text.encode(), password)
            f = open("mysecret.txt", "a")
            f.write(title)
            f.write("\n")
            f.write(str(result))
            f.write("\n")
            f.close()
    except:
        messagebox.showerror("Error", "Encryption problem occured !")

def decryption():
    password=entryMasterkey.get()
    text = secretText.get("1.0", END)
    try:
        if text=="" or password=="":
            messagebox.showwarning("Warning", "Please fill all blanks before decryption !!!")
        else:
            result = password_decrypt(text, password).decode()
            secretText.delete('1.0', END)
            secretText.insert("1.0", result)
            print(result)
    except:
        messagebox.showerror("Error", "masterkey or secret note are wrong !")


#----------------Title Label-------------------------------------
labelMasterkey=Label(text="Enter Master Key",font=("Arial", 16))
labelMasterkey.config(padx=5,pady=5)
labelMasterkey.grid(row=5,column=1)
#----------------Master Key Entry-------------------------------------
entryMasterkey=Entry(width=30)
entryMasterkey.grid(row=6,column=1)
#----------------Enctypt Button-------------------------------------
buttonEncrypt=Button(text="Save&Encrypt",command=encryption)
buttonEncrypt.config(padx=5,pady=5)
buttonEncrypt.grid(row=7,column=1)
#----------------Decrypt Button-------------------------------------
buttonDecrypt=Button(text="Decrypt",command=decryption)
buttonDecrypt.config(padx=5,pady=5)
buttonDecrypt.grid(row=8,column=1)



window.mainloop()
