import simplegui

# define global variables
time = 0
stops = 0
success = 0
score = "0/0"

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    min = (t // 10) // 60
    sec1 = ((t // 10) % 60) // 10
    sec2 = ((t // 10) % 60) % 10
    mil = t % 10
    
    return str(min) + ":" + str(sec1) + str(sec2) + '.' + str(mil)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    global success
    global stops
    global score
    if timer.is_running():
        timer.stop()
        stops = stops + 1
        if time % 10 == 0:
            success = success + 1
    score = str(success) + '/' + str(stops)
    
    
def reset():
    global time
    global score
    global success
    global stops
    timer.stop()
    time = 0
    success = 0
    stops = 0
    score = '0/0'

# define event handler for timer with 0.1 sec interval
def tick():
    global time
    global score
    time = time + 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), [100,112], 36, "White")
    canvas.draw_text(score, [250,30], 32, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)

# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
timer = simplegui.create_timer(100, tick)

# start frame
frame.set_draw_handler(draw)
frame.start()

# Please remember to review the grading rubric
