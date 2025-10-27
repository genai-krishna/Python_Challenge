import turtle
import time
import random

# ==============================
# Classic Snake Game in Python
# ==============================

# Delay to control game speed
delay = 0.1

# Score tracking
score = 0
high_score = 0

# Set up the screen
win = turtle.Screen()
win.title("🐍 Snake Game by Krishna")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)  # Turns off automatic screen updates for smoother animation

# Create the snake head
head = turtle.Turtle()
head.speed(0)  # Animation speed (0 = fastest)
head.shape("square")
head.color("green")
head.penup()  # Prevents drawing lines
head.goto(0, 0)
head.direction = "stop"

# Create the food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# List to store snake body segments
segments = []

# Create a score display
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 18, "normal"))

# ======================
# Movement Functions
# ======================
def go_up():
    if head.direction != "down":  # Prevent reverse movement
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# Move the snake in its direction
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# ======================
# Keyboard Controls
# ======================
win.listen()
win.onkeypress(go_up, "Up")
win.onkeypress(go_down, "Down")
win.onkeypress(go_left, "Left")
win.onkeypress(go_right, "Right")

# ======================
# Main Game Loop
# ======================
while True:
    win.update()

    # Check collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the body segments
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        # Reset score
        score = 0
        delay = 0.1

        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 18, "normal"))

    # Check collision with food
    if head.distance(food) < 20:
        # Move food to a random location
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # Add new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("lightgreen")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten delay to increase speed
        delay -= 0.001

        # Increase score
        score += 10
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 18, "normal"))

    # Move the body segments in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move the first segment to where the head was
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for self-collision
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 18, "normal"))

    time.sleep(delay)

# Keeps the window open
win.mainloop()
