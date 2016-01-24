# Implementation of classic arcade game Pong

import simpleguitk
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
paddle1_pos = [[0, ((HEIGHT / 2) - HALF_PAD_HEIGHT)], [0, ((HEIGHT / 2) + HALF_PAD_HEIGHT)]]
paddle2_pos = [[WIDTH, ((HEIGHT / 2) - HALF_PAD_HEIGHT)], [WIDTH, ((HEIGHT / 2) + HALF_PAD_HEIGHT)]]
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0
# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [1, -1]


# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    vertical = random.randrange(2,4)
    horizonal = random.randrange(1,3)
    if direction == RIGHT:
        ball_vel = [vertical, -horizonal] 
    elif direction == LEFT:
        ball_vel = [-vertical, -horizonal]
        
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    dir = random.randrange(0,2)
    if dir == 0:
        spawn_ball(LEFT)
    else:
        spawn_ball(RIGHT)
    paddle1_pos = [[0, ((HEIGHT / 2) - HALF_PAD_HEIGHT)], [0, ((HEIGHT / 2) + HALF_PAD_HEIGHT)]]
    paddle2_pos = [[WIDTH, ((HEIGHT / 2) - HALF_PAD_HEIGHT)], [WIDTH, ((HEIGHT / 2) + HALF_PAD_HEIGHT)]]
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if (ball_pos[1] <= BALL_RADIUS) or (ball_pos[1] >= ((HEIGHT - 1) - BALL_RADIUS)):
        ball_vel[1] = -ball_vel[1] 
        
    if (ball_pos[0] <= BALL_RADIUS) and ((ball_pos[1] <= paddle1_pos[1][1]) and (ball_pos[1] >= paddle1_pos[0][1])):
        ball_vel[0] = -ball_vel[0] * 1.1
    elif ball_pos[0] < 0:
        score2 += 1
        spawn_ball(RIGHT)
    
    if (ball_pos[0] >= (WIDTH - 1 ) -BALL_RADIUS) and ((ball_pos[1] <= paddle2_pos[1][1]) and (ball_pos[1] >= paddle2_pos[0][1])):
        ball_vel[0] = -ball_vel[0] * 1.1
    elif (ball_pos[0] > (WIDTH - 1 ) -BALL_RADIUS):
        score1 += 1
        spawn_ball(LEFT)

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[0][1] += paddle1_vel
    paddle1_pos[1][1] += paddle1_vel
    
    paddle2_pos[0][1] += paddle2_vel
    paddle2_pos[1][1] += paddle2_vel
    
    if paddle1_pos[0][1] <= 0:
        paddle1_pos[0][1] = 0
        paddle1_pos[1][1] = PAD_HEIGHT
    elif paddle1_pos[1][1] >= HEIGHT:
        paddle1_pos[0][1] = HEIGHT - PAD_HEIGHT
        paddle1_pos[1][1] = HEIGHT
        
    if paddle2_pos[0][1] <= 0:
        paddle2_pos[0][1] = 0
        paddle2_pos[1][1] = PAD_HEIGHT
    elif paddle2_pos[1][1] >= HEIGHT:
        paddle2_pos[0][1] = HEIGHT - PAD_HEIGHT
        paddle2_pos[1][1] = HEIGHT     
    # draw paddles
    canvas.draw_line(paddle1_pos[0], paddle1_pos[1], 8, "White")
    canvas.draw_line(paddle2_pos[0], paddle2_pos[1], 8, "White")
    # draw scores
    canvas.draw_text(str(score1), ((WIDTH / 2) - 50, 50), 30, 'Red')  
    canvas.draw_text(str(score2), ((WIDTH / 2) + 35, 50), 30, 'Red')  

def keydown(key):
    global paddle1_vel, paddle2_vel
    if key==simpleguitk.KEY_MAP["s"]:
        paddle1_vel += 5
    if key==simpleguitk.KEY_MAP["w"]:
        paddle1_vel -= 5
    if key==simpleguitk.KEY_MAP["down"]:
        paddle2_vel += 5
    if key==simpleguitk.KEY_MAP["up"]:
        paddle2_vel -= 5
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simpleguitk.KEY_MAP["s"]:
        paddle1_vel -= 5
    if key==simpleguitk.KEY_MAP["w"]:
        paddle1_vel += 5
    if key==simpleguitk.KEY_MAP["down"]:
        paddle2_vel -= 5
    if key==simpleguitk.KEY_MAP["up"]:
        paddle2_vel += 5


    
# create frame
frame = simpleguitk.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game)

# start frame
new_game()
frame.start()
