from tkinter import *
import math
import winsound
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
paused = False
paused_time = 0


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(time_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    global reps
    reps = 0

def pause_timer():
    global timer, paused, paused_time
    if timer:
        window.after_cancel(timer)
        paused = True
        time_left = canvas.itemcget(time_text, "text")
        minutes, seconds = map(int, time_left.split(":"))
        paused_time = minutes * 60 + seconds
        timer = None

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, paused_time, paused
    if paused:
        paused = False
        count_down(paused_time)  # Resume from the paused time
        return
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)

    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def play_ding():
    winsound.Beep(1000, 500)  # Frequency: 1000Hz, Duration: 500ms

def bring_window_to_front():
    window.lift()
    window.attributes('-topmost', True)
    window.after(3000, lambda: window.attributes("-topmost", False))

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
        if count == 3:
            play_ding()
            bring_window_to_front()
    else:
        if reps % 2 == 1:
            current_marks = check_mark.cget("text")
            check_mark.config(text=current_marks + "✔")

        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

canvas = Canvas(width=220, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
time_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=1)



start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0, sticky='e', padx=10, pady=10)

pause_button = Button(text="Pause", highlightthickness=0, command=pause_timer)
pause_button.grid(row=2, column=1, padx=10, pady=10)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2, sticky='w', padx=10, pady=10)


window.mainloop()