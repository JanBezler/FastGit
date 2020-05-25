import os
import tkinter as tk

root = tk.Tk()

def GitInit():
    os.system("git init")
    print("Repositorium Initialised")

def GitStage():
    os.system("git add .")
    print("Changes Staged")

def GitCommit(commitMessage):
    commitMessage = "git commit -m " + "'" + str(commitMessage) + "'"
    os.system(commitMessage)
    if bool(commitMessage): print("Commited")
    else: print("Add commit message and try again") 


b1 = tk.Button(root, text='Init Repository', command=lambda:GitInit())
b1.pack()


b2 = tk.Button(root, text='Stage Changes', command=lambda:GitStage())
b2.pack()

e1 = tk.Entry()
e1.pack()

b3 = tk.Button(root, text='Commit', command=lambda:GitCommit(e1.get()))
b3.pack()



root.mainloop()

