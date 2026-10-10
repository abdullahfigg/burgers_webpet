import sys
from PyQt6.QtWidgets import QApplication, QLabel
from PyQt6.QtCore import Qt , QTimer
from PyQt6.QtGui import QMovie,QPixmap
import random

class KittyLabel(QLabel):
    def mousePressEvent(self, event):
        if event.button()==Qt.MouseButton.RightButton:
            zoomies()
        elif event.button()==Qt.MouseButton.LeftButton:
            if is_sleeping:
                wake_from_sleep()
            else:
                handle_click()



app = QApplication(sys.argv)

pet =KittyLabel("")
spin_movie=QMovie("kitty_spin.gif")
stand_movie=QMovie("kitty_stand.gif")
pat_movie = QMovie("kitty_pat.gif")
sleep_pixmap = QPixmap("kitty_sleep.png")

current_animation=None

def play_gif(movie):
    global current_animation
    if current_animation==movie:
        return
    if current_animation is not None:
        current_animation.stop()

    
    pet.setMovie(movie)
    current_animation = movie
    movie.start()



pet.setWindowFlags(
    Qt.WindowType.FramelessWindowHint |
    Qt.WindowType.WindowStaysOnTopHint |
    Qt.WindowType.Tool
)

pet.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

pet.resize(100,100)
spin_movie.setScaledSize(pet.size())
stand_movie.setScaledSize(pet.size())
pat_movie.setScaledSize(pet.size())
sleep_pixmap= sleep_pixmap.scaled(pet.size())


play_gif(spin_movie)

pet.setStyleSheet("font-size: 50px;")
pet.move(500,300)
direction_x=1
direction_y=1
speed=10
normal_speed=speed

is_zooming=False
click_count=0



is_resting=False
is_sleeping=False





def move_kitty():
    global direction_x
    global direction_y
    global speed
    if is_sleeping:
        return
    if is_resting:
        if not pat_timer.isActive():
            play_gif(stand_movie)
        return
    if pat_timer.isActive():
        return
    
    play_gif(spin_movie)

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
    global speed,normal_speed
    normal_speed = random.randint(2, 10)

    if not is_zooming:
        speed=normal_speed
    
    print(f"speed changed to{speed}")

speedtimer=QTimer()
speedtimer.timeout.connect(change_speed)
speedtimer.start(10000)



def handle_click():
    global click_count

    click_count +=1

    if click_count>=7:
        click_count=0
        click_timer.stop()
        zoomies()
    else:
        click_timer.start()


def pat_kitty():
    global click_count
    click_count=0
    click_timer.stop()

    if not is_sleeping:
        play_gif(pat_movie)
        pat_timer.start(1500)

def finish_pat():
    if is_sleeping or is_resting:
        play_gif(stand_movie)
    else:
        play_gif(spin_movie)
pat_timer = QTimer()
pat_timer.setSingleShot(True)
pat_timer.timeout.connect(finish_pat)



click_timer=QTimer()
click_timer.setSingleShot(True)
click_timer.timeout.connect(pat_kitty)



def zoomies():
    global speed,is_zooming
    if is_sleeping or is_resting:
        return
    is_zooming=True
    speed=70
    zoom_timer.start(3000)






def end_zoomies():
    global speed,is_zooming
    is_zooming=False
    speed=normal_speed

zoom_timer=QTimer()
zoom_timer.timeout.connect(end_zoomies)
zoom_timer.setSingleShot(True)






def change_direction():
    global direction_x
    global direction_y
    direction_x=random.choice([-1,1])
    direction_y=random.choice([-1,1])

diection_timer=QTimer()
diection_timer.timeout.connect(change_direction)
diection_timer.start(5000)





def rest_kitty():
    global is_resting
    is_resting=True
    wake_timer.start(6000)

rest_timer = QTimer()
rest_timer.timeout.connect(rest_kitty)
rest_timer.start(10000)





def wake_kitty():
    global is_resting
    is_resting=False
wake_timer=QTimer()
wake_timer.timeout.connect(wake_kitty)






def sleep_kitty():
    global is_sleeping
    is_sleeping=True

    current = pet.movie()
    if current is not None:
        current.stop()

    pet.setMovie(None)
    pet.setPixmap(sleep_pixmap)

   
sleep_timer=QTimer()
sleep_timer.timeout.connect(sleep_kitty)
sleep_timer.start(30000)





def wake_from_sleep():
    global is_sleeping,current_animation

    is_sleeping=False
    current_animation=None
    pet.setPixmap(QPixmap())
    play_gif(spin_movie)


pet.show()

sys.exit(app.exec())


