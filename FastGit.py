import os
import tkinter as tk
import subprocess

root = tk.Tk()
text = tk.Text(root)

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

def GitStatus():
    os.system("git status")
    print("Status")


b1 = tk.Button(root, text='Init Repository', command=lambda:GitInit())
b1.pack()


b2 = tk.Button(root, text='Stage Changes', command=lambda:GitStage())
b2.pack()

e1 = tk.Entry()
e1.pack()

b3 = tk.Button(root, text='Commit', command=lambda:GitCommit(e1.get()))
b3.pack()

b4 = tk.Button(root, text='Status', command=lambda:GitCommit(e1.get()))
b4.pack()


def test():
    return os.system("echo 333")

print(test())


text.insert(tk.END, str(test))
text.pack()



root.mainloop()