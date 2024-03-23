from tkinter import *
from tkinter import messagebox

#function to add tasks
def addTask():
    task = entry.get()
    if task:
        listbox.insert(END, task)
        entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "You haven't added any task")

#function to delete task
def deleteTask():
    task = listbox.curselection()
    if task:
        listbox.delete(task)
        messagebox.showinfo("Task", "Task deleted successfully")
    else:
        messagebox.showerror("Task", "No task selected")

#function to clear all tasks
def clear():
    response=messagebox.askyesno("Task","Do you want to clear all tasks?")
    if response:
        listbox.delete(0, END)
        messagebox.showinfo("Task","All task removed")
        

window = Tk()

window.geometry("545x580")
window.title("To Do List Application")

#listbox
listbox = Listbox(window, 
                  width=47, 
                  height=20, 
                  bg="#cbcab8",
                  highlightbackground="black",
                  font=("Helvectia,28"))
listbox.grid(row=0, column=0, padx=10, columnspan=3)

#entry filed to add tasks
entry = Entry(window, 
              width=47, 
              bg="#cbcab8",
              highlightbackground="black",
              highlightthickness=1,
              font=("Helvectia,28"))
entry.grid(row=1, column=0, padx=10, columnspan=3,pady=(10,0))

#buttons for adding and deleting task
addButton = Button(window, text="Add Task", command=addTask, bg="#00ff00")
deleteButton = Button(window, text="Delete", command=deleteTask, bg="grey",padx=10)
clearButton = Button(window, text="Clear All", command=clear, bg="red")

addButton.grid(row=3, column=0,pady=(20,0))
deleteButton.grid(row=3, column=1,pady=(20,0))
clearButton.grid(row=3, column=2,pady=(20,0))

window.mainloop()
