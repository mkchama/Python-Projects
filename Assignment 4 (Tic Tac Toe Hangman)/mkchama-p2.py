import math
import stddraw
import time
time_aggregate = time.localtime()
hour = time_aggregate.tm_hour
minute = time_aggregate.tm_min
second = time_aggregate.tm_sec

stddraw.setPenRadius(0.005)
stddraw.setPenColor(stddraw.WHITE)
stddraw.setPenRadius(0.009)
stddraw.setPenColor(stddraw.BLACK)
stddraw.circle(0.5, 0.5, 0.49)
stddraw.setFontSize(36)

stddraw.setPenColor(stddraw.BLACK)
for i in range(12):
    ang = math.radians((-i+2) * 30)
    stddraw.text(0.5 + 0.4 * math.cos(ang),.5 + 0.4 * math.sin(ang),str(i+1))
    stddraw.setPenRadius(0.0049)
    stddraw.line(0.5 + 0.48 * math.sin(ang), 0.5 + 0.48 * math.cos(ang),0.5 + 0.45 * math.sin(ang), 0.5 + 0.45 * math.cos(ang))

for i in range(60):
    ang_tick = math.radians((i) * 6)
    stddraw.setPenRadius(0.0023)
    stddraw.line(0.5 + 0.47 * math.sin(ang_tick), 0.5 + 0.47 * math.cos(ang_tick),0.5 + 0.45 * math.sin(ang_tick), 0.5 + 0.45 * math.cos(ang_tick))

stddraw.setPenRadius(.012)
stddraw.setPenColor(stddraw.BLACK)
hour_angle = math.radians(30 * hour)
h = 0.05
stddraw.line(0.5, 0.5, 0.5 - h * math.sin(hour_angle), 0.5 - h * math.cos(hour_angle))

stddraw.setPenRadius(.012)
stddraw.setPenColor(stddraw.BLACK)
hour_angle = math.radians(30 * hour)
h = 0.23
stddraw.line(0.5, 0.5, 0.5 + h * math.sin(hour_angle), 0.5 + h * math.cos(hour_angle))

stddraw.setPenRadius(.009)
stddraw.setPenColor(stddraw.BLACK)
min_angle = math.radians(6 * minute)
m = 0.34
stddraw.line(0.5, 0.5, 0.5 + m * math.sin(min_angle), 0.5 + m * math.cos(min_angle))

stddraw.setPenRadius(.009)
stddraw.setPenColor(stddraw.BLACK)
min_angle = math.radians(6 * minute)
m = 0.05
stddraw.line(0.5, 0.5, 0.5 - m * math.sin(min_angle), 0.5 - m * math.cos(min_angle))

stddraw.setPenRadius(.0059)
stddraw.setPenColor(stddraw.RED)
sec_angle = math.radians(6 * second)
s = 0.05
stddraw.line(0.5, 0.5, 0.5 - s * math.sin(sec_angle), 0.5 - s * math.cos(sec_angle))

stddraw.setPenRadius(.0059)
stddraw.setPenColor(stddraw.RED)
sec_angle = math.radians(6 * second)
s = 0.38
stddraw.line(0.5, 0.5, 0.5 + s * math.sin(sec_angle), 0.5 + s * math.cos(sec_angle))

stddraw.show()
