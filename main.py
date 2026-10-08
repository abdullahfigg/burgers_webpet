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

def move_kitty():
    global direction_x
    global direction_y
    global speed
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
    speed = random.randint(2, 15)
    print(f"speed changed to{speed}")

speedtimer=QTimer()
speedtimer.timeout.connect(change_speed)
speedtimer.start(10000)





pet.show()

sys.exit(app.exec())

