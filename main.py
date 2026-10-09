import sys
from PyQt6.QtWidgets import QApplication, QLabel
from PyQt6.QtCore import Qt , QTimer
import random

app = QApplication(sys.argv)

pet = QLabel("🐱")

pet.setWindowFlags(
    Qt.WindowType.FramelessWindowHint |
    Qt.WindowType.WindowStaysOnTopHint |
    Qt.WindowType.Tool
)

pet.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

pet.resize(100,100)
pet.setStyleSheet("font-size: 50px;")
pet.move(500,300)
direction_x=1
direction_y=1
speed=10
is_resting=False

def move_kitty():
    global direction_x
    global direction_y
    global speed
    if is_resting:
        return
    pet.move(pet.x() + speed * direction_x,pet.y() + speed * direction_y)
    if pet.x() >= 1300:
        direction_x=-1
    if pet.x() <= 0:
        direction_x=1
    if pet.y() >= 668:
        direction_y=-1
    if pet.y() <=0:
        direction_y=1
    print(pet.x(), pet.y())
timer = QTimer()
timer.timeout.connect(move_kitty)
timer.start(50)

def change_speed():
    global speed
    speed = random.randint(2, 10)
    print(f"speed changed to{speed}")

speedtimer=QTimer()
speedtimer.timeout.connect(change_speed)
speedtimer.start(10000)
def rest_kitty():
    global is_resting
    is_resting=True
rest_timer = QTimer()
rest_timer.timeout.connect(rest_kitty)
rest_timer.start(15000)

def wake_kitty():
    global is_resting
    is_resting=False
wake_timer=QTimer()
wake_timer.timeout.connect(wake_kitty)
wake_timer.start(18000)


pet.show()

sys.exit(app.exec())



