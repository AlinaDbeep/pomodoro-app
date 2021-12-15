from tkinter import *
import math
import time

green = "#70AF85"
yellow = "#F3F0D7"
orange = "#E0C097"
red="#FF7878"
font_name= "Courier"
work_min = 25
short_break_min = 5
long_break_min = 20
reps = 0
timer = None


def reset_time():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    checkmarks.config(text="")
    global reps
    reps = 0



def start_timer():
    global reps
    reps +=1
    work_sec  = work_min * 60
    short_break_sec = short_break_min * 60
    long_break_sec = long_break_min * 60
    

    if reps %8 ==0:
        countdown(long_break_sec)
        label.config(text="Break", fg=orange)
    elif reps%2 ==0:
        countdown(short_break_sec)
        label.config(text="Break", fg=red)
    else:
        countdown(work_sec)
        label.config(text="Work", fg=green)

def countdown(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec <= 9:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1 )
    else: 
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔️"
        checkmarks.config(text=marks)



window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=yellow)

label = Label(text="Timer", bg=yellow, fg=green, font=(font_name, 30, "bold"))
label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=yellow, highlightthickness=0)
tomato_img= PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(font_name, 30, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)


reset_button = Button(text="Reset", command = reset_time)
reset_button.grid(row=2, column=2)


checkmarks = Label(fg=green, bg=yellow)
checkmarks.grid(column=1, row=3)



window.mainloop()