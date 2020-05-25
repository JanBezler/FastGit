import os
import tkinter as tk

root = tk.Tk()
text = tk.Text(root)

def GitInit():
    os.system("git init " + '"' + os.path.dirname(os.path.abspath(__file__)) + '"')

def GitStage():
    os.system("git add .")
    print("Changes Staged")

def GitCommit(commitMessage):
    if bool(commitMessage):
        commitMessage = "git commit -m " + '"' + str(commitMessage) + '"'
        os.system(commitMessage)
    else: print("Add commit message and try again")

def GitStatus():
    os.system("git status " + os.path.dirname(os.path.abspath(__file__)))


def GitPush():
    print("Trying to push")
    try:
        lines = []
        with open(os.path.dirname(os.path.abspath(__file__)) + "/.git/FastGitconfig.conf",mode="r") as fileconfig:
            for line in fileconfig:
                lines.append(line.strip())
            os.system("git push https://"+lines[0]+":"+lines[1]+"@"+lines[2]+" master")

    except FileNotFoundError:
        print("GitHub account not added yet")

def GitPull():
    print("Trying to pull")
    try:
        lines = []
        with open(os.path.dirname(os.path.abspath(__file__)) + "/.git/FastGitconfig.conf",mode="r") as fileconfig:
            for line in fileconfig:
                lines.append(line.strip())
            os.system("git pull https://"+lines[0]+":"+lines[1]+"@"+lines[2]+" master")
    except FileNotFoundError:
        print("GitHub account not added yet")


def addGitHub():

    def submitGitHub(login,password,repo):
        config = open(".git/FastGitconfig.conf",mode="w")
        config.write(login+"\n"+password+"\n"+repo[8:]+"\n")
        config.close()
        print("Input data saved")

        


    l1 = tk.Label(root,text="Account Name")
    l1.pack()
    e2 = tk.Entry()
    e2.pack()

    l2 = tk.Label(root,text="Password")
    l2.pack()
    e3 = tk.Entry()
    e3.pack()
    

    l3 = tk.Label(root,text="URL of repo")
    l3.pack()
    e4 = tk.Entry()
    e4.pack()

    b7 = tk.Button(root, text='Submit', command=lambda:submitGitHub(e2.get(),e3.get(),e4.get()))
    b7.pack()
    

b1 = tk.Button(root, text='Init Repository', command=lambda:GitInit())
b1.pack()

b4 = tk.Button(root, text='Check status', command=lambda:GitCommit(GitStatus()))
b4.pack()

b2 = tk.Button(root, text='Stage Changes', command=lambda:GitStage())
b2.pack()

l3 = tk.Label(root,text="Commit message 'this_is_example'")
l3.pack()

e1 = tk.Entry()
e1.pack()

b3 = tk.Button(root, text='Commit', command=lambda:GitCommit(e1.get()))
b3.pack()

b7 = tk.Button(root, text='Pull from GitHub', command=lambda:GitPull())
b7.pack()

b5 = tk.Button(root, text='Push to GitHub', command=lambda:GitPush())
b5.pack()

b6 = tk.Button(root, text='Add GitHub Repo', command=lambda:addGitHub())
b6.pack()

root.mainloop()
