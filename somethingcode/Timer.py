# template for "Stopwatch: The Game"
import simpleguitk

# define global variables
time = 0
millisecond = 0
success = 0
attempts = 0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format():
    global time, millisecond
    millisecond = time % 10
    second = int((time / 10) % 60)
    minute = int((time / 10) / 60)
    
    if second < 10:
        second_str = "0" + str(second)
    else:
        second_str = str(second)
    return str(minute) + ":" + second_str + "." + str(millisecond )
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def stop():
    global success, attempts, millisecond, time
    millisecond = int(time % 10)
    timer.stop()
    attempts += 1
    if millisecond == 0:
        success +=1

def reset():
    global time, success, attempts
    timer.stop()
    time = 0
    success = 0
    attempts = 0
       
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time += 1

# define draw handler
def draw(canvas):
    global success, attempts
    present_time = format()
    result = str(success) + "/" + str(attempts)
    canvas.draw_text(present_time, [150,150], 40, "Red")
    canvas.draw_text(result, [250,50], 30, "Green")
    
# create frame
frame = simpleguitk.create_frame("Timer", 500, 500)
timer = simpleguitk.create_timer(100, timer_handler)
# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)

# start frame
frame.start()
print (time)
# Please remember to review the grading rubric
