from tkinter import *    # tkinter är ett GUI som kan visa bilder bland annat
import time    # time visar tid
import math    # math innehåller matematikfunktioner

# Variabler
simulation_time = 1000    # tiden mellan varje beräkning i sekunder
scale = 150000000000
focus = "object"
target = "L2"


G = 6.674*10**-11    # gravitationskonstanten
t = 0                # tidsvariabler
c1x = 0              # variabler c1 används i hastighetsberäkning
c1y = 0

# Konstanter
sun_size = 50  #radius=695700km
sun_mass = 1988400*10**24 #1988400*10^24kg

earth_size = 25  #radius=6371km
earth_mass = 5.9722*10**24  #5.9722*10^24kg
earth_perihelion = 147095000000  #147095000km
earth_aphelion = 152100000000  #152100000km
earth_max_velocity = 30290  #30.29 km/s
earth_min_velocity = 29290  #29.29 km/s

object_size = 10
object_mass = 1000

a = earth_mass/(sun_mass+earth_mass)

#startvärden
sun_x = 0
sun_y = 0
earth_x = 0
earth_y = earth_aphelion
v_Ex = earth_min_velocity
v_Ey = 0
object_x = 0
object_y = 100000000000
v_Ox = 30000
v_Oy = 30000
focus_x = 0
focus_y = 0
target_x = 0
target_y = 0
target2 = True



# Början av GUI
window = Tk()
window.title("Space")

# bildens storlek
canvas = Canvas(window, width=500, height=500, bg="black")
canvas.pack()

# skapar objekten
Sun = canvas.create_oval(0, 0, sun_size, sun_size, fill="yellow")
Earth = canvas.create_oval(0, 0, earth_size, earth_size, fill="blue")
Object = canvas.create_rectangle(0, 0, object_size, object_size, fill="gray")

L1 = canvas.create_oval(0, 0, 10, 10, fill="white")
L2 = canvas.create_oval(0, 0, 10, 10, fill="white")
L3 = canvas.create_oval(0, 0, 10, 10, fill="white")
L4 = canvas.create_oval(0, 0, 10, 10, fill="white")
L5 = canvas.create_oval(0, 0, 10, 10, fill="white")

timer = canvas.create_text(0, 0, anchor=NW, text="", fill="white")
target_distance = canvas.create_text(0, 0, anchor=NW, text="", fill="white")
earth_distance = canvas.create_text(0, 0, anchor=NW, text="", fill="white")
sun_distance = canvas.create_text(0, 0, anchor=NW, text="", fill="white")
line_target = canvas.create_line(0, 0, 0, 0, fill="white")
line_earth = canvas.create_line(0, 0, 0, 0, fill="white")
line_sun = canvas.create_line(0, 0, 0, 0, fill="white")

while True:
  t += 1
  
  r_SE = ((earth_x-sun_x)**2+(earth_y-sun_y)**2)**0.5  # distansen mellan jorden och solen
  F_SE = G*sun_mass*earth_mass/r_SE**2  # Gravitationskraften mellan jorden och solen
  F_Ex = F_SE*(earth_x-sun_x)/r_SE    # delar upp Gravitationskraften i x och y led
  F_Ey = F_SE*(earth_y-sun_y)/r_SE    
  v_Ex += -F_Ex/earth_mass*simulation_time    # jordens hastighet i x och y led
  v_Ey += -F_Ey/earth_mass*simulation_time
  # jordens koordinater
  earth_x += v_Ex*simulation_time+(F_Ex/earth_mass*simulation_time**2)/2  
  earth_y += v_Ey*simulation_time+(F_Ey/earth_mass*simulation_time**2)/2

  # vinkeln mellan solen och jorden från startpunkten
  earth_angle = math.atan(earth_y/earth_x)  
  if earth_x < 0:
    earth_angle += math.pi

  # distansen mellan solen och ett objekt
  r_SO = ((sun_x-object_x)**2+(sun_y-object_y)**2)**0.5  
  # distansen mellan jorden och ett objekt
  r_EO = ((earth_x-object_x)**2+(earth_y-object_y)**2)**0.5
  # gravitationskraften mellan solen och objektet
  F_SO = G*sun_mass*object_mass/r_SO**2
   # gravitationskraften mellan jorden och objektet
  F_EO = G*earth_mass*object_mass/r_EO**2
   # totala kraften på objektet i x och y led
  F_Ox = F_SO*(sun_x-object_x)/r_SO+F_EO*(earth_x-object_x)/r_EO
  F_Oy = F_SO*(sun_y-object_y)/r_SO+F_EO*(earth_y-object_y)/r_EO
  # objektets hastighet i x och y led
  v_Ox += F_Ox/object_mass*simulation_time
  v_Oy += F_Oy/object_mass*simulation_time
  # objekt x och y koordinater
  object_x += v_Ox*simulation_time+(F_Ox/object_mass*simulation_time**2)/2
  object_y += v_Oy*simulation_time+(F_Oy/object_mass*simulation_time**2)/2

  # Lagrangepunkternas x och y koordinater i förhållande till jorden
  L1_x = r_SE*(1-(a/3)**(1/3))*math.cos(earth_angle)
  L1_y = r_SE*(1-(a/3)**(1/3))*math.sin(earth_angle)

  L2_x = r_SE*(1+(a/3)**(1/3))*math.cos(earth_angle)
  L2_y = r_SE*(1+(a/3)**(1/3))*math.sin(earth_angle)

  L3_x = -r_SE*(1+5/12*a)*math.cos(earth_angle)
  L3_y = -r_SE*(1+5/12*a)*math.sin(earth_angle)

  L4_x = r_SE/2*((sun_mass-earth_mass)/(sun_mass+earth_mass))
  L4_y = 3**0.5/2*r_SE
  L4_angle = math.atan(L4_y/L4_x)
  L4_x2 = math.cos(L4_angle+earth_angle)*(L4_x/math.cos(L4_angle))
  L4_y2 = math.sin(L4_angle+earth_angle)*(L4_x/math.cos(L4_angle))

  L5_x = r_SE/2*((sun_mass-earth_mass)/(sun_mass+earth_mass))
  L5_y = -(3**0.5/2*r_SE)
  L5_angle = math.atan(L5_y/L5_x)
  L5_x2 = math.cos(-L5_angle-earth_angle)*(L5_x/math.cos(L5_angle))
  L5_y2 = -math.sin(-L5_angle-earth_angle)*(L5_x/math.cos(L5_angle))

  if target == "L1":
    target_x = L1_x
    target_y = L1_y

  elif target == "L2":
    target_x = L2_x
    target_y = L2_y

  elif target == "L3":
    target_x = L3_x
    target_y = L3_y

  elif target == "L4":
    target_x = L4_x2
    target_y = L4_y2

  elif target == "L5":
    target_x = L5_x2
    target_y = L5_y2

  else:
    target2 = False
  
  
  if t == 1 and target2 is True:
    c1x = target_x
    c1y = target_y
  elif t == 2 and target2 is True:
    c2x = target_x
    c2y = target_y

    
    object_x = c2x
    object_y = c2y
    v_Ox = (c2x-c1x)/simulation_time
    v_Oy = (c2y-c1y)/simulation_time
  
  if focus=="earth":
    focus_x = earth_x
    focus_y = earth_y
  
  elif focus=="object":
    focus_x = object_x
    focus_y = object_y

  elif focus=="L1":
    focus_x = L1_x
    focus_y = L1_y

  elif focus=="L2":
    focus_x = L2_x
    focus_y = L2_y

  elif focus=="L3":
    focus_x = L3_x
    focus_y = L3_y

  elif focus=="L4":
    focus_x = L4_x2
    focus_y = L4_y2

  elif focus=="L5":
    focus_x = L5_x2
    focus_y = L5_y2

  else:
    focus_x = 0
    focus_y = 0
    
  
  canvas.moveto(Sun, 
    round(250-1-sun_size/2-250*focus_x/scale), 
    round(250-1-sun_size/2-250*focus_y/scale))
  
  canvas.moveto(Earth,
    round(250-250*focus_x/scale+250*earth_x/scale-1-earth_size/2),
    round(250-250*focus_y/scale+250*earth_y/scale-1-earth_size/2))

  canvas.moveto(Object,
    round(250-250*focus_x/scale+250*object_x/scale-1-object_size/2),
    round(250-250*focus_y/scale+250*object_y/scale-1-object_size/2))

  canvas.moveto(L1, 
    round(250-250*focus_x/scale+250*L1_x/scale-6),
    round(250-250*focus_y/scale+250*L1_y/scale-6))

  canvas.moveto(L2, 
    round(250-250*focus_x/scale+250*L2_x/scale-6),
    round(250-250*focus_y/scale+250*L2_y/scale-6))

  canvas.moveto(L3, 
    round(250-250*focus_x/scale+250*L3_x/scale-6),
    round(250-250*focus_y/scale+250*L3_y/scale-6))
  
  canvas.moveto(L4, 
    round(250-250*focus_x/scale+250*L4_x2/scale-6),
    round(250-250*focus_y/scale+250*L4_y2/scale-6))

  canvas.moveto(L5, 
    round(250-250*focus_x/scale+250*L5_x2/scale-6),
    round(250-250*focus_y/scale+250*L5_y2/scale-6))

  years = t*simulation_time/(3600*24*365.242)
  days = (years-round(years-0.5))*365.242
  hours = (days-round(days-0.5))*24
  minutes = (hours-round(hours-0.5))*60
  seconds = (minutes-round(minutes-0.5))*60
  
  
  canvas.delete(timer)
  timer = canvas.create_text(0, 0, anchor=NW, 
    text=("T+: " + 
    str(round(years-0.5)) + " yr, " + 
    str(round(days-0.5)) + " d, " + 
    str(round(hours-0.5)) + " h, " + 
    str(round(minutes-0.5)) + " m, " + 
    str(round(seconds-0.5)) + " s"), 
    fill="white")

  canvas.delete(target_distance)
  target_distance = canvas.create_text(500, 0, anchor=NE, 
    text=("Distanse to " + target + ": " + 
    str(round((((object_x-target_x)**2+(object_y-target_y)**2)**0.5)/1000)) + " km"), 
    fill="white")

  canvas.delete(earth_distance)
  earth_distance = canvas.create_text(500, 15, anchor=NE, 
    text=("Distanse to Earth: " + 
    str(round(r_EO/1000)) + " km"), 
    fill="white")

  canvas.delete(sun_distance)
  sun_distance = canvas.create_text(500, 30, anchor=NE, 
    text=("Distanse to Sun: " + 
    str(round(r_SO/1000)) + " km"), 
    fill="white")

  canvas.delete(line_target)
  line_target = canvas.create_line(
    round(250-250*focus_x/scale+250*object_x/scale), 
    round(250-250*focus_y/scale+250*object_y/scale), 
    round(250-250*focus_x/scale+250*target_x/scale), 
    round(250-250*focus_y/scale+250*target_y/scale), 
    fill="white", width=1)

  canvas.delete(line_earth)
  line_earth = canvas.create_line(
    round(250-250*focus_x/scale+250*object_x/scale), 
    round(250-250*focus_y/scale+250*object_y/scale), 
    round(250-250*focus_x/scale+250*earth_x/scale), 
    round(250-250*focus_y/scale+250*earth_y/scale), 
    fill="blue", width=1)

  canvas.delete(line_sun)
  line_sun = canvas.create_line(
    round(250-250*focus_x/scale+250*object_x/scale), 
    round(250-250*focus_y/scale+250*object_y/scale), 
    round(250-250*focus_x/scale+250*sun_x/scale), 
    round(250-250*focus_y/scale+250*sun_y/scale), 
    fill="yellow", width=1)
  
  window.update()
  
  time.sleep(0.001)
