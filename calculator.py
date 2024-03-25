from tkinter import *

expression = ""

#function to make calculations and also handling exceptions
def result(text):
    global expression
    if text=="C":
        entry.delete(0, END)
        expression = ""
    elif text == "=":
        try:
            result_value = eval(expression)
            entry.delete(0, END)
            entry.insert(0, result_value)
            expression = str(result_value)
        except Exception as e:
            entry.delete(0, END)
            entry.insert(0, "Error")
            expression = ""
    else:
        entry.insert(END, text)
        expression += text   

#function to create buttons
def create_button(frame, text, row, column, rowspan=1, columnspan=1, padx=25, pady=10,bg_color="white",active_bg="#829799",font=("Helvectia",18)):
    button = Button(frame, 
                    text=text, 
                    padx=padx, 
                    pady=pady, 
                    bg=bg_color,
                    activebackground=active_bg,
                    font=font,
                    command=lambda: result(text))
    button.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan,pady=5)
    return button

#main window
window = Tk()
window.title("Calculator")
window.config(bg="black")

#frame where we are putting all the buttons
main_frame = Frame(window, bg="black", width=395, height=480)
main_frame.pack()
main_frame.grid_propagate(False)


#entry field
entry = Entry(main_frame, 
              font=("Helvectia", 22), 
              width=23,
              relief=GROOVE,
              bg="#c4bdb9",
              bd=3,
              highlightbackground="black")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=30)


#creating buttons
create_button(main_frame, "C", 1, 0,padx=23,bg_color="#829799",active_bg="red")
create_button(main_frame, "/", 1, 1,padx=28,bg_color="#829799")
create_button(main_frame, "*", 1, 2,padx=27,bg_color="#829799")
create_button(main_frame, "-", 1, 3,padx=28,bg_color="#ffa705",active_bg="#ffa705")

create_button(main_frame, "7", 2, 0,bg_color="#829799")
create_button(main_frame, "8", 2, 1,bg_color="#829799")
create_button(main_frame, "9", 2, 2,bg_color="#829799")
create_button(main_frame, "+", 2, 3, rowspan=2,pady=47,bg_color="#ffa705",active_bg="#ffa705")

create_button(main_frame, "4", 3, 0,bg_color="#829799")
create_button(main_frame, "5", 3, 1,bg_color="#829799")
create_button(main_frame, "6", 3, 2,bg_color="#829799")

create_button(main_frame, "=", 4, 3, rowspan=2,pady=47,bg_color="#ffa705",active_bg="green")
create_button(main_frame, "1", 4, 0,bg_color="#829799")
create_button(main_frame, "2", 4, 1,bg_color="#829799")
create_button(main_frame, "3", 4, 2,bg_color="#829799")

create_button(main_frame, "%", 5, 0,padx=21,bg_color="#829799")
create_button(main_frame, "0", 5, 1,bg_color="#829799")
create_button(main_frame, ".", 5, 2,padx=28,bg_color="#829799")

window.mainloop()
