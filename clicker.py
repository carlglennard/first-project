from tkinter import *
import tkinter.messagebox

root = Tk()

score = 0


tkinter.messagebox.showinfo("Hello!",

"""Welcome to Carl Glennard's Clicker Game! 

Just click the button "Click here" as much you can and try to beat my high score of 268!

You only have 30 seconds!

The time will start after you click the OK button!

Goodluck and Have Fun! """)
def btn():
    global btn
    btn = Button(root, text="Open new game", command=open).pack()


def exitbtn():
    global exitbtn
    exitbtn = Button(root, text="Exit game", command=root.destroy()).pack()


def restartbtn():
    global restartbtn
    restartbtn = Button(root, text="Restart game", command=restart).pack()


def click():
    global score
    score+=1
    lb_score= Label(root, text="Score = " + str(score))
    lb_score.grid(row=2, column=3, padx=10, pady=10, columnspan=5)


seconds=0


def timer():
    global seconds
    if seconds < 10:
        seconds+=1
        lb_time= Label(root, text="Time Left = " + str(seconds) + " s")
        lb_time.grid(row= 4, column=3, padx=10, pady=10, columnspan=5)
        root.after(1000, timer)
    elif seconds == 10:
        bt_click.config(state= DISABLED)
        tkinter.messagebox.showinfo(title=None, message="Congratulations! " "You have scored " +str(score)+ " points!")


bt_click = Button(root, text="Click here!", command=click, padx= 15, pady=10)
bt_click.grid(row=0, column=3, padx=10, pady=10, columnspan=5)

bt_exitbtn = Button(root, text="Close game", command=exitbtn, padx= 15, pady=10)
bt_exitbtn.grid(row=6, column=3, padx=10, pady=10, columnspan=5)

bt_restartbtn = Button(root, text="Restart game", command=restartbtn, padx= 15, pady=10)
bt_restartbtn.grid(row=8, column=3, padx=10, pady=10, columnspan=5,)

root.after(1000, timer)

root.title("Clicking Game")
root.geometry("400x400")
root.mainloop()
