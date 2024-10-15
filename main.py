from tkinter import *
import time

TIME = 1000
G = 6.674*10**-11
SCALE = 200000000000

SUN_SIZE = 100  #radius=695700km
SUN_MASS = 1988400*10**24 #1988400*10^24kg

EARTH_SIZE = 50  #radius=6371km
EARTH_MASS = 5.9722*10**24  #5.9722 x 10^24kg
EARTH_PERIHELION = 147095000000  #147095000km
EARTH_APHELION = 152100000000  #152100000km
EARTH_MAX_VELOCITY = 30290  #30.29 km/s
EARTH_MIN_VELOCITY = 29290  #29.29 km/s

sun_x = 0
sun_y = 0
earth_x = 0
earth_y = EARTH_APHELION
v_Ex = EARTH_MIN_VELOCITY
v_Ey = 0

window = Tk()
window.title("Space")

canvas = Canvas(window, width=500, height=500, bg="black")
canvas.pack()


Sun = canvas.create_oval(0, 0, SUN_SIZE, SUN_SIZE, fill="yellow")
Earth = canvas.create_oval(0, 0, EARTH_SIZE, EARTH_SIZE, fill="blue")
earth_velocity = 0
distance = 250



canvas.moveto(Sun, 250-1-SUN_SIZE/2, 250-1-SUN_SIZE/2)

while True:
  r_SE = ((earth_x-sun_x)**2+(earth_y-sun_y)**2)**0.5
  F_E = G*SUN_MASS*EARTH_MASS/r_SE**2
  F_Ex = F_E*(earth_x-sun_x)/r_SE
  F_Ey = F_E*(earth_y-sun_y)/r_SE
  v_Ex += -F_Ex/EARTH_MASS*TIME
  v_Ey += F_Ey/EARTH_MASS*TIME
  earth_x += v_Ex*TIME+(F_Ex/EARTH_MASS*TIME**2)/2
  earth_y += -v_Ey*TIME+(F_Ey/EARTH_MASS*TIME**2)/2
  v_E = (v_Ex**2+v_Ey**2)**0.5
  
  canvas.moveto(Earth,
    250+250*earth_x/SCALE-1-EARTH_SIZE/2,
    250+250*earth_y/SCALE-1-EARTH_SIZE/2)
  
  print(v_E, r_SE)
  
  window.update()
  time.sleep(0.001)


window.mainloop()
